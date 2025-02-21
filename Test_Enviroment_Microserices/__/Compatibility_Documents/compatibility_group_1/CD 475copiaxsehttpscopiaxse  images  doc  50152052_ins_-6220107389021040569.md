![](_page_0_Picture_0.jpeg)

# **Chock- och vibrationsdetektor**

## **DATABLAD OCH INSTALLATIONSMANUAL CD 475**

![](_page_0_Picture_4.jpeg)

### **BESKRIVNING**

CD 475 erbjuder pålitlig övervakning mot angrepp med mekaniska verktyg. CD 475 är en selektivt avkännande vibrationsdetektor med 3 separata detektionskanaler: en integrationskanal/sågkanal för svaga signaler med lång varaktighet, en räknekanal som känner av stark påverkan på den övervakade ytan och en explosionskanal som känner av mycket starka signaler från t.ex. en explosion.

CD 475 delar design med CD 470 men måste kopplas till analysatorn IU 400 för larmindikering eftersom den saknar inbyggda reläutgångar. Vid larm ökar strömförbrukningen i detektorn vilket analysatorn IU400 känner av och ger larm.

CD 475 polaritetsoberoende, precis som CD 470.

#### **EGENSKAPER**

- EN Grad 3, SBSC Klass 3
- Två tråd polaritetsoberoende ger enkel anslutning
- 3 separata detektionskanaler
- Täckningsradie upp till 3m
- Motståndskraftig mot störningar
- Detaljerad känslighetsinställning
- Lämplig för 24 timmars övervakning
- Låg strömförbrukning
- DAG och NATT kontroll av LED

#### **FUNKTION**

CD 475 har en piezoelektrisk sensor som detekterar de speciella vibrationerna i underlaget vid angrepp. Signalen har en speciell signatur med ett brett spektrum och stor amplitud som elektroniken känner av och signallerar till IU 400 genom strömökning samt tänder upp detektorns lysdiod. CD 475 har en inbyggd självkontroll och spänningsövervakning. Fel indikeras med en blinkande LED och en pulserande strömökning. Indikeringen styrs med en DAG och NATT funktion. Med 8V DC på spänningsingången indikeras DAG och LED lyser med fast sken vid larm och med pulserande sken vid fel. Vid 6V DC råder NATT och LED är släckt vid larm eller fel.

Återställning av detektorn efter larm kan ske på två olika sätt:

- Bryta spänningen till detektorn
- Omkoppling från DAG till NATT

#### **MONTERING**

- 1. Lossa skruven för locket och lyft bort detsamma.
- 2. Välj monteringsplats och markera fästhålen med bottenplattan som mall.
- 3. Borra med en 2-2,5 mm borr för de två medföljande monteringsskruvarna.

**OBS! En ren och slät monteringsyta under detektorn ger maximal räckvidd**.

#### **INKOPPLING**

Detektorn har 2 skruvterminaler:

| # | Funktion                          |  |
|---|-----------------------------------|--|
| 1 | DC Spänningsmatning (-) eller (+) |  |
| 2 | DC Spänningsmatning (-) eller (+) |  |

#### **DIP-SWITCH**

DIP-Switchen med 6 brytare används för att programmera detektorns funktioner.

| DIP | Känslighet (1=lägst känslighet, 8=högst) |
|-----|------------------------------------------|
|-----|------------------------------------------|

|   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8  |
|---|-----|-----|-----|-----|-----|-----|-----|----|
| 1 | OFF | OFF | OFF | OFF | ON  | ON  | ON  | ON |
| 2 | OFF | OFF | ON  | ON  | OFF | OFF | ON  | ON |
| 3 | OFF | ON  | OFF | ON  | OFF | ON  | OFF | ON |

| DIP | Knackkanal, Antal slag |    |  |
|-----|------------------------|----|--|
|     | 3                      | 6  |  |
| 4   | OFF                    | ON |  |

#### **DIP Sågkanal**

|   | Sågkanal AV | Sågkanal PÅ |
|---|-------------|-------------|
| 5 | OFF         | ON          |

**DIP**

|   | Används ej | Används ej |  |
|---|------------|------------|--|
| 6 | X          | X          |  |

## **TÄCKNINGSOMRÅDE**

Den ungefärliga räckvidden i olika material anges i tabellen nedan. Notera dock att angivna siffror endast tjänar som riktvärden och är starkt beroende av skarvar etc. Den faktiska räckvidden måste fastställas vid praktiska tester.

| Material | Trä/Glas/Plywood | Tegel*/Puts * | Stål/Betong * |
|----------|------------------|---------------|---------------|
| Räckvid  | r = 2 m          | r = 1 m       | r =3 m        |

#### **DRIFTSÄTTNING OCH JUSTERING**

#### **OBS! Nedanstående procedur måste utföras inom 5 minuter efter att detektorn startats, annars kommer de korta blinken inte att visas.**

Driftsättning och justering är mycket enkelt. Koppla CD 475 till IU 400 och kalibrera viloström med bygeln på IU 400 (se IU 400 manual). Knackkanalen gör att varje mottagen puls att visas med en kort blink på CD 475:s LED tills antal inställda pulser uppnås (3 eller 6), sedan indikeras larm. Larmet indikeras med fast sken på CD 475:s LED och kvarstår till reset-knappen på IU 400 tryckts ned.

- 1. Ställ in DIP switchen på medium känslighet, 6 knackningar samt aktiv sågkanal. Detta görs genom att ställa **DIP 1=OFF och DIP 2-5=ON.**
- 2. Knacka lätt bredvid detektorn och kontrollera att varje knackning registreras och att larmreläet öppnar efter 6 pulser.
- 3. Knacka nu relativt kraftigt med t.ex. baksidan av en skruvmejsel på den mest avlägsna punkten som ska skyddas.
- 4. Om pulserna inte detekteras (kort blink på lysdioden) öka känsligheten stegvis med DIP 1-3 enligt tabell tills lysdioden visar mottagen puls.
- 5. Om dioden istället visar larm direkt (fast sken) minska känsligheten stegvis med DIP 1-3 enligt tabell tills lysdioden visar mottagen puls (reset av larm sker på IU).
- 6. Kontrollera och efterjustera alla anslutningar. Kontrollera slutligen att både larmutgången och sabotagekontakten tas emot rätt vid centralapparaten.

Ett ganska vanligt misstag är att ställa in för hög känslighet vilket resulterar i falsklarm. Vi rekommenderar därför att inte koppla in detektorn i skarp drift förrän efter några veckor så att inställningen hunnit verifieras.

* Vid montering på tegel/puts/betong skall monteringsplattan MP 550 användas för korrekt reslutat.

#### **TEKNISKA DATA**

| Detektionsradie                                               | Upp till 3m                                     |
|---------------------------------------------------------------|-------------------------------------------------|
| Spänningsområde över detektor i IU-loop                       | 8V i DAG-läge, 6V i NATT-läge                   |
| Strömförbrukning i vila                                       | 2.5 mA                                          |
| Strömförbrukning vid larm                                     | 4.4 mA                                          |
| Larmutgång                                                    | Transistor                                      |
| Larmindikering                                                | LED, DAG/NATT kontrollerad                      |
| DAG och NATT styrning                                         | DAG=8 V, NATT=6 V på slingan                    |
| Larmtid                                                       | Låser i larmläge                                |
| Återställning av larm                                         | Spänningen över detektorn < 1 V                 |
| Sabotageutgång                                                | Transistor                                      |
| Felindikering vid för låg inspänning eller fel i elektroniken | <5V indikeras med blinkande LED                 |
| Miljöklass (EN50130-5:2011)                                   | II                                              |
| Temperaturområde                                              | -40°C till +55°C                                |
| Fukttålighet                                                  | max. 95% RH                                     |
| Kapsling                                                      | ABS Plast i vit färg , IP 42                    |
| Storlek [H x D x B]                                           | 20 x 23 x 80 mm                                 |
| Godkännanden                                                  | EN 50131-2-8 Grad 3, SBSC Klass 3, VdS Klasse C |

#### **BESTÄLLNINGSINFORMATION**

| CD 475                  | E nr. 63 098 92 |
|-------------------------|-----------------|
| Byglingsplint 3041.03   | E nr. 50 153 00 |
| Kopplingsbox 4101.02    | E nr. 50 155 28 |
| Monteringsplatta MP 550 | E nr. 63 098 93 |
|                         |                 |