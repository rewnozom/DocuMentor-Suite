# **RINGA 1707**

#### **INSTALLATIONSANVISNING**

**Revision 10**

# **INSTALLATION 2**

#### **ALLMÄNT**

Ringa 1707 är en kombinerad porttelefon och läsare med knappsats. Den är utrustad med display som visar namn på de boende. Påringning sker genom att navigera till den boende via display och navigeringsknappar. Ringa 1707 ansluts till centralenhet TC 700 via Aptus485-buss.

![](_page_1_Figure_5.jpeg)

#### **TEKNISKA DATA**

|                 | Strömförsörjning: 12 V DC reglerad (10.5 - 14).    |  |
|-----------------|----------------------------------------------------|--|
|                 | Max 525mA                                          |  |
|                 | Min 200mA                                          |  |
|                 | Matning från centralenheten.                       |  |
| Ingångar:       | 2 för att utifrån kunna styra en i läsaren inbyggd |  |
|                 | LED.                                               |  |
| Utgångar:       | 1 för styrning av extern summer.                   |  |
|                 | (12V, max 0.5A)                                    |  |
|                 | 1 för Sabotagebrytare.                             |  |
| Miljökrav:      | -20 till +60 grader Celcius                        |  |
|                 | 10 till 100% luftfuktighet                         |  |
| Mått:           | 116x285x23 mm                                      |  |
| Vikt:           | 1.0kg                                              |  |
| Monteringshöjd: | 1363.5mm (mittpunkt)<br>1310mm (kabelintag)        |  |

#### **PACKLISTA**

- 1 st Porttelefon, Ringa 1707
- 4 st skruv och plugg
- 1 st Installationsanvisning (denna)

#### **SYSTEMBESKRIVNING**

![](_page_1_Figure_13.jpeg)

**MONTERING** Fäst bakstycket med bilagda skruvar. Dra fram kablage och anslut till porttelefonens J2 och läsarens J1. Haka sedan på fronten i övre ändan och för in nederdelen. Fäst med tillhörande skruvar i underkant. Obs! Specialverktyg behövs för dessa skruvar. (Finns hos Aptus). Hålbild för bakstycke framgår av bilden intill.

![](_page_1_Figure_15.jpeg)

#### **INKOPPLINGSANVISNING**

Använd partvinnad kabel t.ex. av typ ELLXB eller ELAQBY för anslutning till centralenhet. Förlägg ett par till 485 (A+B), ett par till spänning(12V+GND) och ett par till Linje(L1+L2). Dubblera vid behov paren för att få rätt area.

Kabelns area måste anpassas efter last och avstånd. Upp till 40m bör 0.5mm2 användas för spänningsmatningen. Avstånd på 40 - 100m -> 1.0mm2.

![](_page_2_Picture_1.jpeg)

# **3**

![](_page_2_Figure_3.jpeg)

![](_page_2_Figure_4.jpeg)

J2 är en skruvplint som jackas direkt på kretskortskanten. Lossa J2 och vänd på den. Kablarna skall anslutas enligt tabellen nedan.

| B                                          | Förbind med J2:1 på TC 700 485PT-interface |  |
|--------------------------------------------|--------------------------------------------|--|
| A                                          | Förbind med J2:2 på TC 700 485PT-interface |  |
| GND                                        | Förbind med J2:3 på TC 700 485PT-interface |  |
| 12V                                        | Förbind med J2:4 på TC 700 485PT-interface |  |
| L1                                         | Anslutning utifrån dörrtillhörighet:       |  |
|                                            | Dörr 3: förbind med J7:1 (L1:1 485PT)      |  |
|                                            | Dörr 4: förbind med J8:1 (L1:2 485PT)      |  |
| L2<br>Anslutning utifrån dörrtillhörighet: |                                            |  |
|                                            | Dörr 3: förbind med J7:2 (L2:1 485PT)      |  |
|                                            | Dörr 4: förbind med J8:2 (L2:2 485PT)      |  |
|                                            |                                            |  |

Skruvplinten J4 sitter precis som J2 jackad direkt på kortkanten. Lossa och vänd innan anslutning. Anslut enligt tabellen nedan. Vid

![](_page_2_Figure_8.jpeg)

![](_page_2_Figure_9.jpeg)

extern 12V-summer ansluts J4:1 till externa summerns Gnd. Anslut 12V: J2:4 till summerns spänningsmatning.

Porttelefonens sabotagebrytare, S14, finns tillgänglig på J4:3,4. Normalt sluten. Kontrollera att fjädern till sabotagebrytaren når underlaget så att slutning verkligen sker.

styrning av

![](_page_2_Figure_12.jpeg)

#### **CENTRALINTERFACE**

För att kunna ansluta Ringa 1707 måste din TC 700 vara utrustad med ett 485PT-interface ver-

sion E eller senare. Uppstår ett klickande vid uppkoppling av externsamtal,(Tele J4)? Uppgradera i så fall 485PT-interface till version J från serienummer 90800001. Dessa började levereras 20090218.

J2 Aptus485-buss

här.

apparater.

S1 Terminering av Aptus485-buss.

AT70 Dörr 3 & 4

![](_page_2_Figure_16.jpeg)

# **4**

#### **LYSDIODER**

Porttelefonkortet har en grön spänningsindikeringsled, endast synlig när enheten är öppnad. Läsaren har flerfärgsledar som sitter så att de tillsammans bildar ett nyckelhål. De styrs av läsaren och kan blinka eller lysa i färgerna rött, grönt och gult, beroende på läsares status.

Lysdioderna för undre delen av nyckelhålet kan reserveras för extern styrning via J2:3,4,5.

En bakgrundsbelysning ger en vit upplyst linje runt hela nyckelhålet samt belysning i knappsatsen.

#### **SUMMER**

Ringa 1707 är utrustad med intern summerfunktion. Denna kan t.ex. ljuda vid "Dörr öppen för länge". Funktionen för summern konfigureras i Multiaccess.

#### **INSTÄLLNINGAR**

För att komma åt de inställningar som kan göras på baksidan av Ringa måste strilskydden lossas.

#### **Läsardel**

| S1:1-2 | Externstyrning<br>av läsares lys<br>diod, undre<br>delen av nyck<br>elhål. | ON,ON<br>=> Hela nyckelhålet används av<br>läsaren.<br>OFF,OFF => Undre delen kan externsty<br>ras via J2:3,4,5.<br>Vid leverans: ON,ON.                                                  |
|--------|----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| S1:3-4 | Terminering                                                                | ON, ON => Terminering inkopplad.<br>Endast ändpunkterna av bussen skall<br>termineras.<br>OFF,OFF => Ej terminerad.<br>Vid leverans: OFF, OFF.<br>Obs! terminera endast på läsarens kort. |

#### **Telefondel**

| S1:1-2 | Terminering           | OFF, OFF => Skall ej termineras.                                                       |
|--------|-----------------------|----------------------------------------------------------------------------------------|
| S1:3   | Inställningsme<br>ny. | ON => Meny för inställning av volym och<br>kontrast är aktiverad.<br>OFF vid leverans. |
| S1:4   | Reserverad            | OFF vid leverans.                                                                      |

#### **SYSTEMKRAV**

MultiAccess från version 7.3. TC 700 från version R0.

#### **PROGRAMMERING**

När Ringa 1707 är inkopplad kan du få in den i MultiAccess genom att hämta hårdvara. Två nya enheter skall komma upp: "Ringa" och "Öppna". Under "Ringa" finns resursen "Porttelefondisplay" och

under "Öppna" finns resurserna "Beröringsfri läsare" och "Tangentbord".

På "**Porttelefondisplay**" gör du inställningar för hur namn på de boende skall presenteras.

-Du måste knyta denna till dörr 3 eller 4. Sätt funktionen till "Används" annars fungerar inte displayen.

-Välkomstmeddelande: Skriv in den text som skall visas på porttelefonens startsida. Anges inget kommer det att stå "Porttelefon".

-Visa startsida: Det är nu valbart om startsidan skall visas. Om start sida inte visas lägenhetsregistret direkt. Funktionen kräver

Multiaccess 7.15.3 // 7.16.1 eller nyare samt Ringa version C0.

-Välj namnordning, dvs om förnamn eller efternam skall vara först. -Välj visningssätt, alfabetisk eller lägenhetsordning. Alfabetisk innebär att listan sorteras på efternamn och lägenhetsordning att listan

sorteras efter lägenhetsnummer. På "**Beröringsfri läsare**" gör du inställning för läsares dörrtillhörighet

och eventuellt kryssar i att den är modifierad. Troligtvis vill du knyta den till samma dörr som porttelefonen i övrigt, men det går att knyta den till annan dörr om så önskas. Sätt funktionen till "Används".

På "**Knappsats**" sätter du funktionen till "Används". Knappsatsen får automatiskt samma dörrtillhörighet som läsaren.

Efter att du är färdig med inställningar för de nya resurserna avslutar du programmeringen med att sända data.

#### **INSTÄLLNING AV LJUD & KONTRAST**

Vid driftsättning skall en justering av ljudets volym samt displayens kontrast utföras. Volym och kontrast ställs till ett värde mellan 0 - 9. Inställningen görs ute vid Ringa via en inställningsmeny.

1. Ställ S1:3 på telefondel till ON. Detta kan göras med spänning påslagen.

Återmontera Ringa i sitt bakstycke. I displayen visas nu menyvalen "LCD Kontrast", "Volym", "Info" och "Ring upp". För att menyn "Ring upp" skall visas måste programmeringen i MultiAccess vara klar.

- 2. Gå in på menyn för LCD Kontrast. Öka eller minska genom att trycka på "+" eller "-". I displayen visas också gällande värde, 0-9. Avsluta med knapp:
- 3. Volymen kan ställas in antingen med samtal uppkopplat eller direkt. Om du inte på förhand vet vilken volymnivå som är lämplig är rekommendationen att göra justeringen med samtal uppkopplat. Gå in på menyn för Ring upp. Gör en uppringning till lämplig telefon eller svarsapparat. Välj Volym. Öka volymen med "+", minska med "-". När du är nöjd avsluta genom att trycka två gånger. Tänk på att uppkopplat samtal kopplas ner efter den i MultiAccess angivna samtalstiden.
- 4. Lossa Ringa, ställ S1:3 till OFF. Återmontera enheten.

![](_page_4_Picture_1.jpeg)

# **5**

#### **AVPROVNING**

Kontrollera en extra gång att alla signalledare är rätt inkopplade innan anläggningen spänningssätts. När spänningen slås på skall displayen tändas upp. Efter att programmering gjorts i Multiaccess skall du gå ut och kontrollera att förväntad information visar sig på displayen, att du kan ringa, läsa en nyckelbricka respektive slå en kod. Om du vid uppringningsförsök får upp texten "PhoneLine Error" skall kablage mellan interfacekort i central och J2:5,6 i Ringa 1707 kontrolleras. Kontrollera också att interfacekortets JP1 och JP2 står i rätt läge.

#### **GARANTI**

Aptus Elektronik AB lämnar två års garanti på material och fabrikationsfel på samtliga produkter. Övrigt enligt leveransbestämmelser NL01.

#### **SERVICE**

För service hänvisar APTUS Elektronik AB till ansvarig återförsäljare som utöver egen kompetens har kontinuerlig kontakt med APTUS Elektronik AB.**NCBKDHFKCHSDKHFCKJ**