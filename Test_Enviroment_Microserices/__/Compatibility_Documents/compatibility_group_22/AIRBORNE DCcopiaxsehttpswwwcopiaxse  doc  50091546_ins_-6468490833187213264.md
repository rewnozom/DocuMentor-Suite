# INSTALLATIONSMANUAL

# AIRBORNE DC

Manualen gäller för följande produktvarianter:

**AIRBORNE DC**

Artikelnr: STC 00275

# **AIRBORNE DC MEDIUM**

Artikelnr: STC 00276

# **AIRBORNE DC-E MEDIUM**

Artikelnr: STC 00337

![](_page_0_Picture_9.jpeg)

2544-CPR-30336-F03-20 Rev.1 RED C-353-44-0923-21-01

EN 54-21:2006

Alarm transmission and fault warning routing equipment for fire alarm systems installed in buildings

Airborne DC

Tekniska data: See Doc STD00003 installation Guide Version 17

| 1  | Introduktion 4                                                          |  |
|----|-------------------------------------------------------------------------|--|
| 2  | Ordlista/förkortningar  5                                               |  |
| 3  | Anslutningar  6                                                         |  |
|    | 3.1 Airborne DC 6                                                       |  |
|    | 3.2 Airborne DC Medium (med laddkort) 7                                 |  |
|    | 3.3 Airborne DC-E Medium (med sabotagekort)  8                          |  |
| 4  | Kort installationsprocedur  9                                           |  |
| 5  | Detaljerad installationsprocedur 10                                     |  |
|    | 5.1 SIM-kort och aktivering av abonnemang 11                            |  |
|    | 5.2 Antennplacering och signalstyrka 11                                 |  |
|    | 5.3 Anslutningar (ingångar, kopplingston etc.) 12                       |  |
|    | 5.3.1<br>För snabb överföring av larm12                                 |  |
|    | 5.3.2<br>Telefonanslutning (simulerad PSTN) 12                          |  |
|    | 5.3.3<br>Sabotageskydd för telefonlinje 13                              |  |
|    | 5.3.4<br>Seriekoppling 13                                               |  |
|    | 5.3.5<br>Ingångar – Digitala signaler13                                 |  |
|    | 5.3.6<br>Ingångar – Anslutning av transistorutgångar och reläutgångar14 |  |
|    | 5.3.7<br>Utgångar14<br>5.3.8<br>Sabotagekontakter14                     |  |
|    | 5.3.9<br>Maximalt antal larm  14                                        |  |
|    | 5.3.10<br>Användning av Airborne DC i brandlarmsanläggning (EN 54-21)15 |  |
|    | 5.4 Strömförsörjning15                                                  |  |
|    | 5.4.1<br>STC 00275 Airborne DC15                                        |  |
|    | 5.4.2<br>STC 00276 Airborne DC Medium15                                 |  |
|    | 5.4.3<br>STC 00337 Airborne DC-E Medium15                               |  |
|    | 5.5 Batteri16                                                           |  |
|    | 5.5.1<br>Batteriinformation 16                                          |  |
|    | 5.5.2<br>Övervakning av batteri 16                                      |  |
|    | 5.6 Knappar och brytare på huvudkortet17                                |  |
|    | 5.7 LED-indikatorer på huvudkortet18                                    |  |
|    | 5.7.1<br>Status för LED-indikatorer18                                   |  |
|    | 5.7.2<br>Status för LED-indikatorer på laddkortet18                     |  |
| 6  | Tjänster  19                                                            |  |
|    | 6.1 AddSecure Tekniskt Larm19                                           |  |
|    | 6.1.1<br>AddSecure Flexi Larm-funktioner19                              |  |
|    | 6.1.2<br>SMS-kommandon20                                                |  |
|    |                                                                         |  |
| 7  | Tilläggsprodukter och reservdelar  21                                   |  |
|    | 7.1 Tilläggsprodukter21                                                 |  |
|    | 7.2 Reservdelar21                                                       |  |
| 8  | Tekniska data  22                                                       |  |
|    | 8.1 Mått och vikt22                                                     |  |
|    |                                                                         |  |
|    | 8.2 Miljövariabler22                                                    |  |
|    | 8.3 Antenn, PSTN-gränssnitt och strömförsörjning22                      |  |
|    | 8.4 Ingångar, digitala signaler22                                       |  |
|    | 8.5 Utgångar22                                                          |  |
| 9  | Godkännanden  23                                                        |  |
| 10 | Monteringsmall 24                                                       |  |
| 11 | Felsökning/Diagnostik 25                                                |  |
|    |                                                                         |  |
| 12 | Revideringslogg 26                                                      |  |
|    |                                                                         |  |

![](_page_2_Figure_0.jpeg)

![](_page_3_Figure_0.jpeg)

![](_page_3_Picture_1.jpeg)

Airborne DC är en larmsändare för dig med krav på eller behov av mycket säker larmkommunikation och tillgänglighet via mobilnätet.

Airborne DC är anpassad för seriell överföring av exempelvis SIA från inbrottslarm eller ESPA-444 från brandlarmsanläggningar. Uppringda protokoll baserade på tonsignaler som SIA, Contact-ID och Robofon digitaliseras innan larmöverföring. Med två ingångar/utgångar täcker sändaren de flesta behov för säker larmöverföring.

Alla Airborne larmsändare kan anslutas till AddSecure-servrar (SSE) för säker larmöverföring. Viktiga SSE-uppgifter är:

- Ta emot, logga och behandla alla inkommande larmsignaler.
- Vidarebefordra larm till en eller flera mottagare enligt respektive kunds önskemål.
- Kontinuerligt övervaka att alla anslutna larmsändare fungerar som de ska.
- Automatisk uppdatering av programvaran i larmsändarna.

#### *OBS!*

*Elektronik är generellt känslig för statisk elektricitet. Undvik därför att vidröra komponenter på kretskortet. AddSecure rekommenderar användning av antistatarmband som är anslutet till jord under installationen. Kretskortet ska alltid vara välemballerat och förvaras i antistatisk påse vid transport.*

| SSE       | Secure Service Engine.<br>Den centrala serverparken som säkerställer att AddSecures larmöverföringstjänst alltid<br>fungerar.                                                                       |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Mobildata | Trådlös dataöverföring med kommunikation via mobilnätet.                                                                                                                                            |
| SMS       | Short Message Service (SMS) är en tjänst som fungerar på de flesta mobiltelefoner.<br>Tjänsten gör det möjligt att skicka korta meddelanden (kallas även textmeddelanden)<br>mellan mobiltelefoner. |
| ATS       | Alarm Transmission System: Larmöverföringssystem.                                                                                                                                                   |
| eSIM      | Inbyggt SIM-kort (e står för embedded).                                                                                                                                                             |
| SIM-kort  | (Subscriber Idendity Module)<br>Ett litet smartkort som används i mobiltelefoner och annan mobil utrustning.                                                                                        |

![](_page_5_Figure_0.jpeg)

![](_page_6_Figure_0.jpeg)

![](_page_7_Figure_0.jpeg)

![](_page_9_Figure_0.jpeg)

#### 5.1 SIM-KORT OCH AKTIVERING AV ABONNEMANG

Airborne DC kommunicerar via mobilnätet och behöver därför ett aktivt AddSecure-abonnemang för att fungera.

#### Obs!

- Airborne DC har eSIM (inbyggt SIM-kort).
- SIM-kort ska normalt inte användas.
- Om SIM-kort används har det företräde framför eSIM.
- SIM-kortet får endast tas bort/bytas ut när enheten är helt avstängd, annars kan enheten förlora sin konfiguration. För återställning av konfiguration: Se kapitel 4.

#### **Så kontrollerar du enkelt att abonnemanget är aktiverat och klart att användas:**

Skicka SMS med meddelandet SW 1111. Om du får svar är allt OK. Om inte, kontakta den tekniska supporten.

#### 5.2 ANTENNPLACERING OCH SIGNALSTYRKA

Airborne DC behöver tillräcklig mobiltäckning för att säkerställa stabil drift. Signalstyrkan kan variera och därför är det viktigt att funktionstest genomförs för att kontrollera signalstyrkan där utrustningen ska placeras. Lokal signalstyrka kan enkelt kontrolleras med en vanlig mobiltelefon med Telenor-abonnemang innan monteringen påbörjas. Tre markeringar eller mer på mobiltelefonen är tillräcklig täckning.

#### **Signalstyrkan kan också kontrolleras när Airborne DC är i drift på följande sätt:**

- Kontrollera LED-indikatorerna på huvudkortet till Airborne DC. Röda blinkningar = ingen kontakt med mobilnätet. Snabba gröna blinkningar = enheten är uppkopplad. (1 blinkning = dålig täckning, 5 blinkningar = bäst täckning). Mer information finns i avsnitt 5.7.
- Skicka ett SMS med meddelandet SW 1111 till larmsändaren. Därefter får du ett svar med uppgift om exakt signalstyrka på en skala från noll (sämst) till 31 (bäst).

#### *Obs!*

*Om du använder en extern antenn (utan inbyggd antenn i höljet) ska det alltid finnas isolering mellan antennfoten och underlaget. Bristande isolering kan leda till jordfel på övervakad utrustning (brandlarmscentral).* 

![](_page_11_Picture_0.jpeg)

- 
- *• Robofon*
- *• Scancom Fast*

*För en uppdaterad lista över protokoll, besök www.addsecure.se.*

#### **5.3.1 För snabb larmöverföring**

Ingångar ska användas när snabba larmöverföringar krävs. Detta gäller i system där larmsändaren ska överföra brandlarmshändelser från byggnader i riskklass 5 eller 6.

#### **5.3.2 Telefonanslutning (simulerad PSTN)**

Airborne DC genererar en kopplingston med 40V linjespänning (motsvarande en traditionell, analog telefonlinje). Linjespänningen är tillräcklig för att försörja uppringare som är avsedda för drift från PSTN-linjer.

Den genererade kopplingstonen kan användas för både utgående samtal (ansluten utrustning måste göra "hook-off" för att få ringspänning) och inkommande samtal. Airborne DC bryter linjespänningen om mobiltäckningen är för dålig för larmöverföring i mer än 10 minuter (fabriksinställning).

AddSecure rekommenderar att endast ett system ansluts till larmsändaren.

#### **Airborne DC kan genomföra utgående samtal för överföring av larm:**

#### **Dialer Capture**

*Panel med taleoppkobling*

Dialer Capture används för överföring av larmprotokoll. Airborne DC tolkar de tonsignalerade larmprotokollen och vidarebefordrar dem som digitala signaler via SSE till larmcentralen. Airborne DC kvitterar larmen när de tagits emot och bekräftats på larmcentralen.

Dialer Capture används för överföring. Airborne DC känner normalt av vilka larm- protokoll som används och sparar aktuella inställningar när protokollen identifierats. Om protokollen inte känns av automatiskt kan AddSecure lägga in en konfiguration för det aktuella protokollet via SSE. Dialer Capture stöder bland annat protokollen SIA, Contact-ID, Scancom Fast och Robofon.

*Överföring av larmprotokoll med Dialer Capture måste avtalas med den berörda larmcentralen.*

![](_page_11_Figure_16.jpeg)

*Tale*

*Airborne DC alarmsender*

*Alarm som lydbølger* *Alarmstasjon*

![](_page_12_Picture_1.jpeg)

*Fig. 2: D-sub seriell kabel*

 *Obs! Den röda markeringen på kabeln ska vara vänd mot batteriet.*

![](_page_12_Figure_4.jpeg)

Input X 4,7 kΩ

*Fig. 3: Digitala ingångar*

Input X 4,7 kΩ

0 V

0 V

#### **5.3.3 Sabotageskydd för telefonlinje**

Sabotage av telefonlinjen upptäcks omedelbart av centralenheten genom att kopplingstonen bryts.

För att larmcentralen ska få meddelande om sabotage på telefonlinjen måste ett trådpar (i samma kabel) kopplas till en larmutgång (NC) i centralenheten som termineras på en ingång på Airborne DC. Glöm inte att registrera vilken ingång som används.

#### **5.3.4 Seriekoppling**

Airborne DC har en kontakt för seriekommunikation med RS-232- och I2C-gränssnitt. Det finns stöd för flera protokoll och anpassning till individuella system kan begäras hos AddSecures tekniska support.

#### **Följande tilläggsprodukter finns tillgängliga:**

**STC00358** Kabel med övergång från serieport till D-sub 9-stifts hankontakt.

- **STC00430** Skruvklämma för serieport.
- **STC00424** RS-232/TTL-omvandlare för fjärrservice av Texecom larmsystem.
- **STC00437** Kabel med övergång från serieport till RJ45 för fjärrservice av PowerMax larmsystem.

Max. kabellängd totalt på en RS-232 kabel är 15 meter.

#### **Följande protokoll stöds:**

| ESPA-444                                    | Detaljerad information från brandlarmsystem som kan<br>överföras till larmmottagare. Testad med utrustning<br>från flera ledande tillverkare. |
|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Gunnebo                                     | Kommunikation med Gunnebo larmsystem.                                                                                                         |
| ISA2000                                     | Gränssnitt för konfiguration och programmering av                                                                                             |
|                                             | ISA2000 larmsystem.                                                                                                                           |
| LarmNet                                     | Speciellt gränssnitt för överföring av SIA-koder från                                                                                         |
|                                             | Extronic larmsystem.                                                                                                                          |
| G4S                                         | Kommunikation med larmsystemen S-20 och S-25.                                                                                                 |
| Stanley och Securitas: S3 och S4 Hedengren. |                                                                                                                                               |

Mer information om hur det seriella gränssnittet används kan på begäran erhållas av AddSecures tekniska support.

#### **5.3.5 Ingångar – Digitala signaler**

 Airborne DC har två klämmor (Fig. 3) som kan konfigureras som ingångar och/eller utgångar. Konfigurationen sker från SSE på basis av informationen som angetts på registreringsformuläret för abonnemanget. Som standard definieras portarna som ingångar för digitala signaler. Meddela AddSecures tekniska support om portarna ska användas på annat sätt, t.ex. mot transistorutgångar eller som utgångar. Se Fig. 3 för anslutning av digitala givare.

 Airborne DC kan definiera både spänningstillstånd (+12 V = logisk 1) eller spänningslöst tillstånd som larmtillstånd. Som standard är spänning = normal.

> Meddela AddSecures tekniska support om tillståndet ska vara det omvända. Tänk på att larmsändare och givare har gemensam referens (0 V) då digitala givare används (Fig. 3).

 Obs! Airborne DC tillåter inte konfigurering av ingångar för hantering av enkelbalanserade slingor eller för analoga mätningar. Ingångar och utgångar är inte galvaniskt åtskilda.

![](_page_13_Picture_0.jpeg)

Om en högre gräns för maximalt antal larm önskas, ska detta meddelas före driftsättning. Obs! Kunden står i så fall för trafikkostnader vid larmloopar i enlighet med AddSecures prislista.

## **5.3.10 Användning av Airborne DC i brandlarmsanläggning (EN 54-21)**

Om Airborne DC ska användas i en anläggning enligt kraven i EN 54-21 ska larmsändaren placeras på insidan av brandlarmsskåpet med strömförsörjning via brandlarmssystemet. Brandlarmsystemet ska vara godkänt enligt EN 54-2.

Ingångarna ska användas för överföring av brandlarmshändelser. Därmed säkerställs snabb larmöverföring.

För att uppfylla kraven för drift av brandlarm i byggnader i riskklass 5 eller 6 väljs abonnemangstypen "Fire Care".

# 5.4 STRÖMFÖRSÖRJNING

![](_page_14_Figure_7.jpeg)

*Fig. 6: Strömförsörjning på huvudkortet*

#### **5.4.1 STC 00275 Airborne DC**

Enheterna kräver extern strömförsörjning: + 7,2–28 VDC. Strömförsörjningen ansluts till huvudkortet.

Typisk strömförbrukning i standby är 80 mA så länge ingångarna inte är aktiverade. Den maximala strömförbrukningen vid överföring är ca 250 mA.

#### **5.4.2 STC 00276 Airborne DC Medium**

Med NiMH-batteri: +15–28 VDC Vid användning utan batterier: +10–28 VDC

*Obs! Strömförsörjningen måste vara ansluten till laddkortet (inte huvudkortet). Annars sker varken laddning av batteriet/batterierna eller övervakning av sabotagekontakterna.*

Airborne DC Medium levereras med extern strömadapter.

*Obs! När extern strömadapter används ska det finnas ett lättåtkomligt 230 VAC-uttag i närheten av sändaren.*

Typisk strömförbrukning är 85 mA så länge ingångarna inte är aktiverade. Den maximala strömförbrukningen vid överföring och batteriladdning är ca 500 mA.

## **5.4.3 STC 00337 Airborne DC-E Medium**

Batterier kan inte anslutas. Strömförsörjning till enheten: +7.2–28 VDC.

*Obs! Strömförsörjningen måste vara ansluten till sabotagekortet (inte huvudkortet). Annars övervakas inte sabotagekontakterna.*

Typisk strömförbrukning i standby är 85 mA så länge ingångarna inte är aktiverade. Den maximala strömförbrukningen vid överföring är ca 255 mA.

![](_page_14_Figure_23.jpeg)

*Fig. 7: Strömförsörjning på laddkortet*

+DC 0 V

![](_page_14_Picture_24.jpeg)

*Fig. 8: Strömförsörjning på sabotagekortet (tamper)*

# 5 Detaljerad installationsprocedur

# 5.5 BATTERI (gäller STC 00276 Airborne DC Medium)

![](_page_15_Picture_4.jpeg)

Används inte

*Fig. 9: Batterikontakter*

#### **5.5.1 Batteriinformation**

Airborne DC i Medium hölje innehåller: 1 st 2200 mAh NiMH-batteri.

Ett batteri levererar ström till larmsändaren i upp till 15 timmar efter avbrott i den externa strömförsörjningen. Den exakta drifttiden varierar beroende på flera faktorer, t.ex. batteriets ålder, temperaturförhållanden på plats och om utgångar är aktiverade. Det medföljande batteriet kommer alltid att ha tillräcklig kapacitet för att uppfylla kraven i EN 50136 för minsta drifttid vid användning av reservbatterier, dvs. 12 timmar för grad 1- och 2-anläggningar.

NiMH-batterier ska alltid kopplas till laddningskortet via batterikontakt A eller batterikontakt B (Fig. 9). Det är valfritt att använda batterikontakt A (till höger) eller B (till vänster).

Efter urladdning tar det ca 16 timmar innan batteriet åter är fulladdat, därefter övergår laddaren till underhållsladdning. Vid normal drift med extern strömförsörjning kontrollerar laddkortet regelbundet batteristatus och aktiverar vid behov underhållsladdning.

Batteriets förväntade livslängd är 5–7 år.

## **5.5.2 Övervakning av batteri**

Test med belastning av batteriet utförs var 25:e timme. Dessutom kontrolleras underhållsladdningen kontinuerligt (6,0 V–10,0 V). Efter perioder med enbart batteridrift görs ett nytt test först när batteriet är laddat igen.

Vid fel på batteriet lyser röd LED på laddkortet samtidigt som ett meddelande om batterifel sänds till larmmottagarna. Vid avbrott i den externa strömförsörjningen med batteriurladdning som följd skickas ett meddelande om batterifel innan sändaren helt slutar fungera. När batteriet senare laddas skickas meddelandet "Batteri OK" när kapaciteten når ca 80% av totalkapaciteten.

Obs! Informera AddSecures tekniska support om larmsändare i höljet används utan internt batteri. Det gäller även då Airborne DC-E Medium används.

# 5 Detaljerad installationsprocedur

# 5.6 KNAPPAR OCH BRYTARE PÅ HUVUDKORTET

![](_page_16_Picture_2.jpeg)

*Fig. 10 Knappar*

![](_page_16_Figure_4.jpeg)

*Fig. 11 Positionsbrytare*

![](_page_16_Figure_6.jpeg)

*Fig. 12 DIP-omkopplare DP1 och DP2*

#### **GUL KNAPP: Reset-knapp**

- Aktiverar processorns återställningsfunktion (inte radiomodulen).
- En kort tryckning räcker för att aktivera funktionen.

#### **RÖD KNAPP: Testknapp**

Används för att initiera följande funktioner mot SSE:

- Förbindelsekontroll tryck 2 sek. (RÖD LED blinkar 1 gång).
- • Begär konfiguration för Airborne DC från SSE tryck 5 sek. (RÖD LED blinkar 2 gånger).
- • Radera tidigare konfiguration och ta emot ny från SSE tryck 7 sek. (RÖD LED blinkar 3 gånger).

#### **SVART KNAPP: Kommunikationstest**

Skickar meddelande om bruten mobilförbindelse till SSE.

- • Meddelandet skickas automatiskt vidare till alla mottagare som konfigurerats att ta emot meddelanden om kommunikationsfel. Nästa mottagna meddelande från Airborne DC kommer då automatiskt att generera ett meddelande om att mobilförbindelsen är ok.
	- Håll knappen intryckt i minst 2 sekunder för att aktivera funktionen.

#### **POSITIONSBRYTARE:**

Position 0: Ska alltid stå på position 0 vid användning i AddSecure-nätverket. Position F: Endast för användning utanför AddSecures tjänster och övervakning – ger kopplingston direkt och kräver inte PIN.

#### **DIP-omkopplare**

LED-indikatorerna kan visa olika signaler beroende på positionerna för DIPomkopplare DP1 och DP2 som är placerade ovanför LED-indikatorerna. Se Fig. 12 och tabellen nedan.

| Position = ON (default)                                  | Position = OFF                                                  |
|----------------------------------------------------------|-----------------------------------------------------------------|
| LED-indikatorer aktiva.<br>Fjärrkonfiguration är möjlig. | LED-indikatorer inaktiva.<br>Fjärrkonfiguration är inte möjlig. |
| LED-indikatorer aktiva.                                  | LED-indikatorer aktiva.<br>(enligt EN 54-21).                   |
| GUL LED = Aktivitet<br>RÖD LED = Fel/test                | GUL LED = Fel/test<br>RÖD LED = Aktivitet och kvitterat larm.   |
|                                                          |                                                                 |

![](_page_17_Figure_0.jpeg)

# 5.7 LED-INDIKATORER PÅ HUVUDKORTET

![](_page_17_Figure_2.jpeg)

*Fig. 13 LED-indikatorer*

- **5.7.1 Status för LED-indikatorer**
#### **GRÖN LED – Strömförsörjning**

- Ska lysa vid normal drift (Obs! Inte på STC-00275).
- PÅ: Enheten drivs från extern strömkälla.
- AV: Enheten drivs inte från extern strömkälla.
- Om andra LED-indikatorer lyser går enheten på batteridrift.
- Om inga andra LED-indikatorer lyser är enheten strömlös.

#### **GRÖN LED – Signalstyrka**

Ska blinka vid normal drift.

- Maximalt antal blinkningar är 5, vilket indikerar att signalstyrkan är mycket bra (mer än -53 dBm).
- Ingen blinkning indikerar att signalstyrkan är för dålig (-113 dBm) för normal drift.
- Rekommenderad lägsta signalstyrka motsvarar 2 gröna blinkningar.

#### **BLÅ LED – Förbindelse med SSE**

Ska lysa vid normal drift.

- PÅ: Förbindelsen med SSE är OK.
- Blinkar varje sekund: Avbruten förbindelse.
- Ska lysa med fast sken när anläggningen lämnas.
	- AV: Förbindelsen med SSE är bruten.

*Prova att trycka på den RÖDA knappen i 2 sekunder om den blinkar (förbindelsekontroll). Om allt annat är testat och ok ska den normalt lysa med fast sken.*

#### **GUL LED – Aktivitetsindikator**

Ska normalt vara släckt.

- Fast sken: Meddelanden i utgående kö som väntar på att bli skickade.
- Tänds en kort stund varje gång larm/bekräftelse ska skickas.
- När den slocknar är det en bekräftelse på att larmet/bekräftelsen gått fram.

#### **RÖD LED = Fel/testindikator**

Ska normalt vara släckt.

- Blinkar långsamt: Airborne DC har inte kontakt med mobilnätet.
- Blinkar snabbt: Allvarligt fel, t.ex. SIM PIN-fel.
- Testblinkning: Röd LED lyser när testknappen används.

#### **5.7.2 Status för LED-indikatorer på laddkortet**

#### **RÖD LED – Batterifel:**

Ska normalt vara släckt.

- Blinkar med frekvensen 1 Hz vid något av följande tillstånd:
- 1. Spänningen på anslutet batteri är för hög.
- 2. Spänningen på anslutet batteri är för låg.
- 3. Belastningstest för anslutet batteri har misslyckats.

*Fig. 14 LED-indikator på laddkort*

![](_page_17_Picture_42.jpeg)

# 6.1 ADDSECURE TEKNISKT LARM

AddSecure Tekniskt Larm är en tilläggstjänst. För Airborne DC larmsändare kan även abonnemanget/tjänsten Flexi Larm användas. Detta möjliggör styrning av utgångar och läsning av status på in-/ utgångar.Tjänsten stöds av nya konfigurationsmöjligheter och gränssnitt för SMS-kommando.

#### **6.1.1 AddSecure Flexi Larm-funktioner:**

- Styrning av utgångar (AV/PÅ) med SMS-kommando.
- Rapportering av status för in-/ utgångar med SMS-kommando.
- Läsning av sändarparametrar samt ändring av PIN-kod med SMS-kommando.
- Lokal utgångsstyrning. Utgångar kan triggas av ingångar.

#### **6.1.2 SMS-kommando och svar**

#### **Allmänt:**

- **Namnet på SMS-kommandot:** (små bokstäver kan användas)
#### **– Beskrivning av och exempel på SMS-kommando** Namn: En del kommandon har flera alias som betyder samma sak.

 Parametrar: Mellanslag åtskiljer kommando och parametrar. AV och PÅ-kommando kan styra mer än en utgång, utgångar åtskiljs med ( ,/eller - ). Värdet A betyder alla utgångar. Tidsfördröjning (0–99) måste anges med T,M,S (Timmar, Minuter, Sekunder).

 *Exempel: T1M15S30 = 1 timme, 15 minuter, 30 sekunder M15S30 = 15 minuter, 30 sekunder S30 = 30 sekunder* 

Alla kommandon kräver användarens PIN-kod som sista parameter.

#### **– Svar**

 Fel användar-PIN: Resulterar i "tamper"-larm och svaret "Error, invalid PIN code".

 Okänt kommando: Resultat i svaret "Error, unknown command".

# 6 Tjänster

SMS-KOMMANDO OCH SVAR

| KOMMANDO              | BESKRIVNING OCH EXEMPEL                                                                                                                                                                                                                                                       | SVAR FRÅN TERMINALEN                                                                             |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| PÅ<br>PA<br>ON        | Aktivering av en, flera eller alla utgångar.<br>Om tidsstyrning specificerats, aktiveras utgången/<br>utgångarna inom angiven tid.<br>PÅ 1 1234 (ställ utgång 1 PÅ)<br>ON 2 T2M30 1234<br>(ställ utgång 2 PÅ i 2 timmar och 30 minuter)<br>ON A 1234 (ställ alla utgångar PÅ) | OK, output control executed                                                                      |
| AV<br>AF<br>OFF<br>OF | Motsatsen till PÅ. Observera att tidsstyrd AV medför<br>fördröjd aktivering (PÅ).<br>AV 1 1234 (ställ utgång 1 AV)<br>OFF 2 M45 1234<br>(ställ utgång 2 PÅ efter 45 minuter, "fördröjd aktivering")<br>OFF A 1234 (ställ alla utgångar AV)                                    | OK, output control executed                                                                      |
| ST<br>STAT<br>STATUS  | Returnerar med status på alla ingångar och utgångar.<br>STATUS 1234                                                                                                                                                                                                           | Status:<br>IN01=76, IN02=1, IN03=+16%,<br>IN04=!+26C, IN05=-15C,<br>IN06=+13C, IN07=1293, IN08=0 |
| PIN                   | Ändra användar-PIN.<br>Den nya PIN-koden ska bestå av 4–8 siffror.<br>PIN 456789 1234<br>("PIN" "NY PIN" "GAMMAL PIN")                                                                                                                                                        | OK, new PIN stored                                                                               |

# 7.1. TILLÄGGSPRODUKTER

#### **Följande tilläggsprodukter kan beställas till Airborne DC:**

| STP 00631 | Antenn med spets (7,5 cm), rundstrålande, 2,3 m kabel, SMA-kontakt.                                |
|-----------|----------------------------------------------------------------------------------------------------|
| STP 00637 | Riktningsstyrd utomhusantenn, 5 m kabel, SMA-kontakt.                                              |
| STP 00656 | Övergång MMCX- till SMA-antennkontakt.                                                             |
| STC 00186 | Antennförlängningskabel 10 m, SMA-kontakt.                                                         |
| STM 00072 | Monteringsfäste för Airborne DC i centralenhet.                                                    |
| STE 00358 | Övergång från 16-stifts serieport hane till D-sub 9-stifts hankontakt.                             |
| STE 00430 | RS-232-gränssnitt med skruvklämma för serieport.                                                   |
| STE 00424 | RS-232/TTL-omvandlare. För fjärrdrift av Texecom larmsystem.                                       |
| STE 00437 | Övergång från 16-stifts serieport hane till RJ45, 30 cm.<br>För fjärrdrift av PowerMax larmsystem. |

#### 7.2. RESERVDELAR

#### **Följande reservdelar lagerförs normalt av AddSecure för leverans till Airborne DC:**

| STP 00586 | 15 VDC extern strömadapter.                       |
|-----------|---------------------------------------------------|
| STE 00376 | Batteripaket typ NiMH 2200 mAh.                   |
| STP 00630 | PCB-antenn, för montering i plasthöljet (Medium). |

# 8.1 MÅTT OCH VIKT

| MODELL                              | MÅTT PRODUKT<br>(BxHxD) | MÅTT KARTONG<br>(BxHxD) | VIKT<br>Produkt | VIKT<br>Inkl. kartong |
|-------------------------------------|-------------------------|-------------------------|-----------------|-----------------------|
| Airborne DC<br>(STC 00275)          | 105x60x27 mm            | 23x15x4 cm              | 0,065 kg        | 0,200 kg              |
| Airborne DC Medium<br>(STC 00276)   | 170x160x60 mm           | 25x22x7 cm              | 0,750 kg        | 1,250 kg              |
| Airborne DC-E Medium<br>(STC 00337) | 170x160x60 mm           | 25x22x7 cm              | 0,443 kg        | 0,810 kg              |
| Strömadapter 15 VDC                 | 30x80x90 mm             | 11x9x3,8 cm             | 0,120 kg        | 0,135 kg              |

# 8.2 MILJÖVARIABLER

**Temperaturområde drift:** Från -10 till +50 grader Celsius **Luftfuktighetsområde drift:** Från 10 % till 90 % relativ fuktighet (inte kondenserande)

# 8.3 ANTENN, PSTN (TELEFON)-GRÄNSSNITT OCH STRÖMFÖRSÖRJNING

| Antenntyp:        |            | RF-signal (Dual band) MMCX-kontakt |  |  |
|-------------------|------------|------------------------------------|--|--|
| Strömförsörjning: | STC 00275: | 7.2–28 VDC                         |  |  |
|                   |            |                                    |  |  |

| Strömförsörjning: | STC 00275: | 7.2–28 VDC |  |
|-------------------|------------|------------|--|
|                   | STC 00276: | 15–28 VDC  |  |
|                   | STC 00337: | 7,2–28 VDC |  |

**Linjespänning, PSTN-linje:** 40 V ± 2 VDC:

 Försvinner vid bortfall av mobilnätet efter 10 minuter (fabriksinställning).

# 8.4 INGÅNGAR, DIGITALA SIGNALER

| SIGNAL     | SPÄNNING            | IMPEDANS                     | KOMMENTAR                                                                          |
|------------|---------------------|------------------------------|------------------------------------------------------------------------------------|
| IoxIn1 – 2 | 0-15 V<br>Max. 15 V | Ingångs<br>impedans<br>75 kΩ | Digital ingång.<br>Tröskelnivå för digitalt läge är ca 1,8 V.<br>(tillstånd 0/1).) |
| 0 V        | 0 V                 | –                            | Negativ retur, gemensam referens för alla ingångar.                                |

# 8.5 UTGÅNGAR

| SIGNAL     | SPÄNNING  | STRÖM       | KOMMENTAR                                           |
|------------|-----------|-------------|-----------------------------------------------------|
| Out1 och 2 | Max. 30 V | Max. 500 mA | Öppen kollektor/zenerdiod som överspänningsskydd.   |
| 0 V        | 0 V       | –           | Negativ retur, gemensam referens för alla utgångar. |

Installationsmanual Airborne DC 22

| PARAMETER/KRAV                                    | NIVÅ                                                         |
|---------------------------------------------------|--------------------------------------------------------------|
| Säkerhetsgrad (EN 50131-1:2006/A1:2009)           | Gr4 ECII*                                                    |
| EN 54-21:2006                                     | Typ 1                                                        |
| EN 54-4:1997/A1:2002/A2:2006                      |                                                              |
| Immunitet mot instrålad störning (EMC)            | 2544-CPR-P20727-F03-16                                       |
| EN 50136-1:2012                                   | ATS:SP4                                                      |
| EN 50136-2:2013                                   |                                                              |
| UMTS                                              | ATS5                                                         |
| EN 50130-4:2011                                   |                                                              |
| EN 50130-5:2011                                   |                                                              |
| SBF110:7                                          |                                                              |
| SSF114:2 Larmklass 2                              |                                                              |
| Rapporteringstid vid strömavbrott (EN 54-4 m.fl.) | Max. 100 sek. (fabriksinställning),<br>ställbar (1–999 sek.) |
| Tillgänglighet (EN 50136-1-1)                     | Klass A4 enligt tabell 4: 99,8 %                             |
| Säkerhet mot ändring (EN 50136-1-1)               | Klass S2 enligt avsnitt 6.5.1                                |
| Säkerhet mot avlyssning (EN 50136-1-1)            | Klass I3 enligt avsnitt 6.5.2                                |
| Klimatklassificering (IEC-60721-3-3)              | Klass 3K5 enligt tabell 1                                    |
| Strömförsörjning (EN 50131-6)                     | Typ A, miljöklass II                                         |
| Strömförsörjning (EN 54-4)**                      | EN 54-4:1997+A1:2002+A2:2006                                 |
| EN 50131-6:2008***                                |                                                              |

#### Anmärkningar:

- *) STC 00275 Airborne DC, STC 00276 Airborne DC Medium är godkända enligt säkerhetsgrad 2.
- **) Produkterna STC 00275 Airborne DC, STC 00276 Airborne DC Medium och STC 00337 Airborne DC-E Medium ska monteras i centralenhet eller batteriskåp enligt denna standard.
- ***) Gäller för: STC 00276 Airborne DC Medium

# **Instruktioner för användning av monteringsmallen:**

- Placera monteringsmallen mot ytan där du vill fästa Airborne DC-enheten.
- Markera monteringsskruvarnas placering med en skruvmejsel eller annat vasst föremål.
- Om du vill använda en sabotagenedrivningskontakt ska plaststyckets placering på väggen också märkas ut.

![](_page_23_Figure_5.jpeg)

| 11 | Felsökning/Diagnostik |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |  |
|----|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
|    |                       | •<br>Kontrollera alla kabelanslutningar.<br>(Om GRÖN LED indikerar dålig mobiltäckning och din mobiltelefon visar<br>god täckning: kontrollera särskilt antennledningen med anslutningar.)<br>•<br>Kontrollera att strömförsörjningen ger rätt spänning (se avsnitt 5.4).<br>•<br>Kontrollera status för LED. Om PIN-koden till SIM-kortet är felaktig blinkar<br>RÖD LED snabbt.<br>•<br>Kontakta vid behov AddSecures tekniska support för kontroll av inkommande<br>meddelanden och driftstatus.<br>•<br>Kontrollera att SIM-kortet är aktiverat. Följ proceduren som beskrivs i avsnitt 5.1.<br>Innan du kontaktar AddSecures tekniska support ska du kontrollera programvaru<br>versionen på Airborne DC genom att skicka ett SMS med följande text till enheten:<br>SW 1111<br>Exempel på svar kan se ut så här:<br>Test59209650, Type: Airborne DC, SW: 1.16.80, Signal: 17,<br>Switch: 0, Power: OK, Battery: OK, Tamper: OK<br>Förklaring:<br>ID<br>= Larmsändarens mobilnummer (ID-nr).<br>Typ<br>= Larmsändarens typ.<br>= Programvaruversion (ska vara version 1.20.74 eller senare).<br>SW |  |
|    |                       | = Signalstyrka på en skala från 0 till 31 (0 = sämst, 31 = bäst).<br>Signal<br>Switch = Positionsbrytare. Normaltillstånd Norge = 0.<br>Power<br>= Status strömförsörjning.*<br>Battery = Status internt batteri.*<br>Tamper = Sabotagestatus.*<br>*) Om larmsändaren har utrustning för detta.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |  |
|    |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |  |
|    |                       | Teknisk support är tillgänglig alla vardagar 08.00 till 16.00<br>Telefon: 020-32 20 00<br>E-post:<br>Support@addsecure.se<br>Webb:<br>www.addsecure.se                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |  |
|    |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |  |

| Nr | Date       | Revision                                       |
|----|------------|------------------------------------------------|
| 00 | 19.10.2009 | Initial Release                                |
| 01 | 04.06.2010 |                                                |
| 02 | 16.06.2010 |                                                |
| 03 | 09.06.2011 |                                                |
| 04 | 01.09.2011 |                                                |
| 05 | 30.01.2012 |                                                |
| 06 | 02.05.2012 |                                                |
| 07 | 20.09.2012 |                                                |
| 08 | 15.11.2012 |                                                |
| 09 | 18.01.2013 |                                                |
| 10 | 07.06.2013 |                                                |
| 11 | 03.12.2013 |                                                |
| 12 | 25.03.2014 |                                                |
| 13 | 08.08.2014 |                                                |
| 14 | 05.05.2015 |                                                |
| 15 | 19.10.2016 | AddSecure update, new design                   |
|    |            | No support for AC powersupply into chargeboard |
| 16 | 07.09.2017 | General update                                 |
| 17 | 08.11.2021 | General updates related to approvals           |

| Approved by, date<br>Arne Jan Dahl, 10.11.2021   | Status<br>APPROVED       | Title<br>Installationsmanual Airborne DC | Page<br>26  |    |
|--------------------------------------------------|--------------------------|------------------------------------------|-------------|----|
| Prepared by, date<br>Bjørn Rosenberg, 10.11.2021 |                          |                                          | Total<br>26 |    |
| Document                                         | Document No.<br>STD00003 | Rev.<br>17                               |             |    |
| Installationsmanual Airborne DC                  |                          |                                          |             | 26 |