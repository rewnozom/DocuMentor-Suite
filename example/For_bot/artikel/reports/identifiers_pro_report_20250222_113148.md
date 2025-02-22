# Detaljerad Produktidentifieringsrapport

**Datum och tid:** 2025-02-22 11:31:53

Denna rapport innehåller en detaljerad analys av produktidentifierare (EAN, artikelnummer, etc.) extraherade från _pro-dokument.

## Innehåll

1. [Sammanfattning](#sammanfattning)
2. [Identifierartyper](#identifierartyper)
3. [Mönsterprestanda](#mönsterprestanda)
   - [Toppresterande mönster](#toppresterande-mönster)
   - [Bottenprestanda mönster](#bottenprestanda-mönster)
   - [Mönstergruppernas prestanda](#mönstergruppernas-prestanda)
4. [Validering och datakvalitet](#validering-och-datakvalitet)
5. [Upptäckta format och mönsterförslag](#upptäckta-format-och-mönsterförslag)
6. [Dokument och filer](#dokument-och-filer)
7. [Nästa steg](#nästa-steg)

## Sammanfattning

- **Totalt antal _pro-filer:** 363
- **Filer med produktidentifierare:** 258 (71.1%)
- **Filer utan produktidentifierare:** 102
- **Totalt antal extraherade identifierare:** 764
- **Genomsnittligt antal identifierare per dokument:** 3.0
- **Antal upptäckta potentiella nya format:** 389
- **Antal föreslagna nya mönster:** 8
- **Valideringsstatus:** 216 giltiga, 548 ogiltiga

## Identifierartyper

Nedan visas fördelningen av olika typer av produktidentifierare som hittats:

| Identifierartyp | Antal | Procentandel |
|----------------|-------|---------------|
| Artikelnummer | 487 | 63.7% |
| EAN-13 | 107 | 14.0% |
| E-nummer | 92 | 12.0% |
| UPC-A | 64 | 8.4% |
| EAN-8 | 14 | 1.8% |

## Mönsterprestanda

Totalt används 49 mönster för extraktion, varav 10 gav träffar.

### Toppresterande mönster

De mönster som gav flest träffar:

| Mönsterindex | Grupp | Antal träffar | Procentandel | Mönster |
|--------------|-------|--------------|--------------|--------|
| 25 | article | 301 | 39.4% | `(?i)Art\.?:?\s*([A-Z0-9]{5,10})(?![A-Z0-9])` |
| 24 | article | 139 | 18.2% | `(?i)Artikel:?\s*([A-Z0-9]{5,10})(?![A-Z0-9])` |
| 9 | enummer | 91 | 11.9% | `(?i)E-n[ru](?:mmer)?[:.\-]?\s*(\d{7})(?!\d)` |
| 40 | upc | 64 | 8.4% | `(?<!\d)(\d{12})(?!\d)` |
| 5 | ean13 | 59 | 7.7% | `(?<!\d)(\d{13})(?!\d)` |
| 0 | ean13 | 48 | 6.3% | `(?i)EAN(?:-13)?[:.\-]?\s*(\d{13})(?!\d)` |
| 23 | article | 24 | 3.1% | `(?i)REF\.?\s*[:.\-]?\s*([A-Z0-9]{5,10})(?![A-Z0-9])` |
| 16 | article | 24 | 3.1% | `(?i)Art(?:ikel)?\.?(?:nummer|nr)[:.\-]?\s*([A-Z0-9]{5,10})(?![A-Z0-9])` |
| 14 | article | 13 | 1.7% | `(?i)Art(?:ikel)?\.?n[ro]\.?[:.\-]?\s*([A-Z0-9]{5,10})(?![A-Z0-9])` |
| 13 | enummer | 1 | 0.1% | `(?<![a-zA-Z0-9])E(\d{7})(?!\d)` |

### Bottenprestanda mönster

De mönster som gav minst antal träffar (men fortfarande gav några träffar):

| Mönsterindex | Grupp | Antal träffar | Procentandel | Mönster |
|--------------|-------|--------------|--------------|--------|

### Mönstergruppernas prestanda

Prestanda per mönstergrupp:

| Mönstergrupp | Antal träffar | Procentandel |
|--------------|--------------|---------------|
| article | 501 | 65.6% |
| ean13 | 107 | 14.0% |
| enummer | 92 | 12.0% |
| upc | 64 | 8.4% |

## Validering och datakvalitet

Av totalt 764 extraherade identifierare är 216 (28.3%) validerade som giltiga.

### Valideringsresultat per identifierartyp

| Identifierartyp | Antal valida | Antal ogiltiga | Valideringsfrekvens |
|-----------------|--------------|----------------|-----------------------|
| EAN-13 | 107 | 0 | 100.0% |
| Artikelnummer | 16 | 471 | 3.3% |
| E-nummer | 92 | 0 | 100.0% |
| UPC-A | 0 | 64 | 0.0% |
| EAN-8 | 1 | 13 | 7.1% |

### Vanliga valideringsfel

| Identifierartyp | Identifierare | Original | Felmeddelande |
|-----------------|---------------|----------|---------------|
| Artikelnummer | erences | erences | För kort artikelnummer |
| Artikelnummer | erence | erence | För kort artikelnummer |
| Artikelnummer | nummer | nummer | För kort artikelnummer |
| Artikelnummer | ikelnummer | ikelnummer | För kort artikelnummer |
| Artikelnummer | nummer | nummer | För kort artikelnummer |
| Artikelnummer | ikelnummer | ikelnummer | För kort artikelnummer |
| Artikelnummer | nummer | nummer | För kort artikelnummer |
| Artikelnummer | ikelnummer | ikelnummer | För kort artikelnummer |
| Artikelnummer | nummer | nummer | För kort artikelnummer |
| Artikelnummer | ikelnummer | ikelnummer | För kort artikelnummer |
| Artikelnummer | nummer | nummer | För kort artikelnummer |
| Artikelnummer | ikelnummer | ikelnummer | För kort artikelnummer |
| Artikelnummer | nummer | nummer | För kort artikelnummer |
| Artikelnummer | ikelnummer | ikelnummer | För kort artikelnummer |
| Artikelnummer | erences | erences | För kort artikelnummer |
| Artikelnummer | Summary | Summary | För kort artikelnummer |
| Artikelnummer | erences | erences | För kort artikelnummer |
| Artikelnummer | erence | erence | För kort artikelnummer |
| Artikelnummer | erences | erences | För kort artikelnummer |
| Artikelnummer | erence | erence | För kort artikelnummer |

## Upptäckta format och mönsterförslag

Baserat på analys av dokument och frekventa identifieringsformat, föreslås följande 8 nya mönster:

| Nyckelord | Potentiell typ | Föreslagen regex | Förekomster |
|-----------|---------------|-----------------|-------------|
| id | Produkt-ID | `r'(?i)id[:\s]+([A-Z0-9\-\.]+)'` | 356 |
| number | Okänd identifierare | `r'(?i)number[:\s]+([A-Z0-9\-\.]+)'` | 10 |
| product | Okänd identifierare | `r'(?i)product[:\s]+([A-Z0-9\-\.]+)'` | 5 |
| item | Okänd identifierare | `r'(?i)item[:\s]+([A-Z0-9\-\.]+)'` | 4 |
| modell | Okänd identifierare | `r'(?i)modell[:\s]+([A-Z0-9\-\.]+)'` | 4 |
| produkt | Okänd identifierare | `r'(?i)produkt[:\s]+([A-Z0-9\-\.]+)'` | 3 |
| ean | EAN-13 | `r'(?i)ean[:\s]+([A-Z0-9\-\.]+)'` | 2 |
| code | Produktkod | `r'(?i)code[:\s]+([A-Z0-9\-\.]+)'` | 2 |

Se den fullständiga listan i JSON-filen för föreslagna mönster.

## Dokument och filer

### Resultatfiler

- **Extraherade produktidentifierare:** [identifiers_pro_20250222_113148.jsonl](extracted_data\artikel\matched\identifiers_pro_20250222_113148.jsonl)
- **Dokument utan identifierare:** [no_identifiers_pro_20250222_113148.jsonl](extracted_data\artikel\unmatched\no_identifiers_pro_20250222_113148.jsonl)
- **Exempel på dokument utan identifierare:** [samples_without_identifiers_20250222_113148.jsonl](extracted_data\artikel\samples\samples_without_identifiers_20250222_113148.jsonl)
- **Upptäckta potentiella format:** [discovered_formats_20250222_113148.jsonl](extracted_data\artikel\discovered\discovered_formats_20250222_113148.jsonl)
- **Mönsterprestanda (JSON):** [pattern_performance_20250222_113148.json](extracted_data\artikel\patterns\pattern_performance_20250222_113148.json)
- **Validering (JSON):** [validation_report_20250222_113148.json](extracted_data\artikel\validation\validation_report_20250222_113148.json)
- **Sammanfattning (JSON):** [identifiers_pro_summary_20250222_113148.json](extracted_data\artikel\reports\identifiers_pro_summary_20250222_113148.json)

### Identifierartypspecifika filer

- **Artikelnummer:** [Artikelnummer_20250222_113148.jsonl](extracted_data\artikel\types\Artikelnummer\Artikelnummer_20250222_113148.jsonl)
- **E-nummer:** [E-nummer_20250222_113148.jsonl](extracted_data\artikel\types\E-nummer\E-nummer_20250222_113148.jsonl)
- **EAN-13:** [EAN-13_20250222_113148.jsonl](extracted_data\artikel\types\EAN-13\EAN-13_20250222_113148.jsonl)
- **EAN-8:** [EAN-8_20250222_113148.jsonl](extracted_data\artikel\types\EAN-8\EAN-8_20250222_113148.jsonl)
- **UPC-A:** [UPC-A_20250222_113148.jsonl](extracted_data\artikel\types\UPC-A\UPC-A_20250222_113148.jsonl)

## Nästa steg

Baserat på denna analys rekommenderas följande åtgärder:

1. **Granska upptäckta format** för att identifiera nya mönster och förbättra befintliga
2. **Implementera föreslagna mönster** och jämför resultaten i nästa körning
3. **Förfina valideringslogiken** för att öka antalet korrekt validerade identifierare
4. **Utveckla specifika extraktorer för andra dokumenttyper** (_TEK, _produktblad, etc.)
5. **Expandera mönster för särskilt viktiga identifierartyper** som EAN-13 och artikelnummer
6. **Jämföra extraherade identifierare mot en känd databas** för att validera resultat
7. **Utveckla system för att följa artiklar över hela dokumentsetet** baserat på EAN-koder

---

Rapport genererad: 2025-02-22 11:31:53
