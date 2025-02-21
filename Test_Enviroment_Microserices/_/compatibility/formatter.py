from typing import List, Dict, Set
from .models import (
    CompatibilityRelation, RelationType,
    CompatibilityCondition, TrainingExample
)

class CompatibilityFormatter:
    """
    Formaterar kompatibilitetsinformation för träningsdata.
    Fokuserar på att skapa tydliga och konsekventa exempel för -c kommandot.
    """
    
    def format_for_training(self, relation: CompatibilityRelation) -> List[TrainingExample]:
        """
        Formaterar en relation för träningsdata.
        Skapar exempel för både artikelnummer- och namnbaserade sökningar.
        """
        examples = []
        
        # Skapa ett strukturerat markdown-svar
        response = self._format_clean_markdown(relation)
        confidence = relation.confidence
        source = relation.source_product.name.replace('**', '')
        
        # Skapa exempel baserat på artikelnummer
        if relation.source_product.article_number:
            examples.append(TrainingExample(
                user_input=f"-c {relation.source_product.article_number}",
                ai_output=response,
                source=source,
                confidence=confidence
            ))
        
        # Skapa exempel baserat på produktnamn (något lägre konfidens)
        if source and not source.startswith("Produkt "):
            examples.append(TrainingExample(
                user_input=f'-c "{source}"',
                ai_output=response,
                source=source,
                confidence=confidence * 0.9
            ))
        
        return examples

    def _format_clean_markdown(self, relation_groups: Dict[str, List[CompatibilityRelation]]) -> str:
        """Formaterar ett rent och strukturerat svar i markdown"""
        if not any(relation_groups.values()):
            return "Ingen kompatibilitetsinformation tillgänglig."

        # Använd första tillgängliga relationen för produktinformation
        first_relation = None
        for group in relation_groups.values():
            if group:
                first_relation = group[0]
                break
        
        if not first_relation:
            return "Ingen kompatibilitetsinformation tillgänglig."

        parts = []
        
        # Huvudrubrik
        product_name = first_relation.source_product.name.replace('**', '')
        parts.append(f"# Kompatibilitetsinformation för {product_name}\n")
        
        # Basinformation
        if first_relation.source_product.article_number:
            parts.append(f"**Artikelnummer:** {first_relation.source_product.article_number}  ")
        if first_relation.source_product.series:
            parts.append(f"**Serie:** {first_relation.source_product.series}  ")
        parts.append("")
        
        # Passar till - från basic relationer
        compat_info = self._get_clean_compatibility_info(relation_groups["basic"])
        if compat_info:
            parts.append("### Passar till")
            for info in compat_info:
                parts.append(f"- {info}  ")
            parts.append("")
        
        # Tekniska specifikationer - från tech relationer
        tech_specs = self._extract_tech_specs(relation_groups["tech"])
        if tech_specs:
            parts.append("### Tekniska specifikationer")
            for spec in tech_specs:
                parts.append(f"- {spec}  ")
            parts.append("")
        
        # Krav och villkor - från requirements relationer
        requirements = self._format_requirements(relation_groups["requirements"])
        if requirements:
            parts.append("### Krav")
            for req in requirements:
                parts.append(f"- {req}  ")
        
        return "\n".join(parts)

    def _get_clean_compatibility_info(self, relations: List[CompatibilityRelation]) -> List[str]:
        """Extraherar och rensar kompatibilitetsinformation"""
        compat_items = set()
        
        for relation in relations:
            if relation.target_product.name:
                name = relation.target_product.name
                # Rensa bort oönskad formatering och text
                name = name.replace('![]', '').strip()
                name = name.split('|')[0].strip()  # Ta bort tabellformatering
                
                if name and not name.startswith('_page') and len(name) > 3:
                    # Formatera om texten för bättre läsbarhet
                    name = name.replace('**', '')
                    name = name.strip('* ')
                    compat_items.add(name)
        
        return sorted(list(compat_items))

    def _extract_tech_specs(self, relations: List[CompatibilityRelation]) -> List[str]:
        """Extraherar tekniska specifikationer från alla tech-relationer"""
        specs = set()
        
        for relation in relations:
            context = relation.context or ""
            
            # Strömförbrukning
            if "mA" in context:
                current_specs = []
                if "låst" in context.lower():
                    pattern_locked = r'låst (\d+)mA'
                    locked_value = self._extract_value(context, pattern_locked)
                    current_specs.append(f"Låst läge: {locked_value} mA")
                if "olåst" in context.lower():
                    pattern_unlocked = r'olåst (\d+)mA'
                    unlocked_value = self._extract_value(context, pattern_unlocked)
                    current_specs.append(f"Olåst läge: {unlocked_value} mA")
                if current_specs:
                    specs.add("**Strömförbrukning:**")
                    specs.update(f"  - {spec}" for spec in current_specs)
            
            # IP-klass
            if "IP" in context:
                ip = self._extract_value(context, r'IP(\d{2})')
                if ip:
                    specs.add(f"**IP-klass:** IP{ip}")
        
        return sorted(list(specs))

    def _extract_value(self, text: str, pattern: str) -> str:
        """Extraherar värden med regex"""
        import re
        match = re.search(pattern, text)
        return match.group(1) if match else ""

    def _extract_functions(self, relation: CompatibilityRelation) -> List[str]:
        """Extraherar funktioner från villkor och kontext"""
        functions = set()
        
        for condition in relation.conditions:
            if condition.description:
                desc = condition.description.strip()
                if desc.lower().startswith(('kan ', 'har ', 'är ')):
                    functions.add(desc)
        
        return sorted(list(functions))

    def _extract_material_info(self, relation: CompatibilityRelation) -> List[str]:
        """Extraherar materialinformation"""
        materials = []
        context = relation.context or ""
        
        # Lägg till vanliga materialextraktioner här
        if "mattborstad" in context.lower():
            materials.append("**Yta:** Mattborstad krom")
        
        return materials

    def _format_requirements(self, relations: List[CompatibilityRelation]) -> List[str]:
        """Formaterar krav och villkor från alla requirement-relationer"""
        requirements = set()
        
        for relation in relations:
            for condition in relation.conditions:
                if condition.description:
                    req = condition.description.strip()
                    if req.lower().startswith(('kräver', 'måste')):
                        req = req[req.find(" ")+1:].strip()
                        if req.endswith('.'):
                            req = req[:-1]
                        requirements.add(req)
        
        return sorted(list(requirements))
