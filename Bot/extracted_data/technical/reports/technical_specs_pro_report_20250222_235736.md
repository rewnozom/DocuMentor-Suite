# Detaljerad Teknisk Specifikationsrapport

**Datum och tid:** 2025-02-22 23:58:39

Denna rapport innehåller en detaljerad analys av tekniska specifikationer extraherade från _pro-dokument.

## Innehåll

1. [Sammanfattning](#sammanfattning)
2. [Kategorifördelning](#kategorifördelning)
3. [Mönsterprestanda](#mönsterprestanda)
   - [Toppresterande mönster](#toppresterande-mönster)
   - [Bottenprestanda mönster](#bottenprestanda-mönster)
   - [Mönstergruppernas prestanda](#mönstergruppernas-prestanda)
4. [Validering och datakvalitet](#validering-och-datakvalitet)
5. [Upptäckta specifikationer och mönsterförslag](#upptäckta-specifikationer-och-mönsterförslag)
6. [Dokument och filer](#dokument-och-filer)
7. [Nästa steg](#nästa-steg)

## Sammanfattning

- **Totalt antal _pro-filer:** 646
- **Filer med tekniska specifikationer:** 301 (46.6%)
- **Filer utan tekniska specifikationer:** 345
- **Totalt antal extraherade specifikationer:** 949
- **Genomsnittligt antal specifikationer per dokument:** 3.2
- **Antal upptäckta potentiella nya specifikationer:** 1449
- **Antal föreslagna nya mönster:** 345
- **Valideringsstatus:** 949 giltiga, 0 ogiltiga

## Kategorifördelning

Nedan visas fördelningen av tekniska specifikationer per kategori:

| Teknisk kategori | Antal specifikationer | Procentandel |
|-----------------|----------------------|---------------|
| ELECTRICAL | 210 | 22.1% |
| DIMENSIONS | 160 | 16.9% |
| MATERIAL | 145 | 15.3% |
| CONNECTION | 125 | 13.2% |
| MISCELLANEOUS | 99 | 10.4% |
| COLOR | 73 | 7.7% |
| PERFORMANCE | 54 | 5.7% |
| ENVIRONMENTAL | 42 | 4.4% |
| NETWORK | 29 | 3.1% |
| WEIGHT | 5 | 0.5% |
| TEMPERATURE | 5 | 0.5% |
| FLOW | 1 | 0.1% |
| LIGHTING | 1 | 0.1% |
| PRESSURE | 0 | 0.0% |
| MECHANICAL | 0 | 0.0% |
| CAPACITY | 0 | 0.0% |
| ENERGY | 0 | 0.0% |
| AUDIO | 0 | 0.0% |
| VIDEO | 0 | 0.0% |
| FREQUENCY | 0 | 0.0% |
| RUNTIME | 0 | 0.0% |
| PROTECTION | 0 | 0.0% |

## Mönsterprestanda

Totalt används 239 mönster för extraktion, varav 58 gav träffar.

### Toppresterande mönster

De mönster som gav flest träffar:

| Mönsterindex | Grupp | Antal träffar | Procentandel | Mönster |
|--------------|-------|--------------|--------------|--------|
| 113 | material | 144 | 15.2% | `(?i)(?:material|material)\s*:\s*([^\.]+)` |
| 151 | connection | 104 | 11.0% | `(?i)(?:utgångar|outputs)\s*:\s*([^\.]+)` |
| 43 | electrical | 100 | 10.5% | `(?i)(?:batterityp|battery type)\s*:\s*([^\.]+)` |
| 123 | color | 71 | 7.5% | `(?i)(?:färg|color)\s*:\s*([^\.]+)` |
| 52 | electrical | 52 | 5.5% | `(?i)(?:skyddsklass|protection class)\s*:\s*([^\.]+)` |
| 171 | certification | 46 | 4.8% | `(?i)(?:CE(?:-märkning)?|CE(?:-mark)?)\s*:\s*([^\.]+)` |
| 111 | environmental | 39 | 4.1% | `(?i)(?:EMC|electromagnetic compatibility)\s*:\s*([^\.]+)` |
| 8 | dimensions | 38 | 4.0% | `(?i)(?:höjd|height)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:mm|cm|m)` |
| 190 | installation | 30 | 3.2% | `(?i)(?:installation|installation)\s*:\s*([^\.]+)` |
| 90 | performance | 28 | 3.0% | `(?i)(?:kapacitet|capacity)\s*:\s*([^\.]+)` |
| 21 | electrical | 26 | 2.7% | `(?i)(?:spänning|voltage)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:V|kV|mV)` |
| 10 | dimensions | 26 | 2.7% | `(?i)(?:djup|depth)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:mm|cm|m)` |
| 9 | dimensions | 22 | 2.3% | `(?i)(?:bredd|width)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:mm|cm|m)` |
| 2 | dimensions | 20 | 2.1% | `(?i)mått\s*:\s*([^\.]+)` |
| 6 | dimensions | 16 | 1.7% | `(?i)(\d+(?:[.,]\d+)?)\s*(?:mm|cm|m)\s*x\s*(\d+(?:[.,]\d+)?)\s*(?:mm|cm...` |
| 1 | dimensions | 16 | 1.7% | `(?i)dimensions?\s*:\s*([^\.]+)` |
| 0 | dimensions | 14 | 1.5% | `(?i)dimensioner\s*:\s*([^\.]+)` |
| 94 | performance | 14 | 1.5% | `(?i)(?:minne|memory)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:MB|GB|TB)` |
| 49 | electrical | 14 | 1.5% | `(?i)(?:säkring|fuse)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:A)` |
| 26 | electrical | 9 | 0.9% | `(?i)(?:ström|current)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:A|mA)` |

### Bottenprestanda mönster

De mönster som gav minst antal träffar (men fortfarande gav några träffar):

| Mönsterindex | Grupp | Antal träffar | Procentandel | Mönster |
|--------------|-------|--------------|--------------|--------|
| 66 | temperature | 1 | 0.1% | `(?i)(?:drifttemperatur|operating temperature)\s*:\s*(-?\d+(?:[.,]\d+)?...` |
| 129 | color | 1 | 0.1% | `(?i)(?:utseende|appearance)\s*:\s*([^\.]+)` |
| 195 | installation | 1 | 0.1% | `(?i)(?:ventilationskrav|ventilation requirements)\s*:\s*([^\.]+)` |
| 24 | electrical | 1 | 0.1% | `(?i)(?:nominell spänning|nominal voltage)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?...` |
| 87 | performance | 1 | 0.1% | `(?i)(?:prestanda|performance)\s*:\s*([^\.]+)` |
| 176 | certification | 1 | 0.1% | `(?i)(?:energiklass|energy class)\s*:\s*([^\.]+)` |
| 128 | color | 1 | 0.1% | `(?i)(?:finish|finish)\s*:\s*([^\.]+)` |
| 105 | environmental | 1 | 0.1% | `(?i)(?:vatten(?:tät|skydd)|water(?:proof|protection))\s*:\s*([^\.]+)` |
| 163 | lighting | 1 | 0.1% | `(?i)(?:ljuskälla|light source)\s*:\s*([^\.]+)` |
| 92 | performance | 1 | 0.1% | `(?i)(?:batteritid|battery life)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:h|timmar|...` |
| 218 | pressure_flow | 1 | 0.1% | `(?i)(?:tryck|pressure)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:bar|Pa|kPa|MPa|psi...` |
| 170 | certification | 1 | 0.1% | `(?i)(?:standarder|standards)\s*:\s*([^\.]+)` |
| 115 | material | 1 | 0.1% | `(?i)(?:ytbehandling|surface treatment)\s*:\s*([^\.]+)` |
| 37 | electrical | 2 | 0.2% | `(?i)(?:frekvens|frequency)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:Hz|kHz|MHz)` |
| 22 | electrical | 2 | 0.2% | `(?i)(?:matningsspänning|supply voltage)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:V...` |
| 210 | operating_conditions | 2 | 0.2% | `(?i)(?:driftsförhållanden|operating conditions)\s*:\s*([^\.]+)` |
| 173 | certification | 2 | 0.2% | `(?i)(?:WEEE|WEEE compliant)\s*:\s*([^\.]+)` |
| 136 | network | 2 | 0.2% | `(?i)(?:räckvidd|range)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:m)` |
| 142 | network | 3 | 0.3% | `(?i)(?:gateway|gateway)\s*:\s*([^\.]+)` |
| 143 | network | 3 | 0.3% | `(?i)(?:nätmask|subnet mask)\s*:\s*([^\.]+)` |

### Mönstergruppernas prestanda

Prestanda per mönstergrupp:

| Mönstergrupp | Antal träffar | Procentandel |
|--------------|--------------|---------------|
| electrical | 210 | 22.1% |
| dimensions | 160 | 16.9% |
| material | 145 | 15.3% |
| connection | 125 | 13.2% |
| color | 73 | 7.7% |
| certification | 68 | 7.2% |
| performance | 48 | 5.1% |
| environmental | 40 | 4.2% |
| installation | 31 | 3.3% |
| network | 29 | 3.1% |
| performance_class | 6 | 0.6% |
| weight | 5 | 0.5% |
| temperature | 5 | 0.5% |
| operating_conditions | 2 | 0.2% |
| lighting | 1 | 0.1% |
| pressure_flow | 1 | 0.1% |

## Validering och datakvalitet

Av totalt 949 extraherade specifikationer är 949 (100.0%) validerade som giltiga.

### Valideringsresultat per kategori

| Kategori | Antal valida | Antal ogiltiga | Valideringsfrekvens |
|----------|--------------|----------------|-----------------------|
| DIMENSIONS | 160 | 0 | 100.0% |
| TEMPERATURE | 5 | 0 | 100.0% |
| MATERIAL | 145 | 0 | 100.0% |
| PERFORMANCE | 54 | 0 | 100.0% |
| COLOR | 73 | 0 | 100.0% |
| MISCELLANEOUS | 99 | 0 | 100.0% |
| ELECTRICAL | 210 | 0 | 100.0% |
| NETWORK | 29 | 0 | 100.0% |
| CONNECTION | 125 | 0 | 100.0% |
| ENVIRONMENTAL | 42 | 0 | 100.0% |
| WEIGHT | 5 | 0 | 100.0% |
| LIGHTING | 1 | 0 | 100.0% |
| FLOW | 1 | 0 | 100.0% |

### Vanliga valideringsfel

Inga validieringsfel hittades.


## Upptäckta specifikationer och mönsterförslag

Baserat på analys av dokument och frekventa specifikationer, föreslås följande 345 nya mönster:

| Specifikationsnamn | Föreslagen kategori | Föreslagen regex | Förekomster |
|---------------------|----------------------|-----------------|-------------|
| extinguishing media | MISCELLANEOUS | `r'(?i)extinguishing\ media\s*:\s*([^\.]+)'` | 30 |
| - and, special provision a67 states "non-spillable batteries are not subject to these instructions ( packing instruction 872) if at the temperature of 55° c (131° f), the electrolyte will not flow from a ruptured or cracked case and there is no free liquid flow and if, when packaged for transport the terminals are protected from short circuit and unintentional activation."

## **vessel – imo-imdg | TEMPERATURE | `r'(?i)\-\ and,\ special\ provision\ a67\ states\ "non\-spillable\ batteries\ are\ not\ subject\ to\ these\ instructions\ \(\ packing\ instruction\ 872\)\ if\ at\ the\ temperature\ of\ 55°\ c\ \(131°\ f\),\ the\ electrolyte\ will\ not\ flow\ from\ a\ ruptured\ or\ cracked\ case\ and\ there\ is\ no\ free\ liquid\ flow\ and\ if,\ when\ packaged\ for\ transport\ the\ terminals\ are\ protected\ from\ short\ circuit\ and\ unintentional\ activation\."\
\
\#\#\ \*\*vessel\ –\ imo\-imdg\s*:\s*([^\.]+)'` | 30 |
| if you are a manufacturing facility under sic codes 20 through 39 the following information is provided to enable you to complete the required reports | CONNECTION | `r'(?i)if\ you\ are\ a\ manufacturing\ facility\ under\ sic\ codes\ 20\ through\ 39\ the\ following\ information\ is\ provided\ to\ enable\ you\ to\ complete\ the\ required\ reports\s*:\s*([^\.]+)'` | 30 |
| tekniska data, moderkort | MISCELLANEOUS | `r'(?i)tekniska\ data,\ moderkort\s*:\s*([^\.]+)'` | 30 |
| tillämpliga delar av direktivet preciseras i den<br>tekniska dokumentationen som har sammanställts enligt avsnitt b i bilaga 7 och kan mot<br>motiverad anledning göras tillgänglig i digital form för behöriga myndigheter.<br>tillämpliga delar | MISCELLANEOUS | `r'(?i)tillämpliga\ delar\ av\ direktivet\ preciseras\ i\ den<br>tekniska\ dokumentationen\ som\ har\ sammanställts\ enligt\ avsnitt\ b\ i\ bilaga\ 7\ och\ kan\ mot<br>motiverad\ anledning\ göras\ tillgänglig\ i\ digital\ form\ för\ behöriga\ myndigheter\.<br>tillämpliga\ delar\s*:\s*([^\.]+)'` | 16 |
| ## **behörig att sammanställa relevant teknisk dokumentation | MISCELLANEOUS | `r'(?i)\#\#\ \*\*behörig\ att\ sammanställa\ relevant\ teknisk\ dokumentation\s*:\s*([^\.]+)'` | 16 |
| |
|                    | appropriate parts | MISCELLANEOUS | `r'(?i)\|\
\|\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \|\ appropriate\ parts\s*:\s*([^\.]+)'` | 16 |
| # **authorized to compile the relevant technical documentation | MISCELLANEOUS | `r'(?i)\#\ \*\*authorized\ to\ compile\ the\ relevant\ technical\ documentation\s*:\s*([^\.]+)'` | 16 |
| enheten skall installeras inomhus, miljöklass 1, omgivningstemperatur | TEMPERATURE | `r'(?i)enheten\ skall\ installeras\ inomhus,\ miljöklass\ 1,\ omgivningstemperatur\s*:\s*([^\.]+)'` | 15 |
| | 2 st                    | 2 st                                                         | 2 st                    |
| relä, lastström                       | max lastström per pol | ELECTRICAL | `r'(?i)\|\ 2\ st\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \|\ 2\ st\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \|\ 2\ st\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \|\
\|\ relä,\ lastström\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \|\ max\ lastström\ per\ pol\s*:\s*([^\.]+)'` | 12 |
| | 2 st                 | 2 st                 | 2 st                  |
| relä, lastström                       | max lastström per pol | ELECTRICAL | `r'(?i)\|\ 2\ st\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \|\ 2\ st\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \|\ 2\ st\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \|\
\|\ relä,\ lastström\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \|\ max\ lastström\ per\ pol\s*:\s*([^\.]+)'` | 12 |
| according to the emc directive 2014/30/eu & the low voltage directive lvd 2014/35/eu

type of equipment | ELECTRICAL | `r'(?i)according\ to\ the\ emc\ directive\ 2014/30/eu\ \&\ the\ low\ voltage\ directive\ lvd\ 2014/35/eu\
\
type\ of\ equipment\s*:\s*([^\.]+)'` | 11 |
| en54-4; 1997/a2 | MISCELLANEOUS | `r'(?i)en54\-4;\ 1997/a2\s*:\s*([^\.]+)'` | 10 |
| |
| reläer                                 | 2 st<br>relä 1 | MISCELLANEOUS | `r'(?i)\|\
\|\ reläer\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \|\ 2\ st<br>relä\ 1\s*:\s*([^\.]+)'` | 9 |
| *ce-märkt enligt en61000-6-3 | MISCELLANEOUS | `r'(?i)\*ce\-märkt\ enligt\ en61000\-6\-3\s*:\s*([^\.]+)'` | 8 |
| |

### tekniska data, nätaggregat | MISCELLANEOUS | `r'(?i)\|\
\
\#\#\#\ tekniska\ data,\ nätaggregat\s*:\s*([^\.]+)'` | 8 |
| spänning, ström och effekt

spänning ut | ELECTRICAL | `r'(?i)spänning,\ ström\ och\ effekt\
\
spänning\ ut\s*:\s*([^\.]+)'` | 8 |
| ## brand name or trade mark | MISCELLANEOUS | `r'(?i)\#\#\ brand\ name\ or\ trade\ mark\s*:\s*([^\.]+)'` | 7 |
| visar test att batterikapacitet har sjunkit till under 60 % - 80 % av batteriets ursprungliga kapacitet ges larm för åldrat batteri

åtgärd vid larm | PERFORMANCE | `r'(?i)visar\ test\ att\ batterikapacitet\ har\ sjunkit\ till\ under\ 60\ %\ \-\ 80\ %\ av\ batteriets\ ursprungliga\ kapacitet\ ges\ larm\ för\ åldrat\ batteri\
\
åtgärd\ vid\ larm\s*:\s*([^\.]+)'` | 7 |
| teknikfakta larm | MISCELLANEOUS | `r'(?i)teknikfakta\ larm\s*:\s*([^\.]+)'` | 7 |

*...och 325 ytterligare förslag. Se JSON-filen för fullständig lista.*

Se den fullständiga listan i JSON-filen för föreslagna mönster.

## Dokument och filer

### Resultatfiler

- **Extraherade tekniska specifikationer:** [technical_specs_pro_20250222_235736.jsonl](extracted_data\technical\matched\technical_specs_pro_20250222_235736.jsonl)
- **Dokument utan specifikationer:** [no_specs_pro_20250222_235736.jsonl](extracted_data\technical\unmatched\no_specs_pro_20250222_235736.jsonl)
- **Exempel på dokument utan specifikationer:** [samples_without_specs_20250222_235736.jsonl](extracted_data\technical\samples\samples_without_specs_20250222_235736.jsonl)
- **Upptäckta potentiella specifikationer:** [discovered_specs_20250222_235736.jsonl](extracted_data\technical\discovered\discovered_specs_20250222_235736.jsonl)
- **Mönsterprestanda (JSON):** [pattern_performance_20250222_235736.json](extracted_data\technical\patterns\pattern_performance_20250222_235736.json)
- **Validering (JSON):** [validation_report_20250222_235736.json](extracted_data\technical\validation\validation_report_20250222_235736.json)
- **Sammanfattning (JSON):** [technical_specs_pro_summary_20250222_235736.json](extracted_data\technical\reports\technical_specs_pro_summary_20250222_235736.json)

### Kategorispecifika filer

- **COLOR:** [COLOR_20250222_235736.jsonl](extracted_data\technical\categories\COLOR\COLOR_20250222_235736.jsonl)
- **CONNECTION:** [CONNECTION_20250222_235736.jsonl](extracted_data\technical\categories\CONNECTION\CONNECTION_20250222_235736.jsonl)
- **DIMENSIONS:** [DIMENSIONS_20250222_235736.jsonl](extracted_data\technical\categories\DIMENSIONS\DIMENSIONS_20250222_235736.jsonl)
- **ELECTRICAL:** [ELECTRICAL_20250222_235736.jsonl](extracted_data\technical\categories\ELECTRICAL\ELECTRICAL_20250222_235736.jsonl)
- **ENVIRONMENTAL:** [ENVIRONMENTAL_20250222_235736.jsonl](extracted_data\technical\categories\ENVIRONMENTAL\ENVIRONMENTAL_20250222_235736.jsonl)
- **FLOW:** [FLOW_20250222_235736.jsonl](extracted_data\technical\categories\FLOW\FLOW_20250222_235736.jsonl)
- **LIGHTING:** [LIGHTING_20250222_235736.jsonl](extracted_data\technical\categories\LIGHTING\LIGHTING_20250222_235736.jsonl)
- **MATERIAL:** [MATERIAL_20250222_235736.jsonl](extracted_data\technical\categories\MATERIAL\MATERIAL_20250222_235736.jsonl)
- **MISCELLANEOUS:** [MISCELLANEOUS_20250222_235736.jsonl](extracted_data\technical\categories\MISCELLANEOUS\MISCELLANEOUS_20250222_235736.jsonl)
- **NETWORK:** [NETWORK_20250222_235736.jsonl](extracted_data\technical\categories\NETWORK\NETWORK_20250222_235736.jsonl)
- **PERFORMANCE:** [PERFORMANCE_20250222_235736.jsonl](extracted_data\technical\categories\PERFORMANCE\PERFORMANCE_20250222_235736.jsonl)
- **TEMPERATURE:** [TEMPERATURE_20250222_235736.jsonl](extracted_data\technical\categories\TEMPERATURE\TEMPERATURE_20250222_235736.jsonl)
- **WEIGHT:** [WEIGHT_20250222_235736.jsonl](extracted_data\technical\categories\WEIGHT\WEIGHT_20250222_235736.jsonl)

## Nästa steg

Baserat på denna analys rekommenderas följande åtgärder:

1. **Granska upptäckta specifikationer** för att identifiera nya mönster och förbättra befintliga
2. **Implementera föreslagna mönster** och jämför resultaten i nästa körning
3. **Förfina valideringslogiken** för att öka antalet korrekt validerade specifikationer
4. **Utveckla specifika extraktorer för andra dokumenttyper** (_TEK, _produktblad, etc.)
5. **Expandera kategorierna** med mer detaljerade underkategorier vid behov
6. **Verifiera och förbättra rimlighetskontroller** för numeriska värden
7. **Utveckla statistiska normalintervall** för vanliga tekniska värden som baseras på extraherad data

---

Rapport genererad: 2025-02-22 23:58:39
