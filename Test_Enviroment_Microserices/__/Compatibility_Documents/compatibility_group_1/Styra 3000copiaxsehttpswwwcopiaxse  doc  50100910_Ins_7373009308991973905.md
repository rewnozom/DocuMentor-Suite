![](_page_0_Picture_0.jpeg)

Aptus Elektronik AB • Ekonomivägen 3-5, 463 33 Askim • www.aptus.se telefon **växel:** 031 68 97 00 • **fax:** +46 31 68 97 99 **support:** support@aptus.se

# **Styra 3000**

**Revision 2**

### **INNEHÅLL 2**4

| INSTALLATIONSANVISNING FÖR STYRA 3000 | ÖVERSIKT                                                     | 3  |
|---------------------------------------|--------------------------------------------------------------|----|
| NCBKDHFKCHSDKHFCKJ                    | KONFIGURATIONSEXEMPEL                                        | 4  |
|                                       | MONTERING                                                    | 5  |
|                                       | Aptus Logga_Silver pantone 877<br>INKOPPLING & TEKNISKA DATA | 7  |
|                                       | BASKORT                                                      | 8  |
|                                       | STYRA GRUND10A                                               | 9  |
|                                       | Scala 1:1<br>FUNKTIONER                                      | 10 |
|                                       | UPPGRADERING & SERVICE                                       | 11 |
|                                       | KOMMUNIKATION                                                | 14 |
|                                       | INGÅNGAR                                                     | 16 |
|                                       | UTGÅNGAR                                                     | 17 |
|                                       | STYRA I/O 4400                                               | 18 |
|                                       | STYRA I/O 8800                                               | 19 |
|                                       | STYRA KOMKORT 4000                                           | 20 |
|                                       | STYRA PORTTELEFONKORT 4400                                   | 21 |
|                                       | STYRA PORTTELEFONKORT 4800                                   | 23 |
|                                       | KABELREDA                                                    | 24 |
|                                       | DRIFTSÄTTNING & PROGRAMMERING                                | 25 |
|                                       | APPENDIX: PROGRAMMERINGSBLANKETT                             | 27 |

### **ÖVERSIKT 3**4

#### **INLEDNING**

Denna anvisning redogör för hur centralenhet Styra 3000 skall installeras. Styra 3000 finns i ett grundutförande men kan dessutom bestyckas med tilläggskort. Anvisningen tar upp Styra 3000 samt tillgängliga tilläggskort.

#### **ÖVERSIKT**

#### **Grundutförande**

Centralenheten är avsedd att betjäna upp till 8 dörrar med passer-, porttelefoni- eller bokningsfunktioner. Dessutom finns funktioner för larm, trygghet , komfort och mätinsamling.

En Styra 3000 består av följande delar:

|           | Utförande för väggmontage. Material plast (polycarbonat).  |  |  |
|-----------|------------------------------------------------------------|--|--|
| Kapsling: |                                                            |  |  |
|           | Fästen för att dragavlasta och hålla ordning på kablaget   |  |  |
|           | är integrerat i kapslingen.                                |  |  |
| Baskort:  | Kretskort som utgör "hjärtat" i centralen. Baskortet       |  |  |
|           | innehåller gränssnitt för kommunikation (IP, RS485 och     |  |  |
|           | RS232), 1 transistorutgång, 2 ingångar för slutande/ bry   |  |  |
|           | tande kontakt samt summer och sabotagebrytare.             |  |  |
| Styra     | Kretskort för tillkoppling av centralens strömförsörjning. |  |  |
| Grund10A: | Innehåller avsäkringsfunktionalitet, en skyddad A485-      |  |  |

port, två portar för tilläggskort samt möjlighet att mata annan utrustning med 12 och 24V.

#### **Tillbehör**

Styra 3000 erbjuder dessutom möjlighet för montage av interna tillbehör. Alla interna tillbehör har ett namn som börjar på Styra. **Aptus Logga_Silver pantone 877**

|           | Styra                 | Kretskort med 4st. avsäkrade och skyddade      |
|-----------|-----------------------|------------------------------------------------|
|           | Komkort 4000:         | A485-bussar för enklare och säkrare funk       |
|           |                       | tion.                                          |
| Scala 1:1 |                       | Upp till två Styra Komkort 4000 per central.   |
|           | Styra                 | Kretskortet innehåller grundfunktionerna för   |
|           | Porttelefonkort 4400: | porttelefoni för upp till fyra dörrar. Max ett |
|           |                       | Styra Porttelefonkort 4400 per central.        |
|           | Styra                 | Kretskortet erbjuder porttelefoni för dörr 5   |
|           | Porttelefonkort 4800: | - dörr 8 om det monteras i central som har     |
|           |                       | Styra Porttelefonkort 4400. Max ett kort per   |
|           |                       | central.                                       |
|           | Styra                 | Kretskort med 8 dubbelbalanserade ingångar     |
|           | I/O 8800:             | och 8 reläutgångar. Upp till två per central.  |
|           | Styra                 | Kretskort med 4 dubbelbalanserade ingångar     |
|           | I/O 4400:             | och 4 reläutgångar. Upp till två per central.  |
|           |                       |                                                |

![](_page_2_Figure_14.jpeg)

![](_page_3_Picture_1.jpeg)

### **4**4

### **KONFIGURATIONSEXEMPEL**

Styra 3000 kan med hjälp av tilläggskort och dörrenheter konfigureras på olika sätt. Här följer ett par exempel.

#### **EN DÖRRMILJÖ**

![](_page_3_Figure_6.jpeg)

Anslut 24 V till G-TB1. Dörrenhet, Koppla, ansluts till G-TB4 som med fördel kan vara ställd att leverera ut 24 V.

Anslut läsare, lås, öppnaknapp o.s.v. till Koppla. Observera att Koppla levererar 12 V även när den matas med 24 V. Montera eventuella tillbehör.

#### **TILLBEHÖRSKORT I CENTRALEN**

![](_page_3_Figure_10.jpeg)

Anslut 24 V till G-TB1. Montera Styra Komkort 4000 på Expansionsplats 1 och Styra I/O 8800 på Expansionsplats 2. Anslut läsare för två olika dörrar till port 1 respektive port 2 på Styra Komkort 4000. **Obs!** Portarna skall stå i 12V-läge eftersom detta gäller för de flesta läsare.

Anslut lås och öppnaknappar till Styra I/O 8800.

![](_page_3_Figure_13.jpeg)

#### **TILLBEHÖRSKORT KOMBINERAT MED DÖRRENHET**

Anslut 24 V till G-TB1. Montera Styra Komkort 4000 på Expansionsplats 1 och Styra I/O 8800 på Expansionsplats 2. Anslut läsare till port 1 och 2 på Styra Komkort 4000 och se till att dessa är ställda i 12V-läge. Anslut lås och öppnaknappar för dessa läsare till Styra I/O 8800.

Anslut Koppla till port 3 på Styra Komkort 4000. Ställ in port 3 för 24V matning så att dörrenhetens reläutgångar kan leverera 24V. Anslut lås och öppnaknapp till dörrenhetens ut och ingångar. Anslut en läsare till dörrenhetens A485-utgång. Denna matas med 12V fast dörrenheten matas med 24V.

### **MONTERING 5**4

![](_page_4_Figure_4.jpeg)

#### **MONTERING** Ta först bort frontkåpan från centralen. Låsmekanismen vrids med

vanlig mejsel. Fäll upp locket tills det åtminstone står rakt upp, 1, tryck lockets gångjärnssida mot centralen, 2, tills gångjärnsaxeln åker ur gångjärnshaken, 3. För ut locket och lägg det åt sidan.

Skruva upp centralen, antingen på vägg eller i ställ alternativt apparatskåp. Centralens normalläge är att monteras så kabelintag hamnar i underkant, men även andra monteringspositioner är möjliga. Tänk på att lämna fritt utrymme ovanför centralen så att det går att lossa respektive sätta tillbaka locket. Vid montering under ett tak krävs det 10cm mellan centrals överkant och tak. Om centralen monteras under en annan central räcker det med 5cm för att kunna manövrera locket, men troligtvis kräver kablaget att centralerna sätts med lite större mellanrum. **Scala 1:1 Kontaktperson Marianne Hauger**

**031 68 97 11**

När centralen är på plats är det lämpligt att montera eventuella tillbehör såsom kort till Kortplats 1 & Kortplats 2 och även skruv för sabotagebrytare.

Efter inkoppling och driftsättning skall fronkåpan återmonteras. För då in lockets gångjärnshake, 3, tryck locket i motsatt riktning så att bottendelens axeltapp åker in i gångjärnshaken, 2, locket kan nu stängas enligt 1, avsluta med att vrida till låsmekanismen.

Observera att det vid service av centralen inte är nödvändigt att haka av locket. Se nästa sida.

![](_page_4_Figure_12.jpeg)

56

![](_page_4_Figure_14.jpeg)

![](_page_5_Picture_1.jpeg)

### **6**4

**Montera skruv för sabotagebrytare**

![](_page_5_Picture_4.jpeg)

2. Visar gångjärnen i normalläge.

- 3. Skjut locket ca 5 mm åt vänster och släpp ner tills locket står av sig självt.
- 4. Visar gångjärnets låsningsläge.

Iaktta försiktighet när locket är uppställt så att du inte av misstag skadar gångjärnen. **Aptus Logga_Silver pantone 877**

För att åter stänga locket igen gör följande:

- 1. Lyft locket en aning och skjut sedan 5 mm åt höger. **Scala 1:1 Kontaktperson Marianne Hauger**
**031 68 97 11**

- 2. Fäll ner locket och stäng låset.
För att sabotagelarmet i Styra 3000 skall fungera måste den bipackade skruven dras in i sitt fäste i locket. Skruven skall justeras tills sabotagebrytaren fungerar men inte trycka onödigt hårt. Försök att trimma så att skruven nuddar sabotagebrytaren samtidigt som locket går om lott med underdelen. Lyssna sedan efter brytarens klick när locket stängs ytterligare. En bra utgångspunkt fås om skruven först dras i botten och sedan backas två varv. Använd stjärnmejsel PZ. **Obs!** Om sabotagebrytarfunktionen inte används på eran anläggning behöver inte skruven monteras.

#### **Lockets uppställningsfunktion**

Vid service behöver locket inte demonteras. Det går istället att låsa i uppfällt läge.

1. Fäll upp locket till ca 110o.

![](_page_5_Figure_16.jpeg)

### **7**4

### **INKOPPLING & TEKNISKA DATA**

#### **INKOPPLING**

Börja med att dra in det kablage som skall anslutas till centralen genom kabelgenomföringarna. Det finns 12 genomföringar och en god strategi är att vika fyra genomföringar i vänsterkant för centralens kommunikation, strömförsörjning samt övrigt som eventuellt skall anslutas på baskort respektive grundkort.

De fyra nästkommande genomföringarna viks för kablage till expansionsplats 1 och de sista fyra för kablage till expansionsplats 2.

#### **Förslag för anläggningsdokumentation**

Eftersom Styra 3000 består av flera olika kort som vart och ett har har anslutningspunkter som heter t.ex. TB1, TB2 o.s.v. så är det viktigt att namnge dessa så att de blir unika i anläggningens dokumentation. Detta uppnås genom att följande prefix sätts framför kortens egna plintbeteckningar:

| Baskort                      | B   |
|------------------------------|-----|
| Styra Grund10A (Grundkort) G |     |
| Expansionsplats 1 (EXP1)     | E1- |
| Expansionsplats 2 (EXP2)     | E2- |

#### **Strömförsörjning**

Dimensionera strömförsörjningsaggregatet och kabel till centralen efter centralens totala strömförbrukning inklusive alla delar som matas via centralen. Strömförsörjningen ansluts till Styra Grund10A, se sida 9. Tänk också på att dimensionera eventuella batterier efter hur lång tid som centralen måste fungera vid ett strömavbrott.

#### **Kommunikation till Multiaccess**

Den central som skall fungera som master skall ha kommunikation upp till Multiaccess-systemet. Kommunikationen kan antingen gå via nätverk eller direkt via RS232, t.ex. vid modemkommunikation. Kommunikationen ansluts till baskortet, se sida 8.

Om du ansluter till ett nätverk, använd en TP-kabel mellan central och nätverksuttag. För att få in TP-kabel med sin RJ45-kontakt i centralens kapsling behöver gummigenomföringen lossas. Slitsa sedan upp gummigenomföringen, trä på den på kabeln samt fäst den i kapslingen.

Se också kapitlet om kommunikation på sidan 14.

#### **Kommunikation mellan centraler**

Mellan centralerna sker kommunikation antingen över nätverket eller via RS485, s.k. Slav485.

Om alla centraler, master och slavar kör nätverkskommunikation så räcker det givetvis att ansluta varje enskild central till nätverket via TP-kabel. Om däremot vissa eller alla slavar kommuniceras med Slav485 så skall det dras en RS485-buss mellan master och de slavar som skall kommunicera via RS485-kommunikation. Obs! Anslut inte både nätverkskommunikation och Slav485 till en slav. Se kommunikation sida 14 och Baskort sida 8.

#### **Kommunikation med centralens enheter**

Enheter som skall styras av centralen ansluts till den s.k. Aptus485 bussen. Anslutning görs då antingen till G-TB4 på grundkortet eller på något av kommunikationskorten om sådana finns monterade i centralen. Se avsnittet kommunikation, sida 14 och Styra Grund10A sida 9 eller sidan för aktuellt kommunikationskort. **Aptus Logga_Silver pantone 877**

#### **Ingångar & Utgångar**

Ingångar och utgångar är centrala för att få funktion i centralen. I grundutförande finns endast två ingångar och en utgång på centralen, på baskortet. Bygg därför på med ytterligare in och utgångar antingen genom att montera I/O-kort i centralen eller att montera dörrenheter ute vid dörrarna. Ingångar, se sida 16, Utgångar, se sida 17 samt avsnittet för aktuellt I/O-kort. Dörrenhet, Koppla 2100 och Koppla 4300 beskrivs i separata installationsanvisningar. **Scala 1:1 Kontaktperson Marianne Hauger**

#### **TEKNISKA DATA**

| Strömförsörjning: | 12 / 24 V DC +15% / -10%                        | [G-TB1] |
|-------------------|-------------------------------------------------|---------|
|                   | Rippel max 1%                                   |         |
|                   | Strömförbrukning: Max 95mA, Min 65mA vid 24V.   |         |
|                   | Max 120mA, Min 65mA vid 12V.                    |         |
|                   | Innefattar Baskort och Grundkort.               |         |
|                   | Maxvärdet inkluderar följande:                  |         |
|                   | Ethernet 19 / 10 mA (vid 12 / 24 V DC)          |         |
|                   | Summer 31 / 22 mA (vid 12 / 24 V DC)            |         |
|                   | Om inte ethernet eller summer används kan       |         |
|                   | maxvärdet reduceras med motsvarande.            |         |
| Utgångar:         | 1 transistorutgång 28V 1A                       | [B-TB1] |
| Ingångar:         | 2 för potentialfri slutning/brytning            | [B-TB2] |
| Kommunikation:    | IP:<br>Nätverkskommunikation mellan centraler   |         |
|                   | och till Multiaccess                            | [B-IP1] |
|                   | RS232: till Multiaccess (endast master) [B-TB3] |         |
|                   | RS485: mellan centraler (Slav485)               | [B-TB5] |
|                   | RS485: till centralens underenheter             |         |
|                   | (Aptus485)                                      | [G-TB4] |
| Miljökrav:        | 0 till +40 grader Celsius,                      |         |
|                   | 10 till 90 % relativ luftfuktighet              |         |
| Mått:             | 270x379x56 mm                                   |         |
| Vikt:             | 1,6 Kg                                          |         |

### **BASKORT 8**4

#### **LYSDIODER**

| Led 1:  | Fast grönt            | Normaldrift                    |
|---------|-----------------------|--------------------------------|
|         | Dubbelblinkande grönt | (Batteridrift)                 |
|         | Enkelblinkande grönt  | Ej programmerad                |
|         | Släckt                | Centralen ej i drift           |
| Led 11: | Gul                   | IP1 ansluten med 100Mb         |
|         | Släckt                | IP1 ansluten med 10Mb          |
| Led 12: | Grön                  | IP1 har länk                   |
|         | Blinkande grön        | IP1 har länk och data överförs |
| Led 6:  | Blinkande röd         | Data sänds på A485 (Aptus485)  |
| Led 7:  | Blinkande röd         | Data sänds på S485 (Slav485)   |
| Led 8:  | Grön                  | Transistorutgång på TB1 aktiv  |
| Led 9:  | Blinkande gul         | Data tas emot på A485          |
| Led 10: | Blinkande gul         | Data tas emot på S485          |

#### **SWITCHAR**

| S1.1:<br>Mem                   | On  | Nollställning av minne                   |
|--------------------------------|-----|------------------------------------------|
|                                | Off | Normal                                   |
| S1.2:<br>Modem                 | On  | Modem                                    |
| Aptus Logga_Silver pantone 877 | Off | Ej modem                                 |
| S2: sabotagebrytare            |     | Detekterar om locket öppnas. Skruv       |
|                                |     | fäst i locket trycker ner brytaren       |
|                                |     | närså att den är sluten när locket är    |
|                                |     | stängt. Programmeras som ingång i        |
| Scala 1:1                      |     | Multiaccess.                             |
| S3:                            |     | On,On A485 bussen terminerad.            |
| S4:                            |     | On,On S485 bussen terminerad.            |
| S5: Minnesbackup               | On  | Kretskortsbatteri BT1 inkopplat.         |
|                                | Off | Kretskortsbatteri BT1 urkopplat.         |
|                                |     | Obs! Om ni nollställer minnet med        |
|                                |     | denna så nollställs även nätverkspara    |
|                                |     | metrar.                                  |
|                                |     | Kontrollera att denna är On vi driftsätt |
|                                |     | ning.                                    |

#### **SUMMER**

En summer finns inbyggd på baskortet. Summerns funktion programmeras via Multiaccess. Multiaccess betraktar summern som en utgång. Du kan t.ex. låta summern ljuda om någon lyfter på locket till centralen.

![](_page_7_Figure_9.jpeg)

| ANSLUTNINGAR |                                                                              |  |  |  |
|--------------|------------------------------------------------------------------------------|--|--|--|
| IP1:         | RJ45-jack för anslutning av nätverkskommunika<br>tion.                       |  |  |  |
| TB1:         | Utgång (transistor). Aktiv utgång ger TB1:1,2 =<br>0,12V. (Inaktiv: 12V,12V) |  |  |  |
| TB2:         | Ingångar, 2st, för potentialfri slutning / brytning.                         |  |  |  |
| TB3:         | RS232 för kommunikation med Multiaccess,<br>modem eller serieport.           |  |  |  |
| TB4:         | Används ej. Anslut Aptus485-buss till grundkort<br>eller kommunikationskort. |  |  |  |
| TB5:         | S485, kommunikation mellan master och slav.                                  |  |  |  |
| TB6:         | Används ej! Anslut spänningsmatning till grund<br>kortet.                    |  |  |  |
|              | Kom ihåg att lägga på "B-" före plintbeteckningarna                          |  |  |  |

ovan vid anläggningsdokumentation.

### **STYRA GRUND10A 9**4

Grundkort till vilket Styra-centralens spänningsmatning kopplas. Kortet har spänningsövervaknings och avsäkringsfunktioner. Kortet omvandlar inkommande 24V till 12V (nom 13,5V). All övrig utrustning i centralen får sin spänning från detta kort. Grundkortet erbjuder också en avsäkrad Aptus485-port, två positioner för tilläggskort samt möjlighet att koppla in avsäkrad spänningsmatning 12V och 24V till extern utrustning.

#### **LYSDIODER**

| D5:  | Fast grön     | Spänning 12-24V, godkänd.             |
|------|---------------|---------------------------------------|
|      | Släckt        | Spänning 12-24V, fel                  |
| D6:  | Fast grön     | Spänning 12V, godkänd.                |
|      | Släckt        | Spänning 12V, fel                     |
| D11: | Blinkande röd | Spänning A485, srömgräns överskridits |
|      | Släckt        | Spänning A485, ström normal           |

![](_page_8_Figure_6.jpeg)

JP1: Höger: 12V: TB4 matar ut 12 V. Standardinställning. Vänster: 24V: TB4 matar ut 24 V. **Obs! Ställ aldrig om en Aptus485-buss till 24 V om du inte kontrollerat att utrustningen på bussen fak tiskt får matas med 24 V.**

#### **ANSLUTNINGAR**

|           | TB1: | 12 V DC - 24 V DC +15% / -10%                                                             |  |
|-----------|------|-------------------------------------------------------------------------------------------|--|
|           |      | Inkommande matningsspänning. Rippel max 1%.                                               |  |
|           | TB2: | 12 V DC - 24 V DC                                                                         |  |
|           |      | Aptus Logga_Silver pantone 877<br>Spänningsmatning till extern utrustning. Spänningsnivån |  |
|           |      | motsvarar den som matas in på TB1.                                                        |  |
|           |      | Avsäkrad till 2,5A.                                                                       |  |
|           | TB3: | 12 V DC                                                                                   |  |
|           |      | Spänningsmatning till extern utrustning. Spänningsnivån                                   |  |
| Scala 1:1 |      | 12 V skapas på Grundkortet utifrån inmatad spänning.                                      |  |
|           |      | Avsäkrad till 2,5A.                                                                       |  |
|           | TB4: | Aptus485-buss                                                                             |  |
|           |      | Bussens spänningsmatning är avsäkrad till 4A.                                             |  |
|           |      | Obs1! Bussens spänning är ställbar 12V eller 24V. Innan                                   |  |
|           |      | växling sker till 24V måste en kontroll göras av att alla                                 |  |
|           |      | enheter på bussen är avsedda för 24V.                                                     |  |
|           |      | Obs2! Använd denna A485-port endast om centralen inte                                     |  |
|           |      | är bestyckad med kort för extra A485-portar.                                              |  |
|           |      | Terminering görs på baskortets S3 [B-S3].                                                 |  |
|           |      | J1, J2: Kontakter där Baskort ansluts till Grundkort.                                     |  |
|           | J3:  | Här ansluts ett eventuellt expansionskort. EXP1.                                          |  |
|           |      | Styra Komkort 4000, Styra Porttelefonkort 4400,                                           |  |
|           |      | Styra I/O 8800 eller Styra I/O 4400 är möjliga att montera.                               |  |
|           | J4:  | Här ansluts ett eventuellt expansionskort. EXP2.                                          |  |
|           |      | Styra Komkort 4000, Styra Porttelefonkort 4800,                                           |  |
|           |      | Styra I/O 8800 eller Styra I/O 4400 är möjliga att montera.                               |  |
|           |      |                                                                                           |  |

Kom ihåg att lägga på "G-" före plintbeteckningarna ovan vid anläggningsdokumentation.

#### **SÄKRINGAR OCH SKYDD**

Grundkortet har försetts med skyddsfunktioner emot felkoppling och överlast.

| F1:    | 10 A, Glasrörssäkring (T5x20). Om sammanlagda inkom         |  |  |  |
|--------|-------------------------------------------------------------|--|--|--|
| 24V In | mande matningströmmen, TB1, överstiger 10A skall denna      |  |  |  |
|        | lösa.                                                       |  |  |  |
| F2:    | 2,5 A, PTC. Förhindrar att extern utrustning som matas via  |  |  |  |
| 24V Ut | TB2 tar för mycket ström.                                   |  |  |  |
| F3:    | 2,5 A, PTC. Förhindrar att extern utrustning som matas via  |  |  |  |
| 12V Ut | TB3 tar för mycket ström.                                   |  |  |  |
| F4:    | 4 A, PTC. Förhindrar att utrustning kopplad till Aptus485-  |  |  |  |
| A485   | bussen, TB4, tar för mycket ström. Lysdiod D11 lyser rött   |  |  |  |
|        | om säkringen löst ut.                                       |  |  |  |
| F5:    | 10 A, Internproducerad 12V strömbegränsas till 10 A. Tänk   |  |  |  |
| 12V    | på att summan av strömuttag på A485-bussar inte kan         |  |  |  |
|        | överstiga dessa 10A om de är byglade för att leverera 12V.  |  |  |  |
| F6:    | Polaritetsskydd av TB1. Om Gnd och 24V kopplas fel kom      |  |  |  |
| 24V In | mer vare sig central eller spänningsaggregat att gå sönder. |  |  |  |
|        | Dock krävs rätt polaritet för att centralen skall fungera.  |  |  |  |

## **FUNKTIONER 10**4

#### **PASSAGE**

Styra 3000 är utmärkt att använda i ett passagesystem. I tabellen nedan listas parametrar av intresse när centralen används för passage.

| Antal dörrar som kan styras     | 8                                | Aptus Logga_Silver pantone 877    |                   |  |
|---------------------------------|----------------------------------|-----------------------------------|-------------------|--|
| Antal läsare som kan anslu      | 16                               | samtidigt med porttelefoni.       |                   |  |
| tas                             |                                  |                                   |                   |  |
| Antal dörrenheter, Koppla, som  | Begränsas av totala antalet in   |                                   |                   |  |
| kan anslutas                    | respektive utgångar i centralen. |                                   |                   |  |
| Antal interna I/O-kort som kan  | 2                                |                                   | telefonkort 4800. |  |
| monteras i centralen.           |                                  | Antal svarsapparater              | 600               |  |
| Antal externa I/O-kort som kan  | Begränsas av totala antalet in   | Maximalt antal telefonummer       | 9000              |  |
| anslutas, t.ex. MC1-I/O, MC1-   | respektive utgångar i centralen. | Maximalt antal lägenheter i       | 600 per Ringa     |  |
| MBus, AXI2O16                   |                                  | Ringas displayvisning             |                   |  |
| Maximalt antal enheter som kan  | 95                               |                                   |                   |  |
| anslutas                        |                                  |                                   |                   |  |
| Maximalt antal resurser som     | 255                              |                                   | Ringa 2707:C1.    |  |
| stöds                           |                                  | Svarsapparater som stöds          | AT20, AT21        |  |
| Maximalt antal ingångar         | 64 (32 av dessa kan vara larmin  | Parallellkoppling av porttelefon  | Ja, max två.      |  |
|                                 | gångar)                          | centraler till svarsapparatslinga |                   |  |
| Maximalt antal utgångar         | 96                               |                                   |                   |  |
| Maximalt antal användare        | 65535                            |                                   |                   |  |
| Maximalt antal kunder           | 9000                             |                                   |                   |  |
| Maximalt antal lagrade händel   | 24000                            |                                   |                   |  |
| ser                             |                                  |                                   |                   |  |
| Maximalt antal tidzo            | 384                              |                                   |                   |  |
| ner                             |                                  |                                   |                   |  |
| Maximalt antal Styra 3000 i ett | 64                               |                                   |                   |  |
| system                          |                                  |                                   |                   |  |
|                                 |                                  |                                   |                   |  |

#### **BOKNING**

Styra 3000 lämpar sig också mycket bra som bokningscentral och kan kombinera passagefunktionerna ovan med bokningsfunktionalitet.

| Maximalt antal bokningstavlor,                              | 4, anslut dock inte mer än en     |
|-------------------------------------------------------------|-----------------------------------|
| Boka på centralen                                           | Boka på samma A485-port.          |
| Antal bokningsobjekt i central                              | 16                                |
| Antal bokningstyper                                         | 4                                 |
| Antal bokningsgrupper                                       | 16                                |
| Bokning mellan centraler                                    | Ja                                |
| Aktivering av bokning via annan                             | Nej, bokade objekt kan endast     |
| central                                                     | aktiveras via den egna centralen. |
| Bokningstavlor som kan användas Boka 1306,1316. Min FW: C0. |                                   |
|                                                             | Boka 2306, 2316. Min FW: A1       |
| Maskinterface                                               | Max 64, (8 per AA TMI-A485)       |

#### **PORTTELEFONI**

Om Styra 3000 skall användas för porttelefoni måste den förses med ett porttelefoninterface. Detta finns inbyggt på tillbehörskortet Styra Porttelefonkort 4400. Även de vanliga passagefunktionerna fungerar bra med porttelefonin, däremot kan inte centralen hantera bokning samtidigt med porttelefoni.

|           | Antal dörrar med porttelefoni     | 8, Detta kräver att centralen   |  |
|-----------|-----------------------------------|---------------------------------|--|
|           |                                   | bestyckats med både Styra port  |  |
|           |                                   | telefonkort 4400 och Styra port |  |
| Scala 1:1 |                                   | telefonkort 4800.               |  |
|           | Antal svarsapparater              | 600                             |  |
|           | Maximalt antal telefonummer       | 9000                            |  |
|           | Maximalt antal lägenheter i       | 600 per Ringa                   |  |
|           | Ringas displayvisning             |                                 |  |
|           | Porttelefoner som kan användas    | Ringa 1307: C1, Ringa 1507:     |  |
|           |                                   | A2, Ringa 1707:C1,              |  |
|           |                                   | Ringa 2707:C1.                  |  |
|           | Svarsapparater som stöds          | AT20, AT21                      |  |
|           | Parallellkoppling av porttelefon  | Ja, max två.                    |  |
|           | centraler till svarsapparatslinga |                                 |  |

![](_page_10_Picture_1.jpeg)

**Scala 1:1 Kontaktperson Marianne Hauger**

**031 68 97 11**

### **11**4

### **UPPGRADERING & SERVICE**

#### **UPPGRADERING AV PROGRAMVARA**

Uppgradera din centralenhet till en senare programversion om den nya versionen innehåller nya funktioner eller förbättringar som du vill kunna utnyttja. Innan du uppgraderar skall du undersöka att den nya versionen är kompatibel med övriga programvaror i din anläggning. När du uppgraderar bör du följa nedanstående lista: **Aptus Logga_Silver pantone 877**

- 1. Vidta lämpliga åtgärder med tanke på att centralen ej fungerar under själva uppgraderingen.
- 2. Hämta hårdvara och kontrollera att centralen är aktiv.
- 3. Hämta händelser.
- 4. Genomför uppgraderingen. Se separat avsnitt nedan.
- 5. Hämta hårdvara. Rapporteras rätt version?
- 6. Sänd minneskonfiguration.
- 7. Sänd all data till centralen.
- 8. Kontrollera klockan.
- 9. Slå av och på kontunuerlig loggning om det används på anlägg ningen.
- 10. Kontrollera att centralen åter är i funktion.

För att kunna genomföra uppgraderingen måste du ha skaffat filen som innehåller programmet. Filen kan t.ex ha namnet "Styra_ C0.bin". Detta är då programvara i version C0 för Styra 3000 och finns att ladda ned från kundinloggningen på www.aptus.se.

#### **Uppgradering**

- 1. Logga in i Multiaccess med behörigheten "Installatör".
- 2. Öppna enhetskonfigurationen.
- 3. Högerklicka på mastercentralen i det system som skall uppgrade ras. Välj "Mjukvara -> Uppgradera".
- 4. Varning om att minne i centralerna kan förloras kommer, svara Ja.
- 5. Windowsruta via vilken du kan välja progranmfil kommer upp, välj och klicka på "Öppna". Nu sätter uppgradering av mastern igång. Grön statusled på baskortet slocknar.
- 6. Vänta tills mastern är färdiguppgraderad. Statusled tänds igen.
- 7. Sänd minneskonfiguration. (Annars hittar mastern ej sina slavar)
- 8. Högerklicka på systemet, välj "Mjukvara -> Ersätt alla slavars
- mjukvara med mastercentralens mjukvara".
- 9. Varning om minne och dylikt, svara Ja.
- 10. Invänta att uppgraderingen skall bli färdig. Tiden beror på hur många slavar som finns i systemet samt vilken kommunikation som används.
- 11. Slutför uppgraderingen enligt punkt 5 10 i listan ovan, Hämta hårdvara....

**Obs,** Vill du byta programvara i endast en utpekad slavcentral skall du högerklicka på denna och välja "Mjukvara - Uppgradera".

![](_page_11_Picture_1.jpeg)

### **12**4

#### **CENTRALOMSTART OCH NOLLSTÄLLNING AV MINNE**

Det finns ett antal sätt att starta om centralen och genomföra rensning eller nollställning av hela eller delar av centralens minne. Tabellen nedan reder ut begreppen.**NCBKDHFKCHSDKHFCKJ**

|                                                                                                                              | Central startar om | Återgång till initial | Aptus Logga_Silver pantone 877<br>Nollställning av | Nollställning av | Nollställning av | Centrals klocka    |
|------------------------------------------------------------------------------------------------------------------------------|--------------------|-----------------------|----------------------------------------------------|------------------|------------------|--------------------|
|                                                                                                                              | men behåller allt  | kryptering, dvs.      | nätmask och övriga                                 | databas, t.ex.   | centrals informa | återgår till 2001- |
|                                                                                                                              | minne intakt och   | okrypterad kommu      | nätverksinställ                                    | användare, tidzo | tion om anslutna | 01-01.             |
|                                                                                                                              | jobbar vidare.     | nikation.             | ningar.                                            | ner, bokningar,  | A485-enheter.    |                    |
|                                                                                                                              |                    |                       | Scala 1:1                                          | händelser, som   |                  |                    |
|                                                                                                                              |                    |                       |                                                    | martidskompen    |                  |                    |
|                                                                                                                              |                    |                       |                                                    | sation, masters  |                  |                    |
|                                                                                                                              |                    |                       |                                                    | slavlista.       |                  |                    |
| Spänningscykla<br>centralen.                                                                                                 | x                  |                       |                                                    |                  |                  |                    |
| Starta om cen<br>tralen från<br>Multiaccess.                                                                                 | x                  |                       |                                                    |                  |                  |                    |
| Starta om med<br>minnesrensning<br>från Multiaccess.                                                                         |                    |                       |                                                    | x                |                  |                    |
| Spänningscykla<br>centralen med<br>mem-switchen<br>uppe.                                                                     |                    | x                     |                                                    | x                | x                |                    |
|                                                                                                                              |                    |                       |                                                    |                  |                  |                    |
| Bryt centralens<br>spänning, slå av<br>batteribackup i<br>60 sekunder slå<br>därefter på och<br>spänningssätt cen<br>tralen. |                    | x                     | x                                                  | x                | x                | x                  |
| Uppgradera cen                                                                                                               |                    |                       |                                                    |                  |                  |                    |
| trals mjukvara.                                                                                                              |                    |                       |                                                    | x                |                  |                    |
|                                                                                                                              |                    |                       |                                                    |                  |                  |                    |
|                                                                                                                              |                    |                       |                                                    |                  |                  |                    |
|                                                                                                                              |                    |                       |                                                    |                  |                  |                    |

![](_page_12_Picture_1.jpeg)

#### **UPPGRADERING AV APTUS485-ENHETER**

Det är nu möjligt att uppgradera mjukvaran även i centralens underliggande enheter, de s.k. Aptus485-enheterna. Det bör dock påpekas att det just nu endast är nyare varianter av Aptus485-enheter för vilka detta kan göras. Vilka det är framgår av tabellen nedan:

| Ringa 1507                 | Alla               |
|----------------------------|--------------------|
| Ringa 1707                 | Från FW version C1 |
| Ringa 2707                 | Alla               |
| Boka 1306                  | Från FW version C0 |
| Boka 1316                  | Från FW version C0 |
| Boka 2306                  | Alla               |
| Boka 2316                  | Alla               |
| Koppla 2100                | Alla               |
| Koppla 4300                | Alla               |
| Koppla 0010                | Från FW version A2 |
| Koppla 0020                | Alla               |
| Styra Komkort 4000         | Alla               |
| Styra Porttelefonkort 4400 | Alla               |
| Styra Porttelefonkort 4800 | Alla               |
| Styra I/O 4400             | Alla               |
| Styra I/O 8800             | Alla               |
| AA TMI-A485                | Alla               |
| Öppna 2100                 | Alla               |
| Öppna 2500                 | Alla               |
| Öppna 2105                 | Alla               |
| Öppna 2505                 | Alla               |

Uppgradera programversionen endast vid behov, t.ex. att Aptus meddelat att ny programvara innehåller funktionsförbättringar som kan vara intressanta för er anläggning.

Börja med att ladda ner den nya mjukvaran som antingen finns upplagd under inloggningen på www.aptus.se eller som distribueras direkt till er.

**Obs!** Innan uppgradering startas måste du tänka igenom vilka funktioner som påverkas. Om t.ex. en porttelefon uppgraderas så är det bara porttelefonin för den dörren som berörs men om ett Styra Komkort 4000 uppgraderas så berörs alla delar som har sin kommunikation genom kortet.

Genomför uppgradering av en enhet i taget enligt följande:

- 1. Logga in i Multiaccess med behörigheten "Installatör".
- 2. Öppna enhetskonfigurationen.
- 3. Högerklicka på den enhet som skall uppgraderas, välj "Uppgradera mjukvara".
- 4. Windowsruta via vilken du kan välja programfil kommer upp, välj och klicka på "Öppna". Nu sätter uppgradering av enheten igång.
- 5. Invänta att uppgraderingen skall bli färdig. Tiden kan variera beroende på typ av enhet samt vilken kommunikationsmetod som används till centralen.

- 6. Hämta hårdvara. Rapporteras rätt version?
#### **ENKELT UTBYTE A485**

Funktionen innebär att det vid service skall vara möjligt att byta ut t.ex. en trasig läsare och ersätta den med en motsvarande som direkt skall träda i funktion. För att detta skall vara möjligt är det dock några villkor som måste vara uppfyllda: **Aptus Logga_Silver pantone 877** Ringa 1307 Från FW version C1

- 1. I systemets detaljbild skall "Tillåt automatiskt utbyte av Aptus485-enheter" vara förbockad. Observera att denna bör vara urkryssad vid driftsättning och nyinstallation. **Scala 1:1 Kontaktperson Marianne Hauger**
	- 2. Den enhet som skall bytas ut måste av centralen ha registrerats som inaktiv. Innebär att om en fungerande enhet skall bytas måste den kopplas ur 1 minut innan den nya ersättningsenheten kopplas in.
	- 3. För att automatiska bytet skall fungera får det inte vara flera lika dana enheter som är trasiga på samma A485-segment. Genom att använda något av kommunikationskorten minskar san nolikheten att det skall finnas flera av samma sort på samma A485-port.

Om automatiska utbytet inte går att genomföra måste du via Multiaccess se till att den nya enheten blir kopplad rätt.

### **KOMMUNIKATION 14**4

#### **NÄTVERK**

Centralen kan anslutas till nätverk. Detta skall i så fall anslutas till IP1 på baskortet.

Anslutning till nätverk kan göras oberoende om centralen är konfigurerad till master eller slav.

Tänk på att inte ansluta direkt till internet, brandvägg skall finnas. Kommunikationshastighet: 10/100 Mbit/sek.

Kabeltyp: CAT5 eller CAT6.

#### **RS232 INKOPPLING**

Till en mastercentral kan kommunikationen från Multiaccess ske via RS232. Inkoppling sker via TB3 på baskortet. Kommunikationen kan ske direkt eller via någon typ av modem.

Du kan också använda RS-232 porten för att ordna sekundär kommunikation, om den primära via nätverket ej fungerar.

| Kommunikationshastighet: | 9600 Baud                       |
|--------------------------|---------------------------------|
| Kabeltyp:                | Aptus programmeringskabel eller |
|                          | modemkabel                      |

#### RS-232 RS-232 TB3 TB3 1 2 3 4 5 6 Brun Gul Vit Grön 1 2 3 4 5 6 7 BrunGul Vit GrönRosaGrå GND Tx Rx RTS CTS CD3.3V GND Tx Rx RTS CTS CD3.3V

#### **Uppkoppling direkt till datorns serieport Anslut programmeringskabeln till TB3.** Specificerad längd för RS232 som

används är 15 meter. Normalt fungerar det med längre avstånd mellan master och dator, 20 till 50 meter är inte ovanligt. Vid längre avstånd bör korthållsmodem (trådbundet) eller telemodem användas.

#### **Uppkoppling via modem (tele, korthålls eller GSM)**

**Anslut modemkabeln till TB3.**

Anslut andra änden till modemet. Om du valt uppringd anslutning kommer uppringning att kunna initieras från båda håll, dvs både MultiAccess respektive mastern kan starta en uppringning om det finns data som behöver överföras. Sätt S1.2 = On, Modem.

Om telelinje saknas kan ett GSMmodem installeras istället.

#### **SLAV485**

Centralerna, mastern och dess slavar, utbyter information genom ett kommunikationsnät enligt RS485-specifikation. Denna kommunikation är mycket tålig mot störningar, men man bör ändå undvika att förlägga kommunikationskabeln parallellt med kraftkabel längre sträckor. **Aptus Logga_Silver pantone 877**

Till varje master kan man ansluta 63 st slavar. Centralerna kopplas ihop med partvinnad kabel till en slinga. Observera att det inte är tillåtet att koppla slingan så att det uppstår ett stjärnnät. Låt A och B bilda ett par och GND ett par. **Scala 1:1 Kontaktperson Marianne Hauger**

Kommunikationshastighet: 38400 Baud.

Kabeltyp: Partvinnad kabel typ ELLXB eller ELAQBY skall användas. 4 ledare används, 1 par till data (A+B) och 1 par till GND. Största avståndet mellan de två ändpunkterna på kommunikations-slingan är normalt 1100 meter.

![](_page_13_Figure_24.jpeg)

Centralerna behöver inte sitta i adressordning utan placeras i den ordning man finner lämplig med tanke på kabeldragningen.

#### **IPSLAV**

Som ett alternativ till att ansluta slavarna via Slav485 kan slaven anslutas direkt till nätverket istället. På en IP-slav används inte Slav485 på TB5.

![](_page_14_Picture_2.jpeg)

#### **APTUS485**

På Aptus485-bussen kommunicerar centralen med sina interna eller externa utrustning såsom I/O-moduler, kommunikationskort, kortläsare, porttelefoner, bokningstavlor, lås, dörrenheter osv. Enheterna får både matning, 12V1, och kommunikation på denna 4-trådsbuss. Undvik att förlägga kommunikationskabeln parallellt med kraftkabel längre sträckor.

Till varje central kan max 95 enheter anslutas. Ihopkoppling av enheterna sker med partvinnad kabel till en slinga.

#### Kommunikationshastighet: 38400 Baud.

Kabeltyp: Partvinnad kabel typ ELLXB eller ELAQBY bör användas. 4 ledare används, 1 par till data (A+B) och 1 par till GND och 12V. Längsta avståndet mellan de två ändpunkterna på kommunikations-slingan är normalt 200 meter.

**Obs 1!** Tänk på att Aptus485 enheterna har sin strömförsörjning via kablaget. Beroende på vad du ansluter kan arean behöva ökas eller avståndet minskas. Du kan öka arean genom att använda Aptuskabel. Den är en partvinnad 2-pars kabel med grövre area i ena paret: 2x0.15mm2 + 2x1.0mm2.

**Obs 2!** Aptus485 bussen är inte avsedd för större installationsavstånd, och skall hållas lokal inom en och samma byggnad.

![](_page_14_Figure_10.jpeg)

Terminering av slingan.

Vid de två enheter som befinner sig vid slingans ändar skall terminering aktiveras. Detta görs med hjälp av omkopplare 1 och 2, ON=Terminerat.

#### **Alternativ topologi - stjärnnät**

I vissa fall kan det bli svårt att förlägga Aptus485-bussen som buss. Om så är fallet kan avsteg göras genom att tillåta kortare stick. Ett enskilt stick får då inte överskrida 100 m och den sammanlagda kabelssträckan får inte översiga 200 m. Terminering görs i så fall i ändpunkterna av den längsta sammanhängande sträckan. En anledning till att bygga stjärnnät är att minska spänningsfallet och störningarna i matningsspänningen från central och ut till enskilda enheter.

#### **Aptus485 på Styra 3000**

På Styra 3000 ansluts Aptus485-bussen till G-TB4 på grundkortet, Styra Grund 10A. Termineringsswitch och lysdioder sitter dock på

#### baskortet.

Anslut Aptus485 till G-TB4 endast om kort för ytterligare Aptus485 bussar inte installerats.

#### **Multipla Aptus485-bussar**

Till Styra 3000 finns tillbehörskort som ger fyra extra Aptus485 bussar. Korten som avses är Styra Komkort 4000, Styra Porttelefonkort 4400 och Styra Porttelefonkort 4800. Totalt kan centralen på detta sätt bestyckas med åtta individuella Aptus485 bussar. Varje sådan buss är elektriskt fristående från de andra bussarna och termineras också individuellt. **Scala 1:1 Kontaktperson Marianne Hauger Aptus Logga_Silver pantone 877**

> Detta innebär att installationen kan delas, t.ex. genom att låta alla enheter som betjänar en speciell dörr vara kopplade till samma Aptus485-port.

När multipla bussar finns i centralen skall en korrekt buss byggas med terminering i varje ända. Görs detta korrekt kan bussens installationslängd vara 1100 m, under förutsättning att spänningsfall i kablaget ej blir för stort.

**Tips!** Om två dörrmiljöer skall anslutas till samma A485-port på kommunikationskortet är det lämpligt att dra separat kabel till respektive dörrmiljö. Detta kan ändå bli en korrekt buss genom att lägga termineringarna vid respektive dörr och låta kommunikationskortsporten vara oterminerad.

![](_page_14_Figure_24.jpeg)

#### **KRYPTERAD KOMMUNIKATION**

Centralkommunikationen är krypterad med 128-bitars AESkryptering. Obs! Vid driftsättning är denna kryptering avslagen. Efter avslutad driftsättning skall krypteringen aktiveras via Multiaccess Styra.

Kommunikationen till Aptus485-enheter är alltid krypterad med 32-bitars nycklar.

**1)Även 24V är möjlig! Konfigurera aldrig en Aptus485 buss till 24 V om du inte har kontrollerat att den anslutna utrustningen får matas med 24 V.**

![](_page_15_Picture_1.jpeg)

### **INGÅNGAR 16**4

#### **DIGITALA INGÅNGAR**

På baskortet, B-TB2, finns 2 ingångar för anslutning av potentialfri kontakt med slutande eller brytande funktion. De kan t.ex användas för inkoppling av öppnaknappar och dörrövervakning. Ingång kan också användas som pulsräknare för att registrera pulser enligt S0-standarden.

Anslutning sker till skruvplint B-TB2 på baskortet. Ingång anses vara aktiv när den sluts mot jord. In1 och In2 har gemensam jord på TB2:1.

![](_page_15_Figure_6.jpeg)

Kabeltyp: Partvinnad kabel typ ELLXB eller ELAQBY.

Ytterligare digitala ingångar kan fås genom att ansluta enheter av typen AXI2Oxx som vardera innehåller två digitala ingångar.

#### **BALANSERADE INGÅNGAR**

Jämfört med en vanlig digital ingång erbjuder BS-ingången ett skydd mot manipulering och felaktigheter. Via Multiaccess kan BS-ingången konfigureras för olika typer av slingor. Ingången kan också konfigureras till vanlig Digital ingång.

Ingångarna är avsedda för allehanda ingångsfunktioner såsom öppna-knappar, larmdetektorer, pulsgivare enligt S0-standarden osv.

Anslutning sker till skruvplint på aktuell enhet. I vissa fall kan flera givare kopplas in mot samma BS-ingång. Detta är lämpligt i de fall man inte behöver veta exakt vilken givare som löst utan bara att minst 1 har aktiverats. Dock gäller max 1 pulsgivare /ingång

![](_page_15_Figure_13.jpeg)

Bilden ovan visar principen för en balanserad slinga och dess inkoppling.

**Normalläge:** Alla larmkontakter slutna.

Rnorm = x*Rs + Rk +/-5%.

**Larmläge:** Minst 1 larmkontakt är bruten.

(xRs + 1Rp + Rk) <= Rlarm <= (xRs + xRp + Rk)

**Linjefel/ Sabotage:** Alla slingvärden som inte ligger inom larm eller normalfönstret. **Aptus Logga_Silver pantone 877**

> Syftet med Rk är att kompensera för att slingan ej är fullt utbyggd. Om slingan max kan vara på 6 kontakter och bara 3 är installerade skall Rk= 3Rs.

Om endast 1 kontakt kopplas in är det onödigt att installera Rk, istället anpassas Rs till x*Rs. **Scala 1:1 Kontaktperson Marianne Hauger**

> **Förenklad inkoppling:** En mycket vanlig inkopplingsvariant av givare är att man låter Rp = Rs = 2200 Ohm och utesluter Rk. Koppla en givare per ingång och sätt gränsvärden i Multiaccess så att omslag erhålls vid rätt nivå. Förslag på gränser:

0 - **1500** Linjefel/Sabotage 1500 - **3000** Normal 3000 - **6000** Larm 6000 - Linjefel/Sabotage

**Avläsning:** Du kan via Multiaccess läsa av aktuellt resistansvärde för inkopplad slinga. Högerklicka på ingången i enhetshanteraren och välj "Hämta aktuellt värde". Detta fungerar dock ej om du satt ingången till att vara pulsräknare eftersom det då är pulsräknarvärdet som presenteras istället.

#### **Lysdiodsfunktion för de balanserade ingångarna**

1 röd lysdiod finns monterad för varje ingång. Lysdioderna skall tolkas på följande sätt:

| Normalläge: Led släckt |             |
|------------------------|-------------|
| Larmläge:              | Led tänd    |
| Linjefel:              | Led blinkar |

Kabeltyp: Partvinnad kabel typ ELLXB eller ELAQBY bör användas.

#### **Enheter med balanserade ingångar**

Följande enheter har ingångar av typen balanserad och kan kopplas till Styra 3000.

| Styra I/O 4400 | 4 |
|----------------|---|
| Styra I/O 8800 | 8 |
| Koppla 2100    | 2 |
| Koppla 4300    | 4 |
| MC1-I/O        | 8 |

### **UTGÅNGAR 17**4

#### **TRANSISTORUTGÅNG**

På Baskortet finns 1 digital utgång i form av en transistorutgång. Den är avsedd för att utföra styrningar, t.ex upplåsning via elslutbleck eller aktivering av en siren.

Obs, Om den utrustning som skall styras av utgången måste vara galvaniskt separerad från Styra 3000 bör utrustningen istället kopplas till en reläugång.

Anslutning görs till B-TB1:1,2 på Baskortet.

![](_page_16_Picture_7.jpeg)

En lysdiod, placerad direkt innanför anslutningen indikerar om utgången är aktiv eller ej.

På bilden visas exempel på hur ett elslutbleck kan kopplas in. Observera att blecket måste vara av 12V variant i detta fall. Notera också skyddsdioden som installerats över blecket.

När utgången dras ansluts TB1:1 (S) till GND.

Kabeltyp: Partvinnad kabel typ ELLXB eller ELAQBY.

#### **Avstörning**

Det som styrs med en utgång måste störas av med en diod direkt över själva förbrukaren, t.ex. ett slutbleck. Till varje central bipackas dioder för detta syfte.

Ytterligare transistorutgångar kan fås genom att ansluta enheter av typen AXI2Oxx som vardera innehåller upp till 16 transistorutgångar.

#### **RELÄUTGÅNGAR**

Digitala utgångar i form av reläer med växlande funktion. Dessa är avsedda för att utföra styrningar, t.ex. upplåsning via elslutbleck eller aktivering av en siren.

Normalt levererar ett relä en potentialfri slutning/brytning, men det går också att ställa om så att spänning kan levereras ut.

![](_page_16_Picture_18.jpeg)

- + Extern spänning

**PWR** Till vänster visas inkoppling av ett elslutbleck med extern matning så att galvanisk isolering erhålles. Draget relä innebär slutning mellan Skruv 1 och 2.

Till höger visas inkoppling av ett elslutbleck med matning från centralen via reläet. Skruv 1 är kopplad till jord och Skruv 2 kopplas till +VDC när reläet aktiveras. +VDC avser aktuell matningsspänning.

![](_page_16_Picture_21.jpeg)

#### **Lysdiod**

Alla reläutgångar har en tillhörande lysdiod som tänds när utgången är aktiv.

Kabeltyp: Partvinnad kabel typ ELLXB eller ELAQBY. **Aptus Logga_Silver pantone 877**

#### **Enheter med reläutgångar**

Följande enheter har utgångar av typen relä och kan kopplas till Styra 3000.

| Scala 1:1 | Styra I/O 4400 | 4 |
|-----------|----------------|---|
|           | Styra I/O 8800 | 8 |
|           | Koppla 2100    | 1 |
|           | Koppla 4300    | 3 |
|           | MC1-I/O        | 2 |
|           |                |   |

![](_page_17_Picture_1.jpeg)

### **STYRA I/O 4400 18**4

#### **ALLMÄNT**

Kort med in och utgångar avsett att monteras i Styra 3000.

#### **TEKNISKA DATA**

|            | Strömförsörjning: 12/24 V DC (10,5 - 27,6).               | NC<br>3<br>TB1. Om t.ex. utgång 1 skall                                                  |  |  |
|------------|-----------------------------------------------------------|------------------------------------------------------------------------------------------|--|--|
|            |                                                           | Aptus Logga_Silver pantone 877<br>PWR ISO<br>TB1<br>K1<br>2<br>NO<br>Ut1<br>C<br>F1<br>1 |  |  |
|            | Max 100mA, Min 10mA vid 24V.                              | användas skall anslutning ske till<br>K1 > TB1:1-3                                       |  |  |
|            | Max 140mA, Min 15mA vid 12V.                              | TB1:1-3. Om slutande funktion                                                            |  |  |
|            | Direktmatning internt i centralenheten.                   | önskas, anslut mellan TB1:1,2 och för brytande funktion gäller                           |  |  |
| Ingångar:  | 4, balanserad slinga, BS, eller kontakter med             | TB1:1,3.                                                                                 |  |  |
|            | Scala 1:1<br>potentialfri slutning/brytning kan anslutas. |                                                                                          |  |  |
|            | Pulsmätning enligt S0 stöds.                              | Ingångar                                                                                 |  |  |
|            | Skydd: Varistor 22V, serieresistans 10KOhm.               | Anslut givare och knappar till                                                           |  |  |
|            | Statusindikering via lysdiod.                             | In4<br>5<br>någon av de fyra ingångarna på<br>In1<br>In3<br>4                            |  |  |
| Utgångar:  | 4, reläutgång med växlande kontakt för att möj            | In2<br>TB3<br>In2<br>3<br>TB3. Om t.ex. ingång 1 skall<br>In3<br>In1<br>2                |  |  |
|            | liggöra inkoppling av slutande eller brytande             | In4<br>användas skall anslutning ske<br>Gnd<br>1                                         |  |  |
|            | funktion.                                                 | mellan TB3:1,2.                                                                          |  |  |
|            | Ställ in PWR/ISO beroende på om centralens                |                                                                                          |  |  |
|            | spänning skall levereras ut eller om endast poten         | INSTÄLLNINGAR                                                                            |  |  |
|            | tialfri slutning/brytning skall användas.                 | Inställning av reläets funktion, spän                                                    |  |  |
|            | Kontaktdata relä: 28V, 1A.                                | JP2<br>JP1<br>ningsutmatning eller isolerad, PWR/                                        |  |  |
|            | Skydd: Termisk säkring 1A (PTC).                          | ISO, görs med byglarna JP1 - JP8.                                                        |  |  |
|            | Statusindikering via lysdiod.                             | PWR 1 ISO<br>Dom skall flyttas parvis och JP1, JP2                                       |  |  |
| Miljökrav: | 0 till 40 grader Celsius.                                 | gäller således för utgång 1. JP1 -                                                       |  |  |
|            | 0 - 90 % luftfuktighet.                                   | JP8 är inte utmärkta på kortet, istället står det en siffra 1 - 4 mellan                 |  |  |
| Mått:      | 65x98x18                                                  | PWR och ISO som pekar ut för vilken utgång inställningen gäller.                         |  |  |
| Vikt:      | 0,1Kg                                                     |                                                                                          |  |  |

#### **MONTERING**

Kortet skall monteras med spänning avslagen. Om kortplats 1, EXP 1, är ledig och inte planerad för annat kort bör kortet monteras där annars monteras det på kortplats 2. Trä på kortet på därför avsedd stiftlist, G-J3 eller G-J4. När kortet är på plats skall det fästas med de fyra bilagda skruvarna.

#### **INKOPPLING Utgångar**

Anslut det som skall styras till någon av de fyra utgångarna på

![](_page_17_Picture_12.jpeg)

#### **Ingångar**

![](_page_17_Picture_16.jpeg)

#### **INSTÄLLNINGAR**

![](_page_17_Picture_19.jpeg)

#### **LYSDIODER**

Ingångarnas status indikeras med lysdioder IN1 - IN4. Lysdiod kan vara släckt, tänd eller blinka beroende på om den är i läge normal. larm eller linjefel/sabotage. Utgångarnas status indikeras på lysdiod invid utgångens relä. Lysdioden är tänd när reläet är draget.

![](_page_17_Figure_23.jpeg)

![](_page_18_Picture_1.jpeg)

### **STYRA I/O 8800 19**4

#### **ALLMÄNT**

**NCBKDHFKCHSDKHFCKJ** Kort med in och utgångar avsett att monteras i Styra 3000.

#### **TEKNISKA DATA**

|            | Strömförsörjning: 12/24 V DC (10,5 - 27,6).       |  |  |
|------------|---------------------------------------------------|--|--|
|            | Max 170mA, Min 10mA vid 24V.                      |  |  |
|            | Max 240mA, Min 15mA vid 12V.                      |  |  |
|            | Direktmatning internt i centralenheten.           |  |  |
| Ingångar:  | 8, balanserad slinga, BS, eller kontakter med     |  |  |
|            | potentialfri slutning/brytning kan anslutas.      |  |  |
|            | Pulsmätning enligt S0 stöds.                      |  |  |
|            | Skydd: Varistor 22V, serieresistans 10KOhm.       |  |  |
|            | Statusindikering via lysdiod.                     |  |  |
| Utgångar:  | 8, reläutgång med växlande kontakt för att möj    |  |  |
|            | liggöra inkoppling av slutande eller brytande     |  |  |
|            | funktion.                                         |  |  |
|            | Ställ in PWR/ISO beroende på om centralens        |  |  |
|            | spänning skall levereras ut eller om endast poten |  |  |
|            | tialfri slutning/brytning skall användas.         |  |  |
|            | Kontaktdata relä: 28V, 1A.                        |  |  |
|            | Skydd: Termisk säkring 1A (PTC).                  |  |  |
|            | Statusindikering via lysdiod.                     |  |  |
| Miljökrav: | 0 till 40 grader Celsius.                         |  |  |
|            | 0 - 90 % luftfuktighet.                           |  |  |
| Mått:      | 65x98x27                                          |  |  |
| Vikt:      | 0,15Kg                                            |  |  |

#### **MONTERING**

Kortet skall monteras med spänning avslagen. Om kortplats 1, EXP 1, är ledig och inte planerad för annat kort bör kortet monteras där annars monteras det på kortplats 2. Trä på kortet på därför avsedd stiftlist, G-J3 eller G-J4. När kortet är på plats skall det fästas med de fyra bilagda skruvarna.

#### **INKOPPLING Utgångar**

**Aptus Logga_Silver pantone 877** Anslut det som skall styras till någon av de åtta utgångarna på TB1 respektive TB2. Om t.ex. utgång 1 skall användas skall anslutning ske till TB1:1-3. Om slutande funktion önskas, anslut

![](_page_18_Picture_11.jpeg)

**Scala 1:1 Kontaktperson Marianne Hauger** mellan TB1:1,2 och för brytande funktion gäller TB1:1,3. Utgång 5 - 8 på motsvarande sätt på TB2.

In3

In2

In1

In7 In8

In6

In5 In4

#### **Ingångar**

Anslut givare och knappar till någon av de åtta ingångarna på TB3 respektive TB4. Om t.ex. ingång 1 skall användas skall anslutning ske mellan TB3:1,2.

![](_page_18_Figure_15.jpeg)

**031 68 97 11**

Ingång 5 - 8 på motsvarande sätt på TB4.

#### **INSTÄLLNINGAR**

Inställning av reläets funktion, spänningsutmatning eller isolerad , PWR/ISO, görs med byglarna JP1 - JP16. Dom skall flyttas parvis och JP1, JP2 gäller såle-

des för utgång 1. JP1 - JP16 är inte utmärkta på kortet, istället står det en siffra 1 - 8 mellan PWR och ISO som pekar ut för vilken utgång inställningen gäller.

PWR 1 ISO

JP1

JP2

#### **LYSDIODER**

Ingångarnas status indikeras med lysdioder IN1 - IN8. Lysdiod kan vara släckt, tänd eller blinka beroende på om den är i läge normal. larm eller linjefel/sabotage. Utgångarnas status indikeras på lysdiod invid utgångens relä. Lysdioden är tänd när reläet är draget.

![](_page_18_Figure_22.jpeg)

## **20**4

### **STYRA KOMKORT 4000**

#### **ALLMÄNT**

Kort med fyra Apus485-portar för inkoppling av externa Aptus485 enheter.

#### **TEKNISKA DATA**

| TEKNISKA DATA |                                             | Aptus Logga_Silver pantone 877                               |
|---------------|---------------------------------------------|--------------------------------------------------------------|
|               | Strömförsörjning: 12/24 V DC (10,5 - 27,6). | Separera dörrar                                              |
|               | Max 15mA, Min 10mA vid 24V.                 |                                                              |
|               | Max 20mA, Min 15mA vid 12V.                 |                                                              |
|               | Direktmatning internt i centralenheten.     | antal fördelar, nämligen:                                    |
| Avsäkrade     | 4, med repeater och säkring.                | -Varje dörr blir individuellt avsäkrad.                      |
| Aptus485-     | Skydd: Elektronisk säkring 2,5A.            | -Vid service kan spänningsmatning till dörr kopplas bort via |
| bussar:       | Statusindikering via lysdiod.               | Multiaccess.                                                 |
| Miljökrav:    | 0 till 40 grader Celsius.                   |                                                              |
|               | 0 - 90 % luftfuktighet.                     |                                                              |
| Mått:         | 65x98x17                                    | tesenhet.                                                    |
| Vikt:         | 0,1Kg                                       |                                                              |

#### **MONTERING**

Kortet skall monteras med spänning avslagen. Om kortplats 1, EXP 1, är ledig och inte planerad för annat kort bör kortet monteras där annars monteras det på kortplats 2. Trä på kortet på därför avsedd stiftlist, G-J3 eller G-J4. När kortet är på plats skall det fästas med de fyra bilagda skruvarna.

#### **INKOPPLING**

Anslut produkter avsedda för Aptus485 buss till valfri anslutning, TB1 - TB4. Använd partvinnad kabel t.ex. av typ ELLXB eller ELAQBY. Använd gärna Aptuskabel 1 som innehåller två tvinnade par där det ena är av grövre area för spänningsmatningsparet. Aptuskabel 1 har samma färgmärkning som plintarna på kortets A485-portar, varför det är enkelt att veta vilken anslutning som skall in i vilken plint. Tabellen visar inkoppling till TB1. Inkoppling för TB2 - TB4 görs på samma sätt.

| TB1:1 | B       |               |
|-------|---------|---------------|
| TB1:2 | A       |               |
| TB1:3 | GND     | Aptus485-buss |
| TB1:4 | 12V/24V |               |

#### **Separera dörrar**

En god strategi är att vika en Aptus485-port per dörr. Anslut då all utrustning som skall betjäna dörr 1 till kortets TB1. Detta ger ett antal fördelar, nämligen:

 -Varje dörr blir individuellt avsäkrad. **Scala 1:1 Kontaktperson Marianne Hauger**

- -Vid service kan spänningsmatning till dörr kopplas bort via Multiaccess.
- -Vid reperation kan automatiskt utbyte av Aptus485-enheter tilläm pas. Innebär att centralen automatiskt kan ge funktion åt en utby tesenhet.
- -Vid installation kan funktionen automatisk dörrtillhörighet använ das. Funktionen väljs i samband med hårdvaruhämtning i Multiaccess och knyter enhets resurser till dörr enligt den port på kommunikationskortet som den är kopplad till.

#### **INSTÄLLNINGAR**

#### **12 Volt eller 24 Volt**

Med byglarna JP1 till JP4 kan utmatad spänning ställas om från 12V till 24V individuellt per port. Obs! Innan detta görs måste det säkerställas att alla enheter som anluts till aktuell port är avsedda för 24V matning. 24V kan dock endast matas ut om centralen matas med 24V.

#### **LYSDIODERKDHFKCHSDKHFCKJ**

| D14-D17 | Status port1 -<br>port4 |  | Släckt: Normaldrift | Röd dubbelblink: Spänningsfel.<br>Röd enkelblink: Kommunikationsfel.<br>Alla blinkar rött: Kortet uppgraderas. |
|---------|-------------------------|--|---------------------|----------------------------------------------------------------------------------------------------------------|
|         |                         |  |                     | D18 Data tas emot Blinkar gult                                                                                 |

![](_page_19_Figure_24.jpeg)

### **21**4

### **STYRA PORTTELEFONKORT 4400**

#### **ALLMÄNT**

Kort med fyra Apus485-portar för inkoppling av externa Aptus485 enheter. Dessutom innehåller kortet porttelefoninterface för dörr 1 - dörr 4.

#### **TEKNISKA DATA**

| Strömförsörjning: | 24 V DC (21,6 - 27,6).                           |
|-------------------|--------------------------------------------------|
|                   | Max 25mA, Min 15mA vid 24V.                      |
|                   | Direktmatning internt i centralenheten.          |
| Avsäkrade         | 4, med repeater och säkring.                     |
| Aptus485-bussar:  | Skydd: Elektronisk säkring 2,5A.                 |
|                   | Statusindikering via lysdiod.                    |
| Porttelefoner     | 4, porttelefon av typ Ringa för dörr 1 - dörr 4. |
| Svarsapparater:   | 600, av typen AT20 och AT21 kan anslutas.        |
|                   | Skydd: Termisk säkring (PTC) 2,5A.               |
|                   | Parallellkoppling av två svarsapparatsslingor.   |
| Anslutning TELE:  | Ansluter till publika telenätet.                 |
| Miljökrav:        | 0 till 40 grader Celsius.                        |
|                   | 0 - 90 % luftfuktighet.                          |
| Mått:             | 97x98x26                                         |
| Vikt:             | 0,15Kg                                           |

#### **MONTERING**

Kortet skall monteras med spänning avslagen. Kan endast monteras på kortplats 1, EXP1. Trä på kortet på därför avsedd stiftlist, G-J3. När kortet är på plats skall det fästas med de fem bilagda skruvarna.

#### **INKOPPLING**

Anslut produkter avsedda för Aptus485 buss till valfri anslutning, TB1 - TB4. Om porttelefon skall anslutas skall också ljudbuss

![](_page_20_Figure_12.jpeg)

![](_page_20_Figure_13.jpeg)

anslutas på TB11 - TB14. Observera att porttelefoner **måste** anslutas till exakt den port som motsvarar dörren den skall betjäna. Endast en porttelefon är tillåten till repsektive

**031 68 97 11**

Aptus485-buss. Anslut således porttelefon för dörr 1 till TB1 och TB11. Dörr 2 - Dörr 4 ansluts på samma sätt till TB2 - TB4 respektive TB12 - TB14. **Scala 1:1 Kontaktperson Marianne Hauger**

> Använd partvinnad kabel t.ex. av typ ELLXB eller ELAQBY. Använd gärna Aptuskabel 2 som innehåller tre tvinnade par där det ena är av grövre area för spänningsmatningsparet. Aptuskabel 2 har samma färgmärkning som plintarna på kortets A485-portar, varför det är enkelt att veta vilken anslutning som skall in i vilken plint.

#### **Separera dörrar**

En god strategi, och för Ringa nödvändig, är att vika en Aptus485 port per dörr. Anslut då all utrustning som skall betjäna dörr 1 till kortets TB1.Detta ger ett antal fördelar, nämligen:

- -Varje dörr blir individuellt avsäkrad.
- -Vid service kan spänningsmatning till enskild dörr kopplas bort via Multiaccess.
- -Vid reperation kan automatiskt utbyte av Aptus485-enheter tilläm pas. Innebär att centralen automatiskt kan ge funktion åt en utby tesenhet.

 -Vid installation kan funktionen automatisk dörrtillhörighet använ das. Funktionen väljs i samband med hårdvaruhämtning i Multiaccess och knyter enhets resurser till dörr enligt den port på kommunikationskortet som den är kopplad till.

| Svarsapparater |      |                                       |
|----------------|------|---------------------------------------|
| TB6:1          | Gnd  | Anslut svarsapparater till TB6 &      |
| TB6:2          | +24V | TB7. Var noggrann i uppbyggnaden      |
| TB7:1          | L    | av linjenätet så att spänningsfall    |
| TB7:2          | L+   | och linjeresistans ej blir för stort. |
|                |      |                                       |

Spänningen vid sista apparat skall vara lägst 20V och linjeresistansen skall ej överstiga 24Ohm enkel väg.

Kabelkrav: Partvinnad och oskärmad, t.ex. ELLXB. Förlägg 24V, Gnd i ett par och L-, L+ i ett annat par. Tänk på att säkringen för svarsapparatsslingan klarar maximalt 130 apparater. Vid större nät måste således 24V-matningen till apparaterna eller en del av apparaterna tas någon annanstans. Här går det också bra att ansluta till grundkortets spänningsutgång: G-TB2 som klarar ytterligare 130 apparater.

 **KDHFKCHSDKHFCKJ HFKCHSDKHFCKJ**

![](_page_21_Picture_2.jpeg)

Vid behov kan två centralenheter vara kopplade till samma svarsapparatsslinga. Gör i så fall följande:

- -Ändra switch "LGH parallell" till "Yes" på båda centra lerna.
- -Ange i Multiaccess att de delar telefonlinje. (Ej = 0).

 -Anslut svarsapparatsslingan till en av centralerna men koppla ihop centralernas linjer samt jord. Dvs. L+, L- och Gnd på TB7:1,2 och TB6:1.

#### **Teleanslutning**

![](_page_21_Figure_8.jpeg)

Om porttelefoner anslutna till centralen skall ringa på det analoga telefonnätet eller till IP-telefoner via ATA-box så skall den analoga **Scala 1:1 Kontaktperson Marianne Hauger**

telelinjen anslutas till TB5.

Om det finns risk för åskurladdningar kan det vara klokt att komplettera med ett externt åskskydd. På kortet finns det överspänningsskydd mellan teleparet samt galvanisk isolering. Urladdningsskydd mot jord finns ej.

Om det finns möjlighet att få s.k. polvändning via det anslutna telefonnätet så är detta en fördel:

- -Porttelefonen kopplar ner direkt när den uppringde lägger på.
- -Det är möjligt att spela upp en melodislinga vid uppringning från porten så att den uppringda förstår att det är porttelefonen som ringt. Om funktionen önskas måste detta ställas in på centralen hetsbilden i Multiaccess.

#### **INSTÄLLNINGAR**

#### **12 Volt eller 24 Volt**

Med byglarna JP1 till JP4 kan utmatad spänning ställas om från 12V till 24V individuellt per port. **Obs!** Innan detta görs måste det säkerställas att alla enheter som anluts till aktuell port är avsedda för 24V matning. 24V kan dock endast matas ut om centralen matas med 24V.

Observera att porttelefonerna Ringa 1307, Ringa 1507, Ringa 1707 och Ringa 2707 **inte** klarar att matas med 24V. Detta kan dock lösas att använda en dörrenhet och koppla porttelefonen på dörrenhetens sekundärsida.

#### **LYSDIODER**

| D14 - D17 | Status port1 - | Släckt: Normaldrift                    |
|-----------|----------------|----------------------------------------|
|           | port4          | Röd dubbelblink: Spänningsfel.         |
|           |                | Röd enkelblink: Kommunikationsfel.     |
|           |                | Alla blinkar rött: Kortet uppgraderas. |
| D18       | Data tas emot  | Blinkar gult                           |
| D19       | Data sänds     | Blinkar rött                           |

#### **SWITCHAR**

| SW1:1-2 On, On |                                | Port 1 terminerad.       |
|----------------|--------------------------------|--------------------------|
| SW1:3-4 On, On |                                | Port 2 terminerad.       |
| SW1:5-6 On, On |                                | Port 3 terminerad.       |
| SW1:7-8 On, On | Aptus Logga_Silver pantone 877 | Port 4 terminerad.       |
| SW2:1,2 No, No |                                | Ingen parallellkoppling. |
|                | Yes, Yes                       | Två centraler paralellt  |
|                |                                |                          |

### **23**4

### **STYRA PORTTELEFONKORT 4800**

#### **ALLMÄNT**

Kort med fyra Apus485-portar för inkoppling av externa Aptus485 enheter. Dessutom innehåller kortet porttelefoninterface för dörr 5 - dörr 8.

#### **TEKNISKA DATA**

| Strömförsörjning: | 24 V DC (21,6 - 27,6).                           |
|-------------------|--------------------------------------------------|
|                   | Max 15mA, Min 10mA vid 24V.                      |
|                   | Direktmatning internt i centralenheten.          |
| Avsäkrade         | 4, med repeater och säkring.                     |
| Aptus485-bussar:  | Skydd: Elektronisk säkring 2,5A.                 |
|                   | Statusindikering via lysdiod.                    |
| Porttelefoner     | 4, porttelefon av typ Ringa för dörr 5 - dörr 8. |
| Svarsapparater:   | Ansluts till Styra Porttelefonkort 4400.         |
| Anslutning TELE:  | Ansluts till Styra Porttelefonkort 4400.         |
| Miljökrav:        | 0 till 40 grader Celsius.                        |
|                   | 0 - 90 % luftfuktighet.                          |
| Mått:             | 65x98x26                                         |
| Vikt:             | 0,10Kg                                           |

#### **MONTERING**

Kortet skall monteras med spänning avslagen. Kan endast monteras på kortplats 2, EXP2. Trä på kortet på därför avsedd stiftlist, G-J4. När kortet är på plats skall det fästas med de fyra bilagda skruvarna.

#### **INKOPPLING**

Anslut produkter avsedda för Aptus485 buss till valfri anslutning, TB1 - TB4. Om porttelefon skall anslutas skall också ljudbuss anslutas på TB11 - TB14. Observera att porttelefoner **måste** anslutas till exakt den port som motsvarar dörren den skall betjäna. Anslut således porttelefon för dörr 5 till TB1 och TB11. Dörr 6 - Dörr 8 ansluts på samma sätt till TB2 - TB4 respektive TB12 - TB14.

![](_page_22_Figure_12.jpeg)

Använd partvinnad kabel t.ex. av typ ELLXB eller ELAQBY. Använd gärna Aptuskabel 2 som innehåller tre tvinnade par där det ena är av grövre area för spänningsmatningsparet.

**031 68 97 11**

Aptuskabel 2 har samma färgmärkning som plintarna på kortets A485-portar, varför det är enkelt att veta vilken anslutning som skall in i vilken plint. **Scala 1:1 Kontaktperson Marianne Hauger**

#### **Separera dörrar**

En god strategi, och för Ringa nödvändig, är att vika en Aptus485 port per dörr. Anslut då all utrustning som skall betjäna dörr 5 till kortets TB1. Detta ger ett antal fördelar, nämligen:

- -Varje dörr blir individuellt avsäkrad.
**NCBKDHFKCHSDKHFCKJ**

- -Vid service kan spänningsmatning till enskild dörr kopplas bort via Multiaccess.
- -Vid reperation kan automatiskt utbyte av Aptus485-enheter tilläm pas. Innebär att centralen automatiskt kan ge funktion åt en utby tesenhet.
- -Vid installation kan funktionen automatisk dörrtillhörighet använ das. Funktionen väljs i samband med hårdvaruhämtning i Multiaccess och knyter enhets resurser till dörr enligt den port på kommunikationskortet som den är kopplad till.

![](_page_22_Figure_21.jpeg)

![](_page_23_Picture_1.jpeg)

### **KABELREDA 24**4

#### **ALLMÄNT**

**CHSDKHFCKJ**

I Styra 3000 med plastkapsling är en kabelreda integrerad. Tillbehöret, Styra kabelreda, behövs därför inte till Styra 3000 med plastkapsling.

#### **ANVÄNDNING AV KABELREDAN**

Dra in inkommande kablage en bit för långt, avmantla och backa sedan kabeln tills manteln är i höjd med dragavlastningsöglan alldeles innanför kabelgenomföringen. Dra fast med buntband.

Dra den avmantlade kabeln fram till tänkt anslutningspunkt. Fäst upp kabeln med buntband i därför avsedda fästen.**KDHFK-Scala 1:1 Kontaktperson Marianne Hauger**

![](_page_23_Figure_8.jpeg)

**Aptus Logga_Silver pantone 877**

### **25**4

### **DRIFTSÄTTNING & PROGRAMMERING**

#### **DRIFTSÄTTNINGSINSTRUKTION**

När Styra 3000 och dess kringutrustning är installerad återstår driftsättning och avtestning av installationen. Till din hjälp finns programmeringsblanketter, sista sidan i detta dokument.

**Plats:** Skriv på blanketten lämplig identifikation på din Styra 3000 central, t.ex. installationsplats.

**Master/Slav:** Anteckna om centralen skall vara en master eller slav. **Etikett:** På Baskortet finns 2 etiketter med samma information.

Lossa den som sitter ovanpå IP-jacket och sätt denna på blanketten. Etiketten innehåller serienummer, (kryptonyckel) samt MAC-adress. **IP Adress:** Om det är bestämt vilken IP-Adress centralenheten skall ha, så anteckna den på blanketten.

**Telefonnummer:** Om centralen har uppringd modemkommunikation, anteckna telefonnumret till centralen.

**In och utgångar:** Anteckna vad respektive in- och utgång är ansluten till.

**Enheter:** Det finns 24 rader avsatta till anslutna enheter. För var och en av dessa skall det framgå:

Monteringsplats,

Aptus485-port, (0 - 8)

 Serienummeretikett, löstagbar etikett på respektive enhet. De två första raderna används till eventuella expansionskort om sådana finns. Dessa är anslutna på Aptus485-port 0.

På programmeringsblankettens andra sida finns fria rader där de olika enheternas in och utgångar kan dokumenteras. Om antalet in & utgångar är för stort för att rymmas på en blankett kan ni ta ut ytterligare.

#### **ENHETER FÖR STYRA 3000**

Nedan följer en översikt på vilka olika typer av Aptus485-enheter som kan vara aktuella att dokumentera på programmeringsblanketten.

**Styra I/O 4400:** Flytta lösttagbara etiketten till blanketten. **Ingång 1 - 4:** Skriv vid respektive ingång vad den kopplats till. **Utgång 1 - 4:** Skriv vid respektive relä vad det kopplats till.

**Styra I/O 8800:** Flytta lösttagbara etiketten till blanketten. **Ingång 1 - 8:** Skriv vid respektive ingång vad den kopplats till. **Utgång 1 - 8:** Skriv vid respektive relä vad det kopplats till.

**Styra Komkort 4000:** Flytta lösttagbara etiketten till blanketten.

**Styra Porttelefonkort 4400:** Flytta lösttagbara etiketten till blanketten. Kortet kan endast sitta på Expansionsplats 1.

**Styra Porttelefonkort 4800:** Flytta lösttagbara etiketten till blanketten. Kortet kan endast sitta på Expansionsplats 2.

**Koppla 2100:** Flytta lösttagbara etiketten till blanketten. **Ingång 1 - 2:** Skriv vid respektive ingång vad den kopplats till. **Utgång 1:** Skriv vid respektive relä vad det kopplats till. **Aptus Logga_Silver pantone 877**

**Koppla 4300:** Flytta lösttagbara etiketten till blanketten. **Ingång 1 - 4:** Skriv vid respektive ingång vad den kopplats till. **Utgång 1 - 3:** Skriv vid respektive relä vad det kopplats till. **Scala 1:1 Kontaktperson Marianne Hauger**

> **Koppla 0010:** Flytta lösttagbara etiketten till blanketten. **Doormanpos. 1 - 8:** Skriv vilket lås som parats med respektive position. Obs! Låset identifieras via radiomodulen vars löstagbara etikett sitter på insidan av batteriluckan.

> **Koppla 0020:** Flytta lösttagbara etiketten till blanketten. **Aperiopos. 1 - 8:** Skriv vilket lås som parats med respektive position. Parningen görs med Aperio Programming Application PAP.

**MC1-I/O:** Flytta löstagbara etiketten till blanketten. **Ingång 1 - 8:** Skriv vid respektive ingång vad den kopplats till. **Utgång 1 - 2:** Skriv vid respektive relä vad det kopplats till. **1wire 1 - 8:** Skriv var respektive temperaturgivare sitter.

**MC1-MBUS:** Flytta löstagbara etiketten till blanketten. **MBusmätare:** Skriv vilka MBusmätare som finns anslutna.

**AXI2O16:** Flytta löstagbara etiketten till blanketten. **Ingång 1 - 2:** Skriv vid respektive ingång vad den kopplats till. **Utgång 1 - 16:** Skriv vid respektive relä vad det kopplats till.

**Läsare n:** Flytta den löstagbara etiketten till blanketten.

**Porttelefon n:** Flytta den löstagbara etiketten på blanketten.

**Bokningstavla n:** Flytta den löstagbara etiketten på blanketten.

**AA TMI-A485 n:** Flytta den löstagbara etiketten på blanketten. **Maskinstyrning 1 - 8**: Notera aktuell Dip-adress samt fabrikat.

**Låsmotor n:** Flytta den löstagbara etiketten på blanketten..

**Låsa:** Flytta den löstagbara etiketten på blanketten.

**Namnskylt:** Flytta lösttagbara etiketten till blanketten.

![](_page_25_Picture_1.jpeg)

### **26**4

#### **PROGRAMMERING**

För att Styra 3000 skall fungera måste den ha blivit programmerad. Programmeringen görs från PC-programmet Multiaccess Styra. Obs! Du behöver uppgifterna du fyllt i på blanketten när du gör programmeringen. **Aptus Logga_Silver pantone 877**

Den central som skall fungera som master i systemet måste ges den konfigurationen. Använd programvaran Konfigurera för att göra inställningen. Konfigurera finns med på installationsskivan för mjukvarorna.

Om din centralenhet kommuniceras över nätverk måste den få en IPadress. Den kan få denna automatiskt om ditt nätverk har en DHCPserver, i annat fall skall du sätta en fast IP-adress med Konfigurera. Multiaccess Styra skall minst vara av version 8.0.0 för att fungera med Styra 3000 version C0. **Scala 1:1 Kontaktperson Marianne Hauger**

#### **GARANTI**

APTUS Elektronik AB lämnar 2 års garanti på material och fabrikationsfel på samtliga produkter. Övrigt enligt leveransbestämmelser NL09.

#### **SERVICE**

För service hänvisar APTUS Elektronik AB till ansvarig återförsäljare som utöver egen kompetens har kontinuerlig kontakt med APTUS Elektronik AB.

![](_page_26_Picture_1.jpeg)

# **27**4

### **APPENDIX: PROGRAMMERINGSBLANKETT**

### **Scala 1:1 Kontaktperson Marianne Hauger Aptus Logga_Silver pantone 877 Placering:** …………………………………………………………… *T.ex installatinsplats.*  Styra 3000 Serienummer *Plats för etikett med serienummer och MAC adress* MAC Adress IP Adress Telefon Nummer Ingång 1: Ingång 2: Utgång 1: Exp1/Enhet1 *Ange enhetens plats samt A485-port, 0 – 8, i centralen Plats för etikett med serienummer* Exp2/Enhet2 *Ange enhetens plats samt A485-port*, 0 – 8, *i centralen Plats för etikett med serienummer* Enhet 3 *Ange enhetens plats samt A485-port*, 0 – 8, *i centralen Plats för etikett med serienummer* Enhet 4 *Ange enhetens plats samt A485-port*, 0 – 8, *i centralen Plats för etikett med serienummer* Enhet 5 *Ange enhetens plats samt A485-port*, 0 – 8, *i centralen Plats för etikett med serienummer* Enhet 6 *Ange enhetens plats samt A485-port*, 0 – 8, *i centralen Plats för etikett med serienummer* Enhet 7 *Ange enhetens plats samt A485-port*, 0 – 8, *i centralen Plats för etikett med serienummer* Enhet 8 *Ange enhetens plats samt A485-port*, 0 – 8, *i centralen Plats för etikett med serienummer* Enhet 9 *Ange enhetens plats samt A485-port*, 0 – 8, *i centralen Plats för etikett med serienummer* Enhet 10 *Ange enhetens plats samt A485-port*, 0 – 8, *i centralen Plats för etikett med serienummer* Enhet 11 *Ange enhetens plats samt A485-port*, 0 – 8, *i centralen Plats för etikett med serienummer* Enhet 12 *Ange enhetens plats samt A485-port*, 0 – 8, *i centralen Plats för etikett med serienummer* Enhet 13 *Ange enhetens plats samt A485-port*, 0 – 8, *i centralen Plats för etikett med serienummer* Enhet 14 *Ange enhetens plats samt A485-port*, 0 – 8, *i centralen Plats för etikett med serienummer* Enhet 15 *Ange enhetens plats samt A485-port*, 0 – 8, *i centralen Plats för etikett med serienummer* Enhet 16 *Ange enhetens plats samt A485-port*, 0 – 8, *i centralen Plats för etikett med serienummer* Enhet 17 *Ange enhetens plats samt A485-port*, 0 – 8, *i centralen Plats för etikett med serienummer* Enhet 18 *Ange enhetens plats samt A485-port*, 0 – 8, *i centralen Plats för etikett med serienummer* Enhet 19 *Ange enhetens plats samt A485-port*, 0 – 8, *i centralen Plats för etikett med serienummer* Enhet 20 *Ange enhetens plats samt A485-port*, 0 – 8, *i centralen Plats för etikett med serienummer* Enhet 21 *Ange enhetens plats samt A485-port*, 0 – 8, *i centralen Plats för etikett med serienummer* Enhet 22 *Ange enhetens plats samt A485-port*, 0 – 8, *i centralen Plats för etikett med serienummer* Enhet 23 *Ange enhetens plats samt A485-port*, 0 – 8, *i centralen Plats för etikett med serienummer* Enhet 24 *Ange enhetens plats samt A485-port*, 0 – 8, *i centralen Plats för etikett med serienummer*  Master Slav

![](_page_27_Picture_2.jpeg)

### **Tilläggsblankett för in och utgångar på anslutna enheter**

| Enhet nr | Ange ingång / utgång nr | Ange vad som kopplats in       |
|----------|-------------------------|--------------------------------|
|          |                         |                                |
|          |                         |                                |
|          |                         |                                |
|          |                         | Aptus Logga_Silver pantone 877 |
|          |                         |                                |
|          |                         |                                |
|          |                         | Scala 1:1                      |
|          |                         |                                |
|          |                         |                                |
|          |                         |                                |
|          |                         |                                |
|          |                         |                                |
|          |                         |                                |
|          |                         |                                |
|          |                         |                                |
|          |                         |                                |
|          |                         |                                |
|          |                         |                                |
|          |                         |                                |
|          |                         |                                |
|          |                         |                                |
|          |                         |                                |
|          |                         |                                |
|          |                         |                                |
|          |                         |                                |
|          |                         |                                |
|          |                         |                                |
|          |                         |                                |
|          |                         |                                |