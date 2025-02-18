# markdown_analyzer/extractors/compatibility/validator.py
import re
import logging
from typing import List, Dict, Optional, Tuple, Set
from dataclasses import dataclass
from .models import (
    CompatibilityRelation, ProductReference,
    TechnicalRequirement, CompatibilityCondition
)

@dataclass
class ValidationResult:
    """Resultat från validering av kompatibilitetsdata"""
    is_valid: bool
    errors: List[str]
    warnings: List[str]
    stats: Dict[str, int]

class CompatibilityValidator:
    """
    Validerar extraherad kompatibilitetsinformation.
    """
    
    def __init__(self):
        self.seen_articles: Set[str] = set()
        self.product_references: Dict[str, List[ProductReference]] = {}

    def validate_relations(self, relations: List[CompatibilityRelation]) -> ValidationResult:
        """
        Validerar en samling kompatibilitetsrelationer.
        """
        errors = []
        warnings = []
        stats = {
            'total_relations': len(relations),
            'with_article_numbers': 0,
            'with_conditions': 0,
            'with_requirements': 0,
            'with_certification': 0,
            'high_confidence': 0
        }

        for idx, relation in enumerate(relations):
            basic_errors = self._validate_basic_relation(relation)
            if basic_errors:
                errors.extend(f"Relation {idx}: {err}" for err in basic_errors)
                continue

            ref_errors = self._validate_product_references(relation)
            if ref_errors:
                errors.extend(f"Relation {idx}: {err}" for err in ref_errors)

            if relation.technical_requirements:
                req_errors = self._validate_technical_requirements(relation.technical_requirements)
                if req_errors:
                    errors.extend(f"Relation {idx}: {err}" for err in req_errors)
                stats['with_requirements'] += 1

            if relation.conditions:
                cond_errors = self._validate_conditions(relation.conditions)
                if cond_errors:
                    errors.extend(f"Relation {idx}: {err}" for err in cond_errors)
                stats['with_conditions'] += 1

            if relation.certification:
                stats['with_certification'] += 1
            if relation.confidence >= 0.8:
                stats['high_confidence'] += 1
            if relation.target_product.article_number:
                stats['with_article_numbers'] += 1

            relation_warnings = self._check_for_warnings(relation)
            if relation_warnings:
                warnings.extend(f"Relation {idx}: {warn}" for warn in relation_warnings)

        return ValidationResult(
            is_valid=len(errors) == 0,
            errors=errors,
            warnings=warnings,
            stats=stats
        )

    def _validate_basic_relation(self, relation: CompatibilityRelation) -> List[str]:
        errors = []
        if not relation.source_product.name:
            errors.append("Källprodukt saknar namn")
        if not relation.target_product.name:
            errors.append("Målprodukt saknar namn")
        if not relation.relation_type:
            errors.append("Relationstyp saknas")
        if not (0 <= relation.confidence <= 1):
            errors.append("Ogiltig konfidensnivå")
        return errors

    def _validate_product_references(self, relation: CompatibilityRelation) -> List[str]:
        errors = []
        source_errors = self._validate_single_reference(relation.source_product)
        if source_errors:
            errors.extend(f"Källprodukt: {err}" for err in source_errors)
        target_errors = self._validate_single_reference(relation.target_product)
        if target_errors:
            errors.extend(f"Målprodukt: {err}" for err in target_errors)
        if relation.source_product.article_number:
            if relation.source_product.article_number in self.seen_articles:
                self._track_product_reference(relation.source_product)
            else:
                self.seen_articles.add(relation.source_product.article_number)
        return errors

    def _validate_single_reference(self, ref: ProductReference) -> List[str]:
        errors = []
        if not ref.name or len(ref.name.strip()) < 2:
            errors.append("Ogiltigt produktnamn")
        if ref.article_number:
            if not re.match(r'^\d{5,8}$', ref.article_number):
                errors.append(f"Ogiltigt artikelnummerformat: {ref.article_number}")
        if ref.series and len(ref.series.strip()) < 2:
            errors.append("Ogiltig serie")
        if ref.variant and len(ref.variant.strip()) < 2:
            errors.append("Ogiltig variant")
        return errors

    def _validate_technical_requirements(self, requirements: List[TechnicalRequirement]) -> List[str]:
        errors = []
        for req in requirements:
            if not req.category:
                errors.append("Tekniskt krav saknar kategori")
                continue
            if not (req.exact_value or (req.min_value is not None or req.max_value is not None)):
                errors.append(f"Tekniskt krav '{req.category}' saknar värde")
            if req.unit:
                valid_units = {
                    'voltage': ['V', 'mV', 'kV'],
                    'current': ['A', 'mA'],
                    'dimensions': ['mm', 'cm', 'm'],
                    'weight': ['g', 'kg'],
                    'temperature': ['C', 'F', 'K']
                }
                if req.category in valid_units and req.unit not in valid_units[req.category]:
                    errors.append(f"Ogiltig enhet '{req.unit}' för kategori '{req.category}'")
            if req.min_value is not None and req.max_value is not None:
                if req.min_value > req.max_value:
                    errors.append(f"Ogiltigt intervall för '{req.category}': min ({req.min_value}) > max ({req.max_value})")
        return errors

    def _validate_conditions(self, conditions: List[CompatibilityCondition]) -> List[str]:
        errors = []
        valid_condition_types = {'installation', 'environment', 'configuration', 'operation', 'maintenance', 'other'}
        for condition in conditions:
            if condition.condition_type not in valid_condition_types:
                errors.append(f"Ogiltig villkorstyp: {condition.condition_type}")
            if not condition.description or len(condition.description.strip()) < 5:
                errors.append("Villkor saknar giltig beskrivning")
            if condition.requirements:
                req_errors = self._validate_technical_requirements(condition.requirements)
                if req_errors:
                    errors.extend(f"Villkor: {err}" for err in req_errors)
        return errors

    def _check_for_warnings(self, relation: CompatibilityRelation) -> List[str]:
        warnings = []
        if relation.confidence < 0.6:
            warnings.append(
                f"Låg konfidens ({relation.confidence}) för relation mellan {relation.source_product.name} och {relation.target_product.name}"
            )
        if len(relation.conditions) > 3:
            warnings.append(f"Komplex kompatibilitet med {len(relation.conditions)} villkor")
        if not relation.target_product.article_number:
            warnings.append("Målprodukt saknar artikelnummer")
        if relation.technical_requirements:
            req_warnings = self._check_technical_conflicts(relation.technical_requirements)
            warnings.extend(req_warnings)
        return warnings

    def _check_technical_conflicts(self, requirements: List[TechnicalRequirement]) -> List[str]:
        warnings = []
        req_by_category = {}
        for req in requirements:
            req_by_category.setdefault(req.category, []).append(req)
        for category, reqs in req_by_category.items():
            if len(reqs) > 1:
                intervals = []
                for req in reqs:
                    if req.min_value is not None and req.max_value is not None:
                        intervals.append((req.min_value, req.max_value))
                if intervals and not self._check_interval_overlap(intervals):
                    warnings.append(f"Motstridiga intervall för kategori '{category}'")
                exact_values = [req.exact_value for req in reqs if req.exact_value is not None]
                if len(set(exact_values)) > 1:
                    warnings.append(f"Flera olika värden för kategori '{category}': {', '.join(exact_values)}")
        return warnings

    def _check_interval_overlap(self, intervals: List[Tuple[float, float]]) -> bool:
        if not intervals:
            return True
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        current_max = sorted_intervals[0][1]
        for start, end in sorted_intervals[1:]:
            if start > current_max:
                return False
            current_max = max(current_max, end)
        return True

    def _track_product_reference(self, ref: ProductReference) -> None:
        if ref.article_number:
            self.product_references.setdefault(ref.article_number, []).append(ref)
