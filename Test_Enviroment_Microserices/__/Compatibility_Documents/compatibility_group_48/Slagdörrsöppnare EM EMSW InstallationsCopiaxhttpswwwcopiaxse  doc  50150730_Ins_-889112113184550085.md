# Slagdörrsöppnare EM EMSW

![](_page_0_Picture_2.jpeg)

# Installations- och servicehandbok Originalinstruktioner

© Alla rättigheter i och till detta material tillhör Entrematic Group AB. Kopiering, skanning, bearbetning eller modifiering är inte tillåtet utan föregående skriftligt godkännande från Entrematic Group AB. Rätt till konstruktions- och måttändringar förbehålles.

Backtrack information: folder:Workspace Main, version:a289, Date:2016-01-27 time:06:49:12, state: Frozen

| 1 |                                                                                                                                                                     | Revision<br>5                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |    |  |  |  |  |  |  |  |
|---|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|--|--|--|--|--|--|--|
| 2 | Anvisningar för säker drift<br>6                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |    |  |  |  |  |  |  |  |
| 3 | Viktig information<br>3.1<br>Avsedd användning<br>3.2<br>Säkerhetsföreskrifter<br>3.3<br>Störning av mottagningen för viss elektronikutrustning<br>3.4<br>Miljökrav |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |    |  |  |  |  |  |  |  |
| 4 |                                                                                                                                                                     | Tekniska data                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 9  |  |  |  |  |  |  |  |
|   | 4.1                                                                                                                                                                 | Tillåten dörrvikt och dörrbredd  11                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |    |  |  |  |  |  |  |  |
| 5 |                                                                                                                                                                     | Så här fungerar EM EMSW  12                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |    |  |  |  |  |  |  |  |
|   | 5.1<br>5.2<br>5.3<br>5.4                                                                                                                                            | Öppning  12<br>Stängning  12<br>Funktioner på styrmodulen CSDB  12<br>5.3.1<br>Nyckelimpuls<br>5.3.2<br>Yttre impuls  12<br>5.3.3<br>Multispänningsinmatning (MVI)  13<br>5.3.4<br>Killingång  14<br>5.3.5<br>Öppningsgränsläge  14<br>5.3.6<br>Hemmagränsläge (tillval)  14<br>5.3.7<br>Låsutgång  14<br>5.3.8<br>Dubbeldörr  15<br>5.3.9<br>Push to Go  15<br>5.3.10<br>Felmeddelanden  15<br>5.3.11<br>Programväljare  15<br>Kompletteringsenhetens EXB funktioner  15<br>5.4.1<br>Inre impuls  15<br>5.4.2<br>Low pass filter ( sekvensförsening)  15<br>5.4.3<br>Närvaroimpuls  16<br>5.4.4<br>Närvarodetektering  16<br>5.4.5<br>Sensorövervakning  16<br>5.4.6<br>Överliggande närvarodetektering (OPD)  16<br>5.4.7<br>Mattsäkerhet  16<br>5.4.8<br>Tillslagspärr  16<br>5.4.9<br>Programväljare  17 | 12 |  |  |  |  |  |  |  |
| 6 | Modeller  18                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |    |  |  |  |  |  |  |  |
|   | 6.1<br>EM EMSW, standardkåpa (vägg- eller dörrbladsmontage)  18                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |    |  |  |  |  |  |  |  |
| 7 | 7.1<br>7.2<br>7.3<br>7.4<br>7.5<br>7.6<br>7.7                                                                                                                       | Identifiering av delar och tillbehör  19<br>Armsystem,PUSH  19<br>Armsystem,PUSH-335  19<br>Armsystem, PULL  20<br>Armsystem,PULL-220  20<br>Armsystem, ST-V / ST-H  20<br>7.5.1<br>Extratillbehör för ST-V / ST-H  20<br>Övriga tillbehör  21<br>Etiketter  23                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |    |  |  |  |  |  |  |  |
| 8 | Förinstallation  24                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |    |  |  |  |  |  |  |  |
|   | 8.1<br>8.2<br>8.3<br>8.4<br>8.5                                                                                                                                     | Allmänna tips/säkerhetsfrågor  24<br>Fästkrav  24<br>Erforderliga verktyg  25<br>Montering på dubbla in- och utgångsdörrar  25<br>Installationsexempel för brandklassade dörrar  26                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |    |  |  |  |  |  |  |  |
| 9 | Mekanisk installation  27                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |    |  |  |  |  |  |  |  |
|   | 9.1<br>9.2                                                                                                                                                          | Väggmonterad öppnare med armsystemet PUSH  27<br>Dörrbladsmonterad öppnare med armsystemetPUSH-335  30                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |    |  |  |  |  |  |  |  |

|    | 9.3          | 9.3.1<br>9.3.2<br>9.3.3 | Väggmonterad öppnare med armsystemet PULL, PULL-220 och ST  31<br>Byte av rotationsriktning  31<br>Installation av öppnare med armsystem PULL  32<br>Installation av dörröppnare med dragande armsystem typ ST  36 |    |
|----|--------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|
| 10 |              |                         | El-anslutning  42                                                                                                                                                                                                  |    |
|    | 10.1         |                         | Styrmoduler  42                                                                                                                                                                                                    |    |
|    |              | 10.1.1                  | CSDB  42                                                                                                                                                                                                           |    |
|    |              | 10.1.2                  | CSDA-S  42                                                                                                                                                                                                         |    |
|    |              | 10.1.3                  | EXB  42                                                                                                                                                                                                            |    |
|    | 10.2         | 10.1.4                  | CSDA-F  42<br>Anslutning av styrmodul CSDB – enkeldörrar  43                                                                                                                                                       |    |
|    | 10.3         |                         | Anslutning av styrmodulerna CSDB och CSDA-S – dubbeldörrar  44                                                                                                                                                     |    |
|    | 10.4         |                         | Anslutning av styrmodulerna CSDB/CSDB – dubbeldörrar  45                                                                                                                                                           |    |
|    | 10.5         |                         | Anslutning av tilläggsmodul EXB - extratillbehör  46                                                                                                                                                               |    |
|    | 10.6         |                         | Kabelingång för sensor  47                                                                                                                                                                                         |    |
| 11 |              |                         | Driftsättning  48                                                                                                                                                                                                  |    |
|    | 11.1         |                         | Stängningskraft  48                                                                                                                                                                                                |    |
|    | 11.2         |                         | Öppningskraft  49                                                                                                                                                                                                  |    |
|    | 11.3         |                         | Anslutning av impulsgivare och tillbehör  50                                                                                                                                                                       |    |
| 12 |              |                         | Kåpa  51                                                                                                                                                                                                           |    |
|    | 12.1         |                         | Montering och demontering av kåpa                                                                                                                                                                                  | 51 |
|    | 12.2         |                         | Mittbitskåpa  52                                                                                                                                                                                                   |    |
| 13 |              |                         | Skyltar  53                                                                                                                                                                                                        |    |
| 14 |              |                         | Montering på branddörrar  54                                                                                                                                                                                       |    |
|    | 14.1         |                         | Styrmodul, CSDA-F (extratillbehör)  54                                                                                                                                                                             |    |
|    |              | 14.1.1                  | Anslutning av styrmodul CSDA-F – enkeldörrar  55                                                                                                                                                                   |    |
|    |              | 14.1.2                  | Anslutning av styrmodul CSDA-F – dubbeldörrar  56                                                                                                                                                                  |    |
|    | 14.2         | 14.1.3                  | Funktionskontroll  56<br>Automatisering av branddörrar utan övergripande branddetekterings- och larmsystem.  57                                                                                                    |    |
|    |              | 14.2.1                  | Allmän anslutning  57                                                                                                                                                                                              |    |
|    | 14.3         |                         | Automatisering av branddörrar med övergripande branddetekterings- och larmsystem.  57                                                                                                                              |    |
|    |              | 14.3.1                  | Anslutning av CSDA-F till ett brandlarmsystem  58                                                                                                                                                                  |    |
| 15 |              |                         | Installation och inställningar - lågenergiöppnare  59                                                                                                                                                              |    |
|    | 15.1         |                         | Kompletterande säkerhetsanordningar för slagdörrar  59                                                                                                                                                             |    |
|    | 15.2         |                         | Öppnings- och stängningstider för slagdörrar.  60                                                                                                                                                                  |    |
|    |              | 15.2.1                  | Hur hittar jag korrekt öppnings- och stängningstid  60                                                                                                                                                             |    |
|    | 15.3         | 15.3.1                  | Diagram för dörrvikt  60<br>Aluminiumram med glas  61                                                                                                                                                              |    |
|    |              | 15.3.2                  | Stålram med glas  61                                                                                                                                                                                               |    |
|    |              | 15.3.3                  | Solitt trä  62                                                                                                                                                                                                     |    |
| 16 |              |                         | Installationsanvisningar för tillbehör  63                                                                                                                                                                         |    |
|    | 16.1         |                         | COOA - Koordinatorenhet  63                                                                                                                                                                                        |    |
|    |              | 16.1.1                  | EM EMSW 2 - Push  63                                                                                                                                                                                               |    |
|    |              | 16.1.2                  | EM EMSW 2 - Pull  64                                                                                                                                                                                               |    |
|    | 16.2<br>16.3 |                         | PAG  65<br>Dörrstopp  66                                                                                                                                                                                           |    |
|    |              |                         |                                                                                                                                                                                                                    |    |
| 17 |              |                         | Felsökning  67                                                                                                                                                                                                     |    |
| 18 |              |                         | Service/Underhåll  68                                                                                                                                                                                              |    |

### 1 Revision

### **Följande sidor har reviderats:**

| Sidan | Revision 9.0 → 10.0                                                              |  |  |  |  |  |
|-------|----------------------------------------------------------------------------------|--|--|--|--|--|
| 10    | Uppdaterad illustration med arm.                                                 |  |  |  |  |  |
| 11    | Nytt avsnitt tillagt.                                                            |  |  |  |  |  |
| 19    | Uppdaterat Art. nr., texter och illustration med arm.                            |  |  |  |  |  |
| 19    | Tillagt PUSH-335.                                                                |  |  |  |  |  |
| 20    | Uppdaterat Art. nr., texter och illustration med arm.                            |  |  |  |  |  |
| 21    | Uppdaterat Art. nr. och borttaget 600149.                                        |  |  |  |  |  |
| 24    | Texter uppdaterade.                                                              |  |  |  |  |  |
| 28    | Uppdaterad illustration med arm.                                                 |  |  |  |  |  |
| 29    | Uppdaterad illustration med arm.                                                 |  |  |  |  |  |
| 30    | Ändrat "PUSH-325" till "PUSH-335" och uppdaterat illustration med arm.           |  |  |  |  |  |
| 32    | Mått har uppdaterats.                                                            |  |  |  |  |  |
| 34    | Uppdaterad illustration med arm.                                                 |  |  |  |  |  |
| 35    | Uppdaterad illustration med arm.                                                 |  |  |  |  |  |
| 36    | Uppdaterad illustration med arm.                                                 |  |  |  |  |  |
| 38    | Uppdaterad illustration med arm.                                                 |  |  |  |  |  |
| 39    | Uppdaterad illustration med arm.                                                 |  |  |  |  |  |
| 40    | Uppdaterad illustration med arm.                                                 |  |  |  |  |  |
| 41    | Uppdaterad illustration med arm.                                                 |  |  |  |  |  |
| 38    | Tillagt "Obs!"                                                                   |  |  |  |  |  |
| 55    | Uppdaterad illustration                                                          |  |  |  |  |  |
| 56    | Uppdaterad illustration med arm.                                                 |  |  |  |  |  |
| 63    | Uppdaterad illustration med arm.                                                 |  |  |  |  |  |
| 64    | Uppdaterad illustration med arm.                                                 |  |  |  |  |  |
| 66    | Uppdaterad illustration med arm.                                                 |  |  |  |  |  |
| 67    | Tillagt fel för "1 blinkande LED"                                                |  |  |  |  |  |
| 68    | Uppdaterat Art. nr. för PUSH och PULL/PULL-220 servicesats och tillagt PUSH-335. |  |  |  |  |  |

### 2 Anvisningar för säker drift

![](_page_5_Picture_2.jpeg)

- Underlåtenhet att följa instruktionerna i denna manual kan leda till person- eller utrustningsskada.
- För att minska risken för personskador får dörröppnaren endast användas med slag- eller vikdörrar med ett eller två dörrblad.
- Använd inte utrustningen om den behöver repareras eller justeras.
- Koppla från strömmen i samband med rengörings- och underhållsarbete.
- Denna utrustning får inte användas av personer (inklusive barn under 8 år) med nedsatt fysisk eller mental förmåga eller som saknar tillräcklig erfarenhet och kunskap, såvida inte detta sker under överinseende av eller efter anvisningar från en person som ansvarar för deras säkerhet.

Detta förhindrar dock inte att dessa personer använder en dörr där dörröppnare har monterats.

- Rengöring och underhåll får inte utföras av barn utan vuxens övervakning.
- Låt inte barn klättra upp på eller leka med dörren eller de fasta reglagen/fjärrstyrningarna.
- Området, där arbete utförs, ska alltid spärras av för personer och strömmen ska kopplas bort för att undvika skador.
- Dörrarna kan manövreras automatiskt via sensorer eller manuellt via impulsgivare. Kan även användas manuellt som dörrstängare.

## 3 Viktig information

#### 3.1 Avsedd användning

Dörren är konstruerad för kontinuerligt bruk, hög säkerhet och maximal livslängd. Systemet är självjusterande, dvs. det anpassar sig i förhållande till påverkan från normala väderväxlingar och mindre friktionsförändringar orsakade av t.ex. damm och smuts.

För utrymning i nödsituationer öppnas dörrarna manuellt.

Denna handbok innehåller alla nödvändiga anvisningar för montage, underhåll och service av Swing Door Operator EM EMSW.

EM EMSW är en automatisk slagdörröppnaredörröppnaredörröppnare som utvecklats för att underlätta in-/utgång samt inom byggnad genom slagdörrar. EM EMSW är en elektrohydraulisk dörröppnare som är godkänd för branddörrstillämpning. Öppnaren ska monteras inomhus vilket gör att den passar praktiskt taget alla typer av yttre och inre slagdörrar. Denna brett använda öppnare finns på applikationer som sträcker sig från handikappentréer i privata hem till högtrafikerad detaljvaruhandel.

Dörröppnare i utrymningsvägar ska installeras så att dörren öppnas i utrymningsriktningen, såvida systemet inte har panikbrytare i utrymningsriktningen.

Dessa dörröppnare ska vara anslutna till ett brandlarmsystem, se sektion 11.1, 14.2 eller 14.3.

Motor, oljepump och hydraulenhet har samlats i en kompakt modul som sitter monterad längs med styrmodulen i kåpan. Öppnaren är kopplad till dörrbladet via olika typer av armsystem.

För användning, se i användarhandbok 1004131.

Spara dessa instruktioner för framtida bruk.

#### 3.2 Säkerhetsföreskrifter

Innan dörren tas i drift ska man genomföra en fullständig riskbedömning och acceptanstest.

För att undvika personskada, sakskada eller driftstörningar ska instruktionerna i denna handbok noggrant följas vid installation, inställning, reparation och underhåll m.m. Det krävs utbildning för att utföra detta arbete på ett säkert sätt. Endast Entrematic Group-utbildade tekniker får av säkerhetsskäl utföra detta arbete.

#### 3.3 Störning av mottagningen för viss elektronikutrustning

Utrustningen uppfyller det europeiska EMC-direktivet (på USA-marknaden: FCC Part 15), förutsatt att installationen utförts enligt Installations- och servicehandboken.

Utrustningen kan alstra samt använda radiovågor och vid bristfällig installation kan utrustningen orsaka störningar på radio-/tv-mottagning eller störningar för annan utrustning som använder radiovågor.

Om annan utrustning inte till fullo uppfyller skyddskraven kan störningar inträffa.

Det finns ingen garanti för att störningar inte kan uppkomma vid en enskild installation. Om denna utrustning orsakar störningar på radio- och TV-mottagningen, vilket kan avgöras genom att sätta på och stänga av utrustningen, uppmanas användaren att försöka eliminera störningen genom en eller flera av följande åtgärder:

- Rikta om mottagarantennen.
- Flytta mottagaren i förhållande till utrustningen.
- Flytta bort mottagaren från utrustningen.
- Anslut mottagaren till ett annat uttag så att utrustningen och mottagaren är på olika strömförgreningar.
- Kontrollera att skyddsjorden är ansluten.

Vid behov bör användaren rådfråga återförsäljaren eller en erfaren elektroniktekniker för andra lösningar.

#### 3.4 Miljökrav

Entrematic Group produkter är försedda med elektronik och eventuellt också med batterier som innehåller material som kan vara farliga för miljön. Koppla bort spänningen innan elektronik och batteri tas bort och se till att dessa hanteras i enlighet med lokala bestämmelser (hur och var), samma sak gäller för förpackningar.

## 4 Tekniska data

| Tillverkare:              | Entrematic Group AB                                                                                                                                                                                                                                                                                             |  |  |  |  |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|--|--|
| Adress:                   | Lodjursgatan 10, SE-261 44 Landskrona, Sweden                                                                                                                                                                                                                                                                   |  |  |  |  |
| Typ:                      | EM EMSW                                                                                                                                                                                                                                                                                                         |  |  |  |  |
| Nätspänning:              | 230 V AC ±10%, 50 Hz, nätsäkring max 10 A                                                                                                                                                                                                                                                                       |  |  |  |  |
|                           | Anm: Den nätspänning som installeras ska vara skyddad, förses med allpolig nät<br>strömbrytare med minst isoleringskapacitet enligt kategori III, ha minst 3 mm<br>mellan kontakterna, samt installationen ska utföras i enlighet med gällande bestäm<br>melser. Dessa komponenter medföljer inte vid leverans. |  |  |  |  |
| Effektförbrukning:        | Max 230 W (Max 460 W dubbeldörrar)                                                                                                                                                                                                                                                                              |  |  |  |  |
| Manöverspänning           | 24 V DC, 700 mA (stabiliserad)                                                                                                                                                                                                                                                                                  |  |  |  |  |
| Motorsäkring F1:          | 6,3 AT                                                                                                                                                                                                                                                                                                          |  |  |  |  |
| Manöversäkring F2:        | 250 mAT                                                                                                                                                                                                                                                                                                         |  |  |  |  |
| Dörrvikt:                 | Max 250 kg                                                                                                                                                                                                                                                                                                      |  |  |  |  |
| Dörrbredd:                | Max 1600 mm                                                                                                                                                                                                                                                                                                     |  |  |  |  |
| Max tröghet J:            | För PUSH = 80 kg m2                                                                                                                                                                                                                                                                                             |  |  |  |  |
|                           | För PULL = 28 kg m2                                                                                                                                                                                                                                                                                             |  |  |  |  |
|                           | Tröghet = Dörrvikt x (Dörrbredd)2 / 3                                                                                                                                                                                                                                                                           |  |  |  |  |
|                           | EM EMSW överensstämmer med dörrvikter/bredder i:<br>Kontrollerad dörrstängning, EN 1154 tabell I, storlek 3-6                                                                                                                                                                                                   |  |  |  |  |
|                           | Koordinatorenhet för falsade dörrar, EN 1158                                                                                                                                                                                                                                                                    |  |  |  |  |
|                           | Dörrstängare med öppningsautomatik (slagdörrsdrivning), DIN 18263-4 AU storlek<br>3-6                                                                                                                                                                                                                           |  |  |  |  |
| Säkerhetskrav:            | I enlighet med DIN 18650-1/2                                                                                                                                                                                                                                                                                    |  |  |  |  |
| Temperaturområde:         | -15 ℃ till +30 ℃                                                                                                                                                                                                                                                                                                |  |  |  |  |
| Relativ luftfuktighet:    | max 85%                                                                                                                                                                                                                                                                                                         |  |  |  |  |
| Mått:                     | Längd: EM EMSW (standardkåpa) 716 mm<br>EM EMSW-SPEC 750--1600 mm<br>EM EMSW-2 1435--3200 mm<br>Höjd: 110 mm<br>Djup: 110 mm                                                                                                                                                                                    |  |  |  |  |
| Skyddsklass:              | IP20                                                                                                                                                                                                                                                                                                            |  |  |  |  |
| Skyddsklass, styrmoduler: | IP54                                                                                                                                                                                                                                                                                                            |  |  |  |  |
| Godkännanden:             | Tredje part-godkännanden från etablerade certifieringsorganisationer som gäller<br>för säkerhet vid användning, se Försäkran om inbyggnad.                                                                                                                                                                      |  |  |  |  |

Säkerställ att dörröppnare med nedanstående tekniska data är avsedda för installationen.

#### Denna produkt ska installeras invändigt.

![](_page_9_Figure_2.jpeg)

| Klassificering enligt 18650-1                                |                             |                                            |                                                                      |          |          |          |          |          |
|--------------------------------------------------------------|-----------------------------|--------------------------------------------|----------------------------------------------------------------------|----------|----------|----------|----------|----------|
| Siffra 1<br>Siffra 2                                         |                             | Siffra 3                                   |                                                                      | Siffra 4 | Siffra 5 | Siffra 6 | Siffra 7 | Siffra 8 |
| 1                                                            | 3                           |                                            |                                                                      | 2        | 1,2,3    | 1,2,3,4  | 1,2,3,4  | 4        |
| Typ av drivning, siffra 1.                                   | 1                           | slagdörrsdrivning                          |                                                                      |          |          |          |          |          |
| Drivhållbarhet, siffra 2.                                    | 3                           | 1 000 000 testcykler, vid 4 000 cykler/dag |                                                                      |          |          |          |          |          |
| Typ av dörrblad, siffra 3.                                   | 1                           | slagdörr                                   |                                                                      |          |          |          |          |          |
| Lämplighet att användas<br>som brandskyddsdörr, siff<br>ra 4 | 2                           | lämplig att använda som branddörr          |                                                                      |          |          |          |          |          |
| Drivsäkerhetsanordning,                                      | 1                           | kraftbegränsning                           |                                                                      |          |          |          |          |          |
| siffra 5.                                                    | 2                           | anslutning för externa säkerhetssystem     |                                                                      |          |          |          |          |          |
|                                                              | 3                           | lågenergi                                  |                                                                      |          |          |          |          |          |
| Specialkrav för driv-                                        | 1                           | vid utrymningsvägar med panikbrytsystem    |                                                                      |          |          |          |          |          |
| ning/funktioner/beslag,<br>siffra 6.                         |                             | 2                                          | vid utrymningsvägar utan panikbrytsystem                             |          |          |          |          |          |
|                                                              |                             | 3                                          | för självstängande brandskyddsdörrar med panikbrytsystem             |          |          |          |          |          |
|                                                              |                             | 4                                          | för självstängande brandskyddsdörrar utan panikbrytsystem.           |          |          |          |          |          |
|                                                              | Säkerhet vid dörrblad eller | 1                                          | med tillräckligt dimensionerade säkerhetsavstånd                     |          |          |          |          |          |
| -bladen, siffra 7                                            |                             | 2                                          | med skydd som förhindrar att fingrar krossas, kapas av eller dras in |          |          |          |          |          |
|                                                              |                             | 3                                          | med inbyggd panikbrytenhet                                           |          |          |          |          |          |
|                                                              |                             | 4                                          | med närvarosensor                                                    |          |          |          |          |          |
| Omgivande temperatur,<br>siffra 8                            |                             | 4                                          | temperaturområde enligt tillverkarens uppgifter                      |          |          |          |          |          |

4.1 Tillåten dörrvikt och dörrbredd

![](_page_10_Figure_2.jpeg)

Dörrbredd (m)

### 5 Så här fungerar EM EMSW

EM EMSW är elektrohydraulisk. Den öppnar med en AC-motor som överför kraften till dörrbladet via en hydraulenhet och ett armsystem. Stängningskraften kommer från en spiralfjäder. Dörrens rörelser regleras av gränslägesbrytare och ventilskruvar.

#### 5.1 Öppning

När styrmodulen tar emot en öppningsimpuls startar motorn och hydraulenheten roterar drivaxeln så att armsystemet (dörren) i hög hastighet rör sig mot öppet läge. Före helt öppet läge bromsas dörren ned till låg hastighet. Dörren stoppar och motorns rotation upphör när dörren nått den förinställda öppningsvinkeln. Det öppna läget upprätthålls av en hydraulventil.

#### 5.2 Stängning

Den fjädermanövrerade stängningsrörelsen startar när öppethållandetiden gått ut. Innan det helt stängda läget nåtts bromsas dörren ned till låg hastighet och den låga hastigheten hålls tills dörren är helt stängd. Dörren hålls stängd av fjäderkraften. För att övervinna motståndet från låsblecket kan en "låskick" ställas in på önskad nivå.

- 5.3 Funktioner på styrmodulen CSDB
#### 5.3.1 Nyckelimpuls

Nyckelimpulsen öppnar dörren i programlägena OFF (AV), EXIT (UTGÅNG) och AUTO och ser till att dörren förblir öppen under nyckelöppethållandetiden.

Nyckelöppethållandetiden kan justeras mellan 0 och 30 sek.

#### 5.3.2 Yttre impuls

En yttre impuls öppnar dörren i programläge AUTO och håller dörren öppen under den yttre öppethållandetiden som kan justeras mellan 0 och 30 sek.

#### 5.3.3 Multispänningsinmatning (MVI)

En MVI-impuls godtar en spänningsfri kontakt eller 6-24 V AC/DC

Låsstatus (driftläge) kan ställas in via en funktionsväljare FS2 och sammanhänger med inmatning TB2:11 och 13.

| FS-2 = OFF (AV) (fabriksinställ-<br>ning)<br>FS-3 = OFF (AV) (fabriksinställ<br>ning) | TB2:11 och 13  | TB2:11 och 13 | TB2:11 och 13<br>6-24 V AC/DC* |  |  |
|---------------------------------------------------------------------------------------|----------------|---------------|--------------------------------|--|--|
| CSDB (Ingen PS)                                                                       |                | AUTO          |                                |  |  |
| EXB OFF (AV)                                                                          |                | FRÅN          |                                |  |  |
| EXB UTGÅNG                                                                            | FRÅN           | UTGÅNG        |                                |  |  |
| EXB AUTO                                                                              |                | AUTO          |                                |  |  |
| EXB ÖPPEN                                                                             |                | ÖPPEN         |                                |  |  |
| FS-2 = ON (PÅ)<br>FS-3 = OFF (AV) (fabriksinställ<br>ning)                            | TB2:11 och 13s | TB2:11 och 13 | TB2:11 och 13<br>6-24 V AC/DC* |  |  |
| CSDB (Ingen PS)                                                                       | AUTO           |               |                                |  |  |
| EXB OFF (AV)                                                                          | FRÅN           |               |                                |  |  |
| EXB UTGÅNG                                                                            | UTGÅNG         | FRÅN          |                                |  |  |
| EXB AUTO                                                                              | AUTO           |               |                                |  |  |
| EXB ÖPPEN                                                                             | ÖPPEN          |               |                                |  |  |
| FS-2 = OFF (AV) (fabriksinställ-<br>ning)<br>FS-3 = ON (PÅ)                           | TB2:11 och 13  | TB2:11 och 13 | TB2:11 och 13<br>6-24 V AC/DC* |  |  |
| CSDB (Ingen PS)                                                                       | FRÅN           | Öppen dörr    |                                |  |  |
| EXB OFF (AV)                                                                          | FRÅN           | Öppen dörr    |                                |  |  |
| EXB UTGÅNG                                                                            | UTGÅNG         | Öppen dörr    |                                |  |  |
| EXB AUTO                                                                              | AUTO           | Öppen dörr    |                                |  |  |
| EXB ÖPPEN                                                                             | ÖPPEN          | Öppen dörr    |                                |  |  |
| FS-2 = ON (PÅ)<br>FS-3 = ON (PÅ)                                                      | TB2:11 och 13  | TB2:11 och 13 | TB2:11 och 13<br>6-24 V AC/DC* |  |  |
| CSDB (Ingen PS)                                                                       | Öppen dörr     | FRÅN          |                                |  |  |
| EXB OFF (AV)                                                                          | Öppen dörr     | FRÅN          |                                |  |  |
| EXB UTGÅNG                                                                            | Öppen dörr     | UTGÅNG        |                                |  |  |
| EXB AUTO                                                                              | Öppen dörr     | AUTO          |                                |  |  |
| EXB ÖPPEN                                                                             | Öppen dörr     | ÖPPEN         |                                |  |  |

* +6-24 V DC **måste** anslutas till TB2:13 och MVI-bygel ska tas bort.

Programväljare **får inte** anslutas till TB2:13 om ingångsspänningen är 6-24 V. Anslut istället programväljaren till EXB.

MVI-impulsen öppnar låset och dörren öppnas. **eller** låser endast upp låset (ändrar driftläge för dörröppnaren). Kan väljas via funktionsväljaren FS-3.

MVI-öppethållandetiden kan justeras mellan 0 och 30 sek.

#### 5.3.4 Killingång

När kill aktiveras stängs dörren omedelbart om den inte redan är stängd. Tiderna för öppethållandeoch low pass filter återställs.

Nyckelimpulsen öppnar låset vid aktiverad kill om den inte är ansluten till TB2:5 med 0 V DC..

När kill avaktiveras kommer dörren att fungera enligt nuvarande inmatningsstatus.

Man kan ansluta flera kill-ingångar parallellt med andra CSDB-styrmoduler. Anslut kill på första dörröppnaren i enlighet med kopplingsschemat. Den andra, tredje, etc. dörröppnaren ska endast anslutas parallellt, från terminal 5 till 5 och 6 till 6.

Avstängningsfunktionen väljs via en funktionsväljare.

Som alternativ till den anslutning som visas under Anslutning av impulsgivare och tillbehör på sida 50 kan man ansluta en 24 V DC larmslinga till CSDB, anslut +24 V DC till terminal 6 och 0 V DC till terminal 5.

#### 5.3.5 Öppningsgränsläge

Gränslägesbrytare anger helt öppen dörr och kan ställas in på öppningsvinkel upp till 120º.

När gränslägesbrytaren aktiveras stannar motorn. Om gränslägesbrytaren inte aktiveras stannar motorn efter 14 sek.

Om gränslägesbrytaren avaktiveras vid öppen dörr kommer motor att starta igen för att återställa dörrens läge.

Lysdioden anger att gränslägesbrytaren är aktiverad.

Kontaktmärkvärde: 1A, 48 V DC, normalt öppen.

#### 5.3.6 Hemmagränsläge (tillval)

Om det inte har monterats något hemmagränsläge och gränslägesbrytaren har avaktiveras i öppet läge startar en timer och efter 6 sek kommer status att ändras från stängande till stängd dörr.

Om **tillbehör** hemmagränsläge har monterats kommer detta istället för timern att indikera stängd dörr.

"Fördröjd öppning" för låset (0-3 sek) ignoreras om hemmagränsläget inte är aktiverat.

"Slavfördröjning" för låset (0-5sek) ignoreras om masterns hemmagränsläge inte är aktiverat.

Närvaroimpuls ignoreras när hemmagränsläget indikerar stängd dörr inom 6 sekunder.

Lysdioden anger att hemmagränsläget är aktiverat.

#### 5.3.7 Låsutgång

Låsutgången är kortslutningssäker och kan försörja ett lås med 24 VDC, 375 mA

Låsutgången kan låsa med eller utan spänning. Den kan väljas via en funktionsväljare (Låst med/utan spänning).

Impulstiden för låset kan antingen vara 1,5 sek + (fördröjd öppning) eller till att dörren börjar stänga. Den kan väljas via en funktionsväljare (Låstid 1,5 s/till stängning).

"Fördröjd öppning" för lås - tiden innan motorn startas - kan ställas in från 0-3 sek.

Om ett hemmagränsläge installeras kommer låsets öppningstid först att starta när hemmagränsläget avaktiveras. Detta för att förhindra att dörren fastnar i låset om närvarodetekteringen aktiveras.

#### 5.3.8 Dubbeldörr

CSDB fungerar som master vid dubbeldörranvändning och ansluts till slavenheten CSDA-S.

Slavenheten har en standard öppningsfördröjning på 0,2 sek. Fördröjningen kan ökas till 0,5 sek för att förhindra att dörrbladen fastnar i varandra. Den kan väljas via en funktionsväljare (Slavfördröjning). Hemmagränsläge rekommenderas för att förhindra fördröjning vid stängning.

Om det krävs mer ström än vad en enstaka CSDB kan leverera, kan ytterligare en CSDB anslutas som slav. CSDB:n på slavenheten måste då konfigureras som slav. Den kan väljas via en funktionsväljare (Master/slav).

För att bara en dörr skall kunna öppnas skall impulserna anslutas parallellt till båda enheterna. Slavdörren måste ha CSDB+EXB samt lågpassfiltrets potentiometer justerad (inre impuls används).

- 5.3.9 Push to Go
En tryckning på dörren i stängt läge kommer att påbörja en automatisk öppningssekvens om programväljaren står i läge AUTO eller EXIT (UTGÅNG) och dörren förblir öppen under öppethållandetiden "Yttre ÖHT" (0-30 sek).

Ett hemmagränsläge på öppnaren behövs för att få Push to Go. Kan väljas via en funktionsväljare (Push to Go).

Lysdioden anger när hemmagränsläget är aktivt

- 5.3.10 Felmeddelanden
LED indikerar:

- Sensorfel: 1 blinkning om 0,2 sek och därefter 1 sek paus etc.
- Låsfel (för hög effektförbrukning eller kortslutning): 1 blinkning om 0,2 sek och därefter 0,2 sek paus etc.
- CSDB-fel: 3 eller 4 blinkningar i 0,2 s och med 0,2 s paus
- Ingen slav ansluten och slavövervakningsbygel saknas: 7 blinkningar i 0,2 s med 0,2 s paus
- Slav är ansluten men slavövervakningsbygel är ej borttagen: 7 blinkningar i 0,2 s med 0,2 s paus
- Fel på slav CSDA-S: 7 blinkningar i 0,2 s och med 0,2 s paus
- Gammal slav är ansluten och slavövervakningsbygel är borttagen: 7 blinkningar i 0,2 s med 0,2 s paus

#### 5.3.11 Programväljare

En programväljare PS-3B med tre lägen OFF-AUTO-OPEN (AV-AUTO-ÖPPEN) kan anslutas till CSDB.

**Anm:** Om MVI-utsignal används för 6-24 V, kan PS-3B inte användas.

Nyckelimpulsen fungerar fortfarande i programväljarläge OFF (AV)

Närvarosensorer är aktiva i alla programväljarlägen men inte om kill är aktiverad.

- 5.4 Kompletteringsenhetens EXB funktioner
- 5.4.1 Inre impuls

Inre impuls öppnar dörren i programlägena EXIT (UTGÅNG) och AUTO och ser till att dörren förblir öppen under öppethållandetiden.

Öppethållandetiden är inställbar från 0-30 sek.

- 5.4.2 Low pass filter ( sekvensförsening)
Denna funktion kräver en konstant inre impuls en viss tid för att starta dörrautomatiken. Tiden kan justeras från 0-5 sek.

Under stängning öppnar dörren omgående vid impuls.

#### 5.4.3 Närvaroimpuls

En närvaroimpuls hindrar en öppen dörr från att stängas och öppnar igen en stängande dörr och styrningen ser till att öppethållandetiden inte blir kortare än 1,5 sek.

Närvaroimpulsen ignoreras om hemmagränsläget är aktivt.

Närvaroimpulsen räknas inte som giltig impuls om dörrarna öppnas manuellt.

Närvaroimpulsen räknas som giltig om dörren öppnas med Push to Go.

Insignalen kan antingen vara "normalt öppen" eller "normalt sluten" vilket kan väljas via en funktionsväljare (Närvaroimpuls NO/NC).

#### 5.4.4 Närvarodetektering

Närvarodetektering hindrar en stängd dörr från att öppnas och stoppar en öppnande dörr.

Ett gränsläge används för att hindra sensorerna från att t.ex. känna av en vägg i närheten av den öppna dörren. Det kan förekomma två gränslägen som överlappar varandra - två för masterdörren och två för slavdörren.

Två lysdioder visar två status för gränslägena. En lysdiod för masterdörren och en för slavdörren. Lysdioderna tänds om någon av de två gränslägena aktiveras.

Närvarodetektering kan väljas via de två funktionsväljarna "Närvarodetektering master" och "närvarodetektering slav".

#### 5.4.5 Sensorövervakning

Test av **Närvarodetektering** utförs före öppning. Test av **Närvaroimpuls** utförs före stängning. Mastersensorerna testas först och slavsensorerna testas när svar har erhållits från mastersensorerna.

Om sensortest **inte** utförs med gott resultat kommer dörren övergå till **manuellt läge** och rapportera sensorfel. Sensortestet fortsätter i manuellt läge.

Om det inte finns någon slavöppnare när sensorövervakningen är igång bör "närvaroimpuls för slav" anslutas till "sensortest för slav".

Det går bara att övervaka sensorerna med utsignalen normalt stängd (NC).

Om sensorfelet försvinner vid manuellt läge återgår dörren automatiskt till autoläge igen.

Övervakning kan väljas via en funktionsväljare (Närvarosensorövervakning).

#### 5.4.6 Överliggande närvarodetektering (OPD)

En OPD-impuls hindrar en stängd dörr från att öppnas och en öppen dörr från att stängas.

En dörr i rörelse ignorerar OPD-signalen. OPD är aktiv 6 sek efter att dörren har börjat stänga. Om ett hemmagränsläge har monterats aktiveras OPD så snart dörren har stängts.

OPD kan väljas via en funktionsväljare (Sensor av typen OPD/matta).

#### 5.4.7 Mattsäkerhet

En mattsäkerhetsimpuls hindrar en stängd dörr från att öppnas och en öppen dörr från att stängas.

Inga impulser godtas under stängning om mattan aktiveras.

Mattsäkerheten kan väljas via en funktionsväljare (Sensor av typen OPD/matta).

- 5.4.8 Tillslagspärr
Tillslagspärren används för att ignorera OPD-sensorn vid öppning och stängning. Utsignalen är låg när dörren anses vara stängd, hög när dörren öppnar och är öppen och växlar när dörren stänger. Tillslagspärrsignalen är låg när dörren öppnas manuellt.

#### 5.4.9 Programväljare

Programväljare PS-4C kan anslutas till EXB.

Jämfört med PS-3B har PS-4C ett fjärde läge, EXIT (UTGÅNG), som gör att CSDB ignorerar den yttre impulsenheten.

Närvarosensorer är aktiva i alla programväljarlägen men inte om kill är aktiverad.

## 6 Modeller

För EM EMSW finns en huvudmodell med standardkåpa.

Öppnaren passar både vänster- och högerhängda dörrar och är inte beroende av gångjärnens placering. Öppnarna passar både tryckande och dragande armsystem.

#### 6.1 EM EMSW, standardkåpa (vägg- eller dörrbladsmontage)

EM EMSW är standardöppnaren. Bilden visar ett tryckande armsystem på en öppnare som är monterad på vägg och dörrblad.

#### **Väggmonterad**

![](_page_17_Figure_7.jpeg)

AAD174

### **Dörrbladsmonterad**

![](_page_17_Figure_10.jpeg)

### 7 Identifiering av delar och tillbehör

![](_page_18_Picture_2.jpeg)

| Nr. | Beskrivning     | Nr.  | Beskrivning                            |
|-----|-----------------|------|----------------------------------------|
| 1   | Monteringsplåt  | 10   | Tilläggsmodul, EXB (extratillbehör)    |
| 2   | Motor/pump      | 11   | Ändplatta                              |
| 3   | Magnetventil    | 12   | Programväljare, PS-3B (extratillbehör) |
| 4   | Hydraulenhet    | 13   | Kåpa                                   |
| 5   | Drivaxel        | 14   | Lagerhylsa                             |
| 6   | Fjäderhylsa     | 15   | Kabelhållare                           |
| 7   | Kabelingång     | CL1= | Mittlinje, drivaxel                    |
| 8   | Nätanslutning   | CL2= | Mittlinje, gångjärn                    |
| 9   | Styrmodul, CSDB |      |                                        |

#### 7.1 Armsystem,PUSH

![](_page_18_Picture_5.jpeg)

#### Art. nr.1014113BK/SI

Det används om dörröppnaren sitter monterad på väggen mittemot dörrens öppningsriktning och är godkända för brandtillämpningar.

- 7.2 Armsystem,PUSH-335
![](_page_18_Picture_9.jpeg)

#### Art. nr.1011706BK/SI

Används om öppnaren har installerats på dörrbladets gångjärnsida.

#### 7.3 Armsystem, PULL

![](_page_19_Picture_2.jpeg)

Används om öppnaren har installerats på väggen på samma sida som dörren öppnar.

7.4 Armsystem,PULL-220

![](_page_19_Picture_5.jpeg)

Art. nr.1014114BK/SI

Art. nr.1011707BK/SI

Används om öppnaren har installerats på väggen på samma sida som dörren öppnar och om dörren är 450-700 mm bred.

#### 7.5 Armsystem, ST-V / ST-H

![](_page_19_Figure_9.jpeg)

ST-VArt. nr.172312SI, 172313BK ST-HArt. nr.172314SI, 172315BK **Anm:** Dörrbeslag ingår ej.

Det används när dörröppnaren har installerats på väggen på samma sida som dörrens öppningsriktning och även då ett panikbrytbeslag krävs.

- 7.5.1 Extratillbehör för ST-V / ST-H
**Dörrbeslag standard**

Artikelnr: 172071

![](_page_19_Figure_15.jpeg)

#### **Panikbrytbeslag**

Artikelnr 172325 för pivåhängd dörr (utbrytning), **höger** när smyg A = 0-60 mm (0-2 3/8") eller **vänster** när A > 60-100 mm (>2 3/8"-3 15/16") för ST-H/ST-V

Artikelnr 172327 för pivåhängd dörr (utbrytning), **höger** när A > 60-100 mm (>2 3/8"-3 15/16") eller **vänster** när A = 0-60 mm (0-2 3/8")

![](_page_19_Picture_19.jpeg)

**Armförlängning** Artikelnr 172320 krävs när smyg A är >60-100 mm (>2 3/8"-3 15/16")

![](_page_19_Figure_21.jpeg)

| 4-läges programväljare            |                           | 2-läges programväljare                           |                         | 3-läges              | Tilläggsmodul   |
|-----------------------------------|---------------------------|--------------------------------------------------|-------------------------|----------------------|-----------------|
| (med EXB)                         | PSW-2                     | PSK-2                                            |                         | programväljare PS-3B | EXB             |
| PS-4C<br>Artikelnr:<br>655845     | 0<br>Artikelnr:<br>655843 | 0<br>1<br>1<br>ILL-01578<br>Artikelnr:<br>655844 |                         | Art. nr 1004117      | Art. nr 1004116 |
| Koordinatorenhet, COOA            |                           | Distans för PULL-Arm                             |                         | Mittbitskåpa kit     |                 |
| Art. nr 100091                    |                           | Art. nr.1014667BK/SI                             |                         | Art. nr 1008385      |                 |
|                                   |                           | 40 mm (1-37/64")<br>(2-23/64")<br>60 mm          |                         |                      |                 |
| Fingerskyddslister                |                           |                                                  |                         |                      |                 |
|                                   | Art. nr 833333            |                                                  | Art. nr 833334          |                      |                 |
| Kablage till slavenhet            |                           | PCB fästplatta                                   |                         | Dörrstopp            |                 |
| 1<br>2<br>3<br>4<br>SW            | Art. nr 656064            |                                                  | Art. nr 1003884         | Art. nr 100147       |                 |
| PUSH, armförlängare               |                           |                                                  |                         | Kabelingång          |                 |
| Smyg                              | Förlängning               |                                                  | Artikelnr:              | Art. No. 1007567     |                 |
| 0-110 mm<br>Upp till 4-3/8-tum    | Ingen (standardarm) -     |                                                  | -                       |                      |                 |
| 110-235 mm<br>4-3/8" till 9-1/4"  | 345 mm                    |                                                  | 173005BK/SI             |                      |                 |
| 235-360 mm<br>9-1/4" till 14-1/8" | 230 mm + skarvdel         | +                                                | 173004BK/SI +<br>173191 |                      |                 |
| 360-485 mm<br>14-1/8" till 19"    | 345 mm + skarvdel         | +                                                | 173005BK/SI +<br>173191 |                      |                 |
|                                   |                           |                                                  |                         |                      |                 |

### 7.6 Övriga tillbehör

![](_page_21_Figure_1.jpeg)

#### 7.7 Etiketter

**Etikettsats** - inklusive alla nedanstående

Art. nr 1005227

![](_page_22_Picture_4.jpeg)

![](_page_22_Picture_5.jpeg)

**Click!**

Art. nr 1001785

Panikbrytbeslag. DIN höger dörr

Panikbrytbeslag. DIN vänster dörr Art. nr 1001786

Aktiveringsenhet för rörelsehindrade Art. nr 1003963

![](_page_22_Picture_9.jpeg)

Öppnare avsedd för rörelsehindrade: Art. nr 1003964

![](_page_22_Picture_11.jpeg)

Uppsikt över barn Art. nr 1001695

### 8 Förinstallation

#### 8.1 Allmänna tips/säkerhetsfrågor

![](_page_23_Picture_3.jpeg)

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
	- för huvud ska avståndet vara större än 200 mm
	- för fötter ska avståndet vara större än 50 mm
	- och för hela kroppen ska avståndet vara större än 500 mm
- Riskpunkter bör skyddas upp till en höjd på 2,5 m från golvnivå.
- Dörröppnaren ska inte användas med dörrset som omfattar en gångdörr.

![](_page_23_Picture_19.jpeg)

Det är inte möjligt att ersätta EM en komponent i dörröppnaren med en komponent från ett annat varumärke.

#### 8.2 Fästkrav

| Grundmaterial  | Minimikrav för väggprofil*                                                 |
|----------------|----------------------------------------------------------------------------|
| Stål           | 5 mm **                                                                    |
| Aluminium      | 6 mm **                                                                    |
| Armerad betong | min. 50 mm från undersidan                                                 |
| Trä            | 50 mm                                                                      |
| Tegelvägg      | Expansionsbult, min. M6x85, UPAT PSEA B10/25 min. 50 mm från<br>undersidan |

* Entrematic Group-rekommenderade minimikrav.. Byggnormerna kan innehålla andra specifikationer. Se myndighetsbeslut.

- ** Tunnare väggar måste förstärkas med blindnitmuttrar.
#### 8.3 Erforderliga verktyg

- Torx T8, T10, T20 och T25
- Metrisk sexkantnyckel 3, 4 och 6 mm
- Flatskruvmejsel, liten
- Momentnyckel med metrisk insexnyckel 6 mm
- 8.4 Montering på dubbla in- och utgångsdörrar

Om öppnarna ska monteras på samma höjd med tryck- och dragarmsystem bestäms höjden av dragarmsystemet, PULL/ST. Tryckarmsystemet PUSH/ måste alltid ha en axelförlängning på minst 50 mm.

Exempel: Om PULL har 20 mm förlängning måste PUSH ha 70 mm förlängning.

Utför monteringen med hjälp av anvisningarna för det aktuella armsystemet.

- 8.5 Installationsexempel för brandklassade dörrar
Nedanstående illustration visar exempel på godkända förstärkningar vid montering av brandklassade dörröppnare.

**Anm:** Typgodkännande för brandklassade slagdörrar gäller endast tillsammans med armsystemet PUSH. Smyg max 480 mm och axelförlängning max 70 mm.

![](_page_25_Figure_4.jpeg)

| Nr. | Beskrivning                                                                                                                                                                    | Nr. | Beskrivning                                                                                                                                                                                                   |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1   | Stål min. 50x5, L=min. 100, centrerad för monteringshål<br>(4x)<br>Detta är kraven vid aluminiumprofiler.<br>Skruvar M6, FS-TT FZB, Taptite, L=40 (4x)                         | 6   | Träskruv M6, KST, L=45 (2x)                                                                                                                                                                                   |
| 2   | Stål min. 50x5, L=min. 150, centrerad på dörren vid armens 7<br>längd.<br>Detta är kraven vid aluminiumprofiler.<br>Skruvar M6, FS-TT FZB, Taptite, L=40 (2x).                 |     | Blindmutter M6, FTT/ST, L=15,9 (4x)<br>Skruvar M6, FS-TT FZB, Taptite, L=40 (4x).<br>Blindmuttrar får endast användas med stålprofiler med<br>en tjocklek på minst 1,5 mm.                                    |
| 3   | Stål min. 50x5, L=min. 100, centrerad för monteringshål<br>(4x)<br>Detta är kraven vid aluminiumprofiler.<br>Skruvar M6, FS-TT FZB, Taptite, L=50 (4x) Distansstycke<br>ø10/13 | 8   | Blindmutter M6, FTT/ST, L=15,9 (2x)<br>Skruvar M6, FS-TT FZB, Taptite, L=40 (2x).<br>Blindmuttrar får endast användas med stålprofiler                                                                        |
| 4   | Expansionsskruv (4x)<br>( för tegelvägg min. M6x85, UPAT PSEA B 10/25)                                                                                                         | 9   | Blindmutter M6, FTT/ST, L=15,9 (4x)<br>Skruvar M6, FS-TT FZB, Taptite, L=50 (4x)<br>Distansstycke ø10/13.<br>Blindmuttrar får endast användas med gipsregel av stål<br>med material tjocklek på minst 1,5 mm. |
| 5   | Träskruv M6, KST, L=min. 70 (4x)<br>Distansstycke ø10/13                                                                                                                       |     |                                                                                                                                                                                                               |

### 9 Mekanisk installation

Dessa instruktioner omfattar installation av EM EMSW med armsystem **PUSH,** som trycker upp dörren till öppet läge och **PULL / ST-V/H,** som drar upp dörren till öppet läge Se även "Quickstart" som medföljer varje öppnare.

#### 9.1 Väggmonterad öppnare med armsystemet PUSH

![](_page_26_Figure_4.jpeg)

![](_page_27_Figure_1.jpeg)

![](_page_27_Figure_2.jpeg)

![](_page_28_Figure_1.jpeg)

**Forts. "Väggmonterad öppnare med armsystemet PUSH"**

![](_page_28_Figure_3.jpeg)

![](_page_28_Figure_4.jpeg)

**8**

#### 9.2 Dörrbladsmonterad öppnare med armsystemetPUSH-335

![](_page_29_Figure_2.jpeg)

- CL1 Pivå- eller kantgångjärn
- CL2 Öppnarens drivaxel
- 1 Kabelingång vid gavelplåt
- Dörrmonteringssats, artikelnummer 100132, tillval 2
- Förstärkning krävs i dörrblad och vid fästhålen 3

- 9.3 Väggmonterad öppnare med armsystemet PULL, PULL-220 och ST
**Anm:** Om dörröppnaren **inte** beställs för **dragande** armssystem måste rotationsriktningen ändras.

- 9.3.1 Byte av rotationsriktning
![](_page_30_Figure_4.jpeg)

#### 9.3.2 Installation av öppnare med armsystem PULL

![](_page_31_Figure_2.jpeg)

![](_page_32_Figure_1.jpeg)

**Forts. "Installation av öppnare med armsystem PULL"**

![](_page_33_Figure_1.jpeg)

#### **Forts. "Installation av öppnare med armsystem PULL"**

I

![](_page_34_Figure_1.jpeg)

### **Forts. "Installation av öppnare med armsystem PULL"**

#### 9.3.3 Installation av dörröppnare med dragande armsystem typ ST

![](_page_35_Figure_2.jpeg)

![](_page_36_Figure_1.jpeg)

![](_page_37_Figure_1.jpeg)

**Forts. "Installation av öppnare med dragande armsystem typ ST"**

![](_page_38_Figure_1.jpeg)

![](_page_39_Picture_1.jpeg)

![](_page_40_Picture_1.jpeg)

### 10 El-anslutning

**Anm:** Under allt arbete med elektriska inkopplingar ska **Nätspänning** kopplas ifrån.

- Placera arbetsbrytaren så att man enkelt kommer åt den från dörröppnaren. Om man använder stickkontakt vid installationen av väggkontakten ska denna vara lätt åtkomlig från öppnaren.
- Om nätsladden är skadad måste den bytas ut av tillverkaren, dennes servicetekniker eller annan behörig person för att undvika fara.

#### 10.1 Styrmoduler

Öppnaren kan förses med olika styrmoduler som är anpassade till de önskade funktionerna.

#### 10.1.1 CSDB

Denna grundläggande styrmodul är försedd med anslutningar för automatiska och manuella aktiveringsenheter som t.ex. radarenheter, fotoceller, vanliga tryckknappar, nödknappar osv. Elektromekaniska låsbleck och slavstyrenhet CSDA-S för dubbeldörrar kan anslutas.

#### 10.1.2 CSDA-S

Denna slavstyrmodul används tillsammans med CSDB för dubbeldörrar enligt ovan.

#### 10.1.3 EXB

Denna tilläggsmodul sitter monterad ovanpå CSDB för att utöka CSDB:s funktioner med ingångar för närvaroimpuls, närvarodetektering, inre impuls, off (av) och (exit) utgång.

- 10.1.4 CSDA-F
Denna enhet tillsammans med CSDB används huvudsakligen för branddörrar. Elektromekaniskt låsbleck, 24 V AC kan anslutas.

#### 10.2 Anslutning av styrmodul CSDB – enkeldörrar

Anslut nätspänningskablarna till nätkopplingsplinten.

**Anm:** Tillbehör och aktiveringsenheter får **inte** anslutas innan hastighet och annat har ställts in.

**Anm:**Det är viktigt att hög- och lågspänningskablarna är ordentligt åtskilda och fixerade. Högspänningskablarna ska dras och fästas på ena sidan av drivenheten med bifogade kabelhållare och lågspänningskablarna ska

dras på motsatt sida med hjälp av samma typ av kabelhållare.

![](_page_42_Figure_6.jpeg)

### 10.3 Anslutning av styrmodulerna CSDB och CSDA-S – dubbeldörrar

När det gäller öppnare för dubbeldörrar måste båda öppnarna anslutas till nätspänningen. En sexledarkabel (medföljer) måste användas mellan TB1 på CSDB och TB6 på CSDA-S.

**Anm:**Det är viktigt att hög- och lågspänningskablarna är ordentligt åtskilda och fixerade. Högspänningskablarna ska dras och fästas på ena sidan av drivenheten med bifogade kabelhållare och lågspänningskablarna ska dras på andra sidan med samma typ av kabelhållare.

![](_page_43_Figure_4.jpeg)

4

#### 10.4 Anslutning av styrmodulerna CSDB/CSDB – dubbeldörrar

När det gäller öppnare för dubbeldörrar måste båda öppnarna anslutas till nätspänningen. En fyrledarkabel (medföljer) måste användas mellan TB1 på CSDB (master) och TB6 på CSDA-S (slav).

**Anm:**Det är viktigt att hög- och lågspänningskablarna är ordentligt åtskilda och fixerade. Högspänningskablarna ska dras och fästas på ena sidan av drivenheten med bifogade kabelhållare och lågspänningskablarna ska dras på andra sidan med samma typ av kabelhållare.

Dörrmonterade sensorer ska anslutas till egen master eller slav CSDB/EXB.

![](_page_44_Figure_5.jpeg)

- 10.5 Anslutning av tilläggsmodul EXB extratillbehör
Tilläggsmodulen EXB skall installeras ovanpå CSDB.

- a Anslut flatkabeln från EXB till CSDB.
- b Snäpp fast EXB på CSDB.

![](_page_45_Figure_5.jpeg)

**Anm:**Det är viktigt att hög- och lågspänningskablarna är ordentligt åtskilda och fixerade. Högspänningskablarna ska dras och fästas på ena sidan av drivenheten med bifogade kabelhållare och lågspänningskablarna ska dras på andra sidan med samma typ av kabelhållare.

#### 10.6 Kabelingång för sensor

![](_page_46_Picture_2.jpeg)

### 11 Driftsättning

Ställ in dörröppnaren så att pulskvoten är max 25%, vilket innebär motorns gångtid.

Ge en kort öppningsimpuls genom att bygla impulsingången och justera vid behov enligt nedan. Se även bild under Stängningskraft.

För beräkning av hastighet, se i "Installation av slagdörrar för persontrafik", dokument PRA-0006.

- a Ställ in öppethållandetiden med potentiometern på styrmodulen.
- b Inställning av **öppningshastighet**.
	- Anpassa höghastighetsöppningen HSO till den befintliga trafiksituationen. Vrid medurs för att sänka hastigheten.
	- Låghastighetsöppningen LSO behöver endast justeras om dörren är extremt tung. Vrid medurs för att sänka hastigheten.

**Anm:** Om det är svårt att få en mjuk och jämn inbromsning måste öppningsmomentet (pumptrycket) minskas.

- c Inställning av **stängningshastighet**.
	- Ställ låghastighetsstängningen LSC så lågt som trafiksituationen medger. Vrid medurs för att sänka hastigheten.
	- Om en högre stängningshastighet krävs, öppna höghastighetsstängningsventilen HSC (stängd vid leverans från fabrik).

**Anm:** Om det krävs en justering av stängningsmomentet i installationen, följ anvisningarna på sida 48.

- d Finjustering av **öppningsvinkel** med hjälp av **gränsläget**. Gränsläget förskjuts i ett spår i hydraulenheten och fixeras med en låsskruv. Genom att förflytta gränsläget i sidled ändras öppningsvinkeln.
**Anm:** För att underlätta inställningen kan gränsläget flyttas till hydraulenhetens undersida. Vilket som helst av spåren på den utgående axelns motorsida kan användas.

- e Om ett elektromekaniskt låsbleck installeras kan ytterligare **"låskick"** utlösas under stängningscykelns sista fem grader genom att skruven LK på hydraulenheten öppnas. Denna skruv är normalt stängd. Öppna skruven 90° och kontrollera funktionen.
**Anm:** Om skruven öppnas för mycket kan öppningen fördröjas.

- f Anslut impulsgivarna.
- g Kontrollera att installationen uppfyller gällande bestämmer och myndighetskrav.
- h Var extra uppmärksam på klämning mellan drivna delar och kringliggande fasta delar.

#### 11.1 Stängningskraft

Stängningskraften kan justeras för att överensstämma med myndighetskrav eller för att åtgärda över-/undertryck.

Stängningskraften (fjäderkraften) justeras på en insexskruv som sitter i fjäderrörets ände. Ändplattan måste demonteras. När skruven vrids medurs ökar kraften. Ett varv motsvarar en momentändring på ungefär 1 Nm (28 varv från min. till max.) . Dörren måste vara i öppet läge när **extremt lågt** stängningskraft ställs in.

**Anm:** I utrymningsvägar är max öppningskraft 150 N.

#### 11.2 Öppningskraft

Om stängningskraften (fjäderkraften) har ändrats, eller om dörren inte öppnas helt, måste öppningskraften (pumptrycket) ställas in enligt följande:

- a Det fabriksinställda momentet för PUSH är 70 Nm och för PULL 40 Nm vid en dörröppningsvinkel på 0-2°.
- b Mät öppningskraften med en fjädervåg och justera vid behov.

Kraften ställs in med en insexskruv som sitter på pumpen. Om skruven vrids medurs ökar öppningskraften/pumptrycket. Ett varv motsvarar en momentändring på ungefär 30 Nm.

![](_page_48_Figure_6.jpeg)

- 11.3 Anslutning av impulsgivare och tillbehör
Se manualen för sensorer rörande montering och justering. Skyddsutrustning ska överensstämma med EN 12978.

![](_page_49_Figure_3.jpeg)

3)Om PS-3B och "Tidkanal" ska "Tidkanal" anslutas i serie till TB2:13 4)Uppkoppling beror på nyckelimpulsöppettiden (Key HOT)

### 12 Kåpa

Kåpan och fästplåten är tillverkade av natureloxerat aluminium. Gavlarna är tillverkade av stål.

- 12.1 Montering och demontering av kåpa
Bryt av och tryck fast täckbrickan på monteringsplåten för utgångsaxeln. Tryck på den andra täckbrickan på det andra hålet.

Kåpan skjuts över flänsarna i ändplattorna och fixeras till fästplåtens undersida med en skruv för jordanslutning.

Efter korrekt installation och injustering ska den medföljande produktetiketten, med CE-märkning, fästas på den nedre högra delen av öppnarens kåpa (se bilden).

Fäst EM-logotypen på kåpan - se illustrationen.

Endast för SE: Montera SITAC-etiketten intill produktetiketten - se illustrationen.

![](_page_50_Picture_9.jpeg)

- 1 Täckbricka (2 st)
- 2 Ändplatta
- 3 Jord-/fästskruv

#### 12.2 Mittbitskåpa

![](_page_51_Figure_2.jpeg)

### 13 Skyltar

![](_page_52_Picture_2.jpeg)

Kontrollera att samtliga erfordrade skyltar sitter och är intakta. Skyltar är obligatoriskt enligt europeiska förordningar och motsvarande nationell lagstiftning utanför Europeiska unionen.

| A | Produktetikett: Obligatoriskt                                                                                                                                                            |
|---|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| B | Panikbrytbeslag: Obligatoriskt om enheten är godkänd som utrymningsväg.                                                                                                                  |
| C | Entrematic Group dörrdekal: Obligatoriskt, om tillämpligt, för att markera förekomsten av glas (appliceras på alla rörliga<br>glaspartier).                                              |
| D | Uppsikt över barn: Obligatoriskt, om tillämpligt (applicerad på båda sidor av dörren). Ska placeras vid entréer där riskanalysen<br>visar användning av barn, äldre och rörelsehindrade. |
| E | Impulsgivare utformad för rörelsehindrade:<br>Rekommenderas, om tillämpligt (applicerad på båda sidor av dörren).                                                                        |
| F | Aktiveringsenhet för rörelsehindrade: Rekommenderat, om tillämpligt.                                                                                                                     |
| G | SITAC-etikett: Obligatorisk i SE                                                                                                                                                         |

## 14 Montering på branddörrar

- EM EMSW är godkänd i enlighet med DIN 18263-4 för användning på branddörrar. Godkännandet omfattar överensstämmelse med EN1154 tabell 1, storlekar 3-6, för användning på branddörrar med kontrollerad dörrstängning. För storlek 3 är max dörrbladsvikt 60 kg och max dörrbladsbredd 950 mm. För storlek 6 är max dörrbladsvikt 120 kg och max dörrbladsbredd 1 400 mm.
- För falsade dubbeldörrar kan man använda koordineringsmodulen COOA, som är ett integrerat tillbehör i EM EMSW. COOA överensstämmer med EN1158, vilket garanterar korrekt stängningssekvens både efter manuell och automatisk öppning.
- EM EMSW kan anslutas till den övergripande brandcentralen och vid behov kan nödtryckknappar för dörrstängningen installeras lokalt. När signalen bryts stängs en öppnande eller öppen dörr omedelbart.
- Armsystemet PUSH måste användas

#### 14.1 Styrmodul, CSDA-F (extratillbehör)

För en mer avancerad lösning kan en särskild styrmodul, CSDA-F, installeras tillsammans med den grundläggande styrmodulen CSDB. Denna modul kan användas som central för erforderliga detektorer, manuella tryckknappar för dörrstängning, osv. Modulen ser också till att den automatiska dörröppningsfunktionen inte återställs efter larm från detektorerna eller efter manuell stängning. För att återställa den automatiska dörrfunktionen måste varje dörr få en separat återställningssignal.

CSDA-F kan anslutas på två olika sätt:

- För automatisering av branddörrar **utan** övergripande branddetekterings- och larmsystem.
- För automatisering av branddörrar **med** övergripande branddetekterings- och larmsystem.

Olika anslutningsexempel visas på sida 57 och sida 57.

#### **Kåpans längd (med CSDA-F)**

Öppnare för enkeldörrar L = 865-1600 mm Öppnare för dubbeldörrar L = 1560-3200 mm

#### 14.1.1 Anslutning av styrmodul CSDA-F – enkeldörrar

**Anm:**Det är viktigt att hög- och lågspänningskablarna är ordentligt åtskilda och fixerade. Högspänningskablarna ska dras och fästas på ena sidan av drivenheten med bifogade kabelhållare och lågspänningskablarna ska dras på andra sidan med samma typ av kabelhållare.

För att förhindra fel som orsakas av kortslutning (oavsiktlig el-anslutning) krävs att man lägger separata kablar till externa branddetektorer.

![](_page_54_Figure_4.jpeg)

1

#### 14.1.2 Anslutning av styrmodul CSDA-F – dubbeldörrar

![](_page_55_Figure_2.jpeg)

#### 14.1.3 Funktionskontroll

Kontrollera att systemen fungerar:

- Koppla på strömmen.
- Utför återställning med knappen "Återställning efter larm".
- Ge impuls på terminal 7-8 på CSDB.
- Bryt bygelterminal 10-12 på CSDA-F under öppningscykel. **Se till att öppningscykeln avbryts och att dörren stängs.**
- Ge en ny öppningsimpuls öppnaren ska förbli stängd.
- Anslut bygeln (eller larmlopp) mellan terminal 10-12.
- Utför återställning med knappen "Återställning efter larm".
- Ge en ny impuls och dörren ska genomföra en ny öppnings-/stängningscykel.

- 14.2 Automatisering av branddörrar utan övergripande branddetekterings- och larmsystem.
#### 14.2.1 Allmän anslutning

Vid denna typ av installation ansluts erforderliga branddetektorer direkt till CSDA-F.

![](_page_56_Figure_4.jpeg)

### 14.3 Automatisering av branddörrar med övergripande branddetekterings- och larmsystem.

Denna anslutning kan bara göras om brandlarmsystemet har en potentialfri brytande kontakt. För att branddörrarna skall stängas vid larm måste kontakten stå öppen. Erforderliga branddetektorer skall anslutas till larmsystemet. En tryckknapp för manuell stängning av dörrarna kan anslutas till respektive dörr. Det antal branddörrar som kan anslutas till brytkontakten i larmsystemet beror på kontaktens brytförmåga.

Kapaciteten för brandlarmets nätanslutning beräknas med siffrorna för använd CSDA-F x 0,05 A.

- 14.3.1 Anslutning av CSDA-F till ett brandlarmsystem
![](_page_57_Figure_3.jpeg)

### 15 Installation och inställningar - lågenergiöppnare

För att begränsa inneslutningskraften samt öppningskraften kan man påverka parametrar som pumptryck, öppnings- och stängningstid, fjäderspänning samt monteringen av PUSH-armsystemet. PULL-armsystemet har standardmontering.

Samtliga kraftberäkningar görs vid dörrhandtaget, ca 25 mm från dörrens ytterkant.

- a Installera öppnaren enligt handboken, men PUSH-armsystemets adapter bör flyttas 50 mm ut från gångjärnen (bild 1).
- b Ställ in fjäderns stängningskraft på det önskade värdet, dock max 67 N. Dörren måste vara öppen när inställningen görs. Kraften behöver endast mätas med öppen dörr där den är som högst.
- c Ställ in stängningstiden från 90-0º (bild 2) enbart på LSC-ventilen (stäng HSC-ventilen helt). Se diagram för öppnings- och stängningstider.

**Anm:** Lägg till 2 sekunder för kontroll av låset.

- d Kontrollera att den maximala öppningskraften inte överstiger 90 N. Man behöver inte mäta kraften med öppen dörr där den är som högst.
- e Justera pumpens öppningskraft till max 67 N i stängt läge.
- f Justera öppningsfunktionen (bild 3) på LSO-ventilen till 2 sekunder.
- g Ställ in öppningstiden från 0-80º (ca 200 mm från fullt öppet läge, se bild 3) på HSO-ventilen. Se diagram för öppnings- och stängningstider.
- h Justera öppethållandetiden på potentiometern till önskat värde, dock minst 5 sekunder.

![](_page_58_Figure_13.jpeg)

#### 15.1 Kompletterande säkerhetsanordningar för slagdörrar

Om det finns risk för att fastna med fingrarna kan man montera fingerskydd på gångjärnsidan av invändiga dörrar, artikelnr 833334 eller fingerskyddsrulle för utvändiga dörrar, artikelnr 833333.

- 15.2 Öppnings- och stängningstider för slagdörrar.
Ställ in öppnarens öppnings- och stängningstider minst enligt nedanstående diagram.

- 15.2.1 Hur hittar jag korrekt öppnings- och stängningstid
	- Mät dörrbredden.
	- Om man inte känner till dörrvikten ska man följa anvisningarna i "diagram för dörrvikt".
	- Gå in i nedanstående diagram för att hitta korrekt minimitid för öppning/stängning "t".

Exempel: Om dörren är 1,1 m bred och väger 50 kg blir minsta öppnings- och stängningstid ~3,5 sekunder.

![](_page_59_Figure_8.jpeg)

#### 15.3 Diagram för dörrvikt

- a Mät dörrens bredd (DW) samt höjd (DH) i meter för bara ett dörrblad.
- b Räkna ut ytan DWxDH
- c Välj diagram för din dörrtyp och glastjocklek. Ta reda på vikten.

*Exempel*: En aluminiumdörr med måtten DW = 1,5 m, DH = 2 m och glastjocklek 12 mm. Beräkna 1,5 x 2 = 3 m2. Titta i det första diagrammet för "aluminiumram med glas". Börja med ytan och följ linjen upp till 12 mm glas, gå sedan till vänster och där hittar du dörrvikten 95 kg.

**Anm:** Vikterna kan variera beroende på dörrens konstruktion (tabellen visar bara exempelvärden).

#### 15.3.1 Aluminiumram med glas

![](_page_60_Figure_2.jpeg)

#### 15.3.2 Stålram med glas

Dörrbladsvikt [kg]

![](_page_60_Figure_4.jpeg)

#### 15.3.3 Solitt trä

![](_page_61_Figure_2.jpeg)

![](_page_61_Figure_3.jpeg)

### 16 Installationsanvisningar för tillbehör

### 16.1 COOA - Koordinatorenhet

- 16.1.1 EM EMSW 2 Push
![](_page_62_Figure_4.jpeg)

- 2 Hävarmskonsol 5 Balansfjäder 8 Löpvals (överföringsstag)
- 3 Wirehjul 6 Plastslang

- 
### **Installation av koordineringsenhet**

Konsolerna 1 2 monteras mot pumpflänsen på "master"-dörröppnaren och kabelhjulet på 3 drivaxeln på "slav"-dörröppnaren.

**Anm:** Om "master" och "slav" dörrar växlas inbördes ska konsolerna monteras på pumpflänsens undersida.

- a Montera upphakningsfästet 1 på pumpflänsens stift och skruva fast hållaren ordentligt.
- b Montera hävarmshållaren 2 på upphakninghållarens krokar 1 , inklusive returfjäder 7 .
- c Dra wire genom plastslangen 6 och fäst den mot motorskruvarna med buntband 4 .
- d Montera wirehjulet 3 på "slav"-dörröppnaren med skruv och bricka. Hjulet ska monteras så som visas i fig. A eller B, beroende på vilken av dörrarna som är "slav". Alltid på dörröppnarens ovansida.
- e Stäng dörrarna och montera wire i hävarmshållaren 2 och kabelhjul 3 med fjädern 5 spänd till ungefär 10 mm. Öppna "master"-dörren och låt den kroka upp. Anpassa fjäderspänningen (lossa kabeln) så att "master"-dörren börjar stängas med normal hastighet.
- f Ställ in stängningstiden till ungefär 6 sekunder.
- g Montera löpvalsen (överföringsstag) 8 så som visas i illustrationen.
- h Ge öppningsimpuls och kontrollera funktionen.

#### 16.1.2 EM EMSW 2 - Pull

![](_page_63_Figure_2.jpeg)

#### **Installation av koordineringsenhet**

Konsolerna 1 2 monteras mot pumpflänsen på "master"-dörröppnaren och kabelhjulet på 3 drivaxeln på "slav"-dörröppnaren.

**Anm:** Om "master" och "slav" dörrar växlas inbördes ska konsolerna monteras på pumpflänsens undersida.

- a Montera upphakningsfästet 1 på pumpflänsens stift och skruva fast hållaren ordentligt.
- b Montera hävarmshållaren 2 på upphakninghållarens krokar 1 , inklusive returfjäder 7 .
- c Dra wire genom plastslangen 6 och fäst den mot motorskruvarna med buntband 4 .
- d Montera wirehjulet 3 på "slav"-dörröppnaren med skruv och bricka. Hjulet ska monteras så som visas i fig. A eller B, beroende på vilken av dörrarna som är "slav". Alltid på dörröppnarens ovansida.
- e Stäng dörrarna och montera kabeln i hävarmshållaren 2 och wirehjul 3 med fjädern 5 spänd till ungefär 10 mm. Öppna "master"-dörren och låt den kroka upp. Anpassa fjäderspänningen (lossa wire) så att "master"-dörren börjar stängas med normal hastighet.
- f Ställ in stängningstiden till ungefär 6 sekunder.
- g Ge öppningsimpuls och kontrollera funktionen.

#### 16.2 PAG

![](_page_64_Figure_2.jpeg)

**Justering av impulskänslighet**

![](_page_64_Figure_4.jpeg)

#### **Important notice**

För att undvika kroppsskada får öppningstiden från stängd till helt öppen inte vara mindre än 4 sekunder.

Om dörrstopp har monterats på dörröppnaren kan PAG monteras på motsatt sida.

#### 16.3 Dörrstopp

![](_page_65_Figure_2.jpeg)

- Montera dörrstopp på ovansidan av utsignalsspindeln för att förhindra att dörren överstiger 90º.
- Montera dörrstopp när dörren är i öppet läge, med en frigång på 2 mm (2/32") enligt nedan. Finjustera, vid behov, gränsläge och/eller armsystem.

![](_page_65_Picture_5.jpeg)

## 17 Felsökning

| Fel                                           | Möjliga orsaker                                                                | Åtgärder/förklaring                                                                                                                                                                           |
|-----------------------------------------------|--------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Dörren öppnar inte.                           | Programväljaren står i läge FRÅN                                               | Ändra inställningen                                                                                                                                                                           |
| - Motorn startar inte.                        | Ingen spänning till motorn                                                     | Kontrollera motorkabeln.                                                                                                                                                                      |
|                                               | Ingen nätspänning                                                              | Kontrollera strömförsörjningen.                                                                                                                                                               |
|                                               | Säkring har löst ut                                                            | Byt säkring.                                                                                                                                                                                  |
|                                               | Impulsgivare fungerar inte                                                     | Spänn fast impulsingångarna.                                                                                                                                                                  |
| - Motorn startar                              | Det elektriska låsblecket kärvar                                               | Justera låsblecket.                                                                                                                                                                           |
|                                               | Armsystemet har lossnat                                                        | Justera förspänningen och dra åt armsystemet.                                                                                                                                                 |
| Dörren öppnas inte till<br>erforderlig vinkel | Gränsläget för öppning sitter löst                                             | Kontrollera gränsläget.                                                                                                                                                                       |
| Dörren stänger inte.                          | Konstant impuls.                                                               | Koppla loss impulsgivaren eller byt styrmodulen.                                                                                                                                              |
| Dörren öppnas inte till-<br>räckligt snabbt   | För lågt pumptryck                                                             | Justera pumptrycket.                                                                                                                                                                          |
| Dörren öppnas med för<br>mycket fördröjning   | "Låskick"-ventilen har öppnats för mycket                                      | Justera ventilskruven.                                                                                                                                                                        |
| Ingen mjuk inbromsning                        | För högt pumptryck                                                             | Justera pumptrycket.                                                                                                                                                                          |
| sker                                          | Sträckan för låghastighetsöppning är för kort                                  | Öka öppningsvinkeln, eller<br>öka armsystemets förspänning.                                                                                                                                   |
| Hög ljudnivå                                  | Motorn vidrör fästplåten                                                       | Montera två extra skruvar på motorsidan så att fästplå<br>ten tvingas mot väggen.                                                                                                             |
| eller kan inte öppnas                         | Dörren förblir inte öppen Magnetventilen fungerar inte                         | Kontrollera genom att trycka på stiftet uppe på mag<br>netventilen.<br>Om dörren stannar, kontrollera resistansen (ska vara<br>150 ohm) i ledningen mellan magnetventilen och<br>styrmodulen. |
| 1 blinkande LED                               | Fel på dörrmonterad sensor                                                     | Kontrollera kabeln eller byt ut sensorn                                                                                                                                                       |
|                                               | För hög effektförbrukning eller kortslutning                                   | Kontrollera kabeln eller byt ut låset                                                                                                                                                         |
| 3 eller 4 blinkande LED:er CSDB-standard      |                                                                                | Byt ut styrmodulen                                                                                                                                                                            |
| 7 blinkande LED:er                            | Ingen slav ansluten och slavövervakningsbygel saknas                           | Sätt tillbaka bygeln                                                                                                                                                                          |
|                                               | Slav ansluten men slavövervakningsbygel är ej bortta- Ta bort bygeln<br>gen    |                                                                                                                                                                                               |
|                                               | CSDA-S-fel                                                                     | Byt ut styrmodulen                                                                                                                                                                            |
|                                               | Gammal CSDA-S ansluten och slavövervakning bortta- Sätt tillbaka bygeln<br>gen |                                                                                                                                                                                               |

## 18 Service/Underhåll

I enlighet med nationella bestämmelser och produktdokumentationen ska regelbundna inspektioner utföras av Entrematic Group-utbildad och behörig servicetekniker. Antalet servicetillfällen ska vara i enlighet med nationella bestämmelser och produktdokumentationen. Detta är särskilt viktigt när installationen handlar om brandklassad dörr eller dörr med nödöppningsfunktion.

Liksom all annan teknisk utrustning behöver en automatisk dörr underhåll och service. Det är viktigt att man känner till underhållets betydelse för en pålitlig och säker produkt.

Service och justering ser till att den automatiska dörren fungerar på ett säkert och korrekt sätt.

Använd medföljande "Serviceloggbok"tillsammans med dokumentet"Test för platsgodkännande och riskbedömning". Ha båda dokumenten tillgängliga för registrering av underhåll och service.

| Reservdel                           | Reservdelsnum<br>mer | Driftsekvenser/timme  |                      |                       |                    |
|-------------------------------------|----------------------|-----------------------|----------------------|-----------------------|--------------------|
|                                     |                      | <10                   | <100                 | >100                  | Besvärlig<br>Miljö |
|                                     |                      | Låg<br>trafike<br>rad | Mellan<br>trafikerad | Hög<br>trafike<br>rad |                    |
| Vibrationsdämpare och ol<br>jeplugg | 331003882            | 24                    | 12                   | 6                     | 6                  |
| PUSH/PUSH-335-servicesats           | 330000485BK/SI       | 24                    | 12                   | 6                     | 6                  |
| PULL/PULL-220 servicesats           | 330000486BK/SI       | 24                    | 12                   | 6                     | 6                  |
| ST-V/H servicesats                  | 331003887            | 24                    | 12                   | 6                     | 6                  |
| Gränsläge                           | 33655614             | 24                    | 12                   | 6                     | 6                  |
| Kondensator                         | 33655599             | 60                    | 60                   | 60                    | 60                 |
| CSDB-230styrmodul                   | 331004115            | 60                    | 60                   | 60                    | 60                 |
| CSDA-S                              | 600089               | 60                    | 60                   | 60                    | 60                 |
| CSDA-F                              | 600081               | 60                    | 60                   | 60                    | 60                 |

Nedanstående tabell visar rekommenderade tidsintervaller i månader när reservdelar behöver bytas vid förebyggande underhåll.

Entrematic Group AB, Lodjursgatan 10, SE-261 44 Landskrona, Sweden Tel: +46 10 47 48 300 • Fax: +46 418 201 15 www.entrematic.com • info.em@entrematic.com