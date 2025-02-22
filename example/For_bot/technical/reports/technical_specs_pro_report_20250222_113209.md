# Detaljerad Teknisk Specifikationsrapport

**Datum och tid:** 2025-02-22 11:32:23

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

- **Totalt antal _pro-filer:** 363
- **Filer med tekniska specifikationer:** 159 (43.8%)
- **Filer utan tekniska specifikationer:** 204
- **Totalt antal extraherade specifikationer:** 405
- **Genomsnittligt antal specifikationer per dokument:** 2.5
- **Antal upptäckta potentiella nya specifikationer:** 317
- **Antal föreslagna nya mönster:** 59
- **Valideringsstatus:** 405 giltiga, 0 ogiltiga

## Kategorifördelning

Nedan visas fördelningen av tekniska specifikationer per kategori:

| Teknisk kategori | Antal specifikationer | Procentandel |
|-----------------|----------------------|---------------|
| ELECTRICAL | 138 | 34.1% |
| CONNECTION | 74 | 18.3% |
| COLOR | 56 | 13.8% |
| DIMENSIONS | 52 | 12.8% |
| MATERIAL | 29 | 7.2% |
| NETWORK | 20 | 4.9% |
| ENVIRONMENTAL | 13 | 3.2% |
| MISCELLANEOUS | 10 | 2.5% |
| PERFORMANCE | 7 | 1.7% |
| WEIGHT | 3 | 0.7% |
| TEMPERATURE | 2 | 0.5% |
| LIGHTING | 1 | 0.2% |
| PRESSURE | 0 | 0.0% |
| FLOW | 0 | 0.0% |
| MECHANICAL | 0 | 0.0% |
| CAPACITY | 0 | 0.0% |
| ENERGY | 0 | 0.0% |
| AUDIO | 0 | 0.0% |
| VIDEO | 0 | 0.0% |
| FREQUENCY | 0 | 0.0% |
| RUNTIME | 0 | 0.0% |
| PROTECTION | 0 | 0.0% |

## Mönsterprestanda

Totalt används 239 mönster för extraktion, varav 34 gav träffar.

### Toppresterande mönster

De mönster som gav flest träffar:

| Mönsterindex | Grupp | Antal träffar | Procentandel | Mönster |
|--------------|-------|--------------|--------------|--------|
| 151 | connection | 66 | 16.3% | `(?i)(?:utgångar|outputs)\s*:\s*([^\.]+)` |
| 43 | electrical | 62 | 15.3% | `(?i)(?:batterityp|battery type)\s*:\s*([^\.]+)` |
| 123 | color | 55 | 13.6% | `(?i)(?:färg|color)\s*:\s*([^\.]+)` |
| 52 | electrical | 52 | 12.8% | `(?i)(?:skyddsklass|protection class)\s*:\s*([^\.]+)` |
| 113 | material | 28 | 6.9% | `(?i)(?:material|material)\s*:\s*([^\.]+)` |
| 2 | dimensions | 17 | 4.2% | `(?i)mått\s*:\s*([^\.]+)` |
| 21 | electrical | 16 | 4.0% | `(?i)(?:spänning|voltage)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:V|kV|mV)` |
| 6 | dimensions | 11 | 2.7% | `(?i)(\d+(?:[.,]\d+)?)\s*(?:mm|cm|m)\s*x\s*(\d+(?:[.,]\d+)?)\s*(?:mm|cm...` |
| 1 | dimensions | 10 | 2.5% | `(?i)dimensions?\s*:\s*([^\.]+)` |
| 111 | environmental | 10 | 2.5% | `(?i)(?:EMC|electromagnetic compatibility)\s*:\s*([^\.]+)` |
| 171 | certification | 10 | 2.5% | `(?i)(?:CE(?:-märkning)?|CE(?:-mark)?)\s*:\s*([^\.]+)` |
| 139 | network | 8 | 2.0% | `(?i)(?:kryptering|encryption)\s*:\s*([^\.]+)` |
| 8 | dimensions | 8 | 2.0% | `(?i)(?:höjd|height)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:mm|cm|m)` |
| 204 | performance_class | 6 | 1.5% | `(?i)(?:effektivitetsklass|efficiency class)\s*:\s*([^\.]+)` |
| 138 | network | 5 | 1.2% | `(?i)(?:protokoll|protocol)\s*:\s*([^\.]+)` |
| 152 | connection | 5 | 1.2% | `(?i)(?:ingångar|inputs)\s*:\s*([^\.]+)` |
| 140 | network | 5 | 1.2% | `(?i)(?:nätverksport|network port)\s*:\s*([^\.]+)` |
| 145 | connection | 3 | 0.7% | `(?i)(?:kontakter|connectors)\s*:\s*([^\.]+)` |
| 53 | weight | 3 | 0.7% | `(?i)(?:vikt|weight)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:kg|g)` |
| 65 | temperature | 2 | 0.5% | `(?i)(?:temperatur|temperature)\s*:\s*(-?\d+(?:[.,]\d+)?)\s*°?C` |

### Bottenprestanda mönster

De mönster som gav minst antal träffar (men fortfarande gav några träffar):

| Mönsterindex | Grupp | Antal träffar | Procentandel | Mönster |
|--------------|-------|--------------|--------------|--------|
| 128 | color | 1 | 0.2% | `(?i)(?:finish|finish)\s*:\s*([^\.]+)` |
| 105 | environmental | 1 | 0.2% | `(?i)(?:vatten(?:tät|skydd)|water(?:proof|protection))\s*:\s*([^\.]+)` |
| 163 | lighting | 1 | 0.2% | `(?i)(?:ljuskälla|light source)\s*:\s*([^\.]+)` |
| 92 | performance | 1 | 0.2% | `(?i)(?:batteritid|battery life)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:h|timmar|...` |
| 115 | material | 1 | 0.2% | `(?i)(?:ytbehandling|surface treatment)\s*:\s*([^\.]+)` |
| 65 | temperature | 2 | 0.5% | `(?i)(?:temperatur|temperature)\s*:\s*(-?\d+(?:[.,]\d+)?)\s*°?C` |
| 37 | electrical | 2 | 0.5% | `(?i)(?:frekvens|frequency)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:Hz|kHz|MHz)` |
| 22 | electrical | 2 | 0.5% | `(?i)(?:matningsspänning|supply voltage)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:V...` |
| 9 | dimensions | 2 | 0.5% | `(?i)(?:bredd|width)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:mm|cm|m)` |
| 10 | dimensions | 2 | 0.5% | `(?i)(?:djup|depth)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:mm|cm|m)` |
| 26 | electrical | 2 | 0.5% | `(?i)(?:ström|current)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:A|mA)` |
| 210 | operating_conditions | 2 | 0.5% | `(?i)(?:driftsförhållanden|operating conditions)\s*:\s*([^\.]+)` |
| 49 | electrical | 2 | 0.5% | `(?i)(?:säkring|fuse)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:A)` |
| 4 | dimensions | 2 | 0.5% | `(?i)storlek\s*:\s*([^\.]+)` |
| 136 | network | 2 | 0.5% | `(?i)(?:räckvidd|range)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:m)` |
| 145 | connection | 3 | 0.7% | `(?i)(?:kontakter|connectors)\s*:\s*([^\.]+)` |
| 53 | weight | 3 | 0.7% | `(?i)(?:vikt|weight)\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:kg|g)` |
| 138 | network | 5 | 1.2% | `(?i)(?:protokoll|protocol)\s*:\s*([^\.]+)` |
| 152 | connection | 5 | 1.2% | `(?i)(?:ingångar|inputs)\s*:\s*([^\.]+)` |
| 140 | network | 5 | 1.2% | `(?i)(?:nätverksport|network port)\s*:\s*([^\.]+)` |

### Mönstergruppernas prestanda

Prestanda per mönstergrupp:

| Mönstergrupp | Antal träffar | Procentandel |
|--------------|--------------|---------------|
| electrical | 138 | 34.1% |
| connection | 74 | 18.3% |
| color | 56 | 13.8% |
| dimensions | 52 | 12.8% |
| material | 29 | 7.2% |
| network | 20 | 4.9% |
| environmental | 11 | 2.7% |
| certification | 10 | 2.5% |
| performance_class | 6 | 1.5% |
| weight | 3 | 0.7% |
| temperature | 2 | 0.5% |
| operating_conditions | 2 | 0.5% |
| performance | 1 | 0.2% |
| lighting | 1 | 0.2% |

## Validering och datakvalitet

Av totalt 405 extraherade specifikationer är 405 (100.0%) validerade som giltiga.

### Valideringsresultat per kategori

| Kategori | Antal valida | Antal ogiltiga | Valideringsfrekvens |
|----------|--------------|----------------|-----------------------|
| DIMENSIONS | 52 | 0 | 100.0% |
| MATERIAL | 29 | 0 | 100.0% |
| TEMPERATURE | 2 | 0 | 100.0% |
| ELECTRICAL | 138 | 0 | 100.0% |
| NETWORK | 20 | 0 | 100.0% |
| CONNECTION | 74 | 0 | 100.0% |
| COLOR | 56 | 0 | 100.0% |
| WEIGHT | 3 | 0 | 100.0% |
| ENVIRONMENTAL | 13 | 0 | 100.0% |
| MISCELLANEOUS | 10 | 0 | 100.0% |
| LIGHTING | 1 | 0 | 100.0% |
| PERFORMANCE | 7 | 0 | 100.0% |

### Vanliga valideringsfel

Inga validieringsfel hittades.


## Upptäckta specifikationer och mönsterförslag

Baserat på analys av dokument och frekventa specifikationer, föreslås följande 59 nya mönster:

| Specifikationsnamn | Föreslagen kategori | Föreslagen regex | Förekomster |
|---------------------|----------------------|-----------------|-------------|
| | 2 st                 | 2 st                 | 2 st                  |
| relä, lastström                       | max lastström per pol | ELECTRICAL | `r'(?i)\|\ 2\ st\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \|\ 2\ st\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \|\ 2\ st\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \|\
\|\ relä,\ lastström\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \|\ max\ lastström\ per\ pol\s*:\s*([^\.]+)'` | 12 |
| *ce-märkt enligt en61000-6-3 | MISCELLANEOUS | `r'(?i)\*ce\-märkt\ enligt\ en61000\-6\-3\s*:\s*([^\.]+)'` | 6 |
| ◼ lighter weight | WEIGHT | `r'(?i)◼\ lighter\ weight\s*:\s*([^\.]+)'` | 5 |
| ◼ higher power | MISCELLANEOUS | `r'(?i)◼\ higher\ power\s*:\s*([^\.]+)'` | 5 |
| ◼ wider temperature range | TEMPERATURE | `r'(?i)◼\ wider\ temperature\ range\s*:\s*([^\.]+)'` | 5 |
| ![](_page_0_picture_15.jpeg)

#### **tekniska data**

| sm910, sm920, sm930<br>inspänning dc | 9-32vdc |
|--------------------------------------|---------|
| sm919, sm929<br>inspänning ac        | 8-30vac |

 **ce-märkt enligt en50081-1 och en50082-1** 

| e-nummer | typ  |                                                | hxbxd mm    |
|----------|------|------------------------------------------------|-------------|
| 5247045  | 910s | sm910 19"ram med 10-gruppsäkringskort 12-24vdc | 135x480x60  |
| 5247046  | 911s | sm911 19" endast ram                           | 135x480x60  |
| 5247047  | 912s | sm912 lock till 19" ram                        | 135x480     |
| 5247048  | 920s | sm920 utökningskort 10-grupp 12-24vdc          | 130x90x45   |
| 5247049  | 930s | sm930 vägg mont.10-gruppsäkringskort 12-24vdc  | 180x180x100 |
| 5247044  | 919s | sm919 19"ram med 10-gruppsäkringskort 12-24vac | 135x480x60  |
| 5247065  | 929s | sm929 utökningskort 10-grupp 12-24vac          | 135x480x60  |

postadress/postal address **swansons telemekanik ab** hålstensvägen 4 se-446 37 älvängen

telefon nr/telephone no +46(0)303-746 320 hemsida/webb www.swtm.se

telefax nr/telefax no +46(0)303-748 490 e-post info@swtm.se

![](_page_1_picture_0.jpeg)

# **sm930 dc e nr | ELECTRICAL | `r'(?i)!\[\]\(_page_0_picture_15\.jpeg\)\
\
\#\#\#\#\ \*\*tekniska\ data\*\*\
\
\|\ sm910,\ sm920,\ sm930<br>inspänning\ dc\ \|\ 9\-32vdc\ \|\
\|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\|\-\-\-\-\-\-\-\-\-\|\
\|\ sm919,\ sm929<br>inspänning\ ac\ \ \ \ \ \ \ \ \|\ 8\-30vac\ \|\
\
\ \*\*ce\-märkt\ enligt\ en50081\-1\ och\ en50082\-1\*\*\ \
\
\|\ e\-nummer\ \|\ typ\ \ \|\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \|\ hxbxd\ mm\ \ \ \ \|\
\|\-\-\-\-\-\-\-\-\-\-\|\-\-\-\-\-\-\|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\|\-\-\-\-\-\-\-\-\-\-\-\-\-\|\
\|\ 5247045\ \ \|\ 910s\ \|\ sm910\ 19"ram\ med\ 10\-gruppsäkringskort\ 12\-24vdc\ \|\ 135x480x60\ \ \|\
\|\ 5247046\ \ \|\ 911s\ \|\ sm911\ 19"\ endast\ ram\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \|\ 135x480x60\ \ \|\
\|\ 5247047\ \ \|\ 912s\ \|\ sm912\ lock\ till\ 19"\ ram\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \|\ 135x480\ \ \ \ \ \|\
\|\ 5247048\ \ \|\ 920s\ \|\ sm920\ utökningskort\ 10\-grupp\ 12\-24vdc\ \ \ \ \ \ \ \ \ \ \|\ 130x90x45\ \ \ \|\
\|\ 5247049\ \ \|\ 930s\ \|\ sm930\ vägg\ mont\.10\-gruppsäkringskort\ 12\-24vdc\ \ \|\ 180x180x100\ \|\
\|\ 5247044\ \ \|\ 919s\ \|\ sm919\ 19"ram\ med\ 10\-gruppsäkringskort\ 12\-24vac\ \|\ 135x480x60\ \ \|\
\|\ 5247065\ \ \|\ 929s\ \|\ sm929\ utökningskort\ 10\-grupp\ 12\-24vac\ \ \ \ \ \ \ \ \ \ \|\ 135x480x60\ \ \|\
\
postadress/postal\ address\ \*\*swansons\ telemekanik\ ab\*\*\ hålstensvägen\ 4\ se\-446\ 37\ älvängen\
\
telefon\ nr/telephone\ no\ \+46\(0\)303\-746\ 320\ hemsida/webb\ www\.swtm\.se\
\
telefax\ nr/telefax\ no\ \+46\(0\)303\-748\ 490\ e\-post\ info@swtm\.se\
\
!\[\]\(_page_1_picture_0\.jpeg\)\
\
\#\ \*\*sm930\ dc\ e\ nr\s*:\s*([^\.]+)'` | 5 |
| # poe-48

# power over ethernet med batteribackup

![](_page_0_picture_2.jpeg)

![](_page_0_picture_4.jpeg)

#### skydd | NETWORK | `r'(?i)\#\ poe\-48\
\
\#\ power\ over\ ethernet\ med\ batteribackup\
\
!\[\]\(_page_0_picture_2\.jpeg\)\
\
!\[\]\(_page_0_picture_4\.jpeg\)\
\
\#\#\#\#\ skydd\s*:\s*([^\.]+)'` | 5 |
| en54-4; 1997/a2 | MISCELLANEOUS | `r'(?i)en54\-4;\ 1997/a2\s*:\s*([^\.]+)'` | 5 |
| ## **huvudfeatures inkluderar | MISCELLANEOUS | `r'(?i)\#\#\ \*\*huvudfeatures\ inkluderar\s*:\s*([^\.]+)'` | 5 |
| **skydd för | MISCELLANEOUS | `r'(?i)\*\*skydd\ för\s*:\s*([^\.]+)'` | 5 |
| **larm för (via rs485) | MISCELLANEOUS | `r'(?i)\*\*larm\ för\ \(via\ rs485\)\s*:\s*([^\.]+)'` | 5 |
| ![](_page_1_picture_15.jpeg)

large-kapsling med 1 batteribox

![](_page_1_picture_17.jpeg)

large-kapsling med 2 batteriboxar

![](_page_1_picture_19.jpeg)

large-kapsling med 3 batteriboxar

![](_page_1_picture_21.jpeg)

large-kapsling med 4 batteriboxar

![](_page_2_picture_0.jpeg)

| teknisk specifikation                   | p5s             | p5l             | p10l            | p15l            | p25l            |
|-----------------------------------------|-----------------|-----------------|-----------------|-----------------|-----------------|
| nätspänning                             |                 |                 | 230v ac         |                 |                 |
| utspänning                              |                 |                 | 27,3v dc        |                 |                 |
| arbetstemperatur | ELECTRICAL | `r'(?i)!\[\]\(_page_1_picture_15\.jpeg\)\
\
large\-kapsling\ med\ 1\ batteribox\
\
!\[\]\(_page_1_picture_17\.jpeg\)\
\
large\-kapsling\ med\ 2\ batteriboxar\
\
!\[\]\(_page_1_picture_19\.jpeg\)\
\
large\-kapsling\ med\ 3\ batteriboxar\
\
!\[\]\(_page_1_picture_21\.jpeg\)\
\
large\-kapsling\ med\ 4\ batteriboxar\
\
!\[\]\(_page_2_picture_0\.jpeg\)\
\
\|\ teknisk\ specifikation\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \|\ p5s\ \ \ \ \ \ \ \ \ \ \ \ \ \|\ p5l\ \ \ \ \ \ \ \ \ \ \ \ \ \|\ p10l\ \ \ \ \ \ \ \ \ \ \ \ \|\ p15l\ \ \ \ \ \ \ \ \ \ \ \ \|\ p25l\ \ \ \ \ \ \ \ \ \ \ \ \|\
\|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\|\
\|\ nätspänning\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \|\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \|\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \|\ 230v\ ac\ \ \ \ \ \ \ \ \ \|\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \|\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \|\
\|\ utspänning\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \|\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \|\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \|\ 27,3v\ dc\ \ \ \ \ \ \ \ \|\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \|\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \|\
\|\ arbetstemperatur\s*:\s*([^\.]+)'` | 5 |
| # tekniskt produktblad jck207.245

![](_page_0_picture_1.jpeg)

![](_page_0_figure_2.jpeg)

går att beställa med | MISCELLANEOUS | `r'(?i)\#\ tekniskt\ produktblad\ jck207\.245\
\
!\[\]\(_page_0_picture_1\.jpeg\)\
\
!\[\]\(_page_0_figure_2\.jpeg\)\
\
går\ att\ beställa\ med\s*:\s*([^\.]+)'` | 4 |
| garantiperiod | MISCELLANEOUS | `r'(?i)garantiperiod\s*:\s*([^\.]+)'` | 4 |
| ## **batterihyllor**

![](_page_0_picture_1.jpeg)

battery shelf 24v m

![](_page_0_picture_3.jpeg)

![](_page_0_picture_4.jpeg)

battery shelf m

![](_page_0_picture_6.jpeg)

för sälj support | CONNECTION | `r'(?i)\#\#\ \*\*batterihyllor\*\*\
\
!\[\]\(_page_0_picture_1\.jpeg\)\
\
battery\ shelf\ 24v\ m\
\
!\[\]\(_page_0_picture_3\.jpeg\)\
\
!\[\]\(_page_0_picture_4\.jpeg\)\
\
battery\ shelf\ m\
\
!\[\]\(_page_0_picture_6\.jpeg\)\
\
för\ sälj\ support\s*:\s*([^\.]+)'` | 4 |
| möjligt att komplettera upp till 4x batteriboxar för upp till 180ah batterikapacitet.**

**en54 flx m-serien** används främst för att driva externa larmdon i brandlarm där en sbf110 | PERFORMANCE | `r'(?i)möjligt\ att\ komplettera\ upp\ till\ 4x\ batteriboxar\ för\ upp\ till\ 180ah\ batterikapacitet\.\*\*\
\
\*\*en54\ flx\ m\-serien\*\*\ används\ främst\ för\ att\ driva\ externa\ larmdon\ i\ brandlarm\ där\ en\ sbf110\s*:\s*([^\.]+)'` | 4 |
| |                           |                         |                       |                   |
| garantiperiod | MISCELLANEOUS | `r'(?i)\|\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \|\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \|\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \|\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \|\
\|\ garantiperiod\s*:\s*([^\.]+)'` | 4 |
| neo 24v flx m display serien erbjuder en grafisk display som visualiserar max / medium / minimum för | MISCELLANEOUS | `r'(?i)neo\ 24v\ flx\ m\ display\ serien\ erbjuder\ en\ grafisk\ display\ som\ visualiserar\ max\ /\ medium\ /\ minimum\ för\s*:\s*([^\.]+)'` | 4 |
| |                                                             |                                                                                                                                       |                           |  |  |
| dimension (höjd x bredd x djup) | DIMENSIONS | `r'(?i)\|\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \|\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \|\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \|\ \ \|\ \ \|\
\|\ dimension\ \(höjd\ x\ bredd\ x\ djup\)\s*:\s*([^\.]+)'` | 4 |
| f10a (glas)                                           | 2x 15a (flatstift)                                                                                                                    | 2x 25a (flatstift)        |  |  |
| djupurladdning av batterier sker vid | DIMENSIONS | `r'(?i)f10a\ \(glas\)\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \|\ 2x\ 15a\ \(flatstift\)\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \|\ 2x\ 25a\ \(flatstift\)\ \ \ \ \ \ \ \ \|\ \ \|\ \ \|\
\|\ djupurladdning\ av\ batterier\ sker\ vid\s*:\s*([^\.]+)'` | 4 |

*...och 39 ytterligare förslag. Se JSON-filen för fullständig lista.*

Se den fullständiga listan i JSON-filen för föreslagna mönster.

## Dokument och filer

### Resultatfiler

- **Extraherade tekniska specifikationer:** [technical_specs_pro_20250222_113209.jsonl](extracted_data\technical\matched\technical_specs_pro_20250222_113209.jsonl)
- **Dokument utan specifikationer:** [no_specs_pro_20250222_113209.jsonl](extracted_data\technical\unmatched\no_specs_pro_20250222_113209.jsonl)
- **Exempel på dokument utan specifikationer:** [samples_without_specs_20250222_113209.jsonl](extracted_data\technical\samples\samples_without_specs_20250222_113209.jsonl)
- **Upptäckta potentiella specifikationer:** [discovered_specs_20250222_113209.jsonl](extracted_data\technical\discovered\discovered_specs_20250222_113209.jsonl)
- **Mönsterprestanda (JSON):** [pattern_performance_20250222_113209.json](extracted_data\technical\patterns\pattern_performance_20250222_113209.json)
- **Validering (JSON):** [validation_report_20250222_113209.json](extracted_data\technical\validation\validation_report_20250222_113209.json)
- **Sammanfattning (JSON):** [technical_specs_pro_summary_20250222_113209.json](extracted_data\technical\reports\technical_specs_pro_summary_20250222_113209.json)

### Kategorispecifika filer

- **COLOR:** [COLOR_20250222_113209.jsonl](extracted_data\technical\categories\COLOR\COLOR_20250222_113209.jsonl)
- **CONNECTION:** [CONNECTION_20250222_113209.jsonl](extracted_data\technical\categories\CONNECTION\CONNECTION_20250222_113209.jsonl)
- **DIMENSIONS:** [DIMENSIONS_20250222_113209.jsonl](extracted_data\technical\categories\DIMENSIONS\DIMENSIONS_20250222_113209.jsonl)
- **ELECTRICAL:** [ELECTRICAL_20250222_113209.jsonl](extracted_data\technical\categories\ELECTRICAL\ELECTRICAL_20250222_113209.jsonl)
- **ENVIRONMENTAL:** [ENVIRONMENTAL_20250222_113209.jsonl](extracted_data\technical\categories\ENVIRONMENTAL\ENVIRONMENTAL_20250222_113209.jsonl)
- **LIGHTING:** [LIGHTING_20250222_113209.jsonl](extracted_data\technical\categories\LIGHTING\LIGHTING_20250222_113209.jsonl)
- **MATERIAL:** [MATERIAL_20250222_113209.jsonl](extracted_data\technical\categories\MATERIAL\MATERIAL_20250222_113209.jsonl)
- **MISCELLANEOUS:** [MISCELLANEOUS_20250222_113209.jsonl](extracted_data\technical\categories\MISCELLANEOUS\MISCELLANEOUS_20250222_113209.jsonl)
- **NETWORK:** [NETWORK_20250222_113209.jsonl](extracted_data\technical\categories\NETWORK\NETWORK_20250222_113209.jsonl)
- **PERFORMANCE:** [PERFORMANCE_20250222_113209.jsonl](extracted_data\technical\categories\PERFORMANCE\PERFORMANCE_20250222_113209.jsonl)
- **TEMPERATURE:** [TEMPERATURE_20250222_113209.jsonl](extracted_data\technical\categories\TEMPERATURE\TEMPERATURE_20250222_113209.jsonl)
- **WEIGHT:** [WEIGHT_20250222_113209.jsonl](extracted_data\technical\categories\WEIGHT\WEIGHT_20250222_113209.jsonl)

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

Rapport genererad: 2025-02-22 11:32:23
