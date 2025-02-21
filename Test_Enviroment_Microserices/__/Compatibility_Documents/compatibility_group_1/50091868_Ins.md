![](_page_0_Picture_0.jpeg)

# **RINGA 1307**

#### **INSTALLATIONSANVISNING**

**Revision 7**

![](_page_1_Picture_1.jpeg)

# **INSTALLATION 2**

#### **ALLMÄNT**

Ringa 1307 är en kombinerad porttelefon och läsare. Den är utrustad med display som visar namn på de boende. Påringning sker genom att navigera till den boende via display och navigeringsknappar. Ringa 1307 ansluts till centralenhet TC 700 via Aptus485-buss.

![](_page_1_Figure_5.jpeg)

#### **TEKNISKA DATA**

|                 | Strömförsörjning: 12 V DC reglerad (10.5 - 14). |  |  |
|-----------------|-------------------------------------------------|--|--|
|                 | Max 400mA                                       |  |  |
|                 | Min 170mA                                       |  |  |
|                 | Matning från centralenheten.                    |  |  |
| Utgångar:       | 1 för styrning av extern summer.                |  |  |
|                 | (12V, max 0.5A)                                 |  |  |
|                 | 1 för Sabotagebrytare.                          |  |  |
| Miljökrav:      | -20 till +60 grader Celcius                     |  |  |
|                 | 10 till 100% luftfuktighet                      |  |  |
| Mått:           | 116x185x23 mm                                   |  |  |
| Vikt:           | 0.7kg                                           |  |  |
| Monteringshöjd: | 1412,5 (mittpunkt)                              |  |  |
|                 | 1336,5 (kabelintag)                             |  |  |

#### **PACKLISTA**

- 1 st Porttelefon, Ringa 1307
- 4 st skruv och plugg
- 1 st Installationsanvisning (denna)

#### **SYSTEMBESKRIVNING**

![](_page_1_Figure_13.jpeg)

#### **MONTERING**

Fäst bakstycket med bilagda skruvar. Dra fram kablage och anslut till J2 och eventuellt J4.

Haka på fronten i övre ändan och för in nederdelen. Fäst med tillhörande skruvar i underkant.

Obs! Specialverktyg behövs för dessa skruvar. (Finns hos Aptus). Hålbild för bakstycket framgår av vidstående ritning.

![](_page_1_Figure_18.jpeg)

#### **INKOPPLINGSANVISNING**

Använd partvinnad kabel t.ex. av typ ELLXB eller ELAQBY för anslutning till centralenhet.

Förlägg ett par till 485 (A+B), ett par till spänning(12V+GND) och ett par till Linje(L1+L2). Dubblera vid behov paren för att få rätt area.

Kabelns area måste anpassas efter last och avstånd. Upp till 40m bör 0.5mm2 användas för spänningsmatningen. Avstånd på 40 - 100m -> 1.0mm2.

![](_page_2_Picture_1.jpeg)

## **3**

![](_page_2_Figure_3.jpeg)

J2 är en skruvplint som jackas direkt på kretskortskanten. Lossa J2 och vänd på den. Kablarna skall anslutas enligt tabellen nedan.

![](_page_2_Figure_5.jpeg)

| J2:1 | B   | Förbind med J2:1 på TC 700 485PT-interface                                                                             |  |
|------|-----|------------------------------------------------------------------------------------------------------------------------|--|
| J2:2 | A   | Förbind med J2:2 på TC 700 485PT-interface                                                                             |  |
| J2:3 | GND | Förbind med J2:3 på TC 700 485PT-interface                                                                             |  |
| J2:4 | 12V | Förbind med J2:4 på TC 700 485PT-interface                                                                             |  |
| J2:5 | L1  | Anslutning utifrån dörrtillhörighet:<br>Dörr 3: förbind med J7:1 (L1:1 485PT)<br>Dörr 4: förbind med J8:1 (L1:2 485PT) |  |
| J2:6 | L2  | Anslutning utifrån dörrtillhörighet:<br>Dörr 3: förbind med J7:2 (L2:1 485PT)<br>Dörr 4: förbind med J8:2 (L2:2 485PT) |  |

Skruvplinten J4 sitter precis som J2 jackad direkt på kortkanten. Lossa och vänd innan anslutning. Anslut enligt tabellen nedan. Vid styrning av extern 12V-summer ansluts J4:1

![](_page_2_Picture_8.jpeg)

![](_page_2_Figure_9.jpeg)

Porttelefonens sabotagebrytare, S14, finns tillgänglig på J4:3,4. Normalt sluten.

#### **CENTRALINTERFACE**

För att kunna ansluta Ringa 1307 måste din TC 700 vara utrustad med ett 485PT-interface ver-

| sion E eller senare.                                         |                    |
|--------------------------------------------------------------|--------------------|
| Uppstår ett klickande vid<br>ON<br>1<br>ON<br>1              |                    |
| uppkoppling av externsam<br>S1                               |                    |
| tal,(Tele J4)? Uppgradera i<br>Ringa Dörr 3                  | 485                |
| så fall 485PT-interface till<br>Ringa Dörr 4                 | från A<br>PT-      |
| version J från serienummer                                   | E-70<br>inte       |
| 90800001. Dessa började<br>AT X0 Dörr 3                      | 1081<br>rfac<br>-J |
| levereras 20090218.<br>AT X0 Dörr 4                          | e                  |
| Aptus485-buss                                                |                    |
| Anslutning Ringa Dörr 3                                      |                    |
| 24VDC +<br>Anslutning Ringa Dörr 4                           |                    |
| Anslutning AT10, AT 30,                                      |                    |
| AT70 Dörr 3 & 4<br>Line -                                    |                    |
| 24V matning till interfa<br>Tele                             |                    |
| cekortet. Ansluts till                                       |                    |
| centralens matning.                                          |                    |
| Svarsapparater ansluts<br>JP1 Styr om en Ringa eller en ATX0 |                    |
| ansluts till dörr 3.                                         |                    |
| Linjeanslutning, svars<br>Vänster (J7): Ringa                |                    |
| apparater.<br>Höger (J3): AT X0                              |                    |
| Linjeanslutning, tele.<br>JP2 Styr om en Ringa eller en ATX0 |                    |
| Terminering av<br>ansluts till dörr 4.                       |                    |
| Aptus485-buss.<br>Vänster (J8): Ringa                        |                    |
| Höger (J3): AT X0                                            |                    |
| -<br>Line +<br>Tele                                          |                    |

#### **LYSDIODER**

Porttelefonkortet har en grön spänningsindikeringsled, LED Power. Denna syns endast när enheten är isärskruvad.

#### **SUMMER**

Ringa 1307 är utrustad med intern summerfunktion. Denna kan t.ex. ljuda vid "Dörr öppen för länge". Funktionen för summern konfigureras i Multiaccess.

## **4**

#### **INSTÄLLNINGAR**

För att komma åt de inställningar som kan göras på baksidan av Ringas kretskort måste strilskyddet lossas.

| S1:1-2 | Terminering | ON, ON => Terminering inkopplad.<br>Endast ändpunkterna av bussen skall ter |
|--------|-------------|-----------------------------------------------------------------------------|
|        |             | mineras.                                                                    |
|        |             | Porttelefonen levereras oterminerad.                                        |
| S1:3   |             | Inställningsmeny ON => Meny för inställning av volym och                    |
|        |             | kontrast är aktiverad.                                                      |
|        |             | OFF vid leverans.                                                           |
| S1:4   | Reserverad  | OFF vid leverans.                                                           |

#### **SYSTEMKRAV**

MultiAccess från version 7.3. TC 700 från version R0.

#### **PROGRAMMERING**

När Ringa 1307 är inkopplad kan du få in den i MultiAccess genom att hämta hårdvara. En ny enhet med namnet "Ringa" skall komma upp. Under denna finns resurserna "Porttelefondisplay" och "Beröringsfri läsare".

På "**Porttelefondisplay**" gör du inställningar för hur namn på de boende skall presenteras.

-Du måste knyta denna till dörr 3 eller 4. Sätt funktionen till "Används" annars fungerar vare sig display eller läsare.

-Välkomstmeddelande: Skriv in den text som skall visas på porttelefonens startsida. Anges inget kommer det att stå "Porttelefon".

-Visa startsida: Det är nu valbart om startsidan skall visas. Om startsida inte visas så visas lägenhetsregistret direkt. Funktionen kräver Multiaccess 7.15.3 // 7.16.1 eller nyare samt Ringa version C0.

-Välj namnordning, dvs om förnamn eller efternamn skall vara först. -Välj visningssätt, alfabetisk eller lägenhetsordning. Alfabetisk innebär att listan sorteras efter lägenhetsnummer.

På "**Beröringsfri läsare**" gör du inställning för läsares dörrtillhörighet och eventuellt kryssar i att den är modifierad. Troligtvis vill du knyta den till samma dörr som porttelefonen i övrigt, men det går att knyta den till annan dörr om så önskas. Sätt funktionen till "Används" om du vill utnyttja den inbyggda läsaren.

Efter att du är färdig med inställningar för de nya resurserna avslutar du programmeringen med att sända data.

#### **INSTÄLLNING AV LJUD & KONTRAST**

Vid driftsättning skall en justering av ljudets volym samt displayens kontrast utföras. Volym och kontrast ställs till ett värde mellan 0 - 9. Inställningen görs ute vid Ringa via en inställningsmeny.

1. Ställ S1:3 till ON. Detta kan göras med spänning påslagen. Återmontera Ringa i sitt bakstycke. I displayen visas nu menyvalen "LCD Kontrast", "Volym", "Info" och "Ring upp". För att menyn "Ring upp" skall visas måste programmeringen i MultiAccess vara klar.

- 2. Gå in på menyn för LCD Kontrast. Öka eller minska genom att trycka på "+" eller "-". I displayen visas också gällande värde, 0-9. Avsluta med "X".
- 3. Volymen kan ställas in antingen med samtal uppkopplat eller direkt. Om du inte på förhand vet vilken volymnivå som är lämplig är rekommendationen att göra justeringen med samtal uppkopplat. Gå in på menyn för Ring upp. Gör en uppringning till lämplig telefon eller svarsapparat. Välj Volym. Öka volymen med "+", minska med "-". När du är nöjd avsluta genom att trycka "X" två gånger. Tänk på att uppkopplat samtal kopplas ner efter den i MultiAccess angivna samtalstiden.
- 4. Lossa Ringa, ställ S1:3 till OFF. Återmontera enheten.

#### **AVPROVNING**

Kontrollera en extra gång att alla signalledare är rätt inkopplade innan anläggningen spänningssätts. När spänningen slås på skall displayen tändas upp. Efter att programmering gjorts i MultiAccess skall du gå ut och kontrollera att förväntad information visar sig på displayen, att du kan ringa respektive läsa en nyckelbricka. Om du vid uppringningsförsök får upp texten "PhoneLine Error" skall kablage mellan 485PT-interface i central och J2:5,6 i Ringa 1307 kontrolleras. Kontrollera också att JP1 och JP2 står i rätt läge.

#### **GARANTI**

**N**

Aptus Elektronik AB lämnar två års garanti på material och fabrikationsfel på samtliga produkter. Övrigt enligt leveransbestämmelser NL01.

#### **SERVICE**

För service hänvisar APTUS Elektronik AB till ansvarig återförsäljare som utöver egen kompetens har kontinuerlig kontakt med APTUS Elektronik AB. **NCBKDHFKCHSDKHFCKJ**