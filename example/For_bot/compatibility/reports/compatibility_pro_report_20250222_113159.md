# Detaljerad Kompatibilitetsextraktionsrapport

**Datum och tid:** 2025-02-22 11:32:02

Denna rapport innehåller en detaljerad analys av kompatibilitetsinformation extraherad från _pro-dokument.

## Innehåll

1. [Sammanfattning](#sammanfattning)
2. [Relationstyper](#relationstyper)
3. [Mönsterprestanda](#mönsterprestanda)
   - [Toppresterande mönster](#toppresterande-mönster)
   - [Bottenprestanda mönster](#bottenprestanda-mönster)
   - [Mönstergruppernas prestanda](#mönstergruppernas-prestanda)
4. [Upptäckta fraser och mönsterförslag](#upptäckta-fraser-och-mönsterförslag)
5. [Dokument och filer](#dokument-och-filer)
6. [Nästa steg](#nästa-steg)

## Sammanfattning

- **Totalt antal _pro-filer:** 363
- **Filer med kompatibilitetsinformation:** 342 (94.2%)
- **Filer utan kompatibilitetsinformation:** 21
- **Totalt antal kompatibilitetsrelationer:** 4049
- **Genomsnittligt antal relationer per dokument:** 11.8
- **Antal upptäckta potentiella nya fraser:** 0
- **Antal föreslagna nya mönster:** 6

## Relationstyper

Nedan visas fördelningen av olika typer av kompatibilitetsrelationer som hittades:

| Relationstyp | Antal träffar | Procentandel |
|--------------|--------------|---------------|
| condition | 1887 | 46.6% |
| version | 1526 | 37.7% |
| basic | 272 | 6.7% |
| requires | 145 | 3.6% |
| replacement | 65 | 1.6% |
| recommended | 52 | 1.3% |
| direct | 48 | 1.2% |
| fits | 22 | 0.5% |
| accessory | 15 | 0.4% |
| designed_for | 14 | 0.3% |
| article_relation | 3 | 0.1% |

## Mönsterprestanda

Totalt används 155 mönster för extraktion, varav 53 gav träffar.

### Toppresterande mönster

De mönster som gav flest träffar:

| Mönsterindex | Grupp | Antal träffar | Procentandel | Mönster |
|--------------|-------|--------------|--------------|--------|
| 101 | condition | 1483 | 36.6% | `(?i)om\s+([^\.;]+)(?:\.|\;|$)` |
| 125 | version | 809 | 20.0% | `(?i)(?:gen|g)(?:\.|:)\s*([^\.;]+)(?:\.|\;|$)` |
| 102 | condition | 361 | 8.9% | `(?i)när\s+([^\.;]+)(?:\.|\;|$)` |
| 124 | version | 243 | 6.0% | `(?i)(?:ver|v)(?:\.|:)\s*([^\.;]+)(?:\.|\;|$)` |
| 128 | version | 239 | 5.9% | `(?i)typ(?:\s+|\:)([^\.;]+)(?:\.|\;|$)` |
| 9 | basic | 114 | 2.8% | `(?i)avsedd\s+för\s+([^\.;]+)(?:\.|\;|$)` |
| 38 | requires | 79 | 2.0% | `(?i)behöver\s+([^\.;]+)(?:\.|\;|$)` |
| 126 | version | 75 | 1.9% | `(?i)modell(?:\s+|\:)([^\.;]+)(?:\.|\;|$)` |
| 1 | basic | 63 | 1.6% | `(?i)passar\s+(?:på|i)?\s*([^\.;]+)(?:\.|\;|$)` |
| 94 | replacement | 53 | 1.3% | `(?i)(?:istället|instead)\s+(?:för|of)\s+([^\.;]+)(?:\.|\;|$)` |

### Bottenprestanda mönster

De mönster som gav minst antal träffar (men fortfarande gav några träffar):

| Mönsterindex | Grupp | Antal träffar | Procentandel | Mönster |
|--------------|-------|--------------|--------------|--------|
| 54 | recommended | 1 | 0.0% | `(?i)ideal\s+for\s+([^\.;]+)(?:\.|\;|$)` |
| 14 | basic | 1 | 0.0% | `(?i)(?:tillval|option)\s+(?:till|för)\s+([^\.;]+)(?:\.|\;|$)` |
| 79 | accessory | 1 | 0.0% | `(?i)(?:tillval|option)\s+(?:till|för)\s+([^\.;]+)(?:\.|\;|$)` |
| 97 | condition | 2 | 0.0% | `(?i)(?:endast|bara)\s+(?:vid|för|med)\s+([^\.;]+)(?:\.|\;|$)` |
| 145 | article_relation | 3 | 0.1% | `(?i)passar\s+(?:till|med|för)\s+(?:[^\.;]*?)((?:\d{5,8}|E-\s*\d{7})(?:...` |
| 3 | basic | 3 | 0.1% | `(?i)compatible\s+with\s+([^\.;]+)(?:\.|\;|$)` |
| 18 | direct | 3 | 0.1% | `(?i)compatible\s+with\s+([^\.;]+)(?:\.|\;|$)` |
| 12 | basic | 3 | 0.1% | `(?i)rekommenderas?\s+(?:till|med|för)\s+([^\.;]+)(?:\.|\;|$)` |
| 45 | recommended | 3 | 0.1% | `(?i)rekommenderas?\s+(?:till|med|för)\s+([^\.;]+)(?:\.|\;|$)` |
| 55 | recommended | 3 | 0.1% | `(?i)perfekt\s+för\s+([^\.;]+)(?:\.|\;|$)` |

### Mönstergruppernas prestanda

Prestanda per mönstergrupp:

| Mönstergrupp | Antal träffar | Procentandel |
|--------------|--------------|---------------|
| condition | 1887 | 46.6% |
| version | 1526 | 37.7% |
| basic | 272 | 6.7% |
| requires | 145 | 3.6% |
| replacement | 65 | 1.6% |
| recommended | 52 | 1.3% |
| direct | 48 | 1.2% |
| fits | 22 | 0.5% |
| accessory | 15 | 0.4% |
| designed_for | 14 | 0.3% |
| article_relation | 3 | 0.1% |

## Upptäckta fraser och mönsterförslag

Baserat på analys av dokument och frekventa fraser, föreslås följande 6 nya mönster:

| Originalfras | Föreslagen relationstyp | Föreslagen regex | Förekomster |
|--------------|-------------------------|-----------------|-------------|
| #### **Kontraster** Prisma Button är designad för ... | designed_for | `(?i)#### **kontraster** prisma button är designad för ([^\.;]+)(?:\.|\;|$)` | 12 |
| **vanderbiltindustries.com** @VanderbiltInd Vander... | designed_for | `(?i)**vanderbiltindustries.com** @vanderbiltind vanderbilt industries ## **vanderbilt international ltd.** clonshaugh business and technology park clonshaugh, dublin d17 kv 84, ireland +353 1 437 2560 ![](_page_3_picture_0.jpeg) ## **tillbehör:** ### **pr1 - reläkort till omnis psu 5a-10a** utökningskort för ([^\.;]+)(?:\.|\;|$)` | 5 |
| ECO-serien kan användas både med AGM-batterier och... | direct | `(?i)eco-serien kan användas både med ([^\.;]+)(?:\.|\;|$)` | 4 |
| Kan användas för styrning av port eller vidaresänd... | designed_for | `(?i)kan användas för ([^\.;]+)(?:\.|\;|$)` | 3 |
| Designad för att uppfylla höga säkerhetskrav.... | designed_for | `(?i)designad för ([^\.;]+)(?:\.|\;|$)` | 2 |
| ## Användningsområde PowerWatch kan användas för a... | designed_for | `(?i)## användningsområde powerwatch kan användas för ([^\.;]+)(?:\.|\;|$)` | 2 |

Se den fullständiga listan i JSON-filen för föreslagna mönster.

## Dokument och filer

### Resultatfiler

- **Extraherade kompatibilitetsrelationer:** [compatibility_pro_20250222_113159.jsonl](extracted_data\compatibility\matched\compatibility_pro_20250222_113159.jsonl)
- **Dokument utan kompatibilitetsinformation:** [no_compatibility_pro_20250222_113159.jsonl](extracted_data\compatibility\unmatched\no_compatibility_pro_20250222_113159.jsonl)
- **Exempel på dokument utan kompatibilitet:** [samples_without_compatibility_20250222_113159.jsonl](extracted_data\compatibility\samples\samples_without_compatibility_20250222_113159.jsonl)
- **Upptäckta potentiella fraser:** [discovered_phrases_20250222_113159.jsonl](extracted_data\compatibility\discovered\discovered_phrases_20250222_113159.jsonl)
- **Mönsterprestanda (JSON):** [pattern_performance_20250222_113159.json](extracted_data\compatibility\patterns\pattern_performance_20250222_113159.json)
- **Valideringsrapport (JSON):** [validation_report_20250222_113159.json](extracted_data\compatibility\validation\validation_report_20250222_113159.json)
- **Sammanfattning (JSON):** [compatibility_pro_summary_20250222_113159.json](extracted_data\compatibility\reports\compatibility_pro_summary_20250222_113159.json)

### Relationsspecifika filer

- **accessory:** [accessory_20250222_113159.jsonl](extracted_data\compatibility\relations\accessory\accessory_20250222_113159.jsonl)
- **article_relation:** [article_relation_20250222_113159.jsonl](extracted_data\compatibility\relations\article_relation\article_relation_20250222_113159.jsonl)
- **basic:** [basic_20250222_113159.jsonl](extracted_data\compatibility\relations\basic\basic_20250222_113159.jsonl)
- **condition:** [condition_20250222_113159.jsonl](extracted_data\compatibility\relations\condition\condition_20250222_113159.jsonl)
- **designed_for:** [designed_for_20250222_113159.jsonl](extracted_data\compatibility\relations\designed_for\designed_for_20250222_113159.jsonl)
- **direct:** [direct_20250222_113159.jsonl](extracted_data\compatibility\relations\direct\direct_20250222_113159.jsonl)
- **fits:** [fits_20250222_113159.jsonl](extracted_data\compatibility\relations\fits\fits_20250222_113159.jsonl)
- **recommended:** [recommended_20250222_113159.jsonl](extracted_data\compatibility\relations\recommended\recommended_20250222_113159.jsonl)
- **replacement:** [replacement_20250222_113159.jsonl](extracted_data\compatibility\relations\replacement\replacement_20250222_113159.jsonl)
- **requires:** [requires_20250222_113159.jsonl](extracted_data\compatibility\relations\requires\requires_20250222_113159.jsonl)
- **version:** [version_20250222_113159.jsonl](extracted_data\compatibility\relations\version\version_20250222_113159.jsonl)

## Nästa steg

Baserat på denna analys rekommenderas följande åtgärder:

1. **Granska upptäckta fraser** för att identifiera nya mönster och förbättra befintliga
2. **Implementera föreslagna mönster** och jämför resultaten i nästa körning
3. **Förfina lågpresterande mönster** eller överväg att ta bort dem om de är redundanta
4. **Utveckla specifika extraktorer för andra dokumenttyper** (_TEK, _produktblad, etc.)
5. **Expandera NLP-metoder** för att upptäcka mer sofistikerade relationer
6. **Validera extraherade relationer** med produkt-till-produktkontroller

---

Rapport genererad: 2025-02-22 11:32:02
