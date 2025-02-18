# Slagdörrsöppnare EM PSW250

![](_page_0_Picture_2.jpeg)

# Installations- och servicehandbok Originalinstruktioner

© Alla rättigheter i och till detta material tillhör Entrematic Nordic AB. Kopiering, skanning, bearbetning eller modifiering är inte tillåtet utan föregående skriftligt godkännande från Entrematic Nordic AB. Rätt till konstruktions- och måttändringar förbehålles.

Backtrack information: folder:Workspace Main, version:a474, Date:2018-08-07 time:05:15:06, state: Frozen

| 1 |                            | Revision                                                                         | 6  |  |
|---|----------------------------|----------------------------------------------------------------------------------|----|--|
| 2 |                            | Anvisningar för säker drift                                                      | 7  |  |
| 3 | Viktig information         |                                                                                  |    |  |
|   | 3.1                        | Avsedd användning                                                                | 8  |  |
|   | 3.2                        | Säkerhetsföreskrifter                                                            | 8  |  |
|   | 3.3                        | Störning av mottagningen för viss elektronikutrustning                           | 8  |  |
|   | 3.4                        | Miljökrav                                                                        | 9  |  |
| 4 |                            | Tekniska specifikationer  10                                                     |    |  |
|   | 4.1                        | Tillåten dörrvikt och dörrbredd för EM PSW250  11                                |    |  |
| 5 | Hur EM PSW250 fungerar  12 |                                                                                  |    |  |
|   | 5.1                        | Öppning  13                                                                      |    |  |
|   | 5.2                        | Stängning  13                                                                    |    |  |
|   | 5.3                        | Omkopplare  13                                                                   |    |  |
|   |                            | 5.3.1<br>FRÅN/AUTO/OPEN Programväljare  13                                       |    |  |
|   | 5.4                        | Funktioner på standardstyrmodulen CUS7  14                                       |    |  |
|   |                            | 5.4.1<br>Strömavbrott  14                                                        |    |  |
|   |                            | 5.4.2<br>Stängningskraft  14                                                     |    |  |
|   |                            | 5.4.3<br>Utökad stängningsmoment (CLTQ)  14<br>5.4.4<br>Servoassistans(POAS)  14 |    |  |
|   |                            | 5.4.5<br>Push & Go (PAG)  14                                                     |    |  |
|   |                            | 5.4.6<br>Omvänd (INV)                                                            | 14 |  |
|   |                            | 5.4.7<br>Aktiveringsfördröjning (AD)  14                                         |    |  |
|   |                            | 5.4.8<br>Överliggande närvarodetektor (OPD) med rammontering.  14                |    |  |
|   |                            | 5.4.9<br>Matta  16                                                               |    |  |
|   |                            | 5.4.10<br>Dubbelverkande  16                                                     |    |  |
|   | 5.5                        | Kompletteringsenhetens EXU-SI funktioner  17                                     |    |  |
|   |                            | 5.5.1<br>KILL eller BRAND-funktion  17                                           |    |  |
|   |                            | 5.5.2<br>Låsens funktioner  17                                                   |    |  |
|   |                            | 5.5.3<br>Programväljare (väggmonterad)  17<br>5.5.4<br>Impulser  17              |    |  |
|   |                            | 5.5.5<br>ÖPPEN/STÄNG-impuls  17                                                  |    |  |
|   |                            | 5.5.6<br>Strömavbrottsläge (reservbatterier installerade) - extratillbehör  17   |    |  |
|   |                            | 5.5.7<br>Funktionen Syster/Säng  19                                              |    |  |
|   | 5.6                        | Funktioner på kompletteringsenheten EXU-SA  20                                   |    |  |
|   |                            | 5.6.1<br>Närvaroimpuls, monterad på dörrens anslagssida.  20                     |    |  |
|   |                            | 5.6.2<br>Närvarodetektering, monterad på dörrens gångjärnssida.  20              |    |  |
|   |                            | 5.6.3<br>Övervakade säkerhetssensorer  20                                        |    |  |
|   |                            | 5.6.4<br>BRAND-signal in  20                                                     |    |  |
|   |                            | 5.6.5<br>Relä utsignal  20                                                       |    |  |
| 6 |                            | Modeller  21                                                                     |    |  |
|   | 6.1                        | Enkelöppnare, utanpåliggande  21                                                 |    |  |
|   | 6.2                        | Dubbelöppnare, utanpåliggande  22                                                |    |  |
| 7 |                            | Reservdelsförteckning  23                                                        |    |  |
| 8 |                            | Armsystem  25                                                                    |    |  |
|   | 8.1                        | Tryckande installation med PUSH-arm  25                                          |    |  |
|   | 8.2                        | Installation med dragande PULL-arm  26                                           |    |  |
|   | 8.3                        | 20 mm förlängning  26                                                            |    |  |
|   | 8.4                        | Tryckinstallation med PULL-arm  27                                               |    |  |
|   | 8.5                        | Förlängningssatser för drivaxel  28                                              |    |  |
| 9 | Tillval  29                |                                                                                  |    |  |
|   | 9.1                        | Omkopplare  29                                                                   |    |  |
|   |                            | 9.1.1<br>Programväljare PS-4C (driver elektriskt lås)  29                        |    |  |
|   | 9.2                        | Synkkabel för dubbeldörrar (synkroniserar 2 dörröppnare)                         | 29 |  |
|   | 9.3                        | Koordinatorenhet  29                                                             |    |  |
|   | 9.4                        | LED-kabel  30                                                                    |    |  |

|    | 9.5                       | Batteribackupsenhet  30                                                                           |    |
|----|---------------------------|---------------------------------------------------------------------------------------------------|----|
|    | 9.6                       | Kåpsats                                                                                           | 30 |
|    | 9.7                       | Kortsats för stängningstid  30                                                                    |    |
|    | 9.8<br>9.9                | Brandsats  31<br>Monteringsplåt (för förstärkning av vägg)  31                                    |    |
|    | 9.10                      | Etiketter  32                                                                                     |    |
| 10 | Förinstallation  33       |                                                                                                   |    |
|    |                           |                                                                                                   |    |
|    | 10.1<br>10.2              | Allmänna tips/säkerhetsfrågor  33<br>Dörröppnare/dörrhängning  33                                 |    |
|    | 10.3                      | Monteringsexempel  34                                                                             |    |
|    | 10.4                      | Fästkrav (ej inkluderat)  34                                                                      |    |
|    | 10.5                      | Erforderliga verktyg  35                                                                          |    |
| 11 | Mekanisk installation  36 |                                                                                                   |    |
|    | 11.1                      | PUSH-armsystem  39                                                                                |    |
|    | 11.2                      | PULL armsystem  45                                                                                |    |
|    | 11.3                      | Dörröppnare med PUSH glidarmsystem  51                                                            |    |
|    | 11.4                      | omvänd installation med tryckarmsystem PUSH  52                                                   |    |
|    | 11.5                      | omvänd installation med tryckarmsystem PULL  53                                                   |    |
|    | 11.6                      | Installation av koordineringsenhet på branddörrar  54                                             |    |
| 12 |                           | El-anslutning  60                                                                                 |    |
|    | 12.1                      | Styrmoduler  61                                                                                   |    |
|    |                           | 12.1.1<br>CUS7  61                                                                                |    |
|    |                           | 12.1.2<br>Val av armsystem  61<br>12.1.3<br>Kompletteringsenheter EXU-SI / EXU-SA  62             |    |
|    |                           | 12.1.4<br>Kompletteringsenhet EXU-SI  63                                                          |    |
|    |                           | 12.1.5<br>Kompletteringsenhet EXU-SA  64                                                          |    |
|    |                           | 12.1.6<br>Montering på dubbla in- och utgångsdörrar  65                                           |    |
|    | 12.2                      | Hur man klipper synkkabelns bygel för dubbeldörrar  65                                            |    |
|    | 12.3                      | Installation av dubbeldörr  66                                                                    |    |
|    | 12.4<br>12.5              | Inställning för dubbeldörrar  66<br>Kabelingång för sensor  67                                    |    |
|    | 12.6                      | Återställnings- och indikeringsenhet för branddörrar  68                                          |    |
|    |                           |                                                                                                   |    |
| 13 |                           | Driftsättning  70                                                                                 |    |
|    | 13.1                      | Fjäderförspännare  70                                                                             |    |
|    | 13.2<br>13.3              | Mikrobrytare  71<br>Ställa in dörrstoppet  71                                                     |    |
|    | 13.4                      | Autoinlärning ställer automatiskt in lågfartssträcka i öppning och stängning (rekommenderas).  73 |    |
|    |                           | 13.4.1<br>Tryck på INLÄRNINGSKNAPPEN (LRN)  74                                                    |    |
|    |                           | 13.4.2<br>Dubbeldörr  74                                                                          |    |
|    | 13.5                      | Allmänna inställningar  74                                                                        |    |
|    | 13.6                      | Anslutning av impulsgivare och tillbehör  75                                                      |    |
| 14 |                           | Kåpa  76                                                                                          |    |
|    | 14.1                      | Montering och demontering av kåpa                                                                 | 76 |
|    | 14.2                      | Kåpsats                                                                                           | 76 |
| 15 |                           | Skyltar  77                                                                                       |    |
| 16 |                           | Avancerade inställningar  78                                                                      |    |
|    | 16.1                      | Inlärning med avancerad inställning av lågfartsområde i öppning och stängning"  78                |    |
|    | 16.2                      | Återgå till ursprungsvärdena för "lågfartsområde i öppning och stängning" (nivå 1).  78           |    |
|    | 16.3                      | Byte av parametergrupp (nivå 2)  79                                                               |    |
|    | 16.4                      | Klassificering (nivå 3)  82                                                                       |    |
|    | 16.5                      | Överliggande närvarodetektering och slussfunktion (nivå 4)  83                                    |    |
|    | 16.6                      | Förbättrad låskick, brand insignal och utökat larmval (nivå 5)  85                                |    |
| 17 |                           | Instruktion för installation och justeringar  86                                                  |    |
|    | 17.1                      | Kompletterande säkerhetsanordningar för slagdörrar  86                                            |    |
|    | 17.2                      | Öppnings- och stängningstider för slagdörrar.  86                                                 |    |
|    |                           | 17.2.1<br>Hur hittar jag korrekt öppnings- och stängningstid  86                                  |    |
|    | 17.3                      | Diagram för dörrvikt  87<br>17.3.1<br>Aluminiumram med glas  87                                   |    |
|    |                           |                                                                                                   |    |

| 18 | Felsökning  88 |                       |  |
|----|----------------|-----------------------|--|
|    | 18.1           | Felindikering  89     |  |
| 19 |                | Service/Underhåll  90 |  |

# 1 Revision

# **Följande sidor har reviderats:**

| Sidan   | Revision 16.0 → 17.0                                        |
|---------|-------------------------------------------------------------|
| Allmänt | Ersatt romerska siffror med bokstäver genom hela filen.     |
| 24      | Lagt till nya reservdelar.                                  |
| 30      | Illustration uppdaterad och nytt namn på kåpsats.           |
| 34      | Lagt till nya anteckningar för väggprofiler 3–5 och 4–6 mm. |
| 40      | Uppdaterad illustration med nya klämmor.                    |
| 41      | Uppdaterad illustration med nya klämmor.                    |
| 46      | Uppdaterad illustration med nya klämmor.                    |
| 47      | Uppdaterad illustration med nya klämmor.                    |
| 49      | Uppdaterad illustration med nya klämmor.                    |
| 74      | Tagit bort "Stängningsagerande vid brandlarm".              |
| 75      | Uppdaterat "Eye-Tech" till "EMSP59-M".                      |
| 76      | Uppdaterat illustrationen för kåpsats.                      |
| 85      | Uppdaterat "Förbättrad" till "Utökad" i status 13.          |
| 89      | Uppdaterat orsak och åtgärd för Tre 0,3s.                   |
| 89      | Uppdaterat orsak för Fem 0,3s och Tio 0,3s.                 |

- 2 Anvisningar för säker drift
![](_page_6_Picture_2.jpeg)

- Underlåtenhet att följa instruktionerna i denna manual kan leda till person- eller utrustningsskada.
- För att minska risken för personskador får dörröppnaren endast användas med slag- eller vikdörrar med ett eller två dörrblad.
- Använd inte utrustningen om den behöver repareras eller justeras.
- Koppla från strömmen i samband med rengörings- och underhållsarbete.
- Dörröppnaren kan användas av barn som är äldre än 8 år om barnet fått instruktioner av en person som ansvarar för deras säkerhet.
- Dörröppnaren kan användas av barn som är 8 år eller yngre om barnet fått instruktioner av en person som ansvarar för deras säkerhet.
- Dörröppnaren kan användas av personermed nedsatt fysisk,motorisk eller mental förmåga om man fått instruktioner av en person som ansvarar för deras säkerhet.
- Rengöring och underhåll får inte utföras av barn.
- Låt inte någon klättra upp på eller leka med dörren eller de fasta reglagen/fjärrstyrning.
- Om fel typ av batteri används finns risk att batteriet exploderar.
- Dörrens säkerhetsfunktioner är bortkopplade vid autoinlärning. Se upp för dörrens svängradie, den kan stänga snabbt.
- Området, där arbete utförs, ska alltid spärras av för personer och strömmen ska kopplas bort för att undvika skador.
- Om KILL-kretsen har aktiverats kommer alla dörrens säkerhetsfunktioner att åsidosättas, vilket gör att dörren stängs även om det finns ett föremål eller en människa i dörrens rörelseväg, detta kan leda till personskador. Detta driftläge används vanligtvis för att isolera ett område i händelse av eldsvåda.
- Dörrarna kan manövreras automatiskt via sensorer eller manuellt via impulsgivare. Kan även användas manuellt som dörrstängare.

# 3 Viktig information

# 3.1 Avsedd användning

EM PSW250 är en automatisk slagdörröppnare som utvecklats för att underlätta in-/utgång samt inom byggnad genom slagdörrar. EM PSW250 är en elektromekanisk dörröppnare som är godkänd för branddörrstillämpning. Öppnaren skamonteras inomhus vilket gör att den passar praktiskt taget alla typer av yttre och inre slagdörrar. Denna brett använda öppnare finns på applikationer som sträcker sig från handikappentréer i privata hem till högtrafikerad detaljvaruhandel.

Dörröppnare i utrymningsvägar ska installeras så att dörren öppnas i utrymningsriktningen, såvida inte systemet tilllåter panikutbrytning i utrymningsriktningen.

Motor och växellåda har samlats i en kompakt modul som sitter monterad längs med styrmodulen i kåpan. Öppnaren är kopplad till dörrbladet via olika typer av armsystem.

Dörren är konstruerad för kontinuerligt bruk, hög säkerhet och maximal livslängd. Systemet är självjusterande, dvs. det anpassar sig i förhållande till påverkan från normala väderväxlingar och mindre friktionsförändringar orsakade av t.ex. damm och smuts.

För utrymning i nödsituationer öppnas dörrarna manuellt.

Denna handbok innehåller alla nödvändiga anvisningar förmontage, underhåll och service av Swing Door Operator EM PSW250.

För användning, se i användarhandbok 1008788.

Spara dessa instruktioner för framtida bruk.

### 3.2 Säkerhetsföreskrifter

Innan dörren tas i drift ska man genomföra en fullständig riskbedömning och acceptanstest.

För att undvika personskada, sakskada eller driftstörningar ska instruktionerna i denna handbok noggrant följas vid installation, inställning, reparation och underhåll m.m. Det krävs utbildning för att utföra detta arbete på ett säkert sätt. Endast Entrematic Nordic-utbildade tekniker får av säkerhetsskäl utföra detta arbete.

#### 3.3 Störning av mottagningen för viss elektronikutrustning

Utrustningen kan alstra samt använda radiovågor och vid bristfällig installation kan utrustningen orsaka störningar på radio-/tv-mottagning eller störningar för annan utrustning som använder radiovågor.

Om annan utrustning inte till fullo uppfyller skyddskraven kan störningar inträffa.

Det finns ingen garanti för att störningar inte kan uppkomma vid en enskild installation. Om denna utrustning orsakar störningar på radio- och TV-mottagningen, vilket kan avgöras genom att sätta på och stänga av utrustningen, uppmanas användaren att försöka eliminera störningen genom en eller flera av följande åtgärder:

- Rikta om mottagarantennen.
- Flytta mottagaren i förhållande till utrustningen.
- Flytta bort mottagaren från utrustningen.
- Anslut mottagaren till ett annat uttag så att utrustningen och mottagaren är på olika strömförgreningar.
- Kontrollera att skyddsjorden är ansluten.

Vid behov bör användaren rådfråga återförsäljaren eller en erfaren elektroniktekniker för andra lösningar.

### 3.4 Miljökrav

Entrematic Nordicprodukter är försedda med elektronik och eventuellt också med batterier som innehåller material som kan vara farliga för miljön. Koppla bort spänningen innan elektronik och batteri tas bort och se till att dessa hanteras i enlighet med lokala bestämmelser (hur och var), samma sak gäller för förpackningar.

# 4 Tekniska specifikationer

Säkerställ att dörröppnare med nedanstående tekniska data är avsedda för installationen.

| Tillverkare:              | Entrematic Nordic AB                                                                                                                                                                                                                                                                                           |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Adress:                   | Lodjursgatan 10, SE-261 44 Landskrona, Sweden                                                                                                                                                                                                                                                                  |
| Typ:                      | EM PSW250                                                                                                                                                                                                                                                                                                      |
| Strömförsörjning:         | 100-240 V AC +10/-15 %, 50/60 Hz, nätsäkring max 10A (byggnads<br>installation)                                                                                                                                                                                                                                |
|                           | Anm:Den nätspänning som installeras ska vara skyddad,försesmed<br>allpolig nätströmbrytare med minst isoleringskapacitet enligt kate<br>gori III, ha minst 3 mm mellan kontakterna, samt installationen ska<br>utföras i enlighet med gällande bestämmelser. Dessa komponenter<br>medföljer inte vid leverans. |
| Effektförbrukning:        | Max 300W                                                                                                                                                                                                                                                                                                       |
| Manöverspänning           | 24 V DC, max. 700 mA                                                                                                                                                                                                                                                                                           |
| Nätsäkring F1, F2:        | 2 x T 6,3 AH/250 V                                                                                                                                                                                                                                                                                             |
| Dörrstorlek:              | Tryckarmsystem, storlek 4 - 7<br>Dragarmsystem, storlek 4 - 6                                                                                                                                                                                                                                                  |
| Max tröghet J:            | För PUSH = 140 kgm2<br>För PULL = 80 kgm2<br>Tröghet = Dörrvikt x (Dörrbredd)2 / 3                                                                                                                                                                                                                             |
| Elektromekanisk låsspärr: | Valbar: 12 V DC, max 1200 mA eller 24 V DC, max 600 mA                                                                                                                                                                                                                                                         |
| Dörröppningsvinkel:       | PUSH-arm:80° - 110°, with reveal 0 - 367 mm<br>PULL-arm:80° - 110°, with reveal -20 - 130 mm                                                                                                                                                                                                                   |
| Öppningstid (0° - 80°):   | Variabel mellan 2.5 - 12sekunder                                                                                                                                                                                                                                                                               |
| Stängningstid (90° -10°): | Variabel mellan 4 - 12sekunder                                                                                                                                                                                                                                                                                 |
| Öppethållandetid:         | 1.5 - 30 sekunder                                                                                                                                                                                                                                                                                              |
| Temperaturområde:         | -20 °C to +45 °C                                                                                                                                                                                                                                                                                               |
| Relativ luftfuktighet:    | Max95%                                                                                                                                                                                                                                                                                                         |
| Drivenhetens vikt:        | 7.6 kg                                                                                                                                                                                                                                                                                                         |
| Skyddsklass:              | IP20                                                                                                                                                                                                                                                                                                           |
| Skyddsklass, styrmoduler: | IP54                                                                                                                                                                                                                                                                                                           |
| Godkännanden:             | Tredje part-godkännandenfrån etablerade certifieringsorganisatio<br>ner som gäller för säkerhet vid användning, se Försäkran om inbygg<br>nad.                                                                                                                                                                 |

Denna produkt ska installeras invändigt.

![](_page_10_Figure_2.jpeg)

4.1 Tillåten dörrvikt och dörrbredd för EM PSW250

![](_page_10_Figure_5.jpeg)

# 5 Hur EM PSW250 fungerar

Slagdörröppnaren EM PSW250 har en likströmsmotor som är ansluten till utgångsaxeln genom en kombination av snäckväxel och cylindriska kugghjul. Armsystemen Push eller Pull som är kopplade till utgångsaxeln öppnar dörren vid utanpåliggande installation.

Det finns en justerbar fjädermekanism som består av en spiralfjäder kombineratmed ett länksystem med tryckrullar som inverkar på en svängd kam som är monterad på utmatningsaxeln. När dörren öppnas spänns tryckfjädern genom utgångsaxelns rotation. Under stängningscykeln överförs den upptagna fjäderkraften till utgångsaxeln genom den svängda kammen och tryckrullen Kraften som överförs från fjädern inverkar på stängningsriktningen.

Fjäderkraften kan anpassas så den ger tillräcklig kraft för att stänga dörren under manuellt läge eller vid strömavbrott.

Det går att öka stängningskraften genom att använda motorn tillsammans med fjädern och på så sätt öka dörrens stängningskraft (driven stängning).

Mekanismen består av:

![](_page_11_Picture_7.jpeg)

- Motor1
- 2 Snäckväxel
- 3 Två cylindriska kugghjul
- 4 Utgångsaxel
- 5 Spiralfjäder
- 6 Fjädermekanism som överför fjäderkraften till utgångsaxeln
- 7 Kam för optimering av vridmoment för utgångsaxeln
- 8 Mekaniskt dörrstopp på utgångsaxeln (justerbart)
- 9 Axel för mekanisk koordinator
- 10 Encoder
- 11 Mikrobrytare

#### 5.1 Öppning

När styrmodulen får en öppningssignal öppnas dörren med den hastighet som är inställd på dörröppnaren. Innan dörren är helt öppen saktar den automatiskt ned till låg hastighet. Motorn stannar när dörren har kommit till den inställda dörröppningsvinkeln. Dörren hålls i öppetläge av motorn.

Om dörren hindras under öppningen kommer den att stanna till eller helt stanna, något som kan ställas in med en DIP-kontakt (SOS). Stopp vid blockering är alltid aktiverat i programvalsläge Off.

- Fortsatt vid blockering dörren fortsätter med öppningsförsöken under öppethållandetiden.
- Stopp vid blockering dörren stänger efter 2 sekunder även om öppethållandetiden inte har gått ut.
- 5.2 Stängning

När öppethållandetiden har gått ut kommer dörröppnaren att stänga dörren automatiskt med hjälp av fjäder- och motorkraft. Dörren saktar ned till låg hastighet innan den stängs helt. Dörren hålls stängd med fjäderkraft eller kombinerat med motorns utökade stängningskraft.

- 5.3 Omkopplare
#### 5.3.1 FRÅN/AUTO/OPEN Programväljare

![](_page_12_Figure_10.jpeg)

| Funktion | Program                              |
|----------|--------------------------------------|
| FRÅN     | Enda giltiga impuls är nyckelimpuls. |
| AUTO     | Alla impulser är giltiga.            |
| ÖPPEN    | Dörren står konstant i öppet läge.   |

### 5.4 Funktioner på standardstyrmodulen CUS7

Se sida 61 för mer information.

#### 5.4.1 Strömavbrott

Vid strömavbrottfungerar dörröppnaren som dörrstängaremed kontrollerad stängningshastighet och enmikrobrytare kommer att utföra en"låskick"för säkert tillslag (endast brandklassademodeller och utan omvänd installation).

#### 5.4.2 Stängningskraft

Stängningskraften kan justeras för att överensstämma med myndighetskrav eller för att åtgärda över-/undertryck i enlighet med EN1154.

#### 5.4.3 Utökad stängningsmoment (CLTQ)

Om potentiometern CLTQ ställs in på 0° kommer dörren att stängas med normal fjäderkraft Om potentiometern vridsmedsols ökasmotorns vridmoment vid stängning.Utökat stängningsmoment reduceras till noll:

- Om dörrmonterad sensor aktiveras i stängt läge eller vid stängning (även vid manuell öppning). Gäller ej för programvalet OFF. Utökad stängningskraft kommer att avbrytas, i alla programval, efter första stängningen med KILL (utom SLAV-dörr med äldre firmware).
#### 5.4.4 Servoassistans(POAS)

Om potentiometern POAS ställs in på 0° ger öppnaren ingen servoassistans. Om potentiometern vrids medsols, kommer motorn att ge/öka servoassistansen när dörren öppnas manuellt. Området för servoassistans (POAS) beror på förspänningen av fjädern.

- 5.4.5 Push & Go (PAG)
Med DIP-kontakten väljer du Push and Go, ON eller FRÅN. Push and Go kan väljas från vilket dörrläge som helst. Push and Go är inte aktivt med programväljaren på FRÅN.

- 5.4.6 Omvänd (INV)
DIP-brytare för val av omvänd installation.

Ska användas till dörrar i utrymningsvägar, där dörren måste kunna öppnas vid brandlarm (rökevakuering). Dörren öppnas med fjäderkraft och stängs med motor. Om lås används måste låset uppfylla standarden ELtVTR.

- 5.4.7 Aktiveringsfördröjning (AD)
Innan dörren öppnas kräver denna funktion en konstant inre impuls under den angivna tiden. Fast inställd på 2 sekunder.

Under stängning öppnar dörren omgående vid impuls.

- 5.4.8 Överliggande närvarodetektor (OPD) med rammontering.
När en OPD sitter monterad på ramen eller dörrstängarkåpan precis ovanför den rörliga sidan på dörren kommer den när den aktiveras att antingen hålla dörren öppen eller stängd. Sensorns insignal är inte aktiv under öppning och stängning. Låssignalen finns att tillgå eftersom denna krävs av vissa OPD-sensorer.

- en stängd dörr kommer inte att öppnas om OPD upptäcker aktivitet i fältet
- en öppen dörr kommer inte att stängas om OPD upptäcker aktivitet i fältet
- under öppning kommer dörren att fortsätta öppnas även om OPD upptäcker aktivitet i fältet
- under stängning kommer dörren att fortsätta stängas även om OPD upptäcker aktivitet i fältet

- OPD är inte aktivt i programläge FRÅN, manuellt öppnad dörr eller vid batteridrift (energisparläge).
#### 5.4.9 Matta

Mattsäkerhet innebär att:

- en stängd dörr inte kommer att öppnas om någon kliver på mattan
- en öppen dörr inte kommer att stängas om någon kliver på mattan
- dörren vid öppning kommer att fortsätta öppnas även om någon kliver på mattan
- dörren vid stängning kommer att fortsätta stängas även om någon kliver på mattan
- öppningsimpulserna förhindras i samband med stängning om någon kliver på mattan
- mattan är inte aktivt i programläge FRÅN, manuellt öppnad dörr eller vid batteridrift (energisparläge).

#### 5.4.10 Dubbelverkande

Öppning inåt och med panikbrytfunktion utåt, se Snabbstartguide 1016464.

- 5.5 Kompletteringsenhetens EXU-SI funktioner
Se även sida 63 för mer information.

- 5.5.1 KILL eller BRAND-funktion
![](_page_16_Picture_4.jpeg)

Om KILL- eller BRNAD-kretsen har aktiverats kommer alla dörrens säkerhetsfunktioner att åsidosättas, vilket gör att dörren stängs även om det finns ett föremål eller en människa i dörrens rörelseväg, detta kan leda till personskador. Detta driftläge används vanligtvis för att isolera ett område i händelse av eldsvåda. För dubbeldörrar ska koordinator användas för att säkerställa korrekt stängning.

- Vid KILL kommer styrmodulen att bortse från alla signaler och stänga dörren(dörrarna) med normal hastighet eller 5 sekunder (se sidan 74).
- Vid impulsstyrd KILL eller BRAND: Dörröppnaren återgår till normaldrift efter KILLÅTERSTÄLL-NING. Vid manuell ÅTERSTÄLLNING ska bygeln tas bort och återställningsknappen ansluts till kopplingsplint nr 8 och jord.
- Eller om statusstyrd KILL När KILL-signalen inte längre är aktiv kommer dörröppnaren att återgå till normal drift.
- Låsets agerande vid KILL beror på vald parametergruppgrupp. Se sidan 79.

#### 5.5.2 Låsens funktioner

- Låsutgången är kortslutningssäker och kan försörja ett lås med 24 V DC, max 600 mA Låsfunktionen är aktiv i programväljarläge UTGÅNG och FRÅN
- Styrningen har utgång för DC till externa lås
- DIP-kontakter för att välja 12 eller 24 V DC, låst med eller utan spänning
- DIP-kontakt för låsavlastning och potentiometer för fördröjd öppning
- DIP-kontakt för låskick för att övervinna att låsenheten kärvar under stängning (inaktiverat för omvänd dörrinstallation)
- Ingång för låsets upplåsningssignal. Potentiometer för fördröjd öppning ska ställas in på max. Så snart upplåsningssignalen kommer börjar dörren öppnas. Låsutsignalen ska vara aktiv låg.
- Om dörren inte kan stängas helt genomför dörröppnaren ett nytt låsningsförsök (en gång vid manuellt, två gånger vid automatisk öppning).
- 5.5.3 Programväljare (väggmonterad)
	- Ingång för ÖPPEN, UTGÅNG och FRÅN (om inget program har valts är AUTO standardinställning).

**Anm:** I FRÅN-position överensstämmer dörröppnaren med lågenergibestämmelserna och dörrmonterade sensorer ska ignoreras.

#### 5.5.4 Impulser

- Ingång för YTTRE impuls, NYCKEL-impuls samt ÖPPEN/STÄNG-impuls.
#### 5.5.5 ÖPPEN/STÄNG-impuls

Impulsen öppnar dörren och den förblir öppen tills en ny impuls avges. Om det inte kommer någon ny impuls stängs dörren efter 15minuter.Detta kan göras oändligt genom att ändra parametergrupp, se sidan 79.

ÖPPEN/STÄNG-impulserfungerar endastmed programväljaren i läge AUTO. Kan även programmeras för FRÅN och UTGÅNG.

- 5.5.6 Strömavbrottsläge (reservbatterier installerade) extratillbehör
	- Vid strömavbrott kan normaldrift bibehållas med impulser från NYCKELBRYTAREN.
- Det finns två kontakter för anslutning av 2 x 12 V batterier (NiMH).
- DIP-kontakt för batteriövervakning finns också. Batterifel visas med LED-indikator på CU-ESD. Reläet på EXU-SA kan ge denna information om den har valts. En ljudsignal kan erhållas genom att man använder tillbehörskortet AIU. Det ansluts till 24 V DC och kopplas in i EXU-SA-reläets utgångsterminal. Batteriövervakning måste alltid återställas efter byte av batterier. Detta görs genom att man trycker på inlärningsknappen när batteriläget är aktivt (strömförsörjning frånkopplad).

**Anm:** Om batteriläget är ENERGISPARLÄGE måste återställningen utföras medan dörren öppnas med nyckelimpuls.

- Vid STRÖMAVBROTT avslutar dörröppnaren den aktuella driftscykeln och stänger sedan av batterimatningen. Batteridriven dörröppnare kan återaktiveras och genomföra en ny driftscykel genom att ge nyckelimpuls.
- Driftläget vid batteridrift kan ändras från ENERGISPARLÄGE till CONVENIENCE, se sidan .79 CONVENIENCE innebär att dörröppnaren fungerar normalt till dess batterierna är urladdade. Batterierna är laddningsbara och laddas av dörröppnarens styrmodul. Nya och fulladdade batterier kan normalt öppna och stänga en dörrmax. 300 gånger i convenience-läge. Energisparläget innebär att dörröppnaren kan vara i stand-byläge i upp till en vecka i väntan på en NYCKEL-impuls. Följande sensorer är inte aktiva vid batteridrift (energisparläge).
	- Matta
	- Överliggande närvarodetektor (OPD/OPS) med rammontering.
	- Närvaroimpuls, monterad på dörrens anslagssida.
	- Närvarodetektering, monterad på dörrens gångjärnssida.

**Anm:** Alla sensorer fungerar som vanligt i bekvämlighetsläge.

# 5.5.7 Funktionen Syster/Säng

# **Lösning 1**

Anslut en bryggning mellan 3 och 7 på EXU-SI-slavkortet. Använd valfri impuls på mastern för att öppna masterdörren. Använd Öppna/stäng impuls på slaven för att öppna båda dörrarna.

### **Lösning 2**

Anslut en bryggning mellan 3 och 7 på EXU-SI-slavkortet.

Ställ dip-kontakt PAG på masterkortet i läge ON.

Använd valfri impuls på mastern för att öppna masterdörren.

Tryck slavdörren manuellt så öppnas den automatiskt och stannar öppen tills masterdörren stängs.

Aktivt i programval OFF, EXIT, AUTO och OPEN.

#### **Lösning 3**

Anslut en 1(0-brytare mellan 3 och 7 på EXU-SI-slavkortet.

Brytare i läge 1, impulser för master kommer endast att öppna masterdörren.

Brytare i läge 0, impulser för master öppnar båda dörrarna.

#### **Lösning 4**

Anslut en bryggning mellan 3 och 7 på EXU-SI-slavkortet.

Ställ dip-kontakt PAG på slavkortet i läge ON.

Ev. impuls i master styrmodul:

– Kortare än 2 s öppnar bara masterdörren.

– Längre än 2 s öppnar båda dörrarna.

**Anm:** Hur man ansluter KILL-ingången beror på vilken parametergrupp som valts för slav, kontrollera att den valda gruppen har KILL-impulskonfigurationen inställd på Normalt öppen. Om KILL måste vara Normalt stängd ska terminalerna 3 och 7 kopplas bort istället för att vara anslutna.

### 5.6 Funktioner på kompletteringsenheten EXU-SA

Se även sida 64 för mer information.

- 5.6.1 Närvaroimpuls, monterad på dörrens anslagssida.
Närvaroimpulsen är aktiv när dörren är helt öppen och under stängning. Sensorn sitter monterad på dörrens anslagssida. När dörren väl är stängd ignoreras sensorn och aktiveras inte förrän nästa impuls tas emot.

**Anm:** När installationen omfattar ett dörrpar kommer närvaroimpulssignalen att öppna båda dörrarna igen. Sensorn är inte aktiv i programläge FRÅN, manuellt öppnad dörr eller vid batteridrift (energisparläge).

#### 5.6.2 Närvarodetektering, monterad på dörrens gångjärnssida.

När en sensor som sitter monterad på dörrens gångjärnssida upptäcker ett objekt skickas ett kommando till styrmodul att stanna upp. Om styrmodulen har fått en kort signal från sensorn och det fortfarande finns öppethållandetid kvar i styrenheten, kommer dörren att fortsätta öppnas om objektet har försvunnit.

Blanking potentiometern kan ställas in så att sensorn inte upptäcker en vägg eller ett föremål i närheten av en helt öppen dörr. Närvarodetekteringen har högre prioritet än närvaroimpulsen.

**Anm:** När installationen omfattar ett dörrpar kommer närvarodetekteringssignalen att stoppa båda dörrarna, utom när det rör sig om dubbel in- och utgångsdörr. Funktionen för dubbel in- och utgångsdörr kan ändras (se sidan 79). Sensorn är inte aktiv i programläge FRÅN eller vid manuellt öppnad dörr. I FRÅN-läge uppfyller dörröppnaren lågenergistandard.

#### 5.6.3 Övervakade säkerhetssensorer

Både närvaroimpuls och närvarodetektering kan övervakas. Om det blir fel på en sensor, t.ex. fel på en närvarodetektor, kommer dörröppnaren inte att godkänna några impulser. Dörren förblir i stängd position och kan endast användas som manuell dörr.

Om närvaroimpulssensorn är defektförblir dörren i öppet läge. Genom att ställa om programväljaren till OFF ställs dörrens styrmodul in på lågenergiläge. Nyckelimpuls kan användas som impuls.

- 5.6.4 BRAND-signal in
Jord och 24 V DC används för matning av rökdetektorer, se sidan 69.

Man kan ansluta brandlarm 12, 24 eller 48 V DC till BRAND-signal in, se sidan 75 och 85.

#### 5.6.5 Relä utsignal

En nedanstående fyra exempel används COM/NO/NC potentialfri kontakt, de tre första alternativen väljs via parametergrupp (se 'Relä' i tabellen på sida 79). Vid indikering Error eller KILL är statusrelä passivt (anslutning COM-NC) och vid indikering Dörr öppen eller stängd är reläet aktivt (anslutning COM-NO).

- Felindikering För extern felindikering, se sida 89.
- KILL-utsignal Används för att distribuera KILL-signalen till andra dörrar.
- Låsutgång Används för att styra lås med annan spänning än 12/24 V DC.
- Dörrindikering (hårdvarukopplad med bygel) Används för att indikera dörrens öppna eller stängda position. Indikeringsläget ställs in via bortkopplingspotentiometern. För indikering av stängd dörr justera bortkopplingspotentiometern till minimum. För indikering av öppen dörr öppnar man dörren med programvalet ÖPPEN eller annan öppningsimpuls.Därefter justerarman bortkopplingspotentiometern så att lysdioden för bortkoppling endast lyser i öppet läge (eller ovan önskade läge, precis som för bortkoppling).

# 6 Modeller

Det finns tre huvudmodeller av EM PSW250:

- Enkeldörrar
- Dubbeldörrar (två dörröppnare)
- Dubbla in-/utgångsdörrar (två dörröppnare)

Öppnarna passar både vänster- och högerhängda dörrar och är inte beroende av gångjärnens placering. Öppnarna passar både tryckande och dragande armsystem.

### 6.1 Enkelöppnare, utanpåliggande

Produkten levereras komplett med bottenplatta, styrenhet, ändgavlar och kåpa. Total kåplängd CL inklusive ändplåtar.

Bilden visar ett tryckande armsystem.

![](_page_20_Figure_10.jpeg)

![](_page_20_Figure_11.jpeg)

Modulkåpan har en täckkåpa utöver standardkåpan.

$$\begin{array}{c} \text{CL}_{\text{min}} = \text{840} \\ \text{CL}_{\text{max}} = 1684 \end{array}$$

![](_page_20_Figure_14.jpeg)

Fullängdskåpa. Ej tillgängligt från Entrematic Nordic, ska ordnas lokalt. CL min =840 CLmax = 1684

# 6.2 Dubbelöppnare, utanpåliggande

Produkten levereras komplett med bottenplatta, styrenhet, ändgavlar och kåpa. Total kåplängd CL inklusive ändplåtar.

Två dörröppnare kan monteras under samma kåpa (full längd eller modulär) för att öppna en dörr vardera. Bilden visar ett tryckande och ett dragande armsystem (dubbel ingång och utgångsdörr). Det går även att använda två tryckande eller två dragande armsystem.

![](_page_21_Figure_4.jpeg)

| Post nr |                                | Artikelnr: Beskrivning                                               |
|---------|--------------------------------|----------------------------------------------------------------------|
| 1       |                                | 331003554 EXU-SI sats för säkerhet & impulser                        |
| 2       |                                | 331003557 EXU-SA-säkerhetssats                                       |
| 3       |                                | 331003583 Synkkabelkit                                               |
| 4       |                                | 330000483 Encoderkabel                                               |
| 5       | 330000487F                     | Transmissionsenhet PSW250 Brand (får ej användas i DE, GB<br>och SE) |
|         |                                | 330000487F-PUSH Transmissionsenhet PSW250 Brand PUSH                 |
|         |                                | 330000487F-PULL Transmissionsenhet PSW250 Brand PULL                 |
|         |                                | 330000487F-SYM Drivenhet PSW250 Brand SYM                            |
| 6       |                                | 330000488 Mikrobrytarsats                                            |
| 7       |                                | 330000489 Stopparmsats                                               |
| 8       |                                | 331011678 Styrmodul CUS7 utan EXU-enheter                            |
| 9       |                                | 331008344 Anslutningsbox reservdel                                   |
| 10      |                                | 330000490 FRÅN/AUTO/ÖPPENprogramväljare                              |
| 11A     | 330000554 Fästsats             | Drivenhet till w.1845                                                |
| 11B     | 330000759 Fästsats FB          | Drivenhet från w.1845                                                |
| 12      | 330000491BK/SI Utfyllnad kåpa  |                                                                      |
| 13      | 331011887BK/SI Kåpa            |                                                                      |
| 14      |                                | 1013484 Koordinatortopp                                              |
| 15      | 1013316 Stagset                |                                                                      |
| 16      |                                | 330000682 Koordinator-servicesats                                    |
| 17      |                                | 330000684 Fäste för styrenhet CUS7                                   |
| 18      |                                | 1012561 Batterienhet                                                 |
| 19      | 331007825BK/SI Nedre gavelplåt |                                                                      |
| 20      | 331008615 LED-kabel            |                                                                      |
| 21      |                                | 1011784 Återställnings- och indikeringsenhet                         |
| 22      |                                | 1012240 Sats för stängningsbroms                                     |
| 23      |                                | 331009903 Mikrobrytare kort och kam                                  |
| 24      | 330000484BK/SI Adaptersats     |                                                                      |
| 25      |                                | 330000485BK/SI PUSH-arm service kit                                  |
| 26      |                                | 330000486BK/SI PULL-armservicesats                                   |
| 27      |                                | 331017738BK/SI Mellanstycke (2 delar)                                |

# 8 Armsystem

Installationsförlopp för armsystem är samma för installation av branddörrar och omvända installationer.

- 8.1 Tryckande installation med PUSH-arm
Detta armsystem levererasmed drivarm, teleskopisk del och dörrbeslag. Används om dörröppnaren ärmonterad på väggen,mittemot dörrens öppningsriktning och är godkändaför branddörrstillämpningar för A upp till 300 mm.

Art. No.: 1011706BK/SI

![](_page_24_Picture_6.jpeg)

![](_page_24_Figure_7.jpeg)

![](_page_24_Figure_8.jpeg)

### 8.2 Installation med dragande PULL-arm

Detta armsystem levereras med drivarm, styrsko och dörrbeslag. Godkänd som branddörr för A upp till 130 mm.

PULL,Art. No.: 1011707BK/SI (A = -20-130 mm)

PULL-220, Art. No.: 1014114BK/SI (A = -20-65 mm), endast för LE-prestanda

![](_page_25_Figure_5.jpeg)

#### 8.3 20 mm förlängning

20 mm förlängning för PULL/PAS och lägre montering av löpskenan. Art. Nr: 1011205

![](_page_25_Figure_8.jpeg)

# 8.4 Tryckinstallation med PULL-arm

Armsystemet består av huvudarm, löpskena, gejdsko och axeladapter. Kan monteras på kombinationer av dörrar och karmstycken (väggar), där väggens tjocklek inte överstiger ungefär 114 mm De mått som anges här motsvarar en öppningsvinkel på 90-100°.

![](_page_26_Figure_3.jpeg)

![](_page_26_Figure_4.jpeg)

### 8.5 Förlängningssatser för drivaxel

![](_page_27_Picture_2.jpeg)

Lägre M10 adapter används för 20 mm lägre installationshöjd.

![](_page_27_Picture_4.jpeg)

Art. Nr:1011705BK/SI

# 9 Tillval

- 9.1 Omkopplare
- 9.1.1 Programväljare PS-4C (driver elektriskt lås)

| Art. Nr:<br>655845 | Befattning |                          | Funktion                                                                                                                                                                                                  |  |  |
|--------------------|------------|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                    |            | FRÅN                     | Dörren är stängd. Dörren kan inte öppnas med inre och yttre im<br>pulsgivare. Dörren är spärrad om en elektromekanisk låsspärr har<br>monterats. Dörren kan öppnas med nyckelkontakt (om sådan<br>finns). |  |  |
|                    |            | UTGÅNG                   | Passage endast från insidan. Dörren är normalt spärrad om en<br>elektromekanisk låsspärr harmonterats.Dörren kan endast öppnas<br>med inre impulsgivare och med nyckelkontakt (om sådan finns).           |  |  |
|                    |            | AUTO<br>Normalt lä<br>ge | Dörren kan öppnasmed de inre och yttremanuella och/eller auto<br>matiska impulsgivarna. Det elektriska låsblecket (om sådant<br>monterats) är öppet.                                                      |  |  |
|                    |            | ÖPPEN                    | Dörren hålls hela tiden öppen av motorn.                                                                                                                                                                  |  |  |

# 9.2 Synkkabel för dubbeldörrar (synkroniserar 2 dörröppnare)

![](_page_28_Figure_6.jpeg)

**Anm:** Synkkabelns anslutningen/märkning avgör vilken av dörröppnarna som är MASTER och

Art. Nr: 1003583

#### 9.3 Koordinatorenhet

För att koordinera falsade dörrar vid dubbeldörrinstallation och för att kontrollera att dörrarna stängs i rätt ordning. Se sida54 för installation och justering.

![](_page_28_Picture_11.jpeg)

| Artikelnr: | Beskrivning       |
|------------|-------------------|
| 1013484    | Koordinatortoppen |
| 1013316    | Stagset           |

![](_page_29_Figure_1.jpeg)

För att uppfylla standarden DIN 18263-4 måste man montera och ansluta detta kort till låskicken. Art. Nr:1012240

#### 9.8 Brandsats

#### För branddörrar

Innehåller rökdetektor ORS142W med silverfärgad kåpa, Återställnings- och indikeringsenhet, Stängningsbromssats och trepolig anslutningskabel.

![](_page_30_Figure_4.jpeg)

Art. Nr:1011785

### 9.9 Monteringsplåt (för förstärkning av vägg)

![](_page_30_Figure_7.jpeg)

| Artikelnr: | Beskrivning                                                  | Anmärkning |
|------------|--------------------------------------------------------------|------------|
| 701588CLS  | Kapa till rätt storlek, tillstånd L (716-3 300mm) 125 x 6 mm |            |
| 1014965CLS | Kapa till rätt storlek, tillstånd L (716-3 300mm) 80 x 6 mm  |            |

# 9.10 Etiketter

**Etikettsats**- inklusive alla nedanstående Art. Nr:1012241

![](_page_31_Picture_3.jpeg)

Panikbrytbeslag. DIN höger dörr

![](_page_31_Picture_5.jpeg)

Panikbrytbeslag. DIN vänster dörr

![](_page_31_Picture_7.jpeg)

Aktiveringsenhet för rörelsehindrade

![](_page_31_Picture_9.jpeg)

Öppnare avsedd för rörelsehindrade:

![](_page_31_Picture_11.jpeg)

Uppsikt över barn

# 10 Förinstallation

# 10.1 Allmänna tips/säkerhetsfrågor

![](_page_32_Picture_3.jpeg)

Området, där arbete utförs, ska alltid spärras av för personer och strömmen ska kopplas bort för att undvika skador.

- Om det finns vassa kanter/grader efter borrning av kabelutgångar ska dessa avfasas för att undvika kabelskador.
- För större säkerhet och skydd mot vandalism bör dörröppnarens enhet om möjligt alltid monteras inuti byggnaden.
- Kontrollera att omgivande temperatur ligger inom specifikationerna i avsnittet Tekniska specifikationer.
- Se till att spänningen är avstängd före installation.
- Se till att dörrblad och vägg är ordentligt förstärkta vid monteringspunkterna.
- Packa upp dörröppnaren och kontrollera att alla delar som anges på packsedeln har bifogats och att öppnaren är i bra mekaniskt skick.
- Använd korrekta material till dörrbladen och se till att det inte finns några vassa kanter. Utskjutande delar får inte utgöra någon fara/risk. Om glas används får inte bara glaskanter ha kontakt med annat glas. Härdat eller laminerat glas är lämpliga glastyper.
- Kontrollera att det inte går att inneslutas mellan drivna delar och kringliggande fasta delar när den drivna delen öppnas. Följande mått anses vara tillräckliga för att undvika inneslutning av nämnda kroppsdelar:
	- för fingrar ska avståndet vara större än 25 mm eller mindre än 8 mm
	- för fötter ska avståndet vara större än 50 mm
	- för huvud ska avståndet vara större än 200 mm
	- och för hela kroppen ska avståndet vara större än 500 mm
- Riskpunkter bör skyddas upp till en höjd på 2,5 m från golvnivå.
- Dörröppnaren ska inte användas med dörrset som omfattar en gångdörr.

### 10.2 Dörröppnare/dörrhängning

Dörröppnare/dörrhängning (DIN höger eller DIN vänster) fastställs genom vilken sida gångjärnen är monterade på sett från dörrens gångjärnssida.

![](_page_32_Picture_21.jpeg)

![](_page_32_Figure_22.jpeg)

ILL-01625

# 10.3 Monteringsexempel

![](_page_33_Figure_2.jpeg)

![](_page_33_Figure_3.jpeg)

![](_page_33_Figure_4.jpeg)

![](_page_33_Figure_5.jpeg)

- 2 Gipsskivevägg
- 3 Tegelvägg och vägg i armerad betong

10.4 Fästkrav (ej inkluderat)

- 4 Gipsskivevägg
	-
- A Stålförstärkning eller blindnitmutter
- B Träförstärkning

B

branddörr

- Expansionsskruv (för tegelväggmin.M6x85,UPAT PSEA B10/25) C
Icke brännbara material vid användning som

| Grundmaterial  | Minimikrav för väggprofil*                                                    |
|----------------|-------------------------------------------------------------------------------|
| Stål           | 5 mm**                                                                        |
| Aluminium      | 6 mm***                                                                       |
| Armerad betong | min. 50 mm från undersidan                                                    |
| Trä            | 50 mm                                                                         |
| Tegelvägg      | Expansionsskruv, min. M6x85, UPAT PSEA B10/25, min. 50 mm från un<br>dersidan |

* Entrematic Nordic rekommenderademinimikrav. Det kanfinnas andra uppgifter i byggnormerna.

** Tunnare väggar (3–5 mm) måste förstärkas med blindnitmuttrar.

*** Tunnare väggar (4–6 mm) måste förstärkas med blindnitmuttrar.

### 10.5 Erforderliga verktyg

- Metriska insexnycklar 1.5; 2.5; 3; 4; 5 och 6 mm
- Momentnyckel 8 Nm, 14 Nm och 50 Nm
- Insexnyckel 1.5; 2.5 och 3 mmmed sfärisk spets
- Torx T10 och T20
- Verktyg för skruv mellan kåpa och bakgavel
- Spårskruvmejsel (för potentiometer och anslutningsplint)
- Skruvmejsel (Phillips storlek 2)
- Fast nyckel 5 och 7 mm
- Måttband
- Borrmaskin och borrsats
- Körnare
- Skaltång
- Silikontätning
- Installations- och servicehandbok (denna handbok)

# 11 Mekanisk installation

Dörröppnaren är monterad på vardera sida om dörrens överstycke, beroende på dörrtyp. Dörren styrs av ett tryckande- eller dragande armssystem.

Om koordineringsenhet skamonteras på dubbeldörrarmonteras koordinatorns bottenplattamed rotor innan man monterar transmisionsenheten, se sida 54.

**Anm:**Obs: Tänk på ingångsställenför samtliga nät- och signalkablar innan bakre plåten görs i ordning.

Drivenheten ska monteras vid mått A och styrenheten ska monteras vid mått B. Illustrationerna visar även hur kablarna ska dras. Om det finns vassa kanter/grader efter borrning av kabelutgångar ska dessa avfasas för att undvika kabelskador.

![](_page_36_Figure_1.jpeg)

![](_page_37_Figure_1.jpeg)

#### 11.1 PUSH-armsystem

![](_page_38_Figure_2.jpeg)

![](_page_39_Figure_1.jpeg)

![](_page_40_Figure_1.jpeg)

**Kontinuerlig "Dörröppnare med PUSH-armsystem"**

![](_page_41_Figure_2.jpeg)

#### **Kontinuerlig "Dörröppnare med PUSH-armsystem"**

![](_page_42_Picture_2.jpeg)

**F**

**G** MÄRKE

Rikta in markeringarna mellan arm och adapter.

Rikta in armen mot dörröppnarens markering.

![](_page_42_Figure_6.jpeg)

**J**

(2x)

Fäst armsystemet i dörren.

![](_page_43_Picture_1.jpeg)

Se tabell på sida 25 för tillgängliga förlängare. Fortsättning på sida 60.

# 11.2 PULL armsystem

Slim löpskena

![](_page_44_Figure_3.jpeg)

**Anm:** Mått Z ska minskas med 20 mm om man använder den lägre adaptern i setet 1011705BK/SI.

![](_page_45_Figure_1.jpeg)

![](_page_46_Figure_1.jpeg)

![](_page_47_Figure_1.jpeg)

#### **Slim löpskena**

Fäst löpskenan (1) i dörren med gejdskon (2) monterad i spåret. Använd avsedda skruvar.

![](_page_48_Picture_3.jpeg)

- 1 Löpskena
- 2 Styrsko

![](_page_49_Figure_1.jpeg)

Håll dörren öppen en bit och ta bort stiftet för startposition.

- 11.3 Dörröppnare med PUSH glidarmsystem
#### Slim löpskena

![](_page_50_Figure_3.jpeg)

Se anvisningarna för dragande installation (PULL)

# 11.4 omvänd installation med tryckarmsystem PUSH

Ta bort mikrobrytararmen (1) men inte mikrobrytaren. Ta även bort stopparmen (3).

![](_page_51_Picture_3.jpeg)

**Anm:** Ställ dip-kontakt INV i läge ON för Inverse funktion, se 12.1.1 på sida 61. Fjäderspänningen ska inte vara mer än 7 mm.

Följ steg **A** till **K** i avsnittPUSH-armsystem på sida 39, med den skillnaden att dörröppnaren svänger 180° så att texten "INVERSE" blir synlig på öppnaren och utför inte steg **D** och **I** .

![](_page_51_Figure_6.jpeg)

#### 11.5 omvänd installation med tryckarmsystem PULL

Ta bort mikrobrytararmen (1) men inte mikrobrytaren. Ta även bort stopparmen (3).

![](_page_52_Picture_3.jpeg)

**Anm:** Ställ dip-kontakt INV i läge ON för Inverse funktion, se 12.1.1 på sida 61. Fjäderspänningen ska inte vara mer än 7 mm.

Följ stegen **A** till **E** på sida 46, med den skillnaden att dörröppnaren svänger 180° så att texten "INVERSE" blir synlig på öppnaren och utför inte utför steg **D** .

![](_page_52_Figure_6.jpeg)

- 11.6 Installation av koordineringsenhet på branddörrar
Innan installation av transmisionsenheten ska nedanstående steg a-e utföras. Skruva in de två styrstiften (1) till korrdinatorbasen.

![](_page_53_Picture_3.jpeg)

Montera rotorn (delarna 2 till 4 nedan) innan motorn installeras på bottenplattan. Installera styrenheten efter installationen av koordineringsenheten slutförts.

Om koordineringsenheten ska installeras på en befintlig installation kan man flytta styrenheten en liten bit, så att man når motorenheten under installationen.

#### **Länkstångens längd = gångjärn till gångjärn - 980 mm**

- a Lossa skruvarna (2) och ta bort kopplingskåpan (3) från rotorn (4).
- b Vrid kopplingskåpan (3) baserat på aktuell PULL- eller PUSH-installation. För PULL-installation visas PULL och för PUSH-installation visas PUSH.
- c Spänn åt skruvarna (2).

![](_page_53_Figure_10.jpeg)

- d Montera rotorn (4) på motorenheten (7) med skruv (5) och bricka (6) på huvuddrivenheten = för dörrar som öppnas först och stängs sist.
![](_page_54_Figure_2.jpeg)

- e Frigör bromsen (26) genom att trycka in länkarmen (14) så att bromsen (26) öppnas, tryck in gaffeln (27) i koordinatorbasen (15).
![](_page_54_Figure_4.jpeg)

- 14 Länkarm
- 15 Koordinatorplatta
- 26 broms
- gaffel27
- f Montera koordineringsbasen (15) med två skruvar (8) på huvuddrivenheten. Ta bort skruv (9) och kasta brickan (24) vid montering av acceptor (11) på justerdonet (10). Montera skruven (9) genom accesslänken (11).
- g Montera transmisionsenheten. Justera bottenskruven (10) genom att vrida tills huvuddörren stannar vid 15-18°från helt stängd (denna vinkel ska varamindre än den elektriska koordinatorn). Stäng dörren genom att trycka på länkarmen (14).

![](_page_55_Figure_3.jpeg)

- h Ställ in bromsmomentet på >50 Nm, uppmätt på dörrbladet när man vrider på en eller båda skruvarna (19).
![](_page_55_Picture_5.jpeg)

Skruv19

- i Montera länkstång (12) med adapter (13) i länkarmen (14).
![](_page_56_Figure_2.jpeg)

- j Montera på den andra sidan av länkstaget (12) till slavmotor med signal (16). Spänn åt stoppskruven (17).
![](_page_56_Figure_4.jpeg)

- 12 Länkstag
- Signal16
- 17 Stoppskruv

- k Justera bromsens frigöring genom att lossa leden (18) och vrida länkstången (12) mot huvuddrivenheten. Ställ in vinkeln mellan dörrarna i nästan stängt läge.
![](_page_57_Figure_2.jpeg)

- l Dra kablarna så som visas i illustrationerna på sidan 37.
- m Applicera fett på stödstången.

![](_page_57_Figure_5.jpeg)

Skarv18

- n Montera löpvals (20) på framkanten, i närheten av toppen på slavdörrbladet (21), använd avsedda skruvar (23).
![](_page_58_Figure_2.jpeg)

# 12 El-anslutning

#### **Anm:**

- Placera strömbrytaren så att man enkelt kommer åt den från dörröppnaren. Om man använder stickkontakt vid installationen av väggkontakten ska denna vara lätt åtkomlig från öppnaren.
- Om nätsladden är skadad måste den bytas ut av tillverkaren, dennes servicetekniker eller annan behörig person för att undvika fara.

Se Autoinlärning ställer automatiskt in lågfartssträcka i öppning och stängning (rekommenderas). på sidan 73.

#### **Nätanslutning**

- a Stäng av huvudströmmen.
- b Anslut stickkontakten till vägguttaget eller anslut till huvudströmbrytaren

Standard

![](_page_59_Picture_10.jpeg)

# 12.1 Styrmoduler

![](_page_60_Figure_2.jpeg)

**Anm:** Anslut motorkabeln till endera PUSH eller PULL, beroende på aktuellt armsystem.

#### 12.1.2 Val av armsystem

Fabriksinställd armkonfiguration är PUSH, om annat önskas:

Välj armkonfiguration via DIP-brytaren i enlighet med nedanstående tabell.

|                      | ON=1<br>OFF=0 |               |                                       |                  |
|----------------------|---------------|---------------|---------------------------------------|------------------|
| Typ av armsystem     | AS 1<br>DIP 6 | AS 2<br>DIP 7 | PUSH<br>PUSH<br>ON<br>3<br>2<br>1     | 7<br>6<br>5<br>4 |
| PUSH                 | 0             | 0             |                                       |                  |
| PULL                 | 1             | 0             | PULL<br>PULL<br>ON<br>3<br>2<br>1     | 7<br>6<br>5<br>4 |
| PULL-220 (smal dörr) | 0             | 1             |                                       |                  |
| Glidskena-PUSH       | 1             | 1             |                                       | 7                |
|                      |               |               | PULL<br>PULL-220<br>ON<br>3<br>2<br>1 | 6<br>5<br>4      |
|                      |               |               | Skjutdörr<br>Sliding<br>ON            | 7<br>6<br>5<br>4 |

**Anm:** Efter ändring av systemval måste man utföra nya INLÄRNING.

 3 2 1

PUSH

PUSH

- 12.1.3 Kompletteringsenheter EXU-SI / EXU-SA
### **Installation**

![](_page_61_Figure_3.jpeg)

#### 12.1.4 Kompletteringsenhet EXU-SI

Denna kompletteringsenhet har ingångar för elektromekanisk låsspärr, programväljare, batterier, KILL-funktion, ÖPPEN/STÄNG, nyckelimpuls och yttre impuls.

# **Funktioner**

Batteribackupsenhet

![](_page_62_Figure_5.jpeg)

- 1 Lock 12 V (OFF) / 24 V (ON)* Lås 12 V (FRÅN) / 24 V (ON)*
- 2 Locked without power (OFF) / with power (ON)* Låst utan spänning (FRÅN)/med spänning (ON)*
- 3 Lock release2) Låsfrigöring* 2)
- 4 Lock kick1) Låskick1)
- 5 Battery monitoring Batteriövervakning
- Position FRÅN: Lugn stängning, för dörrar utan lås.Läge : ON Kraftigare stängning, för dörrar med lås, för att undvika att låsanordningen kärvar (inaktiverad för omvänd dörrinstallation). 1)
- Om kontakten är inställd på ON, är LÅSFRIGÖRNING aktiv under den fördröjda öppningstid som ställts in med potentiometern. 2)

Vid installationer med PARDÖRRAR arbetar LÅSFRIGÖRNING i sekvensen: Först MASTER därefter SLAV.

**Anm:** Spärra endast funktioner när programväljaren är i läge FRÅN eller UTGÅNG.

- * Efter ändring av systemval måste man utföra nya INLÄRNING. Genom valet "Låst utan spänning" aktiveras låset från 0 till 10 grader vid öppning.
# 12.1.5 Kompletteringsenhet EXU-SA

Denna kompletteringsenhet har ingång för dörrmonterade sensorer som kan ge närvaroimpuls på anslagssidan och/eller närvarodetektering på gångjärnsidan. Det finns också reläutgång för felangivelse, KILL-utsignal, låssignal eller dörrindikation. När bygeln för reläet är inställd på "Indikering för öppen/stängd dörr" följer aktiveringen lysdioden för bortkoppling.

# **Funktioner**

![](_page_63_Figure_4.jpeg)

- QTST = Sensorövervakning och referens för KILL (NC)
- PDET = Närvarodetektering (NC)1)
- PIMP = Närvaroimpuls (NC)1)
- 1) Jorda om den inte används.
- 2) Ta bort jordningen från kopplingsplint 2 och/eller 3.

#### 12.1.6 Montering på dubbla in- och utgångsdörrar

Om öppnarna ska monteras med tryckande och dragande amsystem på samma höjd bestäms höjden av det dragande armsystemet, PULL. Tryckarmsystemet PUSHmåste alltid ha axelförlängning på minst 50 mm, maximum 70 mm för att passa monteringshöjden visuellt.

Exempel: om PULL har 20 mm förlängning måste PUSH ha 70 mm förlängning. Om PULL har 0 mm förlängning måste PUSH ha 50 mm förlängning.

Utför monteringen med hjälp av anvisningarna för det aktuella armsystemet. Om man använder stängningskoordinator, se sida 54 a-e innan installationen påbörjas.

![](_page_64_Picture_5.jpeg)

12.2 Hur man klipper synkkabelns bygel för dubbeldörrar

**Anm:** Anslut kabeln mellan Master CU och Slav CU.

![](_page_64_Figure_9.jpeg)

**Anm:** Synkkabelns anslutningen/märkning avgör vilken av dörröppnarna som är MASTER och SLAV. För falsad dörr,

- **masterdörren** ska **öppnas** före **slavdörren**
- **Slavdörren** ska **stängas** före **masterdörren**

| Funktion                   | Dörrkonstruktion |        | Klipp den färgade bygeln |             |            |  |
|----------------------------|------------------|--------|--------------------------|-------------|------------|--|
| Öppning                    | Stängning        | Falsad | Kläm-<br>mande           | MASTER-sida | SLAV-sida  |  |
| Synkron                    | Synkron          | Nej    | Nej                      | Klipp inte  | Klipp inte |  |
| Synkron                    | Asynkron         |        | Nej                      | Klipp svart | Klipp inte |  |
| Asynkron                   | Asynkron         | Ja     |                          | Klipp inte  | Klipp röd  |  |
| Dubbel in- och utgångsdörr | —                | —      | Klipp svart              | Klipp röd   |            |  |

![](_page_64_Figure_14.jpeg)

#### 12.3 Installation av dubbeldörr

Det finns tre typer av installation för dubbeldörrar:

- Falsad Har överlappande master-dörr, kan öppnas synkroniserat om den inte kärvar och ska stängas asynkront för att undvika att dörrarna kärvar eller stängs i fel ordning.
- Klämning Denna dörrtyp måste öppnas och stängas asynkront för att undvika att dörrarna kärvar med varandra.
- Ingen klämning, ingen falsning Denna typ av dörr har dörrar som alltid kan röras oberoende av varandra och kan öppnas/stängas synkroniserat.

#### 12.4 Inställning för dubbeldörrar

|                                          | Inställning på |      |  |  |
|------------------------------------------|----------------|------|--|--|
| Funktion                                 | MASTER         | SLAV |  |  |
| Gemensam                                 |                |      |  |  |
| Programval                               | X              |      |  |  |
| Öppningstid                              | X              |      |  |  |
| Stängningstid                            | X              |      |  |  |
| Öppethållandetid                         | X              |      |  |  |
| Stäng / fortsätt öppna om dörren hindras | X              |      |  |  |
| PAG PÅ/AV                                | X              |      |  |  |
| SOS On/Off                               | X              |      |  |  |
| Servonivå                                | X              | (X)* |  |  |
| Utökad stängningskraft                   | X              | (X)* |  |  |
| OPD/OPS-impuls eller logisk mattimpuls   | X              |      |  |  |
| Välja driftläge vid batteridrift         | X              |      |  |  |
| Individuell                              |                |      |  |  |
| Lås/lås-uppsignalspänning                | X              | X    |  |  |
| Låst utan/med spänning                   | X              | X    |  |  |
| Låsavlastning på/av                      | X              | X    |  |  |
| Öppningsfördröjningstid                  | X              | X    |  |  |
| Låskick på/av                            | X              | X    |  |  |

* Med "dubbel in- och utgångsdörr" måste dessa funktioner ställas in separat för MASTER och SLAV eftersom armsystemen liksom lufttrycket kan variera.

#### **Anm:**

- Låsen på MASTER och SLAV måste anslutas till styrmodulen (CU) på motsvarande dörröppnare.
- Inre och yttre impulser kan anslutas antingen till MASTER eller SLAV-CU eller till båda.
- MASTER
- Sensorer monterade på dörrblad måste alltid anslutas till motsvarande CU.

### 12.5 Kabelingång för sensor

Art. Nr: 1007567

![](_page_66_Picture_3.jpeg)

### 12.6 Återställnings- och indikeringsenhet för branddörrar

Art. Nr: 1011784

![](_page_67_Figure_3.jpeg)

![](_page_67_Figure_4.jpeg)

A Reset & Indication device B Smoke detector Återställnings- och indikeringsenhet Rökdetektor

![](_page_67_Figure_6.jpeg)

A 15.5 29 7.5 ø 3.7 **1 2 3 4 5** 48

![](_page_68_Figure_1.jpeg)

# 13 Driftsättning

### 13.1 Fjäderförspännare

Fjäderspänningen är**fabriksinställd på EN4.** Stängningskraften (fjäderkraften) justeras på en insexskruv som sitter i slutet av fjädern. När muttern vrids medurs ökar kraften. Ett varv motsvarar ett ändrat vridmoment på ungefär 7-9 Nm för PUSH och 4-6 Nm för PULL (ungefär 7 varv från min. till max).

![](_page_69_Figure_4.jpeg)

| Dörröppna<br>re, ef                        | Rekommenderad<br>dörrbladsbredd i | Stängningskraft<br>mellan 0º och 4º |                 | Öppningskraft<br>mellan 0º och 60º |  |
|--------------------------------------------|-----------------------------------|-------------------------------------|-----------------|------------------------------------|--|
| fektstorlek i<br>enlighet<br>med<br>EN1154 | mm max.                           |                                     | Nm min. Nm max. | Nm max *                           |  |
| 4                                          | 1100                              | 26                                  | <37             | 62                                 |  |
| 5                                          | 1250                              | 37                                  | <54             | 83                                 |  |
| 6                                          | 1400                              | 54                                  | <87             | 134                                |  |
| 7                                          | 1600                              | 87                                  | <140            | 215                                |  |

* **Anm:** I utrymningsvägar är max öppningskraft 150 N.

**Anm:** Ovanstående tabell är endast avsedd för Normal dörröppnare (branddörrar). För omvända dörrinstallationer (nödöppningsfunktion) är maximal fjäderspänning 7 mm och detta måste ställas in vid installationen för att dörren ska öppnas och stängas mjukt.

# 13.2 Mikrobrytare

Kontrollera och ställ in mikrobrytaren som reglerar låskick vid strömavbrott.

![](_page_70_Picture_3.jpeg)

# 13.3 Ställa in dörrstoppet

- a Stäng dörren.
![](_page_70_Figure_6.jpeg)

- b Öppna dörren till önskat öppetläge plus ungefär 15 mm. Placera en dörrstopp under dörren.
![](_page_70_Figure_8.jpeg)

- c När stopparmen är på ovansidan av dörröppnaren lyfter man dörrstopparmen och monterar den i räfflingen, så nära stoppblocket 1 som möjligt). Finjustera vid behov med skruven på stopparmen 2).
![](_page_70_Figure_10.jpeg)

0°

SPTE

- d När stopparmen är i dörröppnarens underkant frigör man stopparmsspärren och stopparmen. Montera stopparmen på axelutgångarna, så nära stoppblocket 3 som möjligt). Montera stopparmsspärren. Finjustera vid behov med skruven på stopparmen 4).
![](_page_71_Picture_2.jpeg)

![](_page_71_Picture_3.jpeg)

- e Stäng dörren.
0°

SPTE

![](_page_71_Picture_5.jpeg)

- 1 Stopparm
- 2 Stoppblock
- 3 Finjusteringsskruv

# 13.4 Autoinlärning ställer automatiskt in lågfartssträcka i öppning och stängning (rekommenderas).

Detta gör man genom att trycka in INLÄRNINGSKNAPPEN (LRN).

- Slå på strömmen till dörren (dörröppnaren hittar stängt läge) och kontrollera att lysdioden är tänd.
![](_page_72_Picture_4.jpeg)

- Innan inlärningsproceduren påbörjas måste man se till att dörren är ordentligt stängd, dvs. inte med våld.
- I följande situationer ska ny inlärning utföras
	- Om någon av parametrarna FJÄDERSPÄNNING och STÄNGNINGSMOMENT (CLTQ) ändras efter utförd inlärning.
	- Om någon av armsystemets DIP-kontakter ändras.
- I följande situationer räcker det att man trycker på inlärningsknappen för att bekräfta
	- Vid ev. förändring av MAT-dip.
	- Vid byte av befintliga enheter.
	- Vid byte av Lås med/utan ström.
	- Vid byte av lås 12/24 V.
- Inlärningen kan göras med aktiveringsenheterna och låsen anslutna.
- Lågfartssträcka öppning kommer automatiskt att ställas in på 10° och 1 sekund före öppet läge. Lågfartssträcka stängning kommer automatiskt att ställas in på 10° och 1,5 sekund före stängt läge.

![](_page_72_Picture_16.jpeg)

![](_page_72_Figure_17.jpeg)

# 13.4.1 Tryck på INLÄRNINGSKNAPPEN (LRN)

![](_page_73_Picture_2.jpeg)

Dörrens säkerhetsfunktioner är bortkopplade vid autoinlärning. Se upp för dörrens svängradie, den kan stänga snabbt.

**Anm:** Om inlärningsknappen trycks in en gång utförs inlärning för smyg 0-100 mm. För större smyg ska knappen hållas intryckt och därefter släppas när status-LED blinkar för önskad smyg, se nedanstående tabell.

| LED blinkar                   |            | Smyg [mm] Tillgängligt för armsystem |
|-------------------------------|------------|--------------------------------------|
| En 0,3 sek blink, 2 sek paus  | 0 -- 100   | PUSH, PULL, skjutande PUSH           |
| Två 0,3 sek blink, 2 sek paus | 101 -- 200 | PUSH, PULL                           |
| Tre 0,3 sek blink, 2 sek paus | 201 --     | PUSH, PULL-600                       |

Närman trycker in inlärningsknappen börjar statuslysdioden blinka och slutar inte innan inlärningen slutförts.

**Anm:** Om dörrstopp inte monterats i golvet ska dörren stoppas i önskat öppetläge.

Cykeln för inlärning börjar med sensordetektering, under denna står dörren stilla. När dörren börjar röra sig mäts fjäderspänningens och dörrens tröghet och dörrens positioner för öppen och stängd sparas.När inlärningen har utförts beräknas öppningens och stängningens lågfartssträcka, öppningstid och stängningstid. De ändrade inställningarna påverkar hur installationen agerar och måste kontrolleras.

![](_page_73_Figure_9.jpeg)

#### 13.4.2 Dubbeldörr

Med dubbeldörrar måste MASTER-dörren lära sig först och därefter SLAV-dörren När SLAV-dörren har lärt sig kommer MASTER-dörren att öppnas helt under SLAV-dörrens inlärningsfas.

Dörrarna kan också läras separat innan synkkabeln ansluts. Om det finns falsade dörrar och separat inlärning måste MASTER-dörren hållas öppen innan man kör inlärning för SLAV-dörren.

### 13.5 Allmänna inställningar

- a Ställ in öppethållandetiden med potentiometern på styrmodulen.
- b Justera öppningshastigheten (OPSP). Vrid medsols för att öka hastigheten.
- c Justera stängningshastigheten (CLSP) Vrid motsols för att sänka hastigheten.
- d Anslut impulsgivarna.
- e Kontrollera att installationen överensstämmer med myndighetsbeslut

# 13.6 Anslutning av impulsgivare och tillbehör

Semanualenför sensorer rörandemontering och justering. Skyddsutrustning ska överensstämmamed EN 12978.

#### **Dörrmonterad**

När sensorer används för att undvika kontaktmed dörrbladetmåste närvarodetektorn och närvaroimpulssensorn uppfylla prestandanivå = c i enlighet med EN ISO 13849-1. Dessa sensorer ska även övervakas (testas) med dörröppnare EM PSW250.

** OBS! Om man använder snabbkoppling blir öppningsoch stängningssidorna tvärt om.

Konfigurera sensorn EMSP33-M: DIP A7 till ON (för mastersensor) DIP B4 till ON för närvaroimpuls DIP B4 till OFF för närvarodetektor

|        |                                        |               | PS-4C     | Aktivering             |                                                            |                    |         |                 |      |     |
|--------|----------------------------------------|---------------|-----------|------------------------|------------------------------------------------------------|--------------------|---------|-----------------|------|-----|
|        |                                        | Brand<br>larm |           | ssensor                | EMSP51-M**                                                 | EMSP33-M           |         | EMSP59-M        |      |     |
|        | PRESS<br>TO OPEN                       |               |           |                        |                                                            |                    |         |                 |      |     |
|        |                                        |               |           | 1 2 3 4                | A B C D E F G H                                            | A C H B F D I E    |         | A B C J E F G H |      |     |
|        |                                        |               | 1 2 3 4 5 | GND<br>IMP<br>+        |                                                            |                    |         |                 |      |     |
| CU-S7  | 1<br>2                                 |               |           | 5 1<br>2<br>5 1<br>2   |                                                            |                    |         |                 |      | 1   |
|        |                                        |               |           |                        |                                                            |                    |         |                 |      |     |
| EXU-SI | 3<br>4                                 |               |           | 13 3<br>4<br>13 3<br>4 |                                                            |                    |         |                 |      | 2   |
| EXU-SI | 3<br>6                                 |               | 3 101112  |                        |                                                            |                    |         |                 |      | 3   |
|        |                                        |               |           |                        |                                                            |                    |         |                 |      |     |
| EXU-SA |                                        |               |           |                        | 1 1 1 2<br>4 5 5                                           | 1 1 1 2<br>4 5 5   | 1 1 1 2 | 4 5 5           |      | 4   |
| EXU-SA |                                        |               |           |                        | 1 1 1<br>3<br>54 5                                         | 1 1 1<br>3<br>54 5 | 1 1 1   | 3<br>54 5       |      | 5   |
|        |                                        |               |           |                        |                                                            |                    |         |                 |      |     |
| EXU-SA |                                        |               |           |                        |                                                            |                    |         |                 |      | 4 5 |
|        |                                        |               |           |                        |                                                            |                    |         |                 |      |     |
| EXU-SI |                                        |               |           |                        |                                                            |                    |         | 3<br>10         | 3 10 | 6   |
| EXU-SI | 3<br>7                                 |               |           |                        |                                                            |                    |         |                 |      | 7   |
|        |                                        |               |           |                        |                                                            |                    |         |                 |      |     |
| EXU-SI | 7<br>7                                 |               |           |                        |                                                            |                    |         |                 |      | 8   |
| EXU-SA | 4                                      |               |           |                        |                                                            |                    |         |                 |      |     |
| EXU-SI | 3 8                                    |               |           |                        |                                                            |                    |         |                 |      |     |
|        |                                        |               |           |                        |                                                            |                    |         |                 |      | 9   |
| EXU-SA |                                        | 6 7           |           |                        |                                                            |                    |         |                 |      | 10  |
| 1      | Inre impuls                            |               |           |                        |                                                            |                    | A       | Brun            |      |     |
| 2      | Yttre impuls                           |               |           |                        |                                                            |                    | B       | Gul             |      |     |
| 3      | Nyckelimpuls                           |               |           |                        |                                                            |                    | C       | Rosa            |      |     |
| 4      | Närvaroimpuls                          |               |           |                        |                                                            |                    | D       | Violett         |      |     |
| 5      | Närvarodetektering                     |               |           |                        |                                                            |                    | VitE    |                 |      |     |
| 6      | Av                                     |               |           |                        |                                                            |                    | BlåF    |                 |      |     |
| 7      | Killimpuls NO                          |               |           |                        |                                                            |                    | G       | Röd             |      |     |
| 8      | Kill-impuls NC, brandlarm, rökdetektor |               |           |                        |                                                            |                    | H       | Grön            |      |     |
| 9      | Återställning vid brandlarm            |               |           |                        |                                                            |                    | I       | Svart           |      |     |
| 10     |                                        |               |           |                        | Externt brandlarm (välj 12, 24 eller 48 V DC, se sidan 85) |                    | J       | Grå             |      |     |

# 14 Kåpa

Kåpan och bottenplattan är tillverkade av natureloxerat aluminium. Ändplattorna är tillverkade av svart stålplåt.

- 14.1 Montering och demontering av kåpa
Kåpan skjuts på flänsarna i bottenplattan så att kanterna passar in i spåren. Snäpp på täckkåpan i utgångsaxelns spår. Säkra kåpan med skruven.

Efter korrekt installation och injustering ska den medföljande produktetiketten, med CE-märkning, fästas på den nedre högra delen av öppnarens kåpa (se bilden).

Fäst EM-logotypen på kåpan - se illustrationen.

Endast för SE: Montera SITAC-etiketten intill produktetiketten - se illustrationen.

![](_page_75_Picture_8.jpeg)

14.2 Kåpsats

![](_page_75_Figure_10.jpeg)

|                   | X        |
|-------------------|----------|
| Enkelflyglig dörr | CL-843.5 |
| Dubbeldörr        | CL-1682  |

# 15 Skyltar

![](_page_76_Figure_2.jpeg)

Kontrollera att samtliga erfordrade skyltar sitter och är intakta. Skyltar är obligatoriskt enligt europeiska förordningar och motsvarande nationell lagstiftning utanför Europeiska unionen.

| A | Produktetikett: Obligatoriskt                                                                                                                                                                                |
|---|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| B | Panikbrytbeslag: Obligatoriskt om enheten är godkänd som utrymningsväg.                                                                                                                                      |
| C | Entrematic Nordic dörrdekal: Obligatoriskt i enlighet med Entrematic Nordic anvisningar, Europeiska direktiv och motsvarande<br>nationella lagar utanför EU, för att åskådliggöra att dörrbladet är av glas. |
| D | Uppsikt över barn (applicerad på båda sidor av dörren): Obligatoriskt enligt gällande bestämmelser. Rekommenderas om riskana<br>lysen visar användning av barn.                                              |
| E | Impulsgivare utformad för rörelsehindrade:<br>Rekommenderas, om tillämpligt (applicerad på båda sidor av dörren).                                                                                            |
| F | Aktiveringsenhet för rörelsehindrade: Rekommenderat, om tillämpligt.                                                                                                                                         |
| G | Förbjuden ingång, anger enkelriktad trafik: I förekommande fall obligatoriskt i Storbritannien och USA, ingår inte i produkten.                                                                              |
| H | SITAC-etikett: Obligatorisk i SE                                                                                                                                                                             |

# 16 Avancerade inställningar

- 16.1 Inlärning med avancerad inställning av lågfartsområde i öppning och stängning"
Läs om förutsättningarna för att genomföra en "inlärning" under rubriken Autoinlärning ställer automatiskt in lågfartssträcka i öppning och stängning (rekommenderas). på sida 73.

- a Tryck på knappen en gång, som vid autoinställning. Status-LED börjar blinka. Samma som för autoinställning.
- b Stoppa dörren vid önskad öppningsposition.
- c Dörren återgår till stängt läge.
- d Stoppa dörren vid önskat lågfartsområde i stängning.
- e Dörren återgår till inlärning av öppningsbroms.
- f Stoppa dörren vid önskat lågfartsområde i öppning.
- g Ta bort stoppet.
- h Dörren återgår till stängt läge.
- 16.2 Återgå till ursprungsvärdena för "lågfartsområde i öppning och stängning" (nivå 1).
	- a Koppla bort eventuella batterier.
	- b Koppla från strömmen.
	- c Tryck in och håll INLÄRNINGSKNAPPEN (LRN) intryckt.
	- d Koppla på strömmen.
	- e Iaktta FEL-LED:n.

![](_page_77_Figure_18.jpeg)

- f Släpp INLÄRNINGSKNAPPEN efter 1 blinkning (LED är släckt).
- g LÅGFARTSOMRÅDE ÖPPNING, LÅGFARTSOMRÅDE STÄNGNING och ÖPPETLÄGE har nu återgått till ursprungsvärdena.
- h Koppla från strömmen.
- i Nästa gång strömmen ansluts krävs attman genomför en ny inlärning och dörröppnaren kommer att använda ursprungsvärdena.
- 16.3 Byte av parametergrupp (nivå 2)
	- a Koppla bort eventuella batterier.
	- b Koppla från strömmen.
	- c Tryck in och håll INLÄRNINGSKNAPPEN (LRN) intryckt.
	- d Koppla på strömmen.
	- e Iaktta FEL-LED:n.

![](_page_78_Figure_7.jpeg)

f Släpp INLÄRNINGSKNAPPEN efter 2 blinkningar (LED är släckt). FEL-LED:n blinkar kort några gånger vilket motsvarar parametergruppens nummer (se tabell). Efter en kort paus kommer LED:n att upprepa gruppnumret, osv.

- g Genom att trycka en gång på INLÄRNINGSKNAPPEN ökas parametergruppnumret. När man kommit till det högsta parametergruppnumret börjar det om med nummer 1 (standard) igen.
- h Tryck in knappen till dess du får upp den önskvärda parametergruppen. Kontrollera att önskad parametergrupp har valts genom att räkna antalet blinkningar.
- i Koppla från strömmen.
- j Nästa gång strömmen kopplas på kommer dörröppnaren att använda sig av den nya parametergruppen.

| Parameter/grupp                                                                               | (standard)<br>1                       | 2                                        | 3                                                      | 4                                                     | 5                                                           | 6                                                  | 7                                                | 8                                           | 9                                             | 10                                                        |
|-----------------------------------------------------------------------------------------------|---------------------------------------|------------------------------------------|--------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------------|----------------------------------------------------|--------------------------------------------------|---------------------------------------------|-----------------------------------------------|-----------------------------------------------------------|
| ÖPPETHÅLLANDETID<br>ÖPPNA/STÄNG                                                               | minuter<br>15                         | Oändligt                                 | minuter<br>15                                          | minuter<br>15                                         | minuter<br>15                                               | minuter<br>15                                      | minuter<br>15                                    | minuter<br>15                               | minuter<br>15                                 | minuter<br>15                                             |
| läge<br>Batteri                                                                               | Energisparläge                        | Energisparläge                           | Convenience                                            | Energisparläge                                        | Energisparläge                                              | Energisparläge                                     | Energisparläge                                   | Energisparläge                              | Energisparläge                                | Convenience                                               |
| läge<br>KILL                                                                                  | KILL<br>vid<br>Låst                   | KILL<br>vid<br>Låst                      | KILL<br>vid<br>Låst                                    | KILL<br>pro-<br>följer<br>vid<br>gramvalet<br>Låsning | KILL<br>vid<br>Låst                                         | KILL<br>vid<br>Låst                                | KILL<br>vid<br>Låst                              | KILL<br>vid<br>Låst                         | program<br>KILL*<br>Låsföljer<br>vid<br>valet | KILL<br>vid<br>Låst                                       |
| läge1)<br>HINDER                                                                              | Dörrstängare                          | Dörrstängare                             | Dörrstängare                                           | Dörrstängare                                          | hin-<br>stäng-<br>vid<br>Reverserar<br>under<br>ning<br>der | Dörrstängare                                       | Dörrstängare                                     | Dörrstängare                                | Dörrstängare                                  | hin<br>stäng<br>vid<br>Reverserar<br>under<br>ning<br>der |
| läge<br>UTGÅNG<br>och<br>IN-<br>DUBBELDÖRR                                                    | Separatnärvarode-<br>tektering        | Separatnärvarode-<br>tektering           | Separatnärvarode-<br>tektering                         | Separatnärvarode-<br>tektering                        | Separatnärvarode-<br>tektering                              | Normalnärvarode-<br>tektering                      | Separatnärvarode-<br>tektering                   | Separatnärvarode-<br>tektering              | Separatnärvarode-<br>tektering                | Separatnärvarode<br>tektering                             |
| LÅSNINGSFÖRSÖK2)<br>NYTT                                                                      | On                                    | On                                       | On                                                     | On                                                    | On                                                          | On                                                 | Av                                               | On                                          | On                                            | On                                                        |
| impuls<br>ÖPPNA/STÄNG                                                                         | AUTO-läge<br>I                        | AUTO-läge<br>I                           | AUTO-läge<br>I                                         | AUTO-läge<br>I                                        | AUTO-läge<br>I                                              | AUTO-läge<br>I                                     | AUTO-läge<br>I                                   | och<br>FRÅN,<br>UTGÅNG<br>AUTO<br>läge<br>I | AUTO-läge<br>I                                | AUTO-läge<br>I                                            |
| Konfiguration2)<br>KILL-impuls                                                                | öppen<br>Normalt                      | öppen<br>Normalt                         | öppen<br>Normalt                                       | öppen<br>Normalt                                      | öppen<br>Normalt                                            | öppen<br>Normalt                                   | öppen<br>Normalt                                 | öppen<br>Normalt                            | stängd<br>Övervakad<br>Normalt                | öppen<br>Normalt                                          |
| Relä2)                                                                                        | Felindikering                         | Felindikering                            | Felindikering                                          | Felindikering                                         | Felindikering                                               | Felindikering                                      | Felindikering                                    | Felindikering                               | Felindikering                                 | Felindikering                                             |
| Dubbelverkande2)                                                                              | Nej                                   | Nej                                      | Nej                                                    | Nej                                                   | Nej                                                         | Nej                                                | Nej                                              | Nej                                         | Nej                                           | Nej                                                       |
| under<br>impuls<br>vid<br>upp<br>låses<br>Låset<br>*                                          | läget<br>i<br>KILL                    | UTGÅNG.                                  |                                                        |                                                       |                                                             |                                                    |                                                  |                                             |                                               |                                                           |
| inställd<br>är<br>dörröppnaren<br>Om<br>1)                                                    | VID<br>ÅTERGÅ<br>att<br>på            | kommer<br>HINDER                         | öppnas<br>att<br>den                                   | hinder,<br>vid<br>igen                                | vid<br>som<br>precis                                        | närvaroimpuls.<br>en                               |                                                  |                                             |                                               |                                                           |
| dubbeldörr<br>av<br>installation<br>Vid<br>2)                                                 | parameter<br>denna<br>ska             | SLAV<br>hos                              | valda<br>den<br>följa                                  | parametergruppen                                      | oavsett<br>SLAV,<br>för                                     | MASTER-konfiguration.                              |                                                  |                                             |                                               |                                                           |
|                                                                                               |                                       |                                          |                                                        |                                                       |                                                             |                                                    |                                                  |                                             |                                               |                                                           |
| när<br>låsblecket<br>"NYTT<br>(se<br>mot<br>av<br>kärvar<br>stänga<br>det<br>att<br>Om<br>går | stängs<br>och<br>dörren<br>LÅSFÖRSÖK" | dörren<br>7)<br>parametergrupp<br>kommer | dubbeldörrar<br>två<br>stänga<br>försöka<br>vid<br>och | SLAV<br>måste<br>i<br>gånger                          | för<br>för<br>standardinställning<br>konfigureras           | drift,<br>OBS<br>automatisk<br>(se<br>själv<br>sig | UTGÅNG<br>varför).<br>eller<br>FRÅN<br>för<br>2) | gång<br>en<br>och                           | läge.<br>manuellt<br>i                        | funktion<br>Denna                                         |
|                                                                                               |                                       |                                          |                                                        |                                                       |                                                             |                                                    |                                                  |                                             |                                               |                                                           |

| Parameter/grupp                                                                           | 11                                                 | 12                                 | 13                                    | 14                                                    | 15                                                | 16                                                | 17                                                | 18                                                      | 19                                 | 20                                                | 21                                |
|-------------------------------------------------------------------------------------------|----------------------------------------------------|------------------------------------|---------------------------------------|-------------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------------|------------------------------------|---------------------------------------------------|-----------------------------------|
| ÖPPETHÅLLANDETID<br>ÖPPNA/STÄNG                                                           | minuter<br>15                                      | minuter<br>15                      | minuter<br>15                         | minuter<br>15                                         | Oändligt                                          | Oändligt                                          | minuter<br>15                                     | minuter<br>15                                           | minuter<br>15                      | minuter<br>15                                     | minuter<br>15                     |
| läge<br>Batteri                                                                           | Energisparläge                                     | Energisparläge                     | Energisparläge                        | Energisparläge                                        | Convenience                                       | Convenience                                       | Energisparläge                                    | Convenience                                             | Energisparläge                     | Energisparläge                                    | Convenience                       |
| läge<br>KILL                                                                              | KILL<br>vid<br>Olåst                               | KILL<br>vid<br>Olåst               | KILL<br>vid<br>Låst                   | KILL<br>vid<br>Olåst                                  | KILL<br>vid<br>Låst                               | KILL<br>vid<br>Låst                               | KILL<br>vid<br>Olåst                              | Väljare<br>enligt<br>program<br>KILL*<br>Låsning<br>vid | KILL<br>vid<br>Olåst               | KILL<br>vid<br>Olåst                              | KILL<br>under<br>Olåst            |
| läge1)<br>HINDER                                                                          | Dörrstängare                                       | Dörrstängare                       | Dörrstängare                          | Dörrstängare                                          | vid<br>under<br>Reverserar<br>stängning<br>hinder | vid<br>under<br>Reverserar<br>stängning<br>hinder | vid<br>under<br>Reverserar<br>stängning<br>hinder | vid<br>under<br>Reverserar<br>stängning<br>hinder       | Dörrstängare                       | vid<br>under<br>Reverserar<br>stängning<br>hinder | Dörrstängare                      |
| läge<br>UTGÅNG<br>och<br>IN-<br>DUBBELDÖRR                                                | närvaro-<br>detektering<br>Separat                 | närvaro-<br>detektering<br>Separat | närvaro-<br>detektering<br>Separat    | närvaro-<br>detektering<br>Separat                    | närvaro-<br>detektering<br>Separat                | närvaro-<br>detektering<br>Separat                | närvaro-<br>detektering<br>Separat                | närvaro-<br>detektering<br>Separat                      | närvaro-<br>detektering<br>Separat | närvaro-<br>detektering<br>Separat                | närvaro<br>detektering<br>Separat |
| LÅSNINGSFÖRSÖK2)<br>NYTT                                                                  | On                                                 | On                                 | On                                    | On                                                    | On                                                | On                                                | On                                                | On                                                      | On                                 | On                                                | On                                |
| impuls<br>ÖPPNA/STÄNG                                                                     | AUTO-läge<br>I                                     | AUTO-läge<br>I                     | AUTO-läge<br>I                        | AUTO-läge<br>I                                        | och<br>FRÅN,<br>UTGÅNG<br>AUTO<br>läge<br>I       | och<br>FRÅN,<br>UTGÅNG<br>AUTO<br>läge<br>I       | AUTO-läge<br>I                                    | AUTO-läge<br>I                                          | AUTO-läge<br>I                     | AUTO-läge<br>I                                    | AUTO-läge<br>I                    |
| Konfiguration2)<br>KILL-impuls                                                            | öppen<br>Normalt                                   | stängd<br>Övervakad<br>Normalt     | stängd<br>Övervakad<br>Normalt        | stängd<br>Övervakad<br>Normalt                        | öppen<br>Normalt                                  | stängd<br>Övervakad<br>Normalt                    | stängd<br>Övervakad<br>Normalt                    | stängd<br>Övervakad<br>Normalt                          | stängd<br>Övervakad<br>Normalt     | stängd<br>Övervakad<br>Normalt                    | stängd<br>Övervakad<br>Normalt    |
| Relä2)                                                                                    | KILLut                                             | KILLut                             | KILLut                                | Elslutbleck                                           | Elslutbleck                                       | Elslutbleck                                       | Felindikering                                     | Felindikering                                           | Felindikering                      | Felindikering                                     | Felindikering                     |
| Dubbelverkande2)                                                                          | Nej                                                | Nej                                | Nej                                   | Nej                                                   | Nej                                               | Nej                                               | Nej                                               | Nej                                                     | Ja                                 | Ja                                                | Ja                                |
| inställd<br>impuls<br>är<br>dörröppnaren<br>vid<br>upp<br>låses<br>Låset<br>Om<br>1)<br>* | ÅTERGÅ<br>läget<br>i<br>KILL<br>att<br>under<br>på | HINDER<br>UTGÅNG.<br>VID           | att<br>den<br>kommer                  | vid<br>igen<br>öppnas                                 | precis<br>hinder,                                 | en<br>vid<br>som                                  | närvaroimpuls.                                    |                                                         |                                    |                                                   |                                   |
| dubbeldörr<br>av<br>installation<br>Vid<br>2)                                             | denna<br>ska                                       | hos<br>parameter                   | valda<br>den<br>följa<br>SLAV         | parametergruppen                                      | SLAV,<br>för                                      | oavsett                                           | MASTER-konfiguration.                             |                                                         |                                    |                                                   |                                   |
| låsblecket<br>"NYTT<br>(se<br>mot<br>av<br>kärvar<br>stänga<br>det<br>att<br>Om<br>går    | stängs<br>och<br>dörren<br>LÅSFÖRSÖK"<br>när       | parametergrupp<br>kommer           | försöka<br>vid<br>och<br>dörren<br>7) | måste<br>i<br>gånger<br>dubbeldörrar<br>två<br>stänga | standardinställning<br>konfigureras<br>SLAV       | automatisk<br>själv<br>sig<br>för<br>för          | FRÅN<br>för<br>2)<br>drift,<br>OBS<br>(se         | UTGÅNG<br>varför).<br>eller                             | i<br>gång<br>en<br>och             | läge.<br>manuellt                                 | funktion<br>Denna                 |
| även<br>reläutgången<br>Om<br>Anm:                                                        | Lås<br>för<br>används                              | använder<br>SLAV<br>på             | man                                   | i<br>15<br>parametergrupp                             | SLAV.                                             |                                                   |                                                   |                                                         |                                    |                                                   |                                   |
| med<br>installationer<br>Vid                                                              | dubbla<br>dubbelverkande                           | måste<br>dörrar                    | ha<br>SLAV-dörren                     | samma                                                 | som<br>parametergrupp                             | MASTER-dörren.                                    |                                                   |                                                         |                                    |                                                   |                                   |

# 16.4 Klassificering (nivå 3)

- a Koppla bort eventuella batterier.
- b Koppla från strömmen.
- c Tryck in och håll INLÄRNINGSKNAPPEN (LRN) intryckt.
- d Koppla på strömmen.
- e Iaktta FEL-LED:n.

![](_page_81_Figure_7.jpeg)

- f Släpp INLÄRNINGSKNAPPEN efter 3 blinkningar (LED är släckt).
- g Identifiera aktuell klassificering

FEL-LED:n blinkar kort några gånger vilket motsvarar klassificeringsnumret. Efter en kort paus kommer LED:n att upprepa klassificeringsnumret, osv.

- h Ändra klassifikation
Om man trycker en gång på INLÄRNINGSKNAPPEN ökas klassificeringsnumret. När man når högsta klassifikationsnumret börjar cykeln om på ett igen.

- Tryck in knappen till dess du får upp den önskade klassifikationen.
- Koppla från strömmen.

Nästa gång strömmen kopplas på kommer dörröppnaren att använda sig av den nya klassificeringen.

- i Klassificeringstabell

| Klassificering                    | 1                      | 2                             |
|-----------------------------------|------------------------|-------------------------------|
|                                   | Full effekt (Standard) | Lågenergi (                   |
| Standard                          |                        | EN 16005                      |
| Öppningshastig- 2.5 - 12 s<br>het |                        | Automatisk begränsning 1.69 J |
| Stängningshas-<br>tighet          | 4 - 12 s               | Automatisk begränsning 1.69 J |

Den snabbaste inställningen för öppnings- och stängningshastighet begränsas automatiskt till det värde som anges i tabellen och kan endast minskas.

Om man använder klassificeringen 2 för lågenergi kommer dörröppnaren automatiskt hålla hastighetsbegränsningen i EN 16005.

Inlärningsförloppet måste utföras om inställningen för klassificering ändras.

### **Hastighetsinställningar för lågene**

Tabellen visar max öppningstid till låghastiighetsområdet eller till 80° öppen dörr eller minsta stängningstid från 90° till 10° öppen dörr.

| Dörrbladsbredd (mm) | Dörrvikt (kg)   |     |     |     |     |  |
|---------------------|-----------------|-----|-----|-----|-----|--|
|                     | 50              | 60  | 70  | 80  | 90  |  |
|                     | Tid (s) minimum |     |     |     |     |  |
| 750                 | 3,0             | 3,2 | 3,2 | 3,3 | 3,5 |  |
| 850                 | 3,1             | 3,1 | 3,2 | 3,4 | 3,6 |  |
| 1000                | 3,2             | 3,4 | 3,7 | 4,0 | 4,2 |  |
| 1200                | 3,8             | 4,2 | 4,5 | 4,8 | 5,1 |  |

# 16.5 Överliggande närvarodetektering och slussfunktion (nivå 4)

- a Koppla bort eventuella batterier.
- b Koppla från strömmen.
- c Tryck in och håll INLÄRNINGSKNAPPEN (LRN) intryckt.
- d Koppla på strömmen.
- e Iaktta FEL-LED:n.

![](_page_82_Figure_7.jpeg)

- f Släpp INLÄRNINGSKNAPPEN efter 4 blinkningar (LED är släckt).
- g Identifiera aktuell övervakning

FEL-LED:n blinkar kort några gånger vilket motsvarar statusnummer. Efter en kort paus kommer LED:n att upprepa statusnumret, osv.

- h Ändra status
Om man trycker en gång på INLÄRNINGSKNAPPEN ökas statusnumret. När man når högsta statusnumret börjar cykeln om på ett igen.

| Nivå 4:              | 1 (stan-<br>dard) | 2    | 3           | 4                | 5                | 6                  |
|----------------------|-------------------|------|-------------|------------------|------------------|--------------------|
| OPD-övervakning FRÅN |                   | ON   | FRÅN        | FRÅN             | FRÅN             | FRÅN               |
| Slussfunktion*       | FRÅN              | FRÅN | Slav (låst) | Slav<br>(stängd) | Master<br>(låst) | Master<br>(stängd) |

* Slussfunktion kan inte användas tillsammans med OPD-sensorer. Om (låst) används måste dörröppnaren vara i läge EXIT eller OFF.

- Koppla från strömmen.
Nästa gång strömmen ansluts kommer dörröppnaren använda den nya statusinställningen.

- i Rekommenderade inställningar för sensor SP34-M
![](_page_82_Figure_18.jpeg)

- j Anslutningar för slussfunktion
![](_page_83_Figure_2.jpeg)

# 16.6 Förbättrad låskick, brand insignal och utökat larmval (nivå 5)

- a Koppla bort eventuella batterier.
- b Koppla från strömmen.
- c Tryck in och håll INLÄRNINGSKNAPPEN (LRN) intryckt.
- d Koppla på strömmen.
- e Iaktta FEL-LED:n.

![](_page_84_Figure_7.jpeg)

- f Släpp INLÄRNINGSKNAPPEN efter 5 blinkningar (LED är släckt).
- g Identifiera aktuell status för låskick

FEL-LED:n blinkar kort några gånger vilket motsvarar statusnummer. Efter en kort paus kommer LED:n att upprepa statusnumret, osv.

- h Ändra status
Om man trycker en gång på INLÄRNINGSKNAPPEN ökas statusnumret. När man når högsta statusnumret börjar cykeln om på ett igen.

| Nivå 5:                                           | 1 (stan-<br>dard)            | 2                              | 3                            | 4                              | 5                           | 6                             |
|---------------------------------------------------|------------------------------|--------------------------------|------------------------------|--------------------------------|-----------------------------|-------------------------------|
| Låskick typ<br>Brand-insignal<br>**<br>Val av arm | Standard<br>FRÅN<br>Standard | Förbättrad<br>FRÅN<br>Standard | Standard<br>12 V<br>Standard | Förbättrad<br>12 V<br>Standard | Standard<br>24V<br>Standard | Förbättrad<br>24V<br>Standard |
|                                                   | 7                            | 8                              | 9                            | 10                             | 11                          | 12                            |
| Låskick typ<br>Brand-insignal<br>Val av arm       | Standard<br>48 V<br>Standard | Förbättrad<br>48 V<br>Standard | Standard<br>FRÅN<br>Utökad   | Förbättrad<br>FRÅN<br>Utökad   | Standard<br>12 V<br>Utökad  | Förbättrad<br>12 V<br>Utökad  |
|                                                   | 13                           | 14                             | 15                           | 16                             |                             |                               |
| Låskick typ<br>Brand-insignal<br>Val av arm       | Standard<br>24V<br>Utökad    | Förbättrad<br>24V<br>Utökad    | Standard<br>48 V<br>Utökad   | Förbättrad<br>48 V<br>Utökad   |                             |                               |

** När brand-insignal används måste alla andra inställningar utföras innan man väljer 12 V, 24 V eller 48 V.

| Grundläggande val av arm |    | Utökat val av arm         |
|--------------------------|----|---------------------------|
| PUSH                     | 00 | -                         |
| PULL                     | 10 | PULL-600, 250 mm, -20-230 |
| PULL-220                 | 01 | PULL-600, 420 mm, -20-230 |
| Glidskena-PUSH           | 11 | -                         |

• Koppla från strömmen.

Nästa gång strömmen kopplas på kommer dörröppnaren att använda sig av den nya statusinställningen.

Brandlarmsignal, Uf, ska väljas bland: OFF, 12 V DC, 24 V DC och 48 V DC. Uf ska tolkas som OK, inget brandlarm, i följande ordning: 0,85 x Uf till 1,2 x Uf. Återställ på samma sätt som för KILL-ÅTERSTÄLLNING.

# 17 Instruktion för installation och justeringar

# 17.1 Kompletterande säkerhetsanordningar för slagdörrar

Om det finns risk för att fastna med fingrarna kan man montera fingerskydd på gångjärnsidan av invändiga dörrar, artikelnr 833334 eller fingerskyddsrulle för utvändiga dörrar, artikelnr 833333.

- 17.2 Öppnings- och stängningstider för slagdörrar.
Ställ in öppnarens öppnings- och stängningstider minst enligt nedanstående diagram.

### 17.2.1 Hur hittar jag korrekt öppnings- och stängningstid

- Mät dörrbredden.
- Om man inte känner till dörrvikten ska man följa anvisningarna i "diagram för dörrvikt".
- Gå in i nedanstående diagram för att hitta korrekt minimitid för öppning/stängning "t".

Exempel: Om dörren är 1,1 m bred och väger 80 kg blir minsta öppnings- och stängningstid ~4,3 sekunder.

![](_page_85_Figure_11.jpeg)

Minsta öppnings-/stängningstider "t" för slagdör-

### 17.3 Diagram för dörrvikt

- a Mät dörrens bredd (DW) samt höjd (DH) i meter för bara ett dörrblad.
- b Räkna ut ytan DWxDH.
- c Välj diagram för din dörrtyp och glastjocklek. Ta reda på vikten.

*Exempel*: En aluminiumdörr med måtten DW = 1,5 m, DH = 2 m och glastjocklek 12 mm - räkna ut 1,5x2 = 3 m.2. Titta i det första diagrammet för "aluminiumram med glas". Börja med ytan och följ linjen upp till 12 mm glas, gå till vänster så hittar du dörrvikten på 95 kg.

**Anm:** Vikterna kan variera beroende på dörrens konstruktion (tabellen visar bara exempelvärden).

- 17.3.1 Aluminiumram med glas
![](_page_86_Figure_8.jpeg)

Dörrbladsvikt [kg]

# 18 Felsökning

| Fel                  | Möjliga orsaker                                       | Åtgärder/förklaring                                                                               |  |  |
|----------------------|-------------------------------------------------------|---------------------------------------------------------------------------------------------------|--|--|
| Dörren öppnar inte.  | Programväljaren står på FRÅN                          | Ändra programväljarinställningen                                                                  |  |  |
| Motorn startar inte  | Nätspänning saknas                                    | Kontrollera strömbrytaren                                                                         |  |  |
|                      | Impulsgivare fungerar inte                            | Spänn fast impulsingångarna.                                                                      |  |  |
|                      | Närvarodetektionen är aktiverad                       | Kontrollera att det inte finns några föremål i<br>detekteringszonen                               |  |  |
|                      | KILL aktiverats                                       | Avaktivera KILL                                                                                   |  |  |
| öppnas inte          | Motorn startarmen dörren Det mekaniska låset är låst. | Lås upp låset                                                                                     |  |  |
|                      | Något har fastnat under dörren                        | Ta bort objektet                                                                                  |  |  |
|                      | Det elektriska låsblecket kärvar                      | Välj låsavlastning                                                                                |  |  |
|                      |                                                       | Justera låsblecket                                                                                |  |  |
|                      | Armsystemet har lossnat                               | Använd verktyget och spetsen och placera<br>dörren i önskad öppen position. Spänn armsy<br>stemet |  |  |
| Dörren stänger inte. | Programväljaren står på ÖPPEN                         | Ändra inställning för brytaren FRÅN/AU<br>TO/OPEN                                                 |  |  |
|                      | Närvaroimpuls aktiverad                               | Ta bort objektet i detekteringszonen.                                                             |  |  |
|                      | Något har fastnat under dörren                        | Ta bort objektet                                                                                  |  |  |

### 18.1 Felindikering

- Under normal drift är statuslysdioden (LED) på styrmodulen tänd.
- Släckt LED innebär att strömmen inte är påkopplad.
- Blinkande LED innebär att dörröppnaren inte fungerar (se nedanstående tabell).

| LED blinkfrekvens/Displaymed- Orsak<br>delande          |                                                                                                                 | Åtgärd                                                                                                                                                                                       |  |  |
|---------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
| En 0,3 sek blink, 10 sek paus etc. Kill-impuls är aktiv |                                                                                                                 | Utför kill-återställning, återställ kill<br>kontakt eller brandlarm                                                                                                                          |  |  |
|                                                         | + 24 V DC externt fel                                                                                           | Kontrollera ev. kortslutning                                                                                                                                                                 |  |  |
| En 0,3 sek blink, 2 sek paus etc.                       | Sensorövervakningsfel                                                                                           | Kontrollera att övervakningssensor<br>är hel                                                                                                                                                 |  |  |
| Två 0.3 sek blink, paus, etc.                           | Batterifel                                                                                                      | Ersätt batteriet (normaldrift med<br>strömmen påslagen). Om batteriö<br>vervaknings DIP är i läge ON behövs<br>troligen en återställning av denna<br>(efter batteribyte), se avsnitt 5.5.6.) |  |  |
| Tre 0.3 sek blink, paus, etc.                           | het                                                                                                             | Fel på styrmodul eller driven- Byt ut styrmodul eller drivenhet                                                                                                                              |  |  |
| Fyra 0.3 sek blink, paus, etc.                          | Encoder-fel                                                                                                     | Kontrollera encoderkabeln<br>Öppna och stäng dörren manuellt<br>och kontrollera därefter autofunk<br>tionen.Om dörröppnarenfortfaran<br>de inte fungerar måste drivmodu<br>len bytas ut.     |  |  |
| Fem 0.3 sek blink, paus, etc.                           | Låsenhet defekt eller lås med<br>för hög strömförbrukning                                                       | Undersök ev.kortslutningilåsanord<br>ningen                                                                                                                                                  |  |  |
|                                                         |                                                                                                                 | Byt ut låsanordningen                                                                                                                                                                        |  |  |
|                                                         | Fel på EXU-SI-kortet                                                                                            | Byt ut EXU-SI-kortet                                                                                                                                                                         |  |  |
| Sex 0.3 sek blink, paus, etc.                           | Synkkabelninte ansluten eller Anslut synkkabeln                                                                 |                                                                                                                                                                                              |  |  |
|                                                         | felaktig (gäller endast<br>dubbeldörrar)                                                                        | Byt ut synkkabeln                                                                                                                                                                            |  |  |
| Sju 0.3 sek blink, paus, etc.                           | Fel på SLAV-styrmodulen<br>(endast dubbeldörrar)                                                                | Kontrollera blinkfrekvensen på<br>SLAV-LED:n och vidtag nödvändiga<br>åtgärder i enlighet med denna ta<br>bell.                                                                              |  |  |
| Åtta 0.3 sek blink, paus, etc.                          | Motor överhettad                                                                                                | Vänta tills motorn har kallnat                                                                                                                                                               |  |  |
| Nio 0.3 sek blink, paus, etc.                           | Dörren blockerad och impul- Ändra öppna-/stängimpuls<br>sen konstant                                            |                                                                                                                                                                                              |  |  |
| Tio 0,3 s blink, paus, etc.                             | Inställningar har utförts som<br>kräver ny inlärning eller öpp<br>ningsvinkel utom specifika<br>tion (80-110°)) | Utföra ny inlärning eller justera<br>öppningsvinkel för att ligga inom<br>specifikationerna.                                                                                                 |  |  |
| Tolv 0,3 sek blink, paus, etc.                          | Motorn är ansluten till fel ut<br>tag, alternativt har fel armsy<br>stem ställts in på AS-dipswit<br>ch.        | Koppla från nätspänningen och<br>korrigera däreftermotoranslutning<br>en och DIP för armsystem.                                                                                              |  |  |
| 13 0,3 s blink, paus, etc.                              | Slussfunktion fel                                                                                               | Kontrollera anslutningar för sluss<br>funktion                                                                                                                                               |  |  |

# 19 Service/Underhåll

I enlighetmed nationella bestämmelser och produktdokumentationen ska regelbundnainspektioner utföras av Entrematic Nordic-utbildad och behörig servicetekniker. Antalet servicetillfällen ska vara i enlighet med nationella bestämmelser och produktdokumentationen. Detta är särskilt viktigt när installationen handlar om brandklassad dörr eller dörr med nödöppningsfunktion.

Liksom all annan teknisk utrustning behöver en automatisk dörr underhåll och service. Det är viktigt att man känner till underhållets betydelse för en pålitlig och säker produkt.

Service och justering ser till att den automatiska dörren fungerar på ett säkert och korrekt sätt.

Använd medföljande "Serviceloggbok"tillsammans med dokumentet"Test för platsgodkännande och riskbedömning". Ha båda dokumenten tillgängliga för registrering av underhåll och service.

|                                                                        |                | Driftsekvenser/timme  |                          |                       |           |
|------------------------------------------------------------------------|----------------|-----------------------|--------------------------|-----------------------|-----------|
|                                                                        | Reservdelsnum  | <10                   | <100                     | >100                  | Besvärlig |
| Reservdel                                                              | mer            | Låg<br>trafike<br>rad | Mellan<br>trafike<br>rad | Hög<br>trafike<br>rad | Miljö     |
| Adaptersats                                                            | 330000484BK/SI | 24                    | 12                       | 6                     | 6         |
| PUSH-arm service kit                                                   | 330000485BK/SI | 24                    | 12                       | 6                     | 6         |
| PULL-slim servicesats                                                  | 330000486BK/SI | 24                    | 12                       | 6                     | 6         |
| Mikrobrytarsats                                                        | 330000488      | 24                    | 12                       | 6                     | 6         |
| Stopparmsats                                                           | 330000489      | 24                    | 12                       | 6                     | 6         |
| batteri *                                                              | 33738753       | 24                    | 24                       | 24                    | 24        |
| Transmissionsenhet PSW250<br>Brand PUSH                                | 330000487PUSH  | 60                    | 60                       | 60                    | 60        |
| Transmissionsenhet PSW250<br>Brand PULL                                | 330000487PULL  | 60                    | 60                       | 60                    | 60        |
| Transmissionsenhet PSW250<br>Brand (får ej användas iDE, GB<br>och SE) | 330000487F     | 60                    | 60                       | 60                    | 60        |
| Styrmodul CUS7 utan EXU<br>enheter                                     | 331011678      | 60                    | 60                       | 60                    | 60        |
| EXU-SI sats för säkerhet & im<br>pulser                                | 331003554      | 60                    | 60                       | 60                    | 60        |
| EXU-SA-säkerhetssats                                                   | 331003557      | 60                    | 60                       | 60                    | 60        |

Nedanstående tabell visar rekommenderade tidsintervaller i månader när reservdelar behöver bytas vid förebyggande underhåll.

* Koppla från nätspänningen för byte av batteri.

Om fel typ av batteri används finns risk att batteriet exploderar. Om batteriövervaknings DIP är i läge ON behövs en återställning av denna (efter batteribyte), se sida 17.

Entrematic Nordic AB, Lodjursgatan 10, SE-261 44 Landskrona, Sweden Tel: +46 10 47 48 300 www.entrematic.com • info.em@entrematic.com