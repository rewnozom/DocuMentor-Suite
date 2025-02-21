![](_page_0_Picture_0.jpeg)

# **UC-50 Gen2 Snabbguide**

Anslutning och specifikationer för undercentralen UC-50 Gen2.

![](_page_0_Picture_4.jpeg)

Klikk for norsk [versjon!](https://www.rco.no/File/DownLoadFile?fileId=2daf481d-7a79-44d4-b427-58500cdcbd0c) [Suomeksi,](https://www.rcosecurity.fi/File/DownLoadFile?fileId=931a1ede-abbb-4475-95be-07266914ba7c) paina tästä!

RCO Security AB Box 3130 169 03 Solna

tel 08-546 560 00 info@rco.se

![](_page_0_Picture_8.jpeg)

### **Innehåll**

| Undercentral<br>UC-50<br>Gen2                                        | 3  |
|----------------------------------------------------------------------|----|
| Skillnader<br>mellan<br>UC-50<br>Gen2<br>och<br>tidigare<br>modellen | 3  |
| Anslutningsplintar,<br>byglar<br>och<br>DIP-omkopplare               | 5  |
| Jackbara<br>plintar<br>och<br>rekommenderad<br>kabelarea             | 8  |
| Montering<br>och<br>kabeldragning                                    | 9  |
| Funktioner<br>som<br>kan<br>utföras<br>direkt<br>på<br>UC            | 10 |
|                                                                      | 11 |
| Indikeringar                                                         |    |
| Uppgradera                                                           | 12 |
| Ytterligare<br>information                                           | 12 |

![](_page_1_Picture_2.jpeg)

### **Undercentral UC-50 Gen2**

UC-50 Gen2 är en undercentral för kontroll av upp till åtta enheter som tar en kortläsarplats. I ett integrerat larmsystem från RCO Security tjänstgör UC-50 Gen2 som larmcentral. Den motsvarar kraven i standarden SS-EN 50131-3, certifiering enligt SSF 1014-5.

Vid montering och kabeldragning, följ anvisningarna i avsnittet ["Montering](#page--1-0) och [kabeldragning"](#page--1-0) på sidan 9.

Rekommendation: Alla undercentraler i systemet bör ha samma version (helst senast möjliga version). Man bör konfigurera alla undercentraler samtidigt i ett system, inom en domän eller en anknytning.

För specifikationer se sidan [13.](#page--1-0)

### Skillnader mellan UC-50 Gen2 och tidigare modellen

UC-50 Gen2, med kretskort fr.o.m. revision K, är utformad för att möta uppdaterade krav gällande elsäkerhet och bl.a. försedd med säkring för matningen till underenheter på lokalbussen P2/5–6. Den är även uppdaterad med en ny kapsling.

Om larmklassningen ska gälla får endast nätverksmodul IP-50 Gen2 och larmöverföringsinterface LS-50 Gen3 monteras på UC-50 Gen2-kretskortet.

![](_page_2_Picture_9.jpeg)

Det är viktigt att systembussen på UC-50 Gen2 termineras korrekt. I annat fall fungerar inte enheten.

![](_page_2_Picture_11.jpeg)

### *Kompatibilitet*

| Fungerar<br>UC-50<br>Gen2<br>tillsammans<br>med<br>tidigare<br>modeller<br>i<br>samma<br>system<br>och<br>samma<br>anknytning? | Ja.<br>Se<br>dock<br>till<br>att<br>använda<br>senaste<br>mjukvaruversion<br>på<br>alla<br>undercentraler.                                                                                                                                              |
|--------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Går<br>det<br>bra<br>att<br>montera<br>tidigare<br>IP-50-<br>modeller<br>i<br>en<br>UC-50<br>Gen2?                             | Ja,<br>men<br>då<br>gäller<br>inte<br>larmklassningen.                                                                                                                                                                                                  |
| Går<br>det<br>bra<br>att<br>montera<br>IP-50<br>Gen2<br>i<br>den<br>tidigare<br>UC-50-modellen?                                | Ja,<br>men<br>då<br>gäller<br>inte<br>larmklassningen.                                                                                                                                                                                                  |
| Går<br>det<br>bra<br>att<br>montera<br>tidigare<br>LS-50-<br>modeller<br>i<br>en<br>UC-50<br>Gen2?                             | Nej.<br>I<br>en<br>UC-50<br>Gen2<br>kapsling<br>får<br>inte<br>tidigare<br>LS-50-modeller<br>plats.<br>Om<br>UC-50<br>Gen2-kretskortet<br>sitter<br>i<br>äldre<br>kapsling<br>kan<br>det<br>fungera,<br>men<br>då<br>gäller<br>inte<br>larmklassningen. |
| Går<br>det<br>bra<br>att<br>montera<br>LS-50<br>Gen3<br>i<br>den<br>tidigare<br>UC-50-modellen?                                | Ja,<br>men<br>då<br>gäller<br>inte<br>larmklassningen.                                                                                                                                                                                                  |

![](_page_3_Figure_3.jpeg)

Ritningen och beskrivningen avser undercentralens kretskort revision K.

![](_page_3_Picture_5.jpeg)

### Anslutningsplintar, byglar och DIP-omkopplare

Byglar och DIP-omkopplare som inte beskrivs nedan är fabriksinställda och ska inte ändras.

![](_page_4_Picture_3.jpeg)

UC-50 Gen2 har två rundade plintar. Tryck in en liten flatskruvmejsel i slitsen för att öppna fjäderanslutningen. Se [YouTube-video](https://youtu.be/qqqKl7iSni8).

| P1<br>VIBDET:<br>Sabotageavkänning |                          |                                                                                                                                                                                                       |  |
|------------------------------------|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| Stift                              | Beteckning               | Funktion                                                                                                                                                                                              |  |
| 3                                  | SAB IN                   | Generell<br>ingång<br>där<br>funktionen<br>anges<br>i<br>R-CARD M5.                                                                                                                                   |  |
| 4                                  |                          | Ingången<br>kan<br>inte<br>användas<br>om<br>vibrationsdetektor<br>CD<br>470<br>är<br>kopplad<br>till<br>P5.                                                                                          |  |
| P2                                 | LOCAL BUS:<br>Anslutning | av<br>underenheter                                                                                                                                                                                    |  |
| Stift                              | Beteckning               | Funktion                                                                                                                                                                                              |  |
| 5                                  | DC+<br>OUT               | Utgång<br>för<br>strömförsörjning<br>till<br>underenheter.<br>Strömmen<br>tas                                                                                                                         |  |
| 6                                  | DC-<br>OUT               | ifrån<br>DC IN P4<br>via<br>säkringen<br>FU1.<br>Säkringen<br>ska<br>vara<br>av<br>typen<br>T<br>6.3A<br>L<br>250 V.                                                                                  |  |
| 7                                  | RS485<br>A               | RS-485-kommunikation.<br>Använd<br>partvinnad<br>kabel.<br>Terminera<br>i                                                                                                                             |  |
| 8                                  | RS485<br>B               | första<br>och<br>sista<br>enheten<br>på<br>lokala<br>RS-485-bussen.                                                                                                                                   |  |
| P3<br>COMOUT:<br>CAN-buss          |                          |                                                                                                                                                                                                       |  |
| Stift                              | Beteckning               | Funktion                                                                                                                                                                                              |  |
| 9                                  | CAN<br>L                 | Kommunikation<br>med<br>andra<br>UC-50<br>Gen2-enheter.<br>Använd                                                                                                                                     |  |
| 10                                 | CAN H                    | partvinnad<br>kabel.<br>Anslut<br>CAN<br>L<br>och<br>CAN<br>H<br>till<br>motsvarande<br>plint<br>på<br>nästa<br>UC-50.<br>Terminera<br>i<br>första<br>och<br>sista<br>enheten<br>på<br>CAN<br>bussen. |  |
| P4:<br>IN:<br>Strömförsörjning     |                          |                                                                                                                                                                                                       |  |
| Stift                              | Beteckning               | Funktion                                                                                                                                                                                              |  |
| 13                                 | DC+<br>IN                | Matningsspänning<br>(se<br>specifikationer<br>på<br>sidan<br>13)<br>för                                                                                                                               |  |
| 14                                 | DC-<br>IN                | undercentralen<br>och<br>dess<br>underenheter.                                                                                                                                                        |  |

![](_page_4_Picture_6.jpeg)

| P5<br>VIBDET:<br>Anslutning<br>av<br>vibrationsdetektor<br>(LK4) |                        |                                                                                                |  |
|------------------------------------------------------------------|------------------------|------------------------------------------------------------------------------------------------|--|
| Stift                                                            | Beteckning             | Funktion                                                                                       |  |
| –                                                                | IN,<br>0V,<br>0V, +24V | Koppla<br>vibrationsdetektorn<br>till<br>P5<br>vid<br>montering<br>av<br>UC-50<br>Gen2<br>LK4. |  |

#### **P6**

Anslutning för övervakning av Milletekniks kraftenhet.

För utförlig information se manualen *R-CARD 5000 – Installera*. Manualer och övrig produktdokumentation finns i mappen **Document** på installations-mediet för R-CARD M5. Manualer kan även laddas ner från RCOs [webbplats,](https://www.rco.se/file/4508c5f4-58e5-4dcc-89a1-aa0e00ec92d8) under **Mediaarkivet** > **Manualer** (inloggning krävs). Manualen innehåller information om nätverksmodulen IP-50, larmöverföringsinterfacet LS-50, inkoppling på lokalbussen (med kopplingsexempel), bussterminering, kommunikation med Milletekniks kraftaggregat, tekniska specifikationer för hårdvara och kommunikation m.m.

#### **P13**

Ethernet anslutning via TCP/IP-modulen IP-50 Gen2. För utförlig information se manualen *R-CARD 5000 – Installera* (se ovan).

#### **P14: Larmöverföring via LS-50 Gen2**

Passar mot den 10-poliga hylskontakten på larmöverföringsinterfacet LS-50 Gen3. För utförlig information se manualen *R-CARD 5000 – Installera* (se ovan).

| P16:   | Potentialfri | utgång                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|--------|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Stift  | Beteckning   | Funktion                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 1<br>2 | ALARM        | Potentialfri<br>utgång<br>från<br>relä.<br>Kan<br>bland<br>annat<br>programmeras<br>för<br>någon<br>av<br>följande<br>funktioner<br>i<br>R-CARD M5:<br>Kommunikationsavbrott,<br>tamper,<br>sabotage,<br>dörr<br>uppbruten,<br>l<br>dörr<br>uppställd,<br>hotlarm<br>(överfallslarm<br>–<br>en<br>gruppkod<br>med<br>flagga<br>för<br>att<br>den<br>är<br>hotkod).<br>Växlar<br>när<br>UC-50<br>körs<br>korrekt<br>(fast<br>sluten<br>eller<br>bruten<br>vid<br>l<br>fel). |

![](_page_5_Picture_10.jpeg)

| Beteckning  | Funktion                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SW1         | Adressinställning.<br>Adress<br>1–255<br>kan<br>ställas<br>in.                                                                                                                                                                                                                                                                                                                                                                                                       |
|             | Omkopplarna<br>motsvarar<br>vardera<br>värdet<br>1-2-4-8-16-32-64-128,<br>skrivet<br>bredvid<br>respektive<br>omkopplare<br>i<br>omkopplarbanken.<br>När<br>man<br>sluter<br>en<br>omkopplare<br>(sätter<br>den<br>i<br>läge<br>ON)<br>adderas<br>dess<br>värde<br>till<br>adressen.                                                                                                                                                                                 |
|             | Exempel:<br>Här<br>visas<br>adress<br>27.<br>Omkopplare<br>i<br>ON-läge:<br>Nr.<br>1,<br>2,<br>4,<br>5<br>(1+2+8+16<br>=<br>27).                                                                                                                                                                                                                                                                                                                                     |
| SW2         | Termineringsmotstånd<br>RS-485-kommunikation.<br>Terminera<br>i<br>första<br>och<br>sista<br>enheten<br>på<br>lokala<br>RS-485-<br>bussen.<br>Bygla<br>stift<br>1<br>och<br>2<br>för<br>inkoppling<br>av<br>motståndet.<br>Leveransinställning:<br>Ej terminerad.                                                                                                                                                                                                    |
| SW3         | Reset-knapp<br>för<br>omstart<br>av<br>UC-50.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| SW4         | Sabotageavkänning<br>(tamper).<br>Sluten<br>när<br>kåpan<br>är<br>monterad.<br>Registreras<br>även<br>internt<br>i<br>UC-50.<br>På<br>ett<br>LK4-kretskort<br>består<br>SW4<br>av<br>två<br>brytare,<br>en<br>på<br>ovansidan<br>och<br>en<br>på<br>undersidan<br>av<br>kretskortet.<br>Brytarna<br>är<br>seriekopplade<br>och<br>anslutna<br>till<br>P1/3<br>och<br>P1/4.<br>På<br>ett<br>LK2-kretskort<br>består<br>SW4<br>av<br>en<br>brytare<br>på<br>ovansidan. |
| SW5         | Termineringsmotstånd<br>för<br>CAN-bussen.<br>Terminera<br>i<br>första<br>och<br>sista<br>enheten<br>på<br>CAN-bussen.<br>Bygla<br>stift<br>1<br>och<br>2<br>för<br>inkoppling<br>av<br>motståndet.                                                                                                                                                                                                                                                                  |
| P10,<br>P11 | Fabriksinställda<br>byglar,<br>ska<br>inte<br>ändras!<br>Ritningen<br>på<br>sidan<br>4 visar<br>hur<br>byglarna<br>ska<br>sitta.                                                                                                                                                                                                                                                                                                                                     |

![](_page_6_Picture_2.jpeg)

### **Jackbara plintar och rekommenderad kabelarea**

Rekommenderade kabelareor för medlevererade jackbara plintar enl. nedan. Kablar ska vara CPR klassificerade och uppfylla brandklass enligt EN13501 eller EN50575 och vara testade enligt IEC60332-1-2 eller IEC60332-1-3. Utseendet varierar.

| Strömförsörjningsplint<br>med<br>5<br>mm<br>delning<br>mm2<br>Min.<br>ledararea<br>0,2<br>mm2<br>Max.<br>ledararea<br>2,5<br>Nominell<br>avskalningslängd<br>10<br>mm<br>Tryck<br>in<br>en<br>liten<br>flatskruvmejsel<br>i<br>slitsen<br>för<br>att<br>öppna<br>fjäderan<br>slutningen.<br>Se YouTube-video. |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Plint<br>med<br>3,5<br>mm<br>delning<br>mm2<br>Min.<br>ledararea<br>0,2<br>mm2<br>Max.<br>ledararea<br>1,5<br>Nominell<br>avskalningslängd<br>5<br>mm                                                                                                                                                         |
| Plint<br>med<br>5<br>mm<br>delning<br>mm2<br>Min.<br>ledararea<br>0,2<br>mm2<br>Max.<br>ledararea<br>2,5<br>Nominell<br>avskalningslängd<br>6<br>mm                                                                                                                                                           |

![](_page_7_Picture_4.jpeg)

# **Montering och kabeldragning**

Enheterna monteras i inomhusmiljö.

Kablaget måste fästas med max. 5 mm brett buntband. Sätt bandet längre bak på kabeln, skjut in bandet i den därför avsedda öppningen, dra fast och klipp av.

![](_page_8_Picture_4.jpeg)

Alternativt kan man trä bandet genom slitsarna. (Ej vid LK4.)

För certifiering i larmklass 4 gäller:

- l Kablaget dras igenom gummitätningen som ligger under plåtinsatsen när man sätter på locket.
- l Kapslingen är kompletterad med en plåtinsats försedd med vibrationsdetektor CD 470. Kretskortets anslutning P5 är avsedd för vibrationsdetektorn.

![](_page_8_Figure_9.jpeg)

![](_page_8_Figure_10.jpeg)

### **Funktioner som kan utföras direkt på UC**

Nedanstående funktioner kan köras i undercentralen utan att den har kommunikation med andra enheter eller PC. *Matningsspänningen ska vara på hela tiden.*

- 1. Ställ in adress 0 på UC-50 Gen2 och tryck på RESET-knappen.
- 2. Kontrollera att diod D2 blinkar kontinuerligt (diagnosläge).
- 3. Välj önskad funktion:
	- o **Aktivera DHCP:** Adress 1 (DIP-omkopplare 1=På, övriga=Av).
	- o **Deaktivera DHCP, återställ leveransadressen** 169.254.254.X1 och APIPAfunktionen: Adress 2 (DIP 2=På, övriga=Av).
	- o **Hämta lokalbuss:** Adress 4 (DIP-omkopplare 3=På, övriga=Av).
	- o **Återställa till programmeringsläge** (ta bort fristående driftläge och driftläge): Adress 8 (DIP-omkopplare 4=På, övriga=Av).

Det kan vara lämpligt om anläggningen arbetar i fristående driftläge (kommunikationen med PC avstängd) och du behöver komma åt den men inte kommer in via manöverpanelen.2

- o **Nollställa minnet:** Adress 128 (DIP-omkopplare 8=På, övriga=Av).
- 4. Tryck och håll nere sabotageskyddet tills D2 släcks. (Vid hämtning av lokalbussen kan det dröja upp till 30-sekunder.)
- 5. Släpp sabotageskyddet. D2 börjar åter blinka.
- 6. Endast vid nollställning:
	- a. Ställ åter in adress 0.
	- b. Tryck och håll nere sabotageskyddet igen.
	- c. Släpp sabotageskyddet. D2 börjar åter blinka.
- 7. Ställ in den adress undercentralen ska ha och tryck på RESET-knappen.
- 8. Vid nollställning: Vänta minst 10 sekunder så att undercentralen hinner bli klar.

<sup>2</sup> Om det finns flera undercentraler i anläggningen (på anknytningen) gör du återställningen på anknytningens första undercentral (där anknytningen är ansluten). Om du blir tvungen att hämta anknytningen innan driftläget kan ändras i anläggningen kan du först behöva återställa samtliga undercentraler på anknytningen. Annars får du sätta driftläget senare när R-CARD M5 är uppkopplad, för att alla undercentraler ska synkroniseras till samma läge (välj **MAP-styrning** > **Driftläge**).

![](_page_9_Picture_22.jpeg)

<sup>1</sup> X = värdet på SW1, avläst vid uppstart och återställning (steg 7).

### **Indikeringar**

| Diod | Beskrivning                                                                                                                                                               |                |                                                                                                                       |  |  |  |  |
|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|-----------------------------------------------------------------------------------------------------------------------|--|--|--|--|
| D2   | Indikerar<br>kommunikation<br>med<br>överordnad<br>enhet<br>på<br>systembuss<br>samt<br>ev.<br>fel<br>(se nedan).<br>Följande<br>signalbilder<br>repeteras<br>vid<br>fel: |                |                                                                                                                       |  |  |  |  |
|      | ☼                                                                                                                                                                         | Ett<br>blink:  | Diagnostikläge.*<br>Adress<br>0<br>är<br>inställd.                                                                    |  |  |  |  |
|      | ☼ ☼                                                                                                                                                                       | Två<br>blink:  | Fel<br>har<br>inträffat<br>under<br>flashproceduren.<br>Internt<br>RAM-minnesfel.                                     |  |  |  |  |
|      | ☼ ☼ ☼                                                                                                                                                                     | Tre<br>blink:  |                                                                                                                       |  |  |  |  |
|      | ☼ ☼ ☼ ☼                                                                                                                                                                   | Fyra<br>blink: | Externt<br>RAM-minnesfel.                                                                                             |  |  |  |  |
|      | ☼ ☼ ☼ ☼ ☼                                                                                                                                                                 | Fem<br>blink:  | Fel<br>i<br>flashproceduren<br>vid<br>minnesradering.                                                                 |  |  |  |  |
|      | ☼ ☼ ☼ ☼ ☼ ☼                                                                                                                                                               | Sex<br>blink:  | Fel<br>i<br>flashproceduren<br>vid<br>skrivning<br>till<br>minnet.                                                    |  |  |  |  |
|      | ☼ ☼ ☼ ☼ ☼ ☼ ☼                                                                                                                                                             | Sju<br>blink:  | Fel<br>på<br>oscillator<br>eller<br>annat<br>internt<br>fel.<br>(Kan kopplas<br>till<br>reläutgången<br>på<br>UC-50.) |  |  |  |  |
| D6   | Lyser<br>när<br>kretskortets<br>interna<br>+5V<br>är<br>OK.                                                                                                               |                |                                                                                                                       |  |  |  |  |

D13 Lyser när utgångsreläet är aktivt (P16/1 och 2 är slutna).

* Diagnostikläget används så här: Vid felindikering (2–7 blink), ställ in adress 0 och tryck på RESET-knappen.

- l Om D2 nu indikerar diagnosläge fungerar undercentralen förmodligen fortfarande och nytt försök kan göras. Ställ in adressen igen, tryck på RESET-knappen och gör nytt försök att utföra den misslyckade operationen (t.ex. uppgradering).
- l Om D2 *inte* indikerar diagnosläge har undercentralens program troligen kraschat och enheten måste bytas.

![](_page_10_Picture_7.jpeg)

### **Uppgradera**

Filer för uppgradering av hårdvaran finns på installationsmediet för R-CARD M5. Alternativt, ladda ned dem från RCO:s [hemsida](https://www.rco.se/file/c31a6e65-1218-439a-b459-aa79007d699a) under **Mediearkivet** > **Mjukvara** > **Firmware**. (Inloggning krävs.) Instruktioner ingår.

# **Ytterligare information**

För utförlig information kring montering och anslutning, se manualen *R-CARD 5000 – Installera*. Manualer och övrig produktdokumentation finns i mappen **Document** på installationsmediet för R-CARD M5. Manualer kan även laddas ner från [RCOs](https://www.rco.se/file/4508c5f4-58e5-4dcc-89a1-aa0e00ec92d8) [webbplats](https://www.rco.se/file/4508c5f4-58e5-4dcc-89a1-aa0e00ec92d8), under **Mediaarkivet** > **Manualer** (inloggning krävs).

För driftsättning/programmering se hjälpfunktionen i R-CARD M5 (tryck på **F1**).

![](_page_11_Picture_6.jpeg)

# **Specifikationer**

| DC specifikation (t = +20°C)                                       |                                                                                                                                             | Min.           | Typ                               | Max.                              | Enhet                            |  |  |
|--------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|----------------|-----------------------------------|-----------------------------------|----------------------------------|--|--|
| Matningsspänning                                                   | DC (likspänning)                                                                                                                            | 18             | 24                                | 30                                | V                                |  |  |
| Effektförbrukning                                                  | Utan tillsatsmoduler<br>Inkl. IP-50 Gen2<br>Inkl. IP-50 Gen2 och LS-50 Gen3                                                                 |                | 1<br>2,5<br>3,2                   | 1,1<br>2,6<br>3,2                 | W<br>W<br>W                      |  |  |
| Strömförbrukning                                                   | Normal drift<br>Inkl. IP-50 Gen2<br>Inkl. IP-50 Gen2 och LS-50 Gen3<br>Elektromekaniskt relä<br>Vibrationsdetektor CD 470<br>Full aktivitet |                | 41<br>102<br>130<br>6<br>7<br>145 | 51<br>135<br>175<br>8<br>7<br>190 | mA<br>mA<br>mA<br>mA<br>mA<br>mA |  |  |
| Maximal ström, relä3                                               | Vid 40 °C                                                                                                                                   |                |                                   | 450                               | mA                               |  |  |
| IP-specifikation                                                   |                                                                                                                                             |                |                                   |                                   |                                  |  |  |
| IP-adress vid leverans                                             |                                                                                                                                             | 169.254.254.04 |                                   |                                   |                                  |  |  |
| Nätmask vid leverans                                               |                                                                                                                                             | 255.255.0.0    |                                   |                                   |                                  |  |  |
| Gateway vid leverans                                               |                                                                                                                                             | 0.0.0.0        |                                   |                                   |                                  |  |  |
| Övrigt                                                             |                                                                                                                                             | Min.           | Typ                               | Max.                              | Enhet                            |  |  |
| Temperaturområde UC-50 Gen2 / IP-50 Gen2 /<br>LS-50 Gen3           |                                                                                                                                             | +5             |                                   | +40                               | °C                               |  |  |
| Mått – kapsling (B x H x D): 201 x 181 x 50 mm                     |                                                                                                                                             |                |                                   |                                   |                                  |  |  |
| Vikt: 0,4 kg                                                       |                                                                                                                                             |                |                                   |                                   |                                  |  |  |
| Larmklass 2 eller 3/4 beroende på vald produkt                     |                                                                                                                                             |                |                                   |                                   |                                  |  |  |
| Miljöklass 1                                                       |                                                                                                                                             |                |                                   |                                   |                                  |  |  |
| Ingångar: 1 st. generell ingång där funktionen anges i R-CARD M5.5 |                                                                                                                                             |                |                                   |                                   |                                  |  |  |
| Utgångar: 1 st. potentialfri utgång från relä.                     |                                                                                                                                             |                |                                   |                                   |                                  |  |  |
| Batterireserv för klocka och händelseminne räcker mer än 1 år.     |                                                                                                                                             |                |                                   |                                   |                                  |  |  |

3 Avsäkrad med PTC med en hållström på 750 mA vid 23 °C.

<sup>5</sup> Ingången kan inte användas om vibrationsdetektor CD 470 är kopplad till P5.

![](_page_12_Picture_6.jpeg)

<sup>4</sup> Sista delen av leveransadressen är satt till 0 av följande skäl: När adressen är 0 ersätts nollan av undercentralens inställda adress (1–255). Om man väljer annat än 0 som sista adressdel kvarstår detta värde oberoende av undercentralens inställda adress.