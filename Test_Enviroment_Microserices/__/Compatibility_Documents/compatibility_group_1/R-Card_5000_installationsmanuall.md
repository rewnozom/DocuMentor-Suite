![](_page_0_Picture_0.jpeg)

![](_page_0_Picture_1.jpeg)

| INNEHÅLLSFÖRTECKNING  2                                          |  |
|------------------------------------------------------------------|--|
| FÖRE INSTALLATION  3                                             |  |
| Kontrollmät bussar före spänningssättning  3                     |  |
| Kontrollera spänningsfall i matande ledare  3                    |  |
| Kraftaggregat  3                                                 |  |
| Märkning av godkänd larmutrustning  3                            |  |
| IN/UTENHET DIO-5084  4                                           |  |
| Egenskaper  4                                                    |  |
| Inkoppling av vibrationsdetektor ES-400  4                       |  |
| Placering av plintar och byglar  5                               |  |
| Säkringar  6                                                     |  |
| Omkopplare och byglar  6                                         |  |
| Anslutningar  7                                                  |  |
| Lysdiodindikeringar på kretskort DIO-5084  9                     |  |
| LARMSÄNDARE LS-50  10                                            |  |
| Montering  10                                                    |  |
| Anslutningar på LS-50  10                                        |  |
| Lysdiodsindikeringar  11                                         |  |
| Inkoppling av LS-50 till telenätet  11                           |  |
| Montering och anslutning av separat 5V-regulator  11             |  |
| MANÖVERPANEL MAP-59  12                                          |  |
| Placering av plintar och byglar  12                              |  |
| Montering  13                                                    |  |
| Anslutningar, byglar, och omkopplare  13                         |  |
| MANÖVERPANEL MiniMAP-50  15                                      |  |
| Inställningsmeny:  15                                            |  |
| Anslutningar  15<br>Anslutningar, byglar och omkopplare  16      |  |
|                                                                  |  |
| MANÖVERPANEL MiniMAP-60  17                                      |  |
| Inställningsmeny:  17<br>Anslutningar, byglar och omkopplare  17 |  |
|                                                                  |  |
| KOMMUNIKATION MED MILLETEKNIK:s KRAFTENHET 18                    |  |
| SPECIFIKATIONER  19                                              |  |
| DIO-5084  19                                                     |  |
| MAP-59  19                                                       |  |
| MiniMAP-50/60  20                                                |  |
| LS-50  20<br>LS-50 med GSM  21                                   |  |
|                                                                  |  |

![](_page_1_Picture_7.jpeg)

Denna handbok är ett komplement till "**R-CARD 5000 Passagesystem Installationshandbok**", där det finns information om övriga komponenter i 5000-systemet, adressering, kommunikationsbussar etc.

# **FÖRE INSTALLATION**

# **Kontrollmät bussar före spänningssättning**

Innan strömmen kopplas på bör undercentralernas CAN-bussar och lokala bussar kontrollmätas med alla undercentraler och samtliga enheter anslutna. Se kapitlet "Kommunikation och kabel" i "**R-CARD 5000 Passagesystem Installationshandbok**".

# **Kontrollera spänningsfall i matande ledare**

Kontrollera spänningsfallet på lokala bussen. För stort spänningsfall i den lokala bussen kan ge kommunikationsproblem, se avsnittet "Spänningsfallets inverkan på kommunikationen på lokala bussen" under kapitlet "Kommunikation och kabel" i "**R-CARD 5000 Passagesystem Installationshandbok**".

# **Kraftaggregat**

Se tillverkarens dokumentation samt blad med tilläggsinformation från RCO.

Kraftenheter från Milleteknik kan förses med självdiagnosfunktion ("SDS"-modul) och "BT-COM" adapterkort för I2 C-kommunikation med UC-50. Detta möjliggör att man kan till viss del kan styra kraftenheten och även få felrapporter från den. **Före inkoppling, läs kapitlet "KOMMUNIKATION MED MILLETEKNIK:s KRAFT-ENHET" på sidan 18 för att undvika problem!** 

# **Märkning av godkänd larmutrustning**

Typ: **UC-50** S/n: 1014-0812-0001001 LK: 3 MK: 1 Security Grade: 4 Tillverkare: RCO Security

RCO-produkter som är godkända enligt CLC/TS 50131-3 (Security grade) och SSF-1014 (Larmklass) är märkta med etikett: "*S/n*" är serienumret: "1014" = godkänd produkt, "0812" = tillverkningsår/vecka, "0001001" = löpnummmer. "*LK*" står för Larmklass "*MK*" står för Miljöklass.

Specifikationerna på sidan 19 och följande inkluderar larm- och miljöklassning för larmgodkända produkter i 5000-serien.

![](_page_2_Picture_15.jpeg)

# **IN/UTENHET DIO-5084**

I det integrerade larmsystemet R-CARD MEGA tjänstgör DIO-5084 som in-/utenhet. Den motsvarar kraven i standarden "**CLC/TS 50131-3**", godkännande enligt SSF 1014-3. För godkännande i larmklass 3 ska kapslingen kompletteras med plåtinsats försedd med vibrationsdetektor, se instruktioner nedan.

DIO-5084 kan arbeta på två olika sätt (väljs med bygel P19, se sidan 7):

- Som in-utenhet för 1-8 larmsektioner. DIO-5084 adresseras då som IO-enhet (adresstyp A**2**).
- Som kombinerad Delningsbox och in-utenhet anpassad för anslutning av 1-8 larmsektioner. DIO-5084 adresseras då som en delningsbox (adresstyp A**3**). Till enhetens anslutning "Terminal Bus" kan anslutas **en** MiniMAP-60 plus en annan Reader-60/-62, en eller två läsare av typ Reader-60/-62 med slavläsare (se detaljerad information på sidan 9). Angående MiniMAP-60, se ytterligare information på sidan 17.

# **Egenskaper**:

- Sektionsanslutningarna kan mata ut 12V DC (internt strömbegränsat) till detektorer. Matningen kan brytas (i 2 grupper om 4 anslutningar) för återställning av detektorer.
- De 8 sektionsanslutningarna kan via programmet CARD M5 MEGA konfigureras som icke balanserade eller dubbelbalanserade ingångar.
- Kortet är försett med 2 reläutgångar och 2 transistorutgångar.
- Tamperavkänning med intern registrering finns på kretskortet.
- Ansluts via lokala bussen till undercentral UC-50, adress 1-255 ställs in med 8-polig DIP-omkopplare.
- Strömförsörjningen kan vara 24V DC/AC, alternativt 12 V DC.

# **Inkoppling av vibrationsdetektor ES-400**

![](_page_3_Figure_15.jpeg)

**Bild 1: Inkoppling av vibrationsdetektor, obalanserat.** 

DIO-5084.

Obalanserad slinga: Anslut detektorn till valfri ingång på DIO-5084 enligt bilden t.v.

Programmera ingången som sabotagesektion i R-CARD M5.

Läs bifogat informationsblad för detektorn, där beskrivs övriga anslutningar, funktioner och inställningsmöjligheter.

![](_page_3_Picture_25.jpeg)

# **Placering av plintar och byglar**

![](_page_4_Figure_3.jpeg)

Byglarna visas med samma orientering som de har på kretskortet. Byglar som inte beskrivs är fabriksinställda och ska inte ändras!

![](_page_4_Picture_5.jpeg)

# **Säkringar**

Båda säkringarna är anslutna till anslutning P1:25, anslutning P1:26 är inte avsäkrad. In- och utgångarna har intern 12V-matning med strömbegränsning.

## **FU1**

Avsäkrar elektroniken i DIO-5084 samt följande anslutningar:

- Transistorutgångarna 3 och 4 (plint P12)
- 12V-utgången (plint P10:33) på "Återst. Matning"
- Slingmatningen (plintarna P2-P9)
- Om bygel P15 är ställd för intern 12V-matning av utgångar kommer FU1 även att avsäkra reläutgångarna 1 och 2 (plint P11).

# **FU2**

Avsäkrar reläutgångarna 1 och 2 (plint P11) om bygel P15 är ställd för matning av utgångarna via "DCIN" (plint P1:25). I annat fall har säkringen ingen funktion, all avsäkring görs då av FU1.

# **Omkopplare och byglar**

### **SW1: Tamperavkänning**

Sluten när kåpan är monterad. Registreras endast internt, givaren har ingen plintanslutning.

| SW2: Adressinställning |                                                                                                               |  |  |  |  |
|------------------------|---------------------------------------------------------------------------------------------------------------|--|--|--|--|
| Koppling               | Beskrivning                                                                                                   |  |  |  |  |
|                        | 8-polig DIP-omkopplare för inställning av enhetens adress 1-255.<br>Bild 3: Adress 27 inställd (1+2+8+16=27). |  |  |  |  |

### **SW3: Terminering av Lokal Bus**

Om DIO-5084 sitter i någon ände av *kommunikationskabeln* ska termineringen kopplas in. Kabeln är terminerad när bygel SW3 sitter på plats. **Leveransinställning: Ej terminerad**.

### **P14: Detektormatning, nedbrytningsbar eller fast**

| Koppling | Beskrivning                                                                                                                                                                                                                                                |  |  |  |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|--|
|          | Slinga 1-4 (plint P2-P5) och slinga 5-8 (plint P6-P9) har var för sig valbart fast<br>("12V FAST") eller nedbrytningsbar ("12V RESET") 12V-matning.<br>Nedbrytning används för att återställa vissa typer av detektorer, programmerade<br>för strömslinga. |  |  |  |
|          | Nedbrytning sker alltid gemensamt med utgången för 12V-matning (plint P10, se<br>sidan 8).                                                                                                                                                                 |  |  |  |
|          | Leveransinställning är "12V FAST".                                                                                                                                                                                                                         |  |  |  |

![](_page_5_Picture_23.jpeg)

### **P19: Val av adresstyp: IO- eller DB-typ**

| Koppling | Beskrivning                                                                                                                                                                  |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          | Enheten adresseras som en IO-enhet (adresstyp A2). Läsare kan inte anslutas.<br>Leveransinställning.                                                                         |
|          | Enheten adresseras som en Delningsbox (adresstyp A3). En eller två Reader-60 eller Reader<br>62 (med ev. slavläsare) kan anslutas. En Mini-MAP 60 kan anslutas, se sidan 17. |

# **P20: 12 eller 24V matning på plint P1 ("Lokal bus")**

| Koppling | Beskrivning                               |  |
|----------|-------------------------------------------|--|
|          | Strömförsörjning med 24V AC/DC.           |  |
|          | Leveransinställning.                      |  |
|          | Strömförsörjning med 12V DC.              |  |
|          | OBS: Kräver stabiliserad spänning, +/- 5% |  |

Polaritet på utgångar vid DC-matning: Vid likströmsmatning, tänk på matningens polaritet, se beskrivningen av plint P11: "Polaritet på utgång 1 och 2" på sidan 8.

# **Anslutningar**

Plintarna är jackbara.

| P1: "Lokal Bus". Strömförsörjning och kommunikation. |          |                         |                                                                                                                                             |  |
|------------------------------------------------------|----------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|--|
|                                                      | Stift nr | Beteckning              | Beskrivning                                                                                                                                 |  |
|                                                      | 25, 26   | "DC(AC)"                | Strömförsörjning. Ansluts till motsvarande plint på andra enheter.<br>Vid DC-matning, anslut plus till "DC(AC) +" (P1:25).                  |  |
|                                                      | 27, 28   | "RS485 A",<br>"RS485 B" | RS485 kommunikation. Partvinnad kabel ska användas. Ansluts till motsva<br>rande plint på andra enheter. Terminera sista enheten på kabeln. |  |

### **P2-P9: Detektoranslutningar med nedbrytningsbar 12V-matning**

![](_page_6_Figure_11.jpeg)

**Koppling Beskrivning** 

Varje sektionsplint har en *ingång*, en 12V-*utgång* samt minus. 12V-utgången har *intern reglering och strömbegränsning på 500 mA*, se specifikation på sidan 19. Strömbegränsningen är *gemensam för alla ingångarna*.

Ingången kan i M5-programmet programmeras som *ej balanserad, dubbelbalanserad* eller *strömslinga*.

#### **Anslutning av magnetkontakt, ej balanserad ingång**

![](_page_6_Figure_16.jpeg)

![](_page_6_Picture_18.jpeg)

#### **R-CARD 5000 MEGA INSTALLATION IN/UTENHET DIO-5084**

#### **Anslutning av dubbelbalanserad givare**

![](_page_7_Figure_3.jpeg)

met. Standardvärden är 2.2kOhm för båda motstånden.

#### **Bild 5: Inkoppling av dubbelbalanserad givare, med strömförsörjning**.

#### **Anslutning av glaskrossdetektor**

![](_page_7_Figure_7.jpeg)

Spänningen kan brytas ned för t.ex. återställning av utlöst detektor. Nedbrytning sker **gemensamt** med sektionsanslutningarnas matning i 2 grupper om 4 ingångar (på plintarna P2-P5, P6-P9).

#### **Bild 6: Inkoppling av glaskrossdetektor**.

![](_page_7_Figure_10.jpeg)

+ Om man har en eller ett par detektorer som återställs med matningsavbrott och inte vill förbruka en hel grupp om 4 ingångar (som i Bild 6) kan man använda utgången för separat, nedbrytningsbar detektormatning (P10).

> **Bild 7: Inkoppling av glaskrossdetektor, separat brytande matning**.

#### **P10 "ÅTERST. MATNING": Nedbrytbar 12V-utgång.**

| Stift nr | Beteckning | Funktion                                                    |
|----------|------------|-------------------------------------------------------------|
| 33       | "+12V"     | Strömbegränsad utgång, 12V DC 500 mA. Se spec. på sidan 19. |
| 34       | "0 V"      | Minusanslutning.                                            |

### **P11: Reläutgång 1, reläutgång 2**

| Koppling | Beskrivning |
|----------|-------------|
|          |             |
|          |             |

Utgångarna 1 och 2 på DIO-5084 är försedda med elektromekaniska reläer. Med bygel **P16** resp. **P17** (se nedan) bestämmer man hur utgångarna ska fungera. Strömkälla för *båda* utgångarna (intern, *strömbegränsad* 12V, 750 mA**1** , eller från plint P1 via säkring FU2) bestäms av bygel **P15** (se nedan).

#### **Polaritet på utgång 1 och 2:**

Om bygel P15 är inställd för "DCIN" måste plus anslutas till skruv P1:25 (betecknad "DC(AC) +") för att polariteten på utgångarna 1 och 2 ska överensstämma med kretskortmärkningen vid respektive utgång.

![](_page_7_Picture_23.jpeg)

- 
### **P12: Transistorutgång 3, transistorutgång 4**

| Utgångarna 3 och 4är transistorutgångar som sluter mot minus vid<br>aktivering. Anslutningarna märkta med (+) ger konstant 12V utspän<br>ning med intern strömbegränsning på 750 mA2<br>. Se specifikation på<br>sidan 19. | Koppling | Beskrivning                                                        |  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|--------------------------------------------------------------------|--|
| ning som ansluts till plint P1 och hur den är polariserad.                                                                                                                                                                 |          | Polariteten är alltid densamma, oavsett vilken typ av strömförsörj |  |

### **P13: "TERMINAL BUS": Kommunikation med läsare**

| Stift nr | Beteckning    | Funktion                                                                                                                                                                                                                |
|----------|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 39,40    | "DC+", "DC-": | Strömförsörjning till läsare. Ansluts till motsv. plint på läsare/kraftenhet.                                                                                                                                           |
| 41       | "SCL (Data1)" | Data till/från läsare. Två läsare3<br>kan anslutas till P13, med max 10 meter<br>kabel till varje läsare. Ansluts till motsvarande plint på läsaren.<br>Om partvinnad kabel används får SCL/SDA inte ligga i samma par. |
| 42       | "SDA (Data0)" |                                                                                                                                                                                                                         |

**OBS: Kräver att P19 ställs in för DB-funktion, se sidan 7. Montera/demontera inte P13 under spänning, kommunikationskretsarna kan skadas!**

#### **P15: Intern eller extern matning för reläutgångar 1 och 2**

| Koppling            | Beskrivning                                                                                                       |
|---------------------|-------------------------------------------------------------------------------------------------------------------|
| MATNING PÅ UTGÅNGAR | Matning via plint P1 "DC(AC)" (vänstra bilden). Säkring FU2 avsäkrar utgån                                        |
| DC IN<br>12V        | garna.                                                                                                            |
|                     | Matning med intern, 12V DC, strömbegränsad (högra bilden). Säkring FU2 är<br>inte inkopplad. Leveransinställning. |

![](_page_8_Figure_9.jpeg)

# **Lysdiodindikeringar på kretskort DIO-5084**

| Pos | Beskrivning                                                | Pos | Beskrivning                            |
|-----|------------------------------------------------------------|-----|----------------------------------------|
| D4  | Kretskortets interna +5V är OK.                            | D12 | Lyser när transistorutgång 3 aktiv.    |
| D9  | Lyser när reläutgång 1 aktiv.                              | D13 | Indikerar kommunikation på RS485-buss. |
|     |                                                            |     | Blinkar ungefär var femte sekund.      |
| D10 | Lyser när reläutgång 2 aktiv.                              | D15 | Lyser när Terminal Bus är aktiv.       |
| D11 | Lyser när 12 V till plintarna P2-P9 samt P10<br>är bruten. | D16 | Lyser när transistorutgång 4 är aktiv. |

<sup>2</sup> Strömbegränsningen är 750 mA sammanlagt för alla 4 utgångarna på P11 och P12. 3 Endast **en** Mini-MAP 60 kan anslutas, se sidan 17.

![](_page_8_Picture_13.jpeg)

# **LARMSÄNDARE LS-50**

LS-50 monteras med bifogade distanser på Undercentral UC-50. Undercentralen får inte ha serieport fast inlödd, då finns inte plats för LS-50! Om RS-50 också behövs monteras den *ovanpå* LS-50.

![](_page_9_Figure_4.jpeg)

**Bild 8: Larmsändarens kretskort.** 

# **Montering**

Separat anvisning bifogas larmsändaren.

# **Anslutningar på LS-50**

### **P1: Separat strömförsörjning för GSM-modulen**

Anslutning från separat 5V-regulator. **Ingången används bara när GSM-modul sitter på en LS-50 som är monterad på UC-50** *rev. C,D***4** . På UC-50 rev. F används inte separat 5V för GSM

### **P2: 10-polig hylskontakt för anslutning mot undercentral**

Passar mot undercentralens stiftlist P14.

# **P3: 10-polig stiftlist för anslutning av RS-50 serieportsmodul**

Passar mot den 10-poliga hylskontakten på RS-50.

# **P8: Koaxialkontakt för GSM-antenn**

### **P10: TELE UT, 4-poligt modularjack för utgående teleledning**

Anslutning för utgående linje. Stift 1-3 samt 2-4 är sammankopplade. Avsedd för anslutning av eventuell efterföljande teleutrustning.

![](_page_9_Picture_20.jpeg)

#### **P11: TELE IN, 4-poligt modularjack för inkommande teleledning**

Anslutning för inkommande telefonlinje från publika nätet. Stift 2-3 används för *inkommande* linje och 1-4 för *utgående* linje. Ansluts alltid i *första telejacket*, LS-50 kommer att koppla bort alla efterföljande telefoner vid larmsändning! Koppla ingen utrustning parallellt med LS-50!

# **Lysdiodsindikeringar**

#### **Diod Beskrivning**

- **+5V Kretskortets 5V-spänning.**  Fast sken: 5V-spänning är OK.
#### **Tele ut Linjereläets läge:**

- Släckt: Linjerelä är inte draget, inkommande linje är *vidarekopplad* till utgående linje. Ev. efterföljande utrustning har kontakt med telefonnätet.
- Fast sken: Linjerelä är draget, inkommande linje är *bortkopplad* från utgående linje. Ev. efterföljande utrustning är bortkopplad från nätet.

#### **1 Status för telelinje (PSTN):**

- Släckt: Inaktiv.
- Fast sken: Aktiv.
- Blinkande: Aktiv men linjen kan inte detekteras.

#### **2 Status för GSM:**

- Släckt: Inaktiv.
- Fast sken: Aktiv.
- Fast sken med korta avbrott: Aktiv men signalstyrkan är under gränsvärdet.
- Blinkande: Aktiv men ej registrerad hos operatör.

#### **3 Larmsändning**

- Släckt: Ingen larmsändning pågår.
- Blinkande: Larmsändning pågår.

#### **4 Felindikering**.

Normalt släckt. Fast sken betyder att ett internt fel har uppstått.

# **Inkoppling av LS-50 till telenätet**

Anslut en telekabel med 4-polig modularplugg till plint P11. Anslut kabeln till det första telejacket (larmsändaren ska ha högsta prioritet och ska kunna koppla bort övriga teleapparater). Koppla ingen teleutrustning parallellt med LS-50! Efterföljande telefoner ansluts med 4-polig modularplugg till P10. LS-50 kan använda GSM-nätet samtidigt med det publika, trådbundna telefonnätet (PSTN). Prioriteringsordningen bestäms i M5 programmet. Om GSM används: Prova ut antennplaceringen så att mottagen signalnivå ligger över minimigränsen (lysdiod 2 ska antingen blinka eller lysa fast, se tabellen ovan).

# **Montering och anslutning av separat 5V-regulator**

Regulatorn är kapslad i en plastlåda. 5V-kabeln är fast inlödd i regulatorn och försedd med 2.1 mm propp (plus på höljet). Kabeln bör inte vara längre än 0,5 m. Anslut 24V likspänning (filtrerad 24V +/- 10%) till plint **P2** ("DC IN"). Ta 24V från samma matning som förser undercentralen så finns det ingen risk att undercentralen startas före regulatorn.

OBS! På UC-50 rev. F används inte separat 5V för GSM.

![](_page_10_Picture_29.jpeg)

# **MANÖVERPANEL MAP-59**

Manöverpanel MAP-59 kopplas in på lokala bussen till undercentral UC-50 och upptar en dörrmiljöplats (motsvarande t.ex. en Reader-50).

Om MAP:en ska användas som både manöverpanel och passerterminal måste parametern "Aktivera inloggningsmanöver med *" aktiveras i MAP:ens dörrparametrar under "Övrigt". Orsaken är att alla knapptryckningar annars kommer att tolkas som inloggningskod i MAP:en och omöjliggöra inmatning av PIN-kod vid passage via den enheten.

MAP-59 ersätter MAP-50. Installationsanvisning för MAP-50 finns i "R-CARD MEGA INSTALLATION", rev. G och tidigare.

I det integrerade larmsystemet R-CARD MEGA tjänstgör MAP-59 som manöverpanel. Den motsvarar kraven i standarden "**CLC/TS 50131-3**", godkännande enligt SSF 1014-3.

# **Placering av plintar och byglar**

![](_page_11_Figure_8.jpeg)

**Bild 9: MAP-59 kretskort.** Byglar som inte beskrivs är fabriksinställda och ska inte ändras.

# **Montering**

Montera panelen på ca 150 cm höjd för bekvämt handhavande och bästa läsbarhet för teckenfönstret. MAP-59 använder radiofrekventa signaler för att läsa av passerkort, varför man måste tänka på följande vid montering:

- Montera inte MAP-59 inuti eller bakom elektromagnetiskt skärmande material.
- Om slavläsare används bör avståndet mellan MAP-59 och slavläsare vara minst 0,5 m.
- MAP-59 bör inte placeras närmare andra beröringsfria läsare än 0,5 m.
- Kortavläsningen i MAP-59 kan störas av annan utrustning som utsänder elektromagnetisk strålning, exempelvis bildskärm, mobiltelefon o. dyl.

# **Anslutningar, byglar, och omkopplare**

### **P6: Meny / Adressinställning / Fabriksinställning**

**Koppling Beskrivning**  Bygla de två stiften längst till höger och starta om enheten. Följ instruktioner på skärmen. Ta bort bygeln när inställningen är klar.

### **SW2: Tamperavkänning**

Sluten när kåpan är monterad. Registreras endast *internt*, givaren har ingen plintanslutning.

### **SW3: Reset**

Startar om manöverpanelen.

# **SW1: Terminering av Lokal Bus**

Om MAP-59 sitter i slutet av kommunikationskabeln ska termineringen kopplas in. Kabeln är terminerad när bygeln sitter på plats. **Leveransinställning: Ej terminerad**.

#### **P2: "Lokal Bus".**

| Stift nr | Beteckning              | Beskrivning                                                                                                                                          |  |  |  |  |  |
|----------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|--|--|--|
| 1,2      | "AC/DC"                 | Strömförsörjning. Ansluts till motsvarande plint på andra enheter.<br>OBS: Det finns inga säkringar på kretskortet!                                  |  |  |  |  |  |
| 3,4      | "RS485 A",<br>"RS485 B" | RS485 kommunikation. Partvinnad kabel ska användas. Ansluts till motsva<br>rande plint på andra enheter. Terminera sista enheten på kabeln (se SW1). |  |  |  |  |  |

![](_page_12_Picture_20.jpeg)

### **P4: Anslutningskontakt för slavläsare**

![](_page_13_Figure_3.jpeg)

![](_page_13_Picture_7.jpeg)

# **MANÖVERPANEL MiniMAP-50**

Samma format och utseende som Reader-50, men med teckenfönster och tangentbord. Lästekniker: PROX-50 (beröringsfri), MIF-50 (beröringsfri, Mifare) samt MAG-50 (magnetkort).

Om MiniMAP-50 ska användas som både manöverpanel och passerterminal måste parametern "Aktivera inloggningsmanöver med *" aktiveras i MAP:ens dörrparametrar under "Övrigt". Orsaken är att alla knapptryckningar annars kommer att tolkas som inloggningskod i MAP:en och omöjliggöra inmatning av PIN-kod vid passage via den enheten.

Observera: **Enhetsadressen kan bara ställas in mjukvarumässigt** enligt nedanstående beskrivning, det finns inga omkopplare för adressinställning!

I det integrerade larmsystemet R-CARD MEGA tjänstgör MAP-50 som manöverpanel. Den motsvarar kraven i standarden "**CLC/TS 50131-3**", godkännande enligt SSF 1014-3.

# **Inställningsmeny:**

För att komma till inställningsmenyn, sätt i bygel "MENU", stäng av strömförsörjningen ett par sekunder. Använd tangentbordets "piltangent" **2** för att gå uppåt i menyn, "piltangent" **5** för att gå nedåt.

**Adressinställning**: Gå till meny "Adress", tryck på tangent **#** för att välja.

Skriv in adress (1-255) med tangenterna, avsluta med **#**.

**Kontrastinställning**: Gå till meny "Kontrast", tryck på tangent **#** för att välja. Leveransinställning: 100. Skriv in kontrastvärde (1-255) med tangenterna, avsluta med **#**.

**Spara inställningarna**: Gå till meny "Spara", tryck på **#** .

**Avsluta**: Ta bort bygeln och stäng av strömförsörjningen ett par sekunder, läsaren använder nu de nya inställningarna.

# **Anslutningar**

### **P1: (Lokal Bus).**

| Stift nr | Beteckning         | Beskrivning                                                                                                                                                         |
|----------|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          | "ACDC+"            | Strömförsörjning. Ansluts till motsvarande plint på andra enheter.                                                                                                  |
| 1,2      | "ACDC-"            | OBS: Det finns inga säkringar på läsarens kretskort!                                                                                                                |
| 3,4      | "SCL/A"<br>"SDA/B" | RS485 kommunikation. Partvinnad kabel SKA användas. Ansluts till motsva<br>rande plint på andra enheter. Terminera sista enheten på kabeln (se "TERM"<br>nedenfor). |

# **Inkoppling på Lokal Bus**

![](_page_14_Figure_18.jpeg)

### **P3: (READER B). Anslutning av slavläsare**

Se "R-CARD 5000 Passagesystem Installationshandbok" för anslutning av Reader-30/PROX-32. Använd den anslutningskabel med kontakt som bifogas slavläsaren.

# **Anslutningar, byglar och omkopplare**

### **SW1: Tamperavkänning**

Sluten när kåpan är monterad. Registreras endast *internt*, givaren har ingen plintanslutning.

### **TERM: Terminering av Lokal Bus**

Se bild "Inkoppling på Lokal Bus" på sidan 15. Om MiniMAP-50 sitter i slutet av kommunikationskabeln ska termineringen kopplas in. Kabeln är terminerad när bygel "TERM" sitter på plats. **Leveransinställning: Ej terminerad**.

### **MENU: Visa inställningsmeny**

Bygelns placering visas i bild "Inkoppling på Lokal Bus" på sidan 15. Om "Menu" är byglad vid start av läsaren visas inställningsmenyn i teckenfönstret.

![](_page_15_Picture_15.jpeg)

# **MANÖVERPANEL MiniMAP-60**

Samma format och utseende som Reader-60, men med teckenfönster och tangentbord. Lästekniker: PROX-60 (beröringsfri), MIF-60 (beröringsfri, Mifare) samt MAG-60 (magnetkort). Ansluts till DIO-5084, se sidan 7. **Observera att bara en MiniMap-60 kan anslutas eftersom den är fast inställd som terminal 1. Annan typ av Reader-60/62-läsare kan dock anslutas (byglad som terminal 2).**

Om MiniMAP-60 ska användas som både manöverpanel och passerterminal måste parametern "Aktivera inloggningsmanöver med *" aktiveras i MAP:ens dörrparametrar under "Övrigt". Orsaken är att alla knapptryckningar annars kommer att tolkas som inloggningskod i MAP:en och omöjliggöra inmatning av PIN-kod vid passage via den enheten.

I det integrerade larmsystemet R-CARD MEGA tjänstgör MAP-50 som manöverpanel. Den motsvarar kraven i standarden "**CLC/TS 50131-3**", godkännande enligt SSF 1014-3.

# **Inställningsmeny:**

För att komma till inställningsmenyn, sätt i bygel "MENU", stäng av strömförsörjningen ett par sekunder. Använd tangentbordets "piltangent" **2** för att gå uppåt i menyn, "piltangent" **5** för att gå nedåt.

**Kontrastinställning**: Gå till meny "Kontrast", tryck på tangent **#** för att välja. Leveransinställning: 100.

Skriv in kontrastvärde (1-255) med tangenterna, avsluta med **#**.

**Spara inställningarna**: Gå till meny "Spara", tryck på **#** .

**Avsluta**: Ta bort bygeln och stäng av strömförsörjningen ett par sekunder, läsaren använder nu de nya inställningarna.

# **Anslutningar, byglar och omkopplare**

### **P1: Terminal bus**

| Stift nr | Beteckning         | Beskrivning                                                                                                                                            |  |  |  |  |
|----------|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|--|--|
| 1,2      | "ACDC+"<br>"ACDC-" | Strömförsörjning. Ansluts till P13 "Terminal bus" på DIO-5084.<br>OBS: Det finns inga säkringar på kretskortet!                                        |  |  |  |  |
| 3,4      | "SCL/A"<br>"SDA/B" | 2<br>I<br>C kommunikation. Partvinnad kabel ska INTE användas.<br>Ansluts till P13 på DIO-5084. Max kabellängd 10 meter mellan läsare och<br>DIO-5084. |  |  |  |  |

#### **Inkoppling av MiniMAP-60 mot DIO-5084**

![](_page_16_Figure_16.jpeg)

# **P3: READER B. Anslutning av slavläsare**

Se "R-CARD 5000 Passagesystem Installationshandbok" för anslutning av Reader-30/PROX-32. Använd den anslutningskabel med kontakt som bifogas slavläsaren.

![](_page_16_Picture_19.jpeg)

## **SW1: Tamperavkänning**

Sluten när kåpan är monterad. Registreras endast *internt*, givaren har ingen plintanslutning.

### **MENU: Visa inställningsmeny**

Bygelns placering visas i bild "Inkoppling på Lokal Bus" på sidan 15. Om "Menu" är byglad vid start av läsaren visas inställningsmenyn i teckenfönstret.

# **KOMMUNIKATION MED MILLETEKNIK:s KRAFTENHET**

UC-50 kommunicerar med kraftenhet från Milleteknik via en tretrådsförbindelse (I2 C-kommunikation): *Minus*, *Klocka* samt *Data*. Med UC-50 rev C,D, var noga med att ansluta kabeln korrekt på undercentralens stiftlist P8, det finns ingen nyckling som styr kontakten! Anslut på *stiften närmast kanten på undercentralens kretskort*, se skiss nedan.

Kabel:

- Kan vara oskärmad.
- Maximal längd **10 m**.
- Ska **inte** vara **partvinnad**.

**Läs alltid tillverkarens dokumentation. Observera speciellt följande tillägg som inte står i dokumentationen:** *Anslut kraftenhetens batterier till aggregatet innan det ansluts till elnätet. Koppla först därefter in R-CARD M5 MEGA enligt skissen nedan!* 

Om så *inte* görs kommer larmsystemet att rapportera "Åldrat batteri" eftersom kraftenhetens självdiagnosmodul bl.a. gör en genomgång av batteristatus omedelbart efter anslutning till elnätet. Även om batteriet kopplas in i efterskott kvarstår batterifelet tills nästa åldringstest görs (normalt efter en vecka) eller tills självdiagnosen nollställs manuellt. Se tillverkarens dokumentation.

### **Anslutning av kommunikation till självdiagnosmodulen i Milletekniks kraftenhet**

![](_page_17_Figure_15.jpeg)

Självdiagnosmodulen har beteckningen "**T/BAS-SDX 5269682**" och ska ha programversion "**SDS-BUSS 4.2**" eller senare för att alla larm ska detekteras.

![](_page_17_Picture_20.jpeg)

# **SPECIFIKATIONER**

# **DIO-5084**

| AC/DC specifikation t = +20°C |                       | Min | Typ | Max | Enhet |  |  |
|-------------------------------|-----------------------|-----|-----|-----|-------|--|--|
| Matningsspänning              | DC (likspänning)      | 10  |     | 30  | V     |  |  |
| (matas från UC-50)            | AC (växelspänning)    | 8   |     | 24  | V     |  |  |
|                               | Tomgång               |     | 17  |     | mA    |  |  |
|                               | Elektromekaniskt relä |     | 10  |     | mA    |  |  |
| Strömförbrukning              | Transistor            |     | 4   |     | mA    |  |  |
|                               | Sluten ingång         |     | 8   |     | mA    |  |  |
|                               | Max totalt            |     | 109 |     | mA    |  |  |
| Säkringar FU1-FU2             | Märkström             | 100 | 500 | 500 | mA    |  |  |
| Utgångar                      |                       |     |     |     |       |  |  |
|                               | Elektromekaniskt relä |     |     | 1   | A     |  |  |
| Brytström @ 24 VDC            | Transistor            |     |     | 1   | A     |  |  |
| Belastning                    | Totalt strömuttag 12V |     |     | 750 | mA    |  |  |
| Ingångar                      |                       |     |     |     |       |  |  |
| Belastning                    | Totalt 8 ingångar     |     |     | 500 | mA    |  |  |

#### **Larm- och miljöklassificering SSF 1014-3**

| Larm- och miljöklassificering SSF 1014-3 | Mått Kapsling |       |      |      |       |
|------------------------------------------|---------------|-------|------|------|-------|
| Larmklass (Security Grade)               | Miljöklass    | Bredd | Höjd | Djup | Enhet |
| 3 (4)                                    | 1             | 200   | 180  | 50   | mm    |

#### **Temperaturområde**

| Matningsspänning | Strömförbrukning | Min | Typ | Max | Enhet |
|------------------|------------------|-----|-----|-----|-------|
| 24 VAC           | Max (se ovan)    | +5  |     | +60 | °C    |

# **MAP-59**

| AC/DC specifikation t = +20°C |                    | Min  | Typ | Max | Enhet  |
|-------------------------------|--------------------|------|-----|-----|--------|
| Matningsspänning              | DC likspänning.    | 10   | 24  | 30  | V      |
| (matas från UC-50)            | AC växelspänning.  | 10   |     | 24  | V      |
| PROX                          | Med släckt fönster |      | 18  |     | mA     |
| Strömförbrukning @27,1VDC     | Med tänt fönster   |      | 43  |     | mA     |
| Mifare                        | Med släckt fönster |      | 21  |     | mA     |
| Strömförbrukning @27,1VDC     | Med tänt fönster   |      | 46  |     | mA     |
|                               |                    |      |     |     |        |
| Drifttid                      |                    | Min  | Typ | Max | Enhet  |
| Bakgrundsbelysning            |                    | 5000 |     |     | timmar |

#### **Temperaturområde Matningsspänning Min Typ Max Enhet**  24 V AC/DC +5 +40 °C

| Larm- och miljöklassificering SSF 1014-3 |            |  | Mått Kapsling |      |      |       |
|------------------------------------------|------------|--|---------------|------|------|-------|
| Larmklass (Security Grade)               | Miljöklass |  | Bredd         | Höjd | Djup | Enhet |
| 3 (4)                                    | 1          |  | 95            | 235  | 30   | mm    |

#### **Bildminne**

Av det externa flashminnet på 2 MByte kan 1920 kByte användas för lagring av grafikdata. Varje bildelement (pixel) tar 1 alt. 2 byte. En bild på 200x150 pixel tar då upp max 60kByte. Dessutom krävs minne för information om färger, områden, punkter etc., detta brukar dock bara ta upp en mindre del av minnesutrymmet. Info om minnesutnyttjande kan ses i MAP-59

![](_page_18_Picture_15.jpeg)

#### **R-CARD 5000 MEGA INSTALLATION SPECIFIKATIONER**

| RF-specifikation beröringsfri läsare PROX |                     | Min | Typ | Max | Enhet |
|-------------------------------------------|---------------------|-----|-----|-----|-------|
| Sändarfrekvens                            |                     |     | 125 |     | kHz   |
| Läsavstånd                                | ISO-kort P501       |     | 2   | 3   | cm    |
|                                           | Nyckelringstag P502 |     | 1   | 2   | cm    |

# **MiniMAP-50/60**

| AC/DC specifikation t = +20°C                      |                    | Min | Typ | Max | Enhet |
|----------------------------------------------------|--------------------|-----|-----|-----|-------|
| Matningsspänning (MiniMap                          | DC likspänning.    | 10  | 24  | 30  | V     |
| 50 matas från UC-50, Mini<br>MAP-60 från DIO-5084) | AC växelspänning.  | 8   |     | 24  | V     |
| Strömförbrukning @ 24VDC                           | Med släckt fönster |     |     | 33  | mA    |
|                                                    | Med tänt fönster   |     |     | 37  | mA    |

| Drifttid<br>Min            | Typ | Max | Enhet  |
|----------------------------|-----|-----|--------|
| Bakgrundsbelysning<br>5000 |     |     | timmar |

| Temperaturområde | Min | Typ | Max | Enhet |
|------------------|-----|-----|-----|-------|
| Vid 24 V AC/DC   | +5  |     | +40 | °C    |

| Larm- och miljöklassificering SSF 1014-3 |            | Mått                          |       |      |    |            |
|------------------------------------------|------------|-------------------------------|-------|------|----|------------|
| Larmklass (Security Grade)               | Miljöklass | Kapsling                      | Bredd | Höjd |    | Djup Enhet |
| 3 (4)                                    | 1          | För utanpåliggande<br>montage | 89    | 144  | 36 | mm         |

| RF-specifikation beröringsfri läsare PROX |                     | Min | Typ | Max | Enhet |
|-------------------------------------------|---------------------|-----|-----|-----|-------|
| Sändarfrekvens                            |                     |     | 125 |     | kHz   |
| Läsavstånd                                | ISO-kort P501       |     | 2   | 3   | cm    |
|                                           | Nyckelringstag P502 |     | 1   | 2   | cm    |

| RF-specifikation beröringsfri läsare Mifare |                     | Min                                  | Typ   | Max | Enhet |  |
|---------------------------------------------|---------------------|--------------------------------------|-------|-----|-------|--|
| Sändarfrekvens                              |                     |                                      | 13,56 |     | MHz   |  |
| Läsavstånd                                  | Kort i CR80-storlek | 1                                    | 5     | 8   | cm    |  |
| Korttyper som stöds                         |                     | Mifare® standardkort med 4-byte ID.  |       |     |       |  |
|                                             |                     | Sektorläsning MAD1, MAD2. Max 16byte |       |     |       |  |
| Gränssnitt enligt specifikation             |                     | ISO/IEC 14443 Type A.                |       |     |       |  |

# **LS-50**

| AC/DC specifikation t = +20°C |                  | Min | Typ | Max | Enhet |
|-------------------------------|------------------|-----|-----|-----|-------|
| Matningsspänning              | Matas från UC 50 | -   | -   | -   | V     |
| Strömförbrukning              | Vila             |     | 39  |     | mA    |
|                               | Sändning         |     | 68  |     | mA    |

| Temperaturområde     |                      | Min | Typ | Max | Enhet |
|----------------------|----------------------|-----|-----|-----|-------|
| Vid matningsspänning | Vid strömförbrukning | +5  |     | +40 | °C    |

![](_page_19_Picture_17.jpeg)

# **LS-50 med GSM**

| AC/DC specifikation t = +20°C |                      | Min | Typ | Max | Enhet |
|-------------------------------|----------------------|-----|-----|-----|-------|
| Matningsspänning              | Medföljande aggregat | 4,9 | 5   | 5,1 | V     |
| Strömförbrukning              | Vila                 |     |     |     | mA    |
|                               | Sändning             |     |     |     | mA    |

| Temperaturområde     |                      | Min | Typ | Max | Enhet |
|----------------------|----------------------|-----|-----|-----|-------|
| Vid matningsspänning | Vid strömförbrukning | +5  |     | +40 | °C    |

| GSM-specifikation | Min | Typ | Max | Enhet |
|-------------------|-----|-----|-----|-------|
|                   |     |     |     |       |
|                   |     |     |     |       |
|                   |     |     |     |       |
|                   |     |     |     |       |

![](_page_20_Picture_6.jpeg)

![](_page_21_Picture_2.jpeg)

![](_page_21_Picture_7.jpeg)