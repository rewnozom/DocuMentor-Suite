# Detaljerad Kompatibilitetsextraktionsrapport

**Datum och tid:** 2025-02-22 23:51:49

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

- **Totalt antal _pro-filer:** 646
- **Filer med kompatibilitetsinformation:** 618 (95.7%)
- **Filer utan kompatibilitetsinformation:** 27
- **Totalt antal kompatibilitetsrelationer:** 21295
- **Genomsnittligt antal relationer per dokument:** 34.5
- **Antal upptäckta potentiella nya fraser:** 0
- **Antal föreslagna nya mönster:** 10

## Relationstyper

Nedan visas fördelningen av olika typer av kompatibilitetsrelationer som hittades:

| Relationstyp | Antal träffar | Procentandel |
|--------------|--------------|---------------|
| condition | 12050 | 56.6% |
| version | 7167 | 33.7% |
| requires | 761 | 3.6% |
| basic | 589 | 2.8% |
| replacement | 258 | 1.2% |
| direct | 155 | 0.7% |
| fits | 104 | 0.5% |
| recommended | 100 | 0.5% |
| accessory | 72 | 0.3% |
| designed_for | 26 | 0.1% |
| negative | 9 | 0.0% |
| article_relation | 4 | 0.0% |

## Mönsterprestanda

Totalt används 155 mönster för extraktion, varav 77 gav träffar.

### Toppresterande mönster

De mönster som gav flest träffar:

| Mönsterindex | Grupp | Antal träffar | Procentandel | Mönster |
|--------------|-------|--------------|--------------|--------|
| 101 | condition | 10455 | 49.1% | `(?i)om\s+([^\.;]+)(?:\.|\;|$)` |
| 125 | version | 4299 | 20.2% | `(?i)(?:gen|g)(?:\.|:)\s*([^\.;]+)(?:\.|\;|$)` |
| 102 | condition | 1142 | 5.4% | `(?i)när\s+([^\.;]+)(?:\.|\;|$)` |
| 124 | version | 974 | 4.6% | `(?i)(?:ver|v)(?:\.|:)\s*([^\.;]+)(?:\.|\;|$)` |
| 128 | version | 850 | 4.0% | `(?i)typ(?:\s+|\:)([^\.;]+)(?:\.|\;|$)` |
| 38 | requires | 392 | 1.8% | `(?i)behöver\s+([^\.;]+)(?:\.|\;|$)` |
| 129 | version | 261 | 1.2% | `(?i)type(?:\s+|\:)([^\.;]+)(?:\.|\;|$)` |
| 1 | basic | 193 | 0.9% | `(?i)passar\s+(?:på|i)?\s*([^\.;]+)(?:\.|\;|$)` |
| 127 | version | 186 | 0.9% | `(?i)model(?:\s+|\:)([^\.;]+)(?:\.|\;|$)` |
| 31 | requires | 186 | 0.9% | `(?i)kräver\s+([^\.;]+)(?:\.|\;|$)` |

### Bottenprestanda mönster

De mönster som gav minst antal träffar (men fortfarande gav några träffar):

| Mönsterindex | Grupp | Antal träffar | Procentandel | Mönster |
|--------------|-------|--------------|--------------|--------|
| 85 | replacement | 1 | 0.0% | `(?i)ersätts\s+av\s+([^\.;]+)(?:\.|\;|$)` |
| 135 | negative | 1 | 0.0% | `(?i)(?:passar|fungerar)\s+(?:inte|ej)\s+(?:till|med|för)\s+([^\.;]+)(?...` |
| 54 | recommended | 1 | 0.0% | `(?i)ideal\s+for\s+([^\.;]+)(?:\.|\;|$)` |
| 110 | condition | 1 | 0.0% | `(?i)förut?sättning(?:ar)?:\s*([^\.;]+)(?:\.|\;|$)` |
| 143 | negative | 1 | 0.0% | `(?i)not\s+intended\s+for\s+([^\.;]+)(?:\.|\;|$)` |
| 67 | designed_for | 2 | 0.0% | `(?i)specially\s+designed\s+for\s+([^\.;]+)(?:\.|\;|$)` |
| 33 | requires | 2 | 0.0% | `(?i)måste\s+ha\s+([^\.;]+)(?:\.|\;|$)` |
| 60 | fits | 2 | 0.0% | `(?i)(?:can\s+be|är)\s+monterad\s+(?:på|i)\s+([^\.;]+)(?:\.|\;|$)` |
| 22 | direct | 2 | 0.0% | `(?i)kan\s+kopplas\s+till\s+([^\.;]+)(?:\.|\;|$)` |
| 76 | accessory | 2 | 0.0% | `(?i)accessor(?:y|ies)\s+for\s+([^\.;]+)(?:\.|\;|$)` |

### Mönstergruppernas prestanda

Prestanda per mönstergrupp:

| Mönstergrupp | Antal träffar | Procentandel |
|--------------|--------------|---------------|
| condition | 12050 | 56.6% |
| version | 7167 | 33.7% |
| requires | 761 | 3.6% |
| basic | 589 | 2.8% |
| replacement | 258 | 1.2% |
| direct | 155 | 0.7% |
| fits | 104 | 0.5% |
| recommended | 100 | 0.5% |
| accessory | 72 | 0.3% |
| designed_for | 26 | 0.1% |
| negative | 9 | 0.0% |
| article_relation | 4 | 0.0% |

## Upptäckta fraser och mönsterförslag

Baserat på analys av dokument och frekventa fraser, föreslås följande 10 nya mönster:

| Originalfras | Föreslagen relationstyp | Föreslagen regex | Förekomster |
|--------------|-------------------------|-----------------|-------------|
| #### **Kontraster** Prisma Button är designad för ... | designed_for | `(?i)#### **kontraster** prisma button är designad för ([^\.;]+)(?:\.|\;|$)` | 24 |
| Enheten fungerar normalt då indikeringsdiod på skå... | direct | `(?i)enheten fungerar normalt då indikeringsdiod på skåpluckans utsida lyser med ([^\.;]+)(?:\.|\;|$)` | 21 |
| Med närvarokontrollen ges även möjlighet att använ... | designed_for | `(?i)med närvarokontrollen ges även möjlighet att använda antalslarm där exempelvis en utgång kan användas för ([^\.;]+)(?:\.|\;|$)` | 14 |
| splitspindelfunktion fungerar alltid inre trycket ... | designed_for | `(?i)splitspindelfunktion fungerar alltid inre trycket för ([^\.;]+)(?:\.|\;|$)` | 14 |
| Det finns fyra utgångar på DIO-5084 2 st relälämpl... | designed_for | `(?i)det finns fyra utgångar på dio-5084 2 st relälämpliga för ([^\.;]+)(?:\.|\;|$)` | 14 |
| Enkelbalanserat kan användas för glaskross och bra... | designed_for | `(?i)enkelbalanserat kan användas för ([^\.;]+)(?:\.|\;|$)` | 14 |
| Electrolux Vision Light™ monteras på vägg, i för a... | direct | `(?i)electrolux vision light™ monteras på vägg, i för användare lämplig höjd att betrakta display och att manövrera med ([^\.;]+)(?:\.|\;|$)` | 14 |
| | Bästa alternativ<br>Bra alternativ<br>Möjlig<br>... | designed_for | `(?i)| bästa alternativ<br>bra alternativ<br>möjlig<br>tele, halogenfri, oskärmad: | ■<br>▲<br>● | systembuss | lokalbuss | flexkabel lokalbuss | terminalbuss | terminalbuss rs-485 | signaler | larmsignaler | lan | tele | electrolux network | |-----------------------------------------------------------------------------|------------------------------------------|------------|-----------|---------------------|--------------|---------------------|----------|--------------|-----|------|--------------------| | elqxb | 2x2x0,5 (0,2 mm²) | ▲ | ▲ | | ● | ▲ | | ■ ■ | | ■ | | | elqxb | 4x2x0,5 (0,2 mm²) | ▲ | ▲ | | | ▲ | | ■ ▲ | | ■ | | | elqxb | 6x2x0.5 (0,2 mm²) | ● | ● | | | ● | ▲ | ● | | ■ | | | elqxb | 10x2x0,5 (0,2 mm²) | ● | ● | | | ● | ● | ● | | ■ | | | elqxb | 2x2x0,5 (0,2 mm²) | ▲ | ▲ | | ● | ▲ | | ■ ■ | | ■ | | | elqxb | 4x2x0,5 (0,2 mm²) | ▲ | ▲ | | | ▲ | | ■ ▲ | | ■ | | | elqxb | 6x2x0,5 (0,2 mm²) | ● | ● | | | ● | ▲ | ● | | ■ | | | elqxb | 10x2x0,5 (0,2 mm²) | ● | ● | | | ● | ● | ● | | ■ | | | fqqxb | 6x0,22 | | | | | | | | | | | | 4-skruv, halogenfri, oskärmad: | | | | | | | | | | | | | elqxb | 1x4x0,5 (0,2 mm²) | | | | ■ | | ● | ▲ | | | | | eqqxb | 1x4x0,5 (0,2 mm²) | | | | ■ | | ● | ▲ | | | | | special, halogenfri, oskärmad: | | | | | | | | | | | | | rco kabel | 2x1x1,0 mm²+1x2x0,22mm2 (e-nr 48 866 62) | | ■ ■ | | | ■ | | | | | | | flqqbr | 2x1x1,0 mm²+2x2x0,22 mm² | | ■ ■ | | | | | | | | | | flaqqbr | 4x1x1,0 mm²+1x2x0,22mm2 | | ■ | | | | | | | | | | flaqqly | 2x1x1,0 mm²+1x2x0,22mm2 (inne och ute) | ▲ | ▲ | | | | | | | | | | electrolux nätverkskabel cmis 4x0,22mm2 | | | | | | | | | | | ■ | | cat, halogenfri, oskärmad: | | | | | | | | | | | | | utp lszh | (cat 5e) 4x2x0,5 (0,2 mm²) | ▲ | ▲ | | | ▲ | ● ● | | ■ | | | | utp lszh | (cat 6) 4x2x0,5 (0,2 mm²) | ▲ | ▲ | | | ▲ | ● | ● | ■ | | | angivna kabeltyper i tabellen ovan är enbart exempel på lämpliga kablar för ([^\.;]+)(?:\.|\;|$)` | 14 |
| Vid kabelförläggning utomhus eller i mark rekommen... | direct | `(?i)vid kabelförläggning utomhus eller i mark rekommenderas kabel förstärkt med ([^\.;]+)(?:\.|\;|$)` | 14 |
| Montering Använd lämplig skruv för montering på vä... | designed_for | `(?i)montering använd lämplig skruv för ([^\.;]+)(?:\.|\;|$)` | 13 |

Se den fullständiga listan i JSON-filen för föreslagna mönster.

## Dokument och filer

### Resultatfiler

- **Extraherade kompatibilitetsrelationer:** [compatibility_pro_20250222_235136.jsonl](extracted_data\compatibility\matched\compatibility_pro_20250222_235136.jsonl)
- **Dokument utan kompatibilitetsinformation:** [no_compatibility_pro_20250222_235136.jsonl](extracted_data\compatibility\unmatched\no_compatibility_pro_20250222_235136.jsonl)
- **Exempel på dokument utan kompatibilitet:** [samples_without_compatibility_20250222_235136.jsonl](extracted_data\compatibility\samples\samples_without_compatibility_20250222_235136.jsonl)
- **Upptäckta potentiella fraser:** [discovered_phrases_20250222_235136.jsonl](extracted_data\compatibility\discovered\discovered_phrases_20250222_235136.jsonl)
- **Mönsterprestanda (JSON):** [pattern_performance_20250222_235136.json](extracted_data\compatibility\patterns\pattern_performance_20250222_235136.json)
- **Valideringsrapport (JSON):** [validation_report_20250222_235136.json](extracted_data\compatibility\validation\validation_report_20250222_235136.json)
- **Sammanfattning (JSON):** [compatibility_pro_summary_20250222_235136.json](extracted_data\compatibility\reports\compatibility_pro_summary_20250222_235136.json)

### Relationsspecifika filer

- **accessory:** [accessory_20250222_235136.jsonl](extracted_data\compatibility\relations\accessory\accessory_20250222_235136.jsonl)
- **article_relation:** [article_relation_20250222_235136.jsonl](extracted_data\compatibility\relations\article_relation\article_relation_20250222_235136.jsonl)
- **basic:** [basic_20250222_235136.jsonl](extracted_data\compatibility\relations\basic\basic_20250222_235136.jsonl)
- **condition:** [condition_20250222_235136.jsonl](extracted_data\compatibility\relations\condition\condition_20250222_235136.jsonl)
- **designed_for:** [designed_for_20250222_235136.jsonl](extracted_data\compatibility\relations\designed_for\designed_for_20250222_235136.jsonl)
- **direct:** [direct_20250222_235136.jsonl](extracted_data\compatibility\relations\direct\direct_20250222_235136.jsonl)
- **fits:** [fits_20250222_235136.jsonl](extracted_data\compatibility\relations\fits\fits_20250222_235136.jsonl)
- **negative:** [negative_20250222_235136.jsonl](extracted_data\compatibility\relations\negative\negative_20250222_235136.jsonl)
- **recommended:** [recommended_20250222_235136.jsonl](extracted_data\compatibility\relations\recommended\recommended_20250222_235136.jsonl)
- **replacement:** [replacement_20250222_235136.jsonl](extracted_data\compatibility\relations\replacement\replacement_20250222_235136.jsonl)
- **requires:** [requires_20250222_235136.jsonl](extracted_data\compatibility\relations\requires\requires_20250222_235136.jsonl)
- **version:** [version_20250222_235136.jsonl](extracted_data\compatibility\relations\version\version_20250222_235136.jsonl)

## Nästa steg

Baserat på denna analys rekommenderas följande åtgärder:

1. **Granska upptäckta fraser** för att identifiera nya mönster och förbättra befintliga
2. **Implementera föreslagna mönster** och jämför resultaten i nästa körning
3. **Förfina lågpresterande mönster** eller överväg att ta bort dem om de är redundanta
4. **Utveckla specifika extraktorer för andra dokumenttyper** (_TEK, _produktblad, etc.)
5. **Expandera NLP-metoder** för att upptäcka mer sofistikerade relationer
6. **Validera extraherade relationer** med produkt-till-produktkontroller

---

Rapport genererad: 2025-02-22 23:51:49
