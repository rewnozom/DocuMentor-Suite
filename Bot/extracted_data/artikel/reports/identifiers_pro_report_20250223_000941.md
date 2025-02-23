# Detaljerad Produktidentifieringsrapport

**Datum och tid:** 2025-02-23 00:09:52

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

- **Totalt antal _pro-filer:** 646
- **Filer med produktidentifierare:** 399 (61.8%)
- **Filer utan produktidentifierare:** 240
- **Totalt antal extraherade identifierare:** 1119
- **Genomsnittligt antal identifierare per dokument:** 2.8
- **Antal upptäckta potentiella nya format:** 3716
- **Antal föreslagna nya mönster:** 12
- **Valideringsstatus:** 219 giltiga, 900 ogiltiga

## Identifierartyper

Nedan visas fördelningen av olika typer av produktidentifierare som hittats:

| Identifierartyp | Antal | Procentandel |
|----------------|-------|---------------|
| Artikelnummer | 833 | 74.4% |
| EAN-13 | 113 | 10.1% |
| E-nummer | 94 | 8.4% |
| UPC-A | 65 | 5.8% |
| EAN-8 | 14 | 1.3% |

## Mönsterprestanda

Totalt används 49 mönster för extraktion, varav 10 gav träffar.

### Toppresterande mönster

De mönster som gav flest träffar:

| Mönsterindex | Grupp | Antal träffar | Procentandel | Mönster |
|--------------|-------|--------------|--------------|--------|
| 25 | article | 566 | 50.6% | `(?i)Art\.?:?\s*([A-Z0-9]{5,10})(?![A-Z0-9])` |
| 24 | article | 153 | 13.7% | `(?i)Artikel:?\s*([A-Z0-9]{5,10})(?![A-Z0-9])` |
| 23 | article | 93 | 8.3% | `(?i)REF\.?\s*[:.\-]?\s*([A-Z0-9]{5,10})(?![A-Z0-9])` |
| 9 | enummer | 91 | 8.1% | `(?i)E-n[ru](?:mmer)?[:.\-]?\s*(\d{7})(?!\d)` |
| 5 | ean13 | 65 | 5.8% | `(?<!\d)(\d{13})(?!\d)` |
| 40 | upc | 65 | 5.8% | `(?<!\d)(\d{12})(?!\d)` |
| 0 | ean13 | 48 | 4.3% | `(?i)EAN(?:-13)?[:.\-]?\s*(\d{13})(?!\d)` |
| 16 | article | 24 | 2.1% | `(?i)Art(?:ikel)?\.?(?:nummer|nr)[:.\-]?\s*([A-Z0-9]{5,10})(?![A-Z0-9])` |
| 14 | article | 13 | 1.2% | `(?i)Art(?:ikel)?\.?n[ro]\.?[:.\-]?\s*([A-Z0-9]{5,10})(?![A-Z0-9])` |
| 13 | enummer | 1 | 0.1% | `(?<![a-zA-Z0-9])E(\d{7})(?!\d)` |

### Bottenprestanda mönster

De mönster som gav minst antal träffar (men fortfarande gav några träffar):

| Mönsterindex | Grupp | Antal träffar | Procentandel | Mönster |
|--------------|-------|--------------|--------------|--------|

### Mönstergruppernas prestanda

Prestanda per mönstergrupp:

| Mönstergrupp | Antal träffar | Procentandel |
|--------------|--------------|---------------|
| article | 849 | 75.9% |
| ean13 | 113 | 10.1% |
| enummer | 92 | 8.2% |
| upc | 65 | 5.8% |

## Validering och datakvalitet

Av totalt 1119 extraherade identifierare är 219 (19.6%) validerade som giltiga.

### Valideringsresultat per identifierartyp

| Identifierartyp | Antal valida | Antal ogiltiga | Valideringsfrekvens |
|-----------------|--------------|----------------|-----------------------|
| EAN-13 | 108 | 5 | 95.6% |
| Artikelnummer | 16 | 817 | 1.9% |
| E-nummer | 94 | 0 | 100.0% |
| UPC-A | 0 | 65 | 0.0% |
| EAN-8 | 1 | 13 | 7.1% |

### Vanliga valideringsfel

| Identifierartyp | Identifierare | Original | Felmeddelande |
|-----------------|---------------|----------|---------------|
| EAN-13 | 5785143875090 | 5785143875090 | Felaktig kontrollsiffra (förväntad: 2, faktisk: 0) |
| EAN-13 | 5785143875090 | 5785143875090 | Felaktig kontrollsiffra (förväntad: 2, faktisk: 0) |
| EAN-13 | 5785143875090 | 5785143875090 | Felaktig kontrollsiffra (förväntad: 2, faktisk: 0) |
| EAN-13 | 5785143875090 | 5785143875090 | Felaktig kontrollsiffra (förväntad: 2, faktisk: 0) |
| EAN-13 | 5785143875090 | 5785143875090 | Felaktig kontrollsiffra (förväntad: 2, faktisk: 0) |
| Artikelnummer | erences | erences | För kort artikelnummer |
| Artikelnummer | erence | erence | För kort artikelnummer |
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

## Upptäckta format och mönsterförslag

Baserat på analys av dokument och frekventa identifieringsformat, föreslås följande 12 nya mönster:

| Nyckelord | Potentiell typ | Föreslagen regex | Förekomster |
|-----------|---------------|-----------------|-------------|
| id | Produkt-ID | `r'(?i)id[:\s]+([A-Z0-9\-\.]+)'` | 3240 |
| product | Okänd identifierare | `r'(?i)product[:\s]+([A-Z0-9\-\.]+)'` | 148 |
| number | Okänd identifierare | `r'(?i)number[:\s]+([A-Z0-9\-\.]+)'` | 108 |
| code | Produktkod | `r'(?i)code[:\s]+([A-Z0-9\-\.]+)'` | 60 |
| nummer | Okänd identifierare | `r'(?i)nummer[:\s]+([A-Z0-9\-\.]+)'` | 45 |
| kod | Produktkod | `r'(?i)kod[:\s]+([A-Z0-9\-\.]+)'` | 36 |
| model | Okänd identifierare | `r'(?i)model[:\s]+([A-Z0-9\-\.]+)'` | 22 |
| produkt | Okänd identifierare | `r'(?i)produkt[:\s]+([A-Z0-9\-\.]+)'` | 19 |
| ean | EAN-13 | `r'(?i)ean[:\s]+([A-Z0-9\-\.]+)'` | 15 |
| modell | Okänd identifierare | `r'(?i)modell[:\s]+([A-Z0-9\-\.]+)'` | 14 |
| item | Okänd identifierare | `r'(?i)item[:\s]+([A-Z0-9\-\.]+)'` | 7 |
| serienummer | Okänd identifierare | `r'(?i)serienummer[:\s]+([A-Z0-9\-\.]+)'` | 2 |

Se den fullständiga listan i JSON-filen för föreslagna mönster.

## Dokument och filer

### Resultatfiler

- **Extraherade produktidentifierare:** [identifiers_pro_20250223_000941.jsonl](extracted_data\artikel\matched\identifiers_pro_20250223_000941.jsonl)
- **Dokument utan identifierare:** [no_identifiers_pro_20250223_000941.jsonl](extracted_data\artikel\unmatched\no_identifiers_pro_20250223_000941.jsonl)
- **Exempel på dokument utan identifierare:** [samples_without_identifiers_20250223_000941.jsonl](extracted_data\artikel\samples\samples_without_identifiers_20250223_000941.jsonl)
- **Upptäckta potentiella format:** [discovered_formats_20250223_000941.jsonl](extracted_data\artikel\discovered\discovered_formats_20250223_000941.jsonl)
- **Mönsterprestanda (JSON):** [pattern_performance_20250223_000941.json](extracted_data\artikel\patterns\pattern_performance_20250223_000941.json)
- **Validering (JSON):** [validation_report_20250223_000941.json](extracted_data\artikel\validation\validation_report_20250223_000941.json)
- **Sammanfattning (JSON):** [identifiers_pro_summary_20250223_000941.json](extracted_data\artikel\reports\identifiers_pro_summary_20250223_000941.json)

### Identifierartypspecifika filer

- **Artikelnummer:** [Artikelnummer_20250223_000941.jsonl](extracted_data\artikel\types\Artikelnummer\Artikelnummer_20250223_000941.jsonl)
- **E-nummer:** [E-nummer_20250223_000941.jsonl](extracted_data\artikel\types\E-nummer\E-nummer_20250223_000941.jsonl)
- **EAN-13:** [EAN-13_20250223_000941.jsonl](extracted_data\artikel\types\EAN-13\EAN-13_20250223_000941.jsonl)
- **EAN-8:** [EAN-8_20250223_000941.jsonl](extracted_data\artikel\types\EAN-8\EAN-8_20250223_000941.jsonl)
- **UPC-A:** [UPC-A_20250223_000941.jsonl](extracted_data\artikel\types\UPC-A\UPC-A_20250223_000941.jsonl)

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

Rapport genererad: 2025-02-23 00:09:52
