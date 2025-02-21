# **Programmeringsmanual**

![](_page_0_Picture_1.jpeg)

www.kseniasecurity.com

2019-03-06

![](_page_0_Picture_5.jpeg)

|  | INNEHÅLLSFÖRTECKNING |
|--|----------------------|

| INTRODUKTION������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 3       |  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| PROGRAMMERING MED MANÖVERPANEL������������������������������������������������������������������������������������������������������������������������������� 4                                    |  |
| PROGRAMMERING I "PEER TO PEER" MODE (PROGRAMMERING VIA PC)������������������������������������������������������������������������� 5                                                              |  |
| TILLGÅNG TILL SECUREWEB-PORTALEN VIA EN DATOR OCH APPEN KSENIA PRO �������������������������������������������������������� 6                                                                      |  |
| AKTIVERA TALLICENS�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 6           |  |
| PROGRAMMERING VIA SECUREWEB ����������������������������������������������������������������������������������������������������������������������������������������� 6                            |  |
| WEBSERVERNS MENY OCH IKONER������������������������������������������������������������������������������������������������������������������������������������������� 7                           |  |
| ÄNDRA PARAMETRAR������������������������������������������������������������������������������������������������������������������������������������������������������������������� 7              |  |
| ÄNDRA ELLER TA BORT PARAMETRAR �������������������������������������������������������������������������������������������������������������������������������������� 9                            |  |
| AKTIVERA ELLER INAKTIVERA ALTERNATIV ���������������������������������������������������������������������������������������������������������������������������� 9                                |  |
| FÖRTECKNING ÖVER PROGRAMMINGSESSIONER SOM VISAS I WEBSERVER���������������������������������������������������������������� 10                                                                     |  |
| HEM ����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 10   |  |
| RADERING AV SABOTAGEMINNE OCH RELATERADE HÄNDELSER������������������������������������������������������������������������������������ 11                                                          |  |
| RADERA FELMINNEN������������������������������������������������������������������������������������������������������������������������������������������������������������������� 12             |  |
| ALTERNATIV�������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 13            |  |
| ALLMÄNT��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 13  |  |
| NÄTVERK ��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 15 |  |
| GSM/GPRS/PSTN LARMSÄNDARE�������������������������������������������������������������������������������������������������������������������������������������������� 18                           |  |
| HÄNDELSELOGG������������������������������������������������������������������������������������������������������������������������������������������������������������������� 19                 |  |
| HASHTAGS ����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 19          |  |
| OMRÅDEN������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 20           |  |
| BUSSTILLBEHÖR�������������������������������������������������������������������������������������������������������������������������������������������������������������������� 20               |  |
| AUTOMATISK INLÄRNING AV TILLBEHÖR������������������������������������������������������������������������������������������������������������������������������ 21                                 |  |
| VERIFIERA INLÄRNING AV BUSSTILLBEHÖR �������������������������������������������������������������������������������������������������������������������������� 22                                 |  |
| RADERA ETT ELLER FLERA TILLBEHÖR������������������������������������������������������������������������������������������������������������������������������������� 22                           |  |
| PROGRAMMERING AV TILLBEHÖRSPARAMETRAR���������������������������������������������������������������������������������������������������������������� 23                                           |  |
| RADIOTILLBEHÖR ����������������������������������������������������������������������������������������������������������������������������������������������������������������� 25                |  |
| FÖR ATT RADERA EN ELLER FLERA ENHETER������������������������������������������������������������������������������������������������������������������������� 28                                  |  |
| IP KAMEROR �������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 28           |  |
| SYSTEM����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 29       |  |
| TILLKOPPLINGSLÄGEN���������������������������������������������������������������������������������������������������������������������������������������������������������������� 29              |  |
| UTGÅNGAR������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������ 29    |  |
| VALBARA BALANSERINGSVÄRDEN ����������������������������������������������������������������������������������������������������������������������������������������� 31                            |  |
| SEKTIONER������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 32  |  |
| ANVÄNDARE��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 37      |  |
| CONTACT ID MOTTAGARE���������������������������������������������������������������������������������������������������������������������������������������������������������� 40                  |  |
| SIA IP MOTTAGARE ���������������������������������������������������������������������������������������������������������������������������������������������������������������������� 40         |  |
| SCENARIER������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 41  |  |
| HÄNDELSER���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 43     |  |
| KONTAKTLISTA����������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 47       |  |
| MEDDELANDEN ���������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 47        |  |
| REALTID �������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� 51        |  |
| TALMEDDELANDEN������������������������������������������������������������������������������������������������������������������������������������������������������������ 56                      |  |

#### **INTRODUKTION**

Programmering kan ske på följande sätt:

- 1. Fjärr, via portal https://www.kseniasecureweb.com/
- 2. Via webserver lokalt eller i peer-to-peer mode.
- 3. Fjärr via mobila enheter (mobiltelefon, surfplatta) med installatörsappen Ksenia PRO .
- 4. Via manöverpanel: dock är detta begränsat till vissa funktioner.

Till skillnad från den tidigare (lares) plattformen, kan lares 4.0 programmeras via en vanlig webbläsare (t.ex. Chrome, Safari, Firefox, Edge etc.): Vi rekommenderar dock att använda Google Chrome. Att använda en webbläsare underlättar programmeringen och kräver inte stor bearbetningskapacitet eller någon programvara. Användarappen "lares 4.0" för slutanvändaren är också tillgänglig gratis eller laddning via respektive appbutiker.

#### *Notering:*

*"System OK" visas på manöverpanelen första gången, och menyn på engelska visas. I KseniaSecureWerb kan man ändra språk.*

*Installatörsappen Ksenia Pro-appen kan också användas för plattformen "lares WLS 96-IP".*

*Användarappen lares 4.0 app kan inte användas för centralapparat "lares" och "lares WLS" "bara för lares 4.0".*

![](_page_2_Figure_11.jpeg)

# **PROGRAMMERING MED MANÖVERPANEL**

Nedan hittar du de funktioner som kan ändras via manöverpanelen genom att öppna installationsmenyn med **installatörskoden (standard: 123456).**

- Du kan navigera mellan de olika menyerna genom att trycka på knapparna när du har angett **installatörskoden**:
- **• ENTER:** för att komma in i undermenyn.
- **• ESC:** för att lämna en meny och återgå till föregående meny.
- **• NER PIL (SCROLL MEDSOLS) / UPP PIL (SCROLL MODSOLS):** för att stega i menyer.
	- 1 Alfanumeriskt tangentbord med knappar från 1 till
	- 9, * 0 #
	- 2 ESC knapp
	- 3 ENTER knapp
	- 4 Du kan också bläddra genom att använda:
		- 4.1 Vänsterpil
		- 4.2 Nedåtpil
		- 4.3 Högerpil
		- 4.4 Uppåtpil
	- 5 Display

6 RFID område

7 Mikrofon

#### Lista över installatörsmenyns funktioner:

- **• Systemhantering:** För att återställa larm, radera samtalskö samt blockera systemet för att inte utlösa larm. - **Larmåterställning:** Om du väljer det här alternativet stoppas alla larm, och larmminnet raderas.
	- **Radera samtalskö**: Om du väljer det här funktioner (du måste bekräfta det två gånger) raderas alla meddelanden som är aktiva och i kö (SMS, telefonsamtal, e-post etc.).
	- **Systemspärr:** Tryck på ENTER för att komma till de tre undermenyerna:
		- 1. **Inget lås:** Normalt funktionsläge, inga lås finns.
		- 2. **Spärra alla larm:** Blockera alla larm.
		- 3. **Spärra alla åtgärder:** Blockera alla åtgärder.
- **Användarhantering:** Möjlighet att tilldela en RFID-bricka till användare.
- **Händelselista:** Lista med alla händelser som har ägt rum, tillsammans med respektive detaljer.
- **Felstatus:** Lista på fel som finns.
- **Sektionsstatus:** Aktivera visning av alla programmerade sektioner.
- **• Sektionstest:** Användbart under installation. Visa lista över sektioner som aldrig har utlöst ett larm sedan testet började.
- **Installatörsinfo:** Den här menyn innehåller följande undermenyer för hantering av data som är associerade med installationsprogrammet.
	- **Ändra kod:** Ändra installatörskoden.
	- **Beskrivning:** Ändra installationsnamnet.
	- **Nummer:** Ändra installatörens telefonnummer.

Knapp 1 = 1 [mellanslag]? ! , . " ' &

*Notering: Dessa tre senaste funktionerna måste ändras genom att använda manöverpanelen. Se nedan för lista över tecken som är associerade med de olika knapparna.*

> Knapp 2 = A B C a b c 2 \$ @ Knapp 3 = D E F d e f 3 ; < Knapp 4 = G H I g h i 4 = > Knapp 5 = J K L j k l 5 [ ] Knapp 6 = M N O m n o 6 { : Knapp 7 = P Q R S p q r s 7 Knapp 8 = T U V t u v 8 + } Knapp 9 = W X Y Z w x y z 9 Knapp 0 = 0 ( ) / % - _ # * Knapp = raderar tecknet som skrivits in tidigare. Den motsvarar backspace på PC-tangentbordet. Knapp # = raderar allt som har skrivits.

- **Uppdatering:** installera uppdatering av centralapparat genom att ladda upp filen som finns på SD-kortet och som tidigare har hämtats från www.kseniasecurity.com**.**
![](_page_3_Figure_37.jpeg)

#### **Backup:**

- **Skapa ny backup:** Skapa en ny backup kopia och spara filen på ett SD-kort.
- **Återställning från backup:** Ladda upp en programmering från SD-kortet.

#### **Nätverk: Meny för nätverksparametrarna som kan läsas / ändras.**

- **IP-adress:** Centralapparatens IP-adress.
- **Subnätmask:** Subnätmask.
- **Gateway:** Gateway IP-adress.
- **DHCP-server:** För att aktivera DHCP om centralapparaten är inställd på en fast IP-adress.
- **Språk:** Välja manöverpanelens språk.
- **Vers. centralapparat:** Se firmwareversionen i centralapparat (men inte webbservern).

# **PROGRAMMERING I "PEER TO PEER" MODE (PROGRAMMERING VIA PC)**

Programmering av funktioner med någon av de metoder som beskrivs på (sidan 3) med undantag för att använda manöverpanel och generera talmeddelanden: Talmeddelanden kan endast användas med en Loquendo USB-minnesticka (den som används för lares / basis) eller genom att aktivera en tallicens via SecureWeb.

Vänligen se relevant avsnitt för att generera talmeddelanden via en lokal anslutning och en Loquendo USB-minnesticka.

Centralapparaten har DHCP aktiverad som standard, därför finns det två möjligheter att ta reda på IP-adressen:

- 1. Via manöverpanel, tryck installatörskod och stega till IP-adress.
- 2. Genom att använda servernamnet https: // KS-BOARD-xx-yy-zz (genom att byta xx-yy-zz med de sista sex siffrorna i MAC-adressen som skrivs ut på centralapparaten etikett).

#### Notering:

- Standardadressen kommer alltid att vara 192.168.2.97 om nätverket som centralapparaten är anslutet till inte stöder DHCP. Centralapparaten kommunicerar som standard endast i säkert läge (https) via port 443.
- Var vänlig skriv https://192.168.2.97 för att komma åt centralapparaten om DHCP inte stöds.
- Installatörskoden är som standard för att komma åt konfigurationsinställningarna är 123456.
- Det är INTE möjligt att utföra en konfiguration om systemet via fjärr om användaren har **inaktiverat åtkomst** med hjälp av installatörskoden.

# **Tillgång till SecureWeb-portalen via en dator och appen Ksenia PRO**

Uppgifterna som krävs för att komma åt SecureWeb-tjänsten "https://www.kseniasecureweb.com " är densamma som som används för att logga in på webbplatsen **http://www.kseniasecurity.com**. Om du inte redan har ett konto gå till https://www.kseniasecureweb.com och klicka på Register.

**Förslag 1:**

- 1. Logga in på molntjänst https://www.kseniasecureweb.com.
- 2. Klicka på Devices.
- 3. Skriv in serienummer för centralapparaten i rutan "Serial Number".
- 4. Ge larmsystemet ett namn och en beskrivning.
- 5. Klicka på "Register new panel"

#### **Förslag 2:**

- 1. Öppna appen "Ksenia PRO".
- 2. Klicka på symbolen (+) i nedre högra hörnet (Android) eller i det övre vänstra hörnet (IOS).
- 3. Skriv serienummer eller klicka på kameran i telefonen för att skanna QR koden (finns på centralapparatens etikett).
- 4. Ge systemet ett namn och en beskrivning.
- 5. Klicka på "Spara".

Centralapparaten är nu redo att konfigureras med hjälp av SecureWeb och den kommer att visas i listan över enheter.

# **Aktivera tallicens**

För att skapa talmeddelanden för "lares WLS" och "lares 4.0" krävs en tallicens. Denna tallicens kan bara användas i SecureWeb portalen (vänligen se (s. 56) → för peer-to-peer-läge och avsnittet om talmeddelanden). Denna funktion aktiveras med hjälp av ett nummer som finns på ett skrapkort som säljs separat.

För att aktivera tallicensen måste du:

- 1. Gå till www.kseniasecureweb.com.
- 2. Klicka på licenser.
- 3. Registrera en ny licens.
- 4. Skriv in serienumret som finns på skrapkortet.
- 5. Välj det objekt du behöver.

# **Programmering via Secureweb**

Programmering via Secureweb kommer att förklaras i denna manual, och det är också möjligt att hantera talmeddelanden via detta läge.

Samma möjligheter gäller även för appen Ksenia Pro. Välj den enhet som ska konfigureras när du har loggat in på portalen och klicka på knappen i kolumnen "Ändra konfiguration". Installatörskoden måste anges (standard 123456): ange den här koden för att komma åt centralapparatens webbserver.

# **Webserverns meny och ikoner**

När du loggar in kommer du att se att två kolumner på skärmen: Menyer till vänster och programmering till höger.

Följande ikoner kommer att visas:

| Ladda konfiguration från en tidigare sparad fil, filerna har (.bck) -tillägget.                                                                                                  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Spara centralapparatens konfiguration som (.bck) -filen.                                                                                                                         |
| Öppna programmering.                                                                                                                                                             |
| Återgå till inloggningssidan utan att spara några ändringar.                                                                                                                     |
| Ändra parametrar                                                                                                                                                                 |
| Nedan beskrivs proceduren för att ändra alla parametrarna "lares 4.0" och gäller alla webbserverns sidor.                                                                        |
| Klicka på ikonen för att ändra parametrarna:                                                                                                                                     |
|                                                                                                                                                                                  |
| Skärmen visar nu följande:                                                                                                                                                       |
|                                                                                                                                                                                  |
|                                                                                                                                                                                  |
|                                                                                                                                                                                  |
| För att stänga programmeringsessionen som är kopplad till sidan om den är öppen.<br>Detta kommer att visas när ingen av alternativen har ändrats.                                |
|                                                                                                                                                                                  |
| Menyradens status ändras när en eller flera parametrar har ändrats:                                                                                                              |
|                                                                                                                                                                                  |
|                                                                                                                                                                                  |
|                                                                                                                                                                                  |
| Avbryta:<br>Eventuella ändringar som inte sparats kommer att gå förlorade och kan inte hämtas tillbaka.<br>Klicka på "Avbryta" för att bekräfta detta val.                       |
| Spara sessionen:<br>Ändringar kommer att sparas i centralapparaten och två ikoner kommer att aktiveras som tillåter ytterligare<br>alternativ när du klickar på "Spara session": |
|                                                                                                                                                                                  |
|                                                                                                                                                                                  |

![](_page_7_Figure_0.jpeg)

# **Ändra eller ta bort parametrar**

Klicka på ikonen och på parameterar som kräver ändring.

Du kan sedan ange de nya inställningarna och spara dem som beskrivits ovan.

Det är också möjligt att radera en eller flera parametrar som tidigare har konfigurerats:

| Klicka på ikonen för att radera parametrarna om programmeringsessionen ännu inte är öppen. Skärmen kommer<br>nu att visa:                               |  |  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                                                                                                                                                         |  |  |
|                                                                                                                                                         |  |  |
|                                                                                                                                                         |  |  |
| Klicka på den här ikonen för att radera det valda objektet. Du kommer att behöva bekräfta detta två gånger.                                             |  |  |
| Aktivera eller inaktivera alternativ                                                                                                                    |  |  |
| I vissa fall kan det hända att du måste välja om du vill aktivera eller inaktivera en viss parameter.<br>Alternativ aktiverat<br>Alternativ deaktiverat |  |  |
| Säkringsfel: alternativet aktiverat                                                                                                                     |  |  |
| Säkringsfel: alternativet är inaktiverat                                                                                                                |  |  |
|                                                                                                                                                         |  |  |
|                                                                                                                                                         |  |  |
|                                                                                                                                                         |  |  |
|                                                                                                                                                         |  |  |
|                                                                                                                                                         |  |  |
|                                                                                                                                                         |  |  |
|                                                                                                                                                         |  |  |
|                                                                                                                                                         |  |  |
|                                                                                                                                                         |  |  |
|                                                                                                                                                         |  |  |
|                                                                                                                                                         |  |  |

# **Hem**

Du hittar all information om centralapparaten i denna session (enhet, områdesstatus, realtid etc.) tillsammans med de tio senaste händelserna som lagras i minnet.

Om det finns uppdatering av firmware- och webbserver så visas detta med ( ). För att uppdatera: Klicka på ikonen ( ). Klicka på ikonen och vänta tills processen är klar.

Nedan hittar du några exempel på ikonerna och menyerna som visas på webbservern beroende på pågående händelser:

1) Följande fönster visas när det inte finns några fel. I det här exemplet är systemet frånkopplat.

![](_page_9_Figure_6.jpeg)

2) Visas när det finns fel:

I det här exemplet har även systemet frånkopplats.

![](_page_9_Figure_9.jpeg)

# 3) System är tillkopplat och larm har utlösts. 7) Visas när sabotagelarm har återställts

![](_page_9_Picture_11.jpeg)

4) Visas när det finns ett systemfel och / eller sabotage och larmstatusen visar sabotage aktivt (t ex sirener ljuder). Om du klickar på rullgardinsmenyn längst ned till höger visas fel eller mer information.

![](_page_9_Figure_13.jpeg)

5) Det här fönstret visas när det har funnits ett sabotage i systemet, men att ett aktivt sabotagelarm inte längre finns, bara minnesindikering. Om du klickar på rullgardinsmenyn längst ned till höger så visas mer information.

![](_page_9_Picture_15.jpeg)

6) Lista över systemsabotage:

En eller flera sektioner i exemplet har utlöst sabotage samt att det finns eller har funnits ett avbrott i nätverksuppkopplingen.'

![](_page_9_Picture_18.jpeg)

(sabotageminne), men att ett utlöst aktivt larm kvarstår (röd klocka).

![](_page_9_Picture_20.jpeg)

8) Visas när det finns ett sabotageminne. Om du klickar på rullgardinsmenyn i det nedre högra hörnet kommer du att lista systemets sabotageminnen.

![](_page_9_Picture_22.jpeg)

9) Lista över fel eller systemfel. I detta fall visas meddelande om fel på en eller flera sektioner. Flera händelser kan visas.

| Status<br>fel |           |  |  |
|---------------|-----------|--|--|
|               | Sektioner |  |  |

#### 10) Förteckning över systemets sabotageminne. I det här fallet gäller det ett sabotageminne på en sektion. Flera händelser kan visas.

# **Radering av sabotageminne och relaterade händelser**

Om du vill rensa sabotageminnen gör som följer:

- 1. Tryck installatörskod på manöverpanelen.
- 2. Stega till **"Systemhantering"** och tryck **ENTER.**
- 3. Stega till **"Återställa larm"** och tryck **ENTER.**

Upprepa stegen ovan för att radera eventuella sabotageminnen från webbservern och manöverpanelen.

1) Detta visas först när sabotageminne återställts. Det visas inte på webbservern eller på manöverpanelen.

![](_page_10_Picture_12.jpeg)

2) Visas när batterispänningsnivån sjunker under tröskeln (<11V) eller om batteri inte längre är anslutet.

![](_page_10_Picture_14.jpeg)

3) Visas när det finns ett systemfel. Om du klickar på rullgardinsmenyn längst ned till höger visas en lista på fel eller systemskillnader.

![](_page_10_Picture_16.jpeg)

4) Lista över fel eller systemskillnader. I detta fall gäller meddelandet sabotage i en eller i flera sektioner. Flera händelser kan visas.

| Status<br>fel |           |  |  |
|---------------|-----------|--|--|
|               | Sektioner |  |  |

5) Visas när fel har återställts: Felminnet kommer då att visas. Genom att klicka på rullningsmenyn i nedre högra hörnet för att visa systemfelsminnen.

![](_page_10_Picture_20.jpeg)

6) Lista på över systemfelsminnen. I detta fall visas minne för ett lågt batteri. Flera händelser kan visas.

| Status | Sabotage (Minne) |  |  |  |
|--------|------------------|--|--|--|
| 49     | Sektion          |  |  |  |

#### **Radera felminnen**

För att radera felminnen från webbservern och manöverpanelen måste du:

- 1. Ange installatörskoden.
- 2. Gå till "Felstatus" och tryck på ENTER.
- 3. Visa meddelandet "Inga fel finns".

Felminnet har återställts för både webbservern och manöverpanelen.

Detta indikerar att en annan användare är ansluten via webbservern.

Detta indikerar status för Ethernet-anslutningen:

- Internetanslutning OK (Eth).
- Internetanslutning utan Internet.
- Detta indikerar GSM / GPRS operatören som används och att det är en bra signal.
- Detta indikerar GSM / GPRS operatören som används och att det finns signal, men är halvbra.
	- Det finns ingen GSM- eller SIM-signal.
- Temperaturerna (interna och externa) som rapporteras av sirener på bussen.
- 14.8 Centralapparatens inspänning.
- 14.3 Batterispänning.

# **Alternativ**

Undermenyer i det här avsnittet: Allmänt, nätverk, GSM/PSTN kommunikation.

#### **Allmänt**

# **Systemspråk**

Välj menyspråk. Du kommer att kunna välja språk efter ditt land.

# **Radio**

- **Mottagare i centralapparat:** för att aktivera eller inaktivera den trådlösa mottagaren i centralapparaten. (ej tillgänglig på lares 4.0 - 16 och lares 4.0 - 40 som kräver separat DUO mottagare).
- **Störningströskel (dBm):** Nivå för störningar på radiokanalen, när denna tröskel överskrides kan det indikera att ett sabotageförsök är på gång.

#### **Tillkoppling**

I det här avsnittet kommer du att kunna välja hur larm hanteras och eventuellt förhindra dem vid fel. Larm- och felsignaler hanteras också.

- **Sabotagetimer cyklisk tid:** tiden i minuter som bestämmer den maximala varaktigheten för en sabotagecykel. Dvs den tid en siren ska ljuda när det blir sabotage.
- **• Ta bort larm under varje sektionscykel:** om man väljer denna funktion så kan en sektion utlösa max 1 larm under en områdescykel. Inaktiverar man denna funktion kan en ingång ge obegränsat antal larm.
- **Förbikoppla också sektionssabotage:** inga sabotagelarm kommer att genereras när en sektion har förbikopplats om det här alternativet har aktiverats. Eventuell sabotage kommer inte att loggas i händelseloggen och visas på manöverpanel eller i webbservern.
- **Tillkoppla systemet även fast det finns fel:** grundinställt tillåts inte tillkoppling vid fel och / eller sabotage. Om du väljer denna funktion kan man tillkoppla oavsett fel.
- **Radera larmminne vid tillkoppling:** Larmminnen kommer att raderas vid en tillkoppling, dvs de kommer inte längre att visas på manöverpanelerna.
- **Radera sabotageminne med användarkod:** För att även kunna radera sabotageminne med en användarkod som visas på manöverpanelen (huvudmeny / återställning av larm).
- **Hantera tillbehör som saknas som fel:** ett felhändelse kommer att genereras istället för en sabotagehändelse om en buss eller en trådlös enhet inte längre kommunicerar med centralapparaten om det är fel på enheten eller om den inte längre är ansluten till systemet.

#### **System**

- **Ändra tiden:** det går inte att ändra denna parametrar för närvarande.
- **Datumformat:** Det går inte att ändra denna parametrar för närvarande.
- **Tidsformat:** Det går inte att ändra denna parametrar för närvarande.

### **Talmeddelanden**

**Rubrik:** Ange rubrik för objektet i det här fältet (Huvudkontor, lager, Göteborg ...). Detta meddelande kommer att genereras av talsyntesen och identifiera vilket objekt det är. Det kommer att vara det första som ska spelas upp; (t ex rubrik / sektionslarm / sektion 1).

# **Användare**

- **Ej säker kod:** Om du väljer det här alternativet kommer du att inaktivera kontroll av koden som centralapparaten normalt gör för att förhindra att alltför lätta koder används (till exempel födelsedatum etc.)
**Bekräfta scenario:** när du väljer ett scenario via manöverpanelen (genom att ange koden eller genom att hålla ned den knapp som är associerad med ett scenario, om man har valt att aktivering utan att kod har aktiverats) kommer systemet att utföra det valda scenariot efter tre sekunder om åtgärden inte har bekräftats genom att trycka på enterknappen. Välj det här alternativet om du inte vill ha en automatisk aktivering av scenario, det vill säga om du vill bekräfta val varje gång med ENTER.

#### **Aktivera fel**

I det här avsnittet kan du välja vilka fel som ska ignoreras av centralapparaten och som du inte vill ska visas (exempel: att Ethernet saknas). Dessa är alla aktiverade som standard.

- **• Felminne:** manöverpanelen visar normalt detta när ett fel inte längre kvarstår när detta är valt. Felminnet kan i detta fall bara att raderas av en huvudanvändare eller installatör genom tryck kod och stega till Fellista. Önskas inte detta kan funktionen inaktiveras, då visas inget felminne alls när felet inte kvarstår längre.
**Funktion aktiverad**

**Funktion deaktiverad**

- **• Nätfel:** om nätspänning saknas i centralapparat eller i en bussförstärkare "opis".
- **Låg spänning i en strömförsörjning:** om det är låg spänning i en strömförsörjning.
- **Batteriladdningsfel:** om fel finns i batteriladdningen.
- **• Säkring:** en säkring har löst ut (dvs en kortslutning) i centralapparat eller i "opis" bussförstärkare.
- **• Låg batteri:** Detta uppstår när batterier ("lares", "imago", "radius", "duo" eller "opis") har låg batterispänning eller om tröskel för nivån i de trådlösa enheterna är under driftsgränsen.
- **• Batterifel:** uppstår om centralapparat, sirenerna eller "opis" nätaggregat inte klarar batterietestet. Detta uppstår också när batteriet i trådlösa tillbehör är för lågt.
- **Busstillbehör saknas:** om en eller flera tillbehör på bussen inte längre kommunicerar med centralapparaten.
- **Radiotillbehör saknas:** om en eller flera trådlösa tillbehör inte kommunicerar med centralapparaten, dvs. när övervakningsperioden har överskridits.
- **Sektionsfel:** när en detektor som är balanserad genererar ett övertäckningslarm. Denna händelse kommer att genereras när området som tilldelats sektionen har frånkopplats och sektionen inte har blivit påverkad under en programmerad period för inaktivitet (uttryckt i minuter. Se sektionsprogrammering).
- **• Ethernet saknas:** Detta betyder att Ethernet-kabeln har kopplats från routern / switchen. Dock kan anslutningen till "DNS" eller "molnservern fortfarande vara aktiv (via GPRS-anslutning).
- **Internetanslutning saknas (Eth.):** Ingen internetanslutning trots att kabel är anslutet till Ethernet-nätverket är och fungerar korrekt.
- **PSTN-fel:** PSTN-modul har installerats och aktiverats, men kan inte detektera telefonlinjen.
- **GSM fel / signal saknas:** SIM-kort har gått ut eller är inaktiverat eller om inte GSM-signalen kan detekteras.
- **SIM utgått:** om SIM-kortet är avstängt eller gått ut.
- **Lågt saldonivå:** när SIM-saldo är under tröskelvärde.
- **Kommunikationsfel:** detta inträffar när centralapparaten har misslyckats att ringa programmerade nummer.
- **SIA IP-övervakningsrapportsfel:** detta uppstår när centralapparaten inte längre kommunicerar med SIA IP-mottagaren.
- **Systemfel:** detta uppstår när ett systemfel tvingar centralapparaten att startas om.

# **Strömförsörjning**

**Nätfelsfördröjning (min.):** fördröjningstid i minuter innan rapport kommer att skickas när nätspänning (230VAC) saknas. Felmeddelandet visas omedelbart om det är inställt på noll.

# **Nätverk**

# **Ethernet**

**DHCP:** det här gör det möjligt för centralapparaten att ansluta till ett lokalt nätverk och att konfigurera nätverksparametrar automatiskt. Om DHCP inte är aktiverat måste alla nätverksparametrar anges manuellt.

#### **Webserver**

- **Protokoll:** det här aktiverar / inaktiverar krypteringsprotokollet (TLS), används för att ansluta centralapparaten via webbservern.
- **Port:** port för vilken centralapparaten kommer att kommunicera via (standard 443 för en aktiv TLS , 80 för en inaktiv TLS).

**OBSERVERA Vi rekommenderar inte att du ändrar dessa parametrar om det inte är absolut nödvändigt. Vänligen kontakta nätverksadministratören om så är fallet.**

| NTP                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Aktiverad: Aktivera eller inaktivera anslutningen till NTP-servern (Network Time Protocol).<br>Detta för att se till att klockan uppdaterats automatiskt. Om det behövs kommer du att kunna ändra parametrarna<br>genom att aktivera det här alternativet.                                                                                                                                                                                                                                      |
| Funktion aktiverad                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Funktion inaktiverad                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 1) Servernamn: Det här är den server som används av centralapparaten för att synkronisera tiden.<br>2) Port: Port för NTP-protokollet.<br>3) Övervakningsperiod: Det här är den tidsperiod som löper mellan en kommunikation och en annan från<br>centralapparaten med NTP-servern.<br>4) Retentivperiod vid fel: Detta är tid mellan en kommunikation och en annan i händelse av ett fel<br>OBSERVERA! Vi rekommenderar inte att du ändrar dessa parametrar om det inte är absolut nödvändigt. |
| SMTP                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| • Detta gör att SMTP-servern kan konfigureras, vilket gör det möjligt för centralapparaten att skicka e-post.                                                                                                                                                                                                                                                                                                                                                                                   |
| Funktion aktiverad                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Funktion inaktiverad                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Parametrarna som måste ställas in för att skicka e-post är listade nedan. (De som visas som standard är inte giltiga!)                                                                                                                                                                                                                                                                                                                                                                          |
| Den nya lares 4.0-plattformen kan också hantera e-postadresser som använder SSL- eller TLS-protokoll (t.ex. Gmail)                                                                                                                                                                                                                                                                                                                                                                              |
| Annars kan du skapa ett konto på www.kseniadns.com och använder följande inställningar.                                                                                                                                                                                                                                                                                                                                                                                                         |
| Avsändare: Avsändarens namn måste programmeras i detta avsnitt (exempel: Larmsystem hemma). Vissa mailserverar<br>kan dock kräva att en giltig e-postadress ska anges (till exempel för servrar som inte kräver autentisering).<br>Exempelvis kommer avsändaren att vara följande om du använder inställningarna för "Kseniadns" -servern: (xxxxxx@<br>kseniadns.com)                                                                                                                           |
| • Protokoll: Välj mellan SSL, TLS eller ingen. Kontrollera vilka parametrar som ska användas för mailservern. (SSL om du<br>använder kseniadns).                                                                                                                                                                                                                                                                                                                                                |
| • Port: Kommunikationsporten för protokollet. Kontrollera vilka parametrar som ska användas för mailservern. (465 om<br>du använder kseniadns)                                                                                                                                                                                                                                                                                                                                                  |
| • Användarnamn: Användarnamn för SMTP-tjänsten. Namnet på användaren för "Kseniadns" server som har skapats för<br>att namnge systemet (t.ex. användarnamnet kommer att vara nisse om värdnamnet är nisse.kseniadns.com)                                                                                                                                                                                                                                                                        |
| • Lösenord: Lösenordet som används för SMTP-tjänsten (standard är 123456) för "Kseniadns".                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

# **DDNS**

- **Aktiverad:** Det här aktiverar eller inaktiverar synkronisering med en DDNS-server för att erhålla en dynamisk rublik IP-adress.
![](_page_16_Picture_2.jpeg)

**Funktion aktiverad**

**Funktion inaktiverad**

#### **DynDns-serverns namn och adress:** kseniadns.com

- **DynDns port:** 80
- **Hostname:** nisse.kseniadns.com (exampel: nisse.kseniadns.com)
- **Användarnamn:** användarnamn (exampel: nisse).
- **Kontrollera namn och adress:** checkip.kseniadns.com
- **Kontrollera port:** 80

Du kan också använda en DDNS-server från tredje part om så önskas.

#### **Anslutning till KseniaSecureWeb**

• **Aktiverad:** Detta aktiverar eller inaktiverar anslutningen till SecureWeb-servern

**Funktion aktiverad**

**Funktion inaktiverad**

**Notering: Om du inaktiverar det här alternativet kan du inte längre ansluta till centralapparaten via APP (SecureWeb) och via konfigurationsportalen! Den lokala peer-to-peer- eller fjärranslutningen är endast möjlig via en offentlig IP- eller DDNS-adress och du måste i så fall också öppna portar på routern till centralapparaten tillsammans med alla IP-kameror som är anslutna till systemet.**

**Du kan använda lares 4.0 APP via en lokal eller fjärranslutning (via en publik IP eller DDNS), men du kommer inte att kunna få några PUSH-meddelanden (dessa skickas bara via Ksenia molntjänst).**

# **GSM/GPRS/PSTN larmsändare**

#### **Allmänt**

- **Antal försök:** Antalet uppringningsförsök som sker för varje nummer som har konfigurerats innan en misslyckad kommunikationshändelse ställs ut (även om en bekräftelsen inte har mottagits).
- **Antal repeteringar av meddelanden:** Antalet repetitioner av röstmeddelanden under samma telefonsamtal.
- **Begär bekräftelse:** Uppringning måste bekräftas genom att trycka på (*) på mottagartelefonen när du väljer det här alternativet. I annat fall anser centralapparaten att samtalet har misslyckats och fortsätter till följande nummer som har konfigurerats.
- **Ringer alla nummer:** Röstmeddelanden skickas till alla nummer som har konfigurerats när du väljer det här alternativet. Samtalssekvensen stoppas endast när samtliga nummer i listan har besvarat samtalet. Telefonkön stoppas och avbryts vid en första bekräftelse från någon av användarna om den här funktionen är inaktiverad.

#### **Notering: Systemet kan detektera elektroniska enheter (t.ex. fax- och modem) som ett giltigt svar.**

- **Begär bekräftelse och ringer alla nummer:** Röstmeddelanden skickas till alla nummer som har konfigurerats när de två alternativen kombineras. Uppringning stoppas endast när samtliga nummer i listan har bekräftat samtalet genom att trycka på (*) -knappen.
#### **GSM/GPRS**

**Datatrafik:** Detta möjliggör eller inaktiverar datatrafik på GSM / GPRS. Detta används för att styra systemet om fast nätverk saknas. Den kan också användas som en backupp av det fasta nätet.

**Funktion aktiverad**

**Funktion inaktiverad**

- **APN:** (Access Point Name) är namnet på den åtkomstpunkt som centralapparaten är ansluten till via GPRS / 3G / 4G.
- **Användare:** om det är nödvändigt så ange användarnamnet som krävs för att ansluta till APN.
- **Lösenord**: Om det är nödvändigt så ange lösenord som krävs för att ansluta till APN.

**Notering.: Kontakta din mobilleverantör för GPRS / 3G / 4G-parametrar.**

#### **PSTN**

- **Inaktivera tonkontroll:** Detta inaktiverar kontroll/övervakning av tonkontroll på telefonlinjen.
# **Händelselogg**

I det här avsnittet kan du se och hämta centralapparatens händelselogg.

 **Sök**

Använd sökfunktionen för att filtrera och söka händelser.

#### **Händelser som ska visas**

Ange hur många händelser som ska visas och klicka på knappen ( ) för att begränsa visningen till ett visst antal händelser på sidan.

- **Beskrivning:** Detta ger en kort beskrivning av händelsen. Det föregås av en ikon
# ( ) Allmänna händelser:

- Användarkod igenkänd
- Installatörskod igenkändd
- Scenario utfört
- Start/avslut av programmering
- Start/avslut av konfiguration
- Periodisk rapport
- Kommunikationskö raderad (kommunikationshändelse)

( ) Händelser för:

- Ej godkänd kod
- Låg batteri/batteri återställt
- Nätfel/återställning av nätfel 220 VAC
- Sektionsövertäckning/sektionsfel
- Återställning av sektionsövertäckning/sektionsfel
- Radiotillbehör saknas

( ) Händelser för:

- Förbikoppling/återinkoppling av sektion
- Scenario aktiverat
- Tillkoppling/frånkoppling av område
- ( ) Händelser för:
	- Sektion återställd/larm
	- Larm i område
	- Inpassering i område startad
	- Inpassering i område avslutad
	- Utpassering i område startad
	- Utpassering i område avslutad

( ) Händelser för:

- Sabotage/sektionssabotage återställd
- Sabotage i område återställd
- **Datum:** visar datum och tid när händelsen inträffade.
- **Info:** visar detaljer om händelsen (användaren, enheten som aktiverade den).
- **Bild:** visar bilderna som har sparats tillsammans med händelsen som beskrivs.
	- Genom att klicka på ikonen visas bilderna.

# **Hashtags**

Hashtags är funktioner som kan kopplas till användare, utgångar, sektioner och enheter som används av användare (manöverpaneler och läsare), och kan användas att styra separat upptill åtta utgångar som kan aktiveras för varje händelse.

**Exempel: du kan aktivera de två utgångar (exempel: utgång 1 och utgång 2) individuellt, men du kan aktivera alla utgångar med "#utgång" (eller ett annat fritt konfigurerbart namn) på en gång om de är associerade med "#utgång" hashtag.**

Klicka på ( ) ikonen och sen ( ) symbolen för att programmera hashtagen. Lägg sedan till en beskrivning till utgången. Klicka på ( ) för att lägga till fler hashtags.

# **Områden**

Klicka på ( ) ikonen och sen på ( ) symbolen för att programmera områden, följande kan programmeras:

- **Beskrivning:** Det här är namnet på området (t.ex. skalskydd, volymskydd, lager etc.).
- **Utpasseringstid:** Tid i sekunder för sektioner som programmeras med utgångslogik för att dessa sektioner inte ska utlösa larm under tillkoppling.
- **Inpasseringstid:** Tid i sekunder för sektioner som programmeras med ingångsfördröjning för att dessa sektioner inte utlösa tillkoppling under inpassering.
- **Cykel:** Tid i minuter som bestämmer maximal varaktighet för larmcykeln. Eventuella ytterligare larm i området kommer inte att genereras, inte av centralapparaten under larmperioden och endast en larmhändelse för varje sektion som är associerad med området kommer att genereras. Detta förhindrar att många telefonsamtal eller rapporter att läggas i kö.
- **Varning:** Tid i minuter för varning att detta område tillkopplas av en förprogrammerad kopplingsur (kalender), varningen ljuder i sumrarna i manöverpanelerna.
- **Rondering (min)** Tid i minuter innan området aktiveras igen efter att en kod (bricka) med en väktarattribut har frånkopplat området. När denna tid har gått ut, kommer området att automatiskt aktiveras igen.
- **Område ej tillkopplat:** Tid i timmar för en timer som startar vid en frånkoppling. När denna tid har gått ut och om området inte är tillkopplat vid denna tidpunkt kommer en händelse "Område ej tillkopplat" att genereras. Händelsen kan kopplas till en åtgärd (exempel, att skicka ett e-post meddelande eller utföra en tillkoppling. En bra funktion för att inte glömma bort att systemet tillkopplas.

Klicka på ( ) ikon för att lägga till fler områden.

 **Busstillbehör**

Klicka på ( ) ikonen och sedan på ( ) ikonen för att programmera busstillbehör. Välj sedan den enhet du behöver genom att klicka på ( ) ikonen och skriv sedan serienumret som finns på etiketten på produkten. Klicka på ( ) ikonen för att lägga till ett annat tillbehör som tillhör samma sektion (t ex expansionskort, isolatorer etc.).

# **Expansionskort auxi**

- **auxi:** expansionskort med 5 in/utgångar.
- **auxi 10in:** expansionskort med 10 ingångar.
- **• auxi relä/auxi-L:** expansionskort med 5 utgångar som kan styra 8A.
- **• auxi-H:** expansionskort med 2 utgångar som kan styra 8A och 3 ingångar (+ 2 lokala ingångar som styr utgångar direkt).

#### **Isolator devide**

- **divide:** bussisolator och bussförstärkare.
- **opis:** busströmförsörjning med isolator och förstärkare för busskommunikationen.

 **Mottagare duo**

**duo:** radiomottagare

#### **Manöverpaneler och läsare**

- **ergo-rev.0:** manöverpanel med hårdvaruversion fram till maj 2017.
- **ergo S:** manöverpanel med touch och integrerad temperatursensor.
- **ergo M:** manöverpanel med mekaniska knappar.
- **ergo:** manöverpanel producerad efter maj 2017.
- **volo:** utomhusläsare för utanpåliggande montage.
- **volo-in:** läsare för infällt montage.

#### **Sirener**

- **imago:** en utomhus siren med integrerad temperatursensor.
- **radius:** en inomhus siren med integrerad temperatursensor och nödljus.

#### **Automatisk inlärning av tillbehör**

Du kan lära in tillbehör automatiskt om du inte vet serienumret. Gå till realtid fliken och välj den enhet som du vill lägga till automtiskt.

#### **Tillbehöret måste vara anslutet och spänningssatt!**

Alla tillbehör som har anslutits men som ännu inte har programmerats in, visas i det aktuella fönstret för realtidsvisning och det betyder att tillbehören är redo att läras in. Om enheten inte har anslutits korrekt eller misslyckas med att kommunicera med BUS om fönstret förblir tomt.

Tillbehör är uppdelade per kategori (t ex manöverpaneler, expansionskort etc.)

#### **Detta exempel visar inlärning av en "auxi-L" -kort som är ansluten till bussen:**

![](_page_20_Figure_16.jpeg)

# **Verifiera inlärning av busstillbehör**

Gå till respektive realtidsvisningsmeny för att verifiera att enheten har lärts in korrekt. Klicka på "realtid" och välj sedan "expansionsmoduler" i undermenyn och välj det tillbehör som du just har programmerat.

![](_page_21_Picture_2.jpeg)

Enheten har lärts in korrekt (en ny firmware finns att hämta hem).

Detta visas när en enhet inte längre kan detekteras på bussen eller när ett felaktigt serienummer har angetts.

Ett annat sätt att kontrollera att enheten har lärts in korrekt är att verifiera detta direkt på sidan "Tillbehör":

| Expansion modules     |             |
|-----------------------|-------------|
| Description           | Serial Numb |
| Expansion module auxi | 041922      |

Den enhet som just har lärts in visas tillsammans med sitt serienummer.

Klicka på enheten för att öppna konfigurationssidan för att visa serienumret om numret inte visas (som i "manöverpaneler").

| Tangentbordet "ergo" har lärts in korrekt. |
|--------------------------------------------|
|                                            |
|                                            |
|                                            |

# **Radera ett eller flera tillbehör**

Klicka på ( ) ikonen och sen på ( ) vid den enheten som ska raderas. I detta steg kan välja att avbryta eller fortsätta för att genomföra denna åtgärd (bekräfta två gånger).

| Confirm Remove                            |                   |
|-------------------------------------------|-------------------|
| Are you sure you want to remove the item? |                   |
|                                           | X Cancel / Remove |

# **Programmering av tillbehörsparametrar**

Du måste programmera parametrarna i inlärda tillbehör (t ex manöverpaneler, sirener etc.) för att säkerställa att den fungerar korrekt. Följande är exempel på tillbehör som kräver detta.

Tillbehör som måste programmeras med respektive parametrar är:

#### **Expansionskort**

**auxi, auxi-10, auxi relä/auxi-L, auxi-HT** Parametrar som är tillgängliga är:

- **Beskrivning:** namnet som ges till tillbehöret (t ex lager, kontor).
- **Serienummer:** serienumret som identifierar tillbehöret. Ska tillbehöret bytas ut kan serienumret ändras till det nya för det nya tillbehöret och för att behålla alla tidigare sparade inställningar om enheten byts ut.

Endast följande alternativ är tillgängliga för auxi-HT tillbehör:

- **"I1" för detektering av krosskydd:** i1-ingången kan användas för att anslutas till en sensor (t.ex. en fotocell) om detta alternativ är aktiverat och detta kommer att leda till att stängningsprocessen avbryts och öppnas helt om den har återaktiverats medan gardinen stängs.
- **Förbikoppla ingång "t" under rörelse:** räkneanalysen har avaktiverats och kommer inte att generera några larm om det här alternativet har aktiverats när gardinen är under rörelse.

# **Manöverpaneler**

#### **ergo-rev.0, ergo S, ergo M, ergo**

Parametrar som är tillgängliga för manöverpaneler är:

- **Beskrivning:** namnet som ges till det tillbehöret (t ex entre, lager etc.)
- **Hashtags:** se avsnittet hashtags (sidan 19) i manualer. Det är möjligt att associera flera hashtags.
- **Områden:** välj de områden som är associerade med enheten. En manöverpanel/läsare kan t ex styra villan och en manöverpanel garaget.
- **Serienummer:** Detta är serienumret som identifierar tillbehöret. Uppdatera serienummret för att få det nya tillbehöret för att behålla alla tidigare sparade inställningar om enheten byts ut.
- **Datum och tidsvisning:** detta aktiverar / inaktiverar datum- och tidsvisning på manöverpanelen.
- **• Utetemperaturvisning:** Detta aktiverar eller inaktiverar visning av temperatur från utomhussirener (imago) på displayen.
- **• Inomhustemperaturvisning:** Detta aktiverar eller inaktiverar visning av temperatur från inomhussirener (radius) på displayen.
- **GSM-operatör:** detta aktiverar / inaktiverar GSM-operatör på displayen (om GSM / GPRS-sändaren har konfigurerats i systemet).
- **Områdesstatus på display:** detta aktiverar / inaktiverar status för områden på displayen som är associerade med manöverpanelen. Man kan se status för områden genom att trycka på ( ) -knappen.
- **Sektionsstatus på display:** detta aktiverar / inaktiverar status för sektioner på displayen som är associerade med manöverpanelen. Man kan se status för sektioner genom att trycka på ( ) -knappen.
- **Meddelanden visas med kod:** Systemstatus visas inte på displayen automtiskt när du väljer det här alternativet (SYSTEM OK, LARM, SABOTAGE, etc.) , visas först när en giltig kod har angetts.
- **Ljud under utpassering:** detta aktiverar / inaktiverar den akustiska signalen i manöverpanelen under utpasseringstiden.
- **Ljud under inpassering:** Detta aktiverar / inaktiverar den akustiska signalen i manöverpanelen under inpasseringstiden.
- **Sirenkontroll:** detta aktiverar / inaktiverar den akustiska signalen i manöverpanelen som hör samman med sektionerna som hör ihop med sirenen.
- **Varningsljudkontroll:** Om summer ska ljuda i manöverpanelen under tillkoppling via kalender.
- **Ljusstyrka:** I det här avsnittet kan du justera manöverpanelens ljusstyrka. Ljusstyrkan kan justeras i tre steg: låg, medium, hög. Välj det låga läget om du vill att manöverpanelens belysning ska vara helt avstängt när den inte används.
- **Volym:** I det här avsnittet kan du justera högtalarens volymnivå. Volymen kan justeras i fyra steg: låg / medium / normal / hög / av.
- **• CapSense-känslighet:** känslighetsnivån för knappar. Känsligheten kan justeras i tre steg: låg / medium / hög. DETTA ÄR INTE tillgängligt för Ergo M!

- **Snabbval:** Snabbval av funktion för knappar för att snabbt välja ett scenarie och bestämma om det ske med eller utan en kod (alla är inställda som standard för att ske med en kod). Du kan ändra konfigurationen genom att klicka på de olika knapparna.
![](_page_23_Picture_1.jpeg)

I det här fallet är alternativet utan kod aktiverat medan alternativet med kod är inaktiverat. Knappen blir helt blank när du avaktiverar båda alternativen och detta indikerar att den inte har konfigurerats och därför inte kan användas. Det går att välja scenariot från manöverpanelen antingen med en kod eller genom att trycka direkt på knappen om båda alternativen har aktiverats.

**Utan kod:** tillåter möjligheten att aktivera det associerade scenariot genom att trycka och hålla ned den associerade knappen. Om alternativet "Bekräfta scenariet utförande" är aktiverat, tryck på ENTER för att bekräfta valet, annars i slutet av 3 sekunder, kommer åtgärden att utföras automatiskt.

**Med kod:** tillåter du att utföra åtgärden först efter att har angett koden (t.ex. kod / knapp 1).

#### **Utomhussirener**

#### **imago**

Parametrarna som är tillgängliga för "imago" sirener är:

- **Beskrivning:** Namnet som ges till enheten (t.ex. utomhussiren, etc.)
- **Serienummer:** Detta är serienumret som identifierar tillbehöret. Uppdatera serienummret för att det nya tillbehöret ska behålla alla tidigare sparade inställningar om enheten byts ut.
- **Max larmtid:** Maximal larmtid vid strömavbrott.
- **• Busskontroll:** Om detta alternativ väljs kommer sirenen att avge ljud- och ljussignalen i avsaknad av kommunikation med centralapparaten i mer än 10 sekunder.
- **Temperatursensor:** Om avstängt, skickar sirenen inte temperaturen till centralapparaten och den yttre temperaturen kommer inte att visas på manöverpanelen (detta är användbart om det finns två sirener och en är installerad i en position som är utsatt för solen, vilket leder till falsk utetemperaturmätning).
- **Obs! Om det här alternativet "Temperaturgivare" är aktiverat på sirenen men displayen på manöverpanelen är avstängd (se displayens utomhustemperatur), kommer temperaturen inte att visas.**
- **• Dubbeltonssiren:** Om detta alternativ är vald ljuder summern med två distinkta frekvenser, om inte så sveper summern genom flera frekvenser.

#### **Inomhussirener**

#### **radius**

Parametrarna som är tillgängliga för "radius" sirener är:

- **Beskrivning:** namnet på enheten (t.ex. inomhus siren, etc.)
- **Inaktivera siren om inte alla områden är tillkopplade:** Områdestillhörighet för inomhussiren radius. Om listan för områdestillhörighet inte är tom kommer sirenen att ljuda endast om alla områden i listan är tillkopplade. Detta är användbart om en siren inte ska ljuda under natt eller dagläge, dvs när man är hemma. Om en "alltid aktiv" (24h) ingång tillhör ett område som är valt på inomhussirenen radius, kommer sirenen ej ljud när ingången går i larmläge.
- **Serienummer:** Detta är serienumret som identifierar tillbehöret. Uppdatera serienummret för att få det nya tillbehöret för att behålla alla tidigare sparade inställningar om enheten byts ut.
- **Max larmtid:** Maximal larmtid vid strömavbrott.
- **• Fast LED:** När denna funktion är vald så kommer lysdioden att lysa fast istället för blinka om den virituella utgången som är kopplad till utgång "Endast LED" aktiveras.
- **Använd nödbelysning:** Om denna funktion används kommer lysdioden i sirenen att lysa fast vid nätbortfall. Denna funktion kräver att ett batteri är anslutet i sirenen.
- **Inaktivera temperatur kontroll:** Om denna är vald kommer inte sirenen att skicka temperaturer till centralapparaten och kan således inte visas på manöverpanelerna för kontroll av temperaturer utomhus. Detta är använbart om två utomhussirener används och en är monterad på en vägg utsatt för solljus, vilket kan påverka temperaturkontrollen.

# **Radiotillbehör**

De trådlösa enheterna är grupperade efter typ och identifieras separat.

För att programmera radiotillbehör, klicka på ikonen ( ) och sen på symbolen ( ). Välj sedan den enhet du behöver genom att klicka på ( ) symbolen och skriv sedan serienumret på den tillbehörsetiketten. För att lägga till en annan enhet som tillhör samma sektion (t.ex. trådlösa sensorer, trådlösa I / O-moduler etc.), klicka igen på symbolen ( ). Annars, för att avsluta sessionen, klicka på( ).

För vissa trådlösa enheter är det nödvändigt att programmera övervakningstiden.

Övervakningsintervallet representerar den maximala tiden som går mellan två sändningar av samma trådlösa enhet, även om det inte har skett någon statusändring, som till exempel ett larm. Dessa periodiska kommunikationer används av centralapparaten för att verifiera funktionen av alla trådlösa enheter. Ju högre detta värde är ju sämre säkerhet då man har mindre koll på de trådlösa enheterna. Å andra sidan kan programmering av ett mycket lågt värde förkorta batteritiden på grund av mer frekvent överföring av enheterna. Beroende på det programmerade värdet, varierar beteende i centralapparaten när meddelanden avseende radiokommunikationsfel eller manipulering som beskrivs nedan. Om de trådlösa enheterna programmeras med ett övervakningsintervall som är lika med 1 minut, genererar centralapparaten ett "radiofel" och händelsen "förlust av trådlös enhet" om den inte får någon överföring inom 100 sekunder. Om alla trådlösa enheter programmeras med ett övervakningsintervall på mer än 1 minut genereras händelsen "förlust av trådlös enhet" först om centralapparaten inte får någon överföring från ett tillbehör under en period som är lika med den högre än 2 timmar och det dubbla intervallet om övervakningen är programmerad för enheten.

Centralapparaten övervakar inte radiotillbehör som har ett övervakningsintervall programmerat till 0. Vi rekommenderar att du använder denna programmering endast för enheter som används i hemautomatiseringsapplikationer och inte för säkerhetsapplikationer.

# **Radiosiren**

#### **imago WLS**

Parametrarna som är tillgängliga för "imago wls" sirener är:

- **Beskrivning:** Namnet som ges till enheten (t.ex. utomhussiren, etc.)
- **Serienummer:** Detta är serienumret som identifierar tillbehöret. Uppdatera serienummret för att det nya tillbehöret ska behålla alla tidigare sparade inställningar om enheten byts ut.
- **Övervakning:** Max tid mellan två på varandra följande överföringar.
- **Max larmtid:** Maximal larmtid för siren vid strömavbrott. När den maximala tiden går ut, tystnar sirenen även om den inte tar emot återställningskommandot från centralapparaten.
	- **Temperatursensor:** Om avstängt, skickar sirenen inte temperaturen till centralapparaten och den yttre temperaturen kommer inte att visas på manöverpanelen (detta är användbart om det finns två sirener och en är installerad i en position som är utsatt för solen, vilket leder till falsk utetemperaturmätning).

**Obs! Om det här alternativet "Temperaturgivare" är aktiverat på sirenen men displayen på manöverpanelen är avstängd (se Displayens utomhustemperatur), kommer temperaturen inte att visas.**

- **• Dubbeltonssiren:** Om detta alternativ är vald ljuder summern med två distinkta frekvenser, om inte så sveper summern genom flera frekvenser.
#### **Radiorepeater**

**duo (med extern strömförsörjning och batteri).**

Parametrarna som är tillgängliga för duo repeaters är:

- **Beskrivning:** namnet som ges till enheten (t ex garage, nedre plan etc.)
- **Serienummer:** Detta är serienumret som identifierar tillbehöret. Uppdatera serienummret för att få den nya tillbehöret för att behålla alla tidigare sparade inställningar om enheten byts ut.

# **Radioexpansionsmodul auxi wls**

#### **auxi wls**

Parametrarna som är tillgängliga för wls auxi är:

- **Beskrivning:** Namnet som ges till enheten (t ex utomhusbelysning, framsida etc.)
- **Serienummer:** Serienumret som identifierar tillbehöret. Uppdatera serienummret för att det nya tillbehöret ska behålla alla tidigare sparade inställningar om enheten byts ut.
- **Utgångstyp:** utgångarna kan programmeras att fungera enligt följande lägen:
	- **Oberoende utgångar:** utgångarna som är associerade till enheten är helt oberoende av varandra.
	- **Växelvis:** i det här läget kan reläutgångarna inte vara aktiva samtidigt. Om en utgång är aktiv och du vill aktivera den andra utgången, måste båda utgångarna inaktiveras inom en halv sekund innan du kan aktivera den andra utgången.
	- **SPTD:** båda utgångarna hanteras som en enda logisk utgång. Den första som normalt öppen (NO) och den andra som normalt stängd (NC).

## **Radiodetektorer**

#### **Magnetkontakt nanus poli**

Parametrarna som är tillgängliga för magnetkontakt nanus poli är:

- **Beskrivning:** Namnet som ges till enheten (t ex entredörr, fönster kök etc.)
- **Serienummer:** Serienumret som identifierar tillbehöret.Uppdatera serienummret för att det nya tillbehöret ska behålla alla tidigare sparade inställningar om enheten byts ut.
- **Övervakning:** Max tid mellan två på varandra följande överföringar.

#### **Magnetkontakt poli**

Parametrarna som är tillgängliga för magnetkontakt poli är:

- **Beskrivning: N**amnet som ges till enheten (t ex entredörr, fönster kök etc.)
- **Serienummer:** Detta är serienumret som identifierar tillbehöret. Uppdatera serienummret för att det nya tillbehöret ska behålla alla tidigare sparade inställningar om enheten byts ut.
- **Övervakning:** Max tid mellan två på varandra följande överföringar.

#### **IR-detektor unum**

Parametrarna som är tillgängliga för IR-detektor unum är:

- **Beskrivning: N**amnet som ges till enheten (t ex vardagsrum, kök etc.)
- **Serienummer:** Detta är serienumret som identifierar tillbehöret. Uppdatera serienummret för att det nya tillbehöret ska behålla alla tidigare sparade inställningar om enheten byts ut.
- **Övervakning:** Max tid mellan två på varandra följande överföringar.
- **Inhibition: T**iden i sekunder mellan överföringen av två larm. För att spara batteriet sänder detektorn endast ett larm under det inställda intervallet även om händelserna som genererar larmet är flera. **Minsta konfigurerbar tid:** 5 sekunder. **Max konfigurerbar tid:** 300 sekunder.

# **Obs: Inhiberingstiden ställs in med 5 sekunders intervall.**

Om parametern "alltid aktiv" är avstängd, kommer detekteringen endast att ske när systemet är tillkopplat (sabotage är dock alltid aktiv).

**Detektor alltid aktiv:** Om denna funktion inte är vald är detektorn aktiv endast när systemet är tillkopplat. Om denna funktion väljs kommer detektorn att alltid vara aktiv, används om detektorn ska användas för närvarostyrning. Efter tillkoppling är den maximala tiden innan detektorn är fullt fungerande 30 sekunder.

- **Hög känslighet:** Om det här alternativet är avaktiverat införs en högre tröskel för immuniteten mot störningarna i detekteringsanalysen. Känsligheten minskas med 30%.
- **Minskad detekteringsyta:** Under optimala förhållanden har givaren ett intervall på ca 12 meter. Genom att välja detta alternativ sänks detekteringsytan till ca 6 meter

#### **IR-detektor velum**

Parametrarna som är tillgängliga för IR-detektor velum är:

- **Beskrivning:** Namnet som ges till enheten (t ex utomhus, framsida etc.)
- **Serienummer:** Detta är serienumret som identifierar tillbehöret. Uppdatera serienumeret för det nya tillbehöret för att behålla alla tidigare sparade inställningar om enheten byts ut.
- **Övervakning:** Max tid mellan två på varandra följande överföringar.
- **Inhibition:** Tiden i sekunder mellan överföringen av två larm. För att spara batteriet sänder detektorn endast ett larm under det inställda intervallet även om händelserna som genererar larmet är flera.

**Minsta konfigurerbar tid:** 5 sekunder.

**Max konfigurerbar tid:** 300 sekunder.

# **Obs: Inhiberingstiden ställs in med 5 sekunders intervall.**

Om parametern "alltid aktiv" är avstängd, kommer detekteringen endast att ske när systemet är tillkopplat (sabotage är dock alltid aktiv).

- **Detektor alltid aktiv:** Om denna funktion inte är vald är detektorn aktiv endast när systemet är tillkopplat. Om denna funktion väljs kommer detektorn att alltid vara aktiv, används om detektorn ska användas för närvarostyrning. Efter tillkoppling kan maximala tiden innan detektorn är fullt fungerande vara 80 sekunder.
- **Hög känslighet:** Om det här alternativet är avaktiverat införs en högre tröskel för immuniteten mot störningarna i detekteringsanalysen. Känsligheten minskas med 30%.
- **Minskad detekteringsyta:** Under optimala förhållanden har givaren ett intervall på ca 12 meter. Genom att välja detta alternativ sänks detekteringsytan till ca 6 meter.
- **Ner rivningsskydd:** Genom att aktivera det här alternativet aktiveras funktionen MEMS-rivningsskydd (accelerometer).
- **Mikrovåg:** Aktivera eller inaktivera mikrovåg (dubbelteknikfunktionen där både IR och MW måste detektera för att generera ett larm).
- **Övertäckning:** Övertäckninganalysen kan ställas in på tre nivåer:
- **Inaktiverad:** Övertäckningsfunktionen är inaktiverad.
- **Standard:** Övertäckning inom 10 minuter.
- **Fast:** Övertäckning inom 180 sekunder och 3 minuter.

#### **Rökdetektor nebula**

Parametrarna som är tillgängliga för IR-detektor unum är:

- **Beskrivning:** Namnet som ges till enheten (t ex vardagsrum, kök etc.)
- **Serienummer:** Detta är serienumret som identifierar tillbehöret. Uppdatera serienumeret för det nya tillbehöret för att behålla alla tidigare sparade inställningar om enheten byts ut.
- **Övervakning:** Max tid mellan två på varandra följande överföringar.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | För att radera en eller flera enheter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| För att radera en enhet, klicka på trådlösa enheter, klicka på ikonen (<br>) och sen på (<br>) bredvid namnet på enheten<br>som ska raderas. I detta skede kan du välja om du vill avbryta eller fortsätta (bekräfta två gånger).                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | IP kameror                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |  |
| Beroende på version av centralapparat kan ett visst antal IP-kameror hanteras:<br>• lares 4.0 - 16 / lares 4.0-16WLS: 4 IP-kameror.<br>• lares 4.0 - 40 / lares 4.0-40WLS: 12 IP-kameror.<br>• lares 4.0 - 140 WLS: 20 IP-kameror.<br>• lares 4.0 - 644 WLS: 30 IP-kameror.                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  |
| För att programmera IP-kamerorna klickar du på ikonen (<br>Parametrarna som finns tillgängliga för IP-kameror är:                                                                                                                                                                                                                                                                                                                                                             | ) och sedan på symbolen (<br>).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  |
| • Beskrivning: Namnet som ges till enheten (t ex vardagsrum, kök etc.)<br>vissa användare, t.ex. i ett system som är inbyggt i ett parhus)<br>• IP-adress: Kamerans IP-adress (lokal).<br>RTSP-streaming med dedikerad programvara (t.ex. Onvif Device Manager).<br>• Intern port: Porten i det lokala nätverket som kameran ligger på.<br>• Extern port: Porten för att nå kameran utanförför nätverket.<br>användarnamn och lösenord för att få access för att se bilderna. | • Områden: Det område (eller områden) som kameran är associerad med (till exempel för att begränsa övervakning till<br>• Fabrikat: Du kan välja mellan olika fabrikat (Axis, Dahua, Hikvision, Ksenia etc.), som redan har parametern " url". Om<br>så önskas kan du också anpassa parametrarna för IP-enheten (kontakta tillverkaren).<br>• Direktwebbadresser: RTSP-streaming (Real Time Streaming Protocol), det vill säga videoströmmen som kameran<br>använder för att överföra bilder på nätverket. Om en kamera väljs från menyn "varumärke", konfigureras denna<br>parameter automatiskt. I vissa fall måste det konfigureras manuellt (kontakta tillverkaren). Det är möjligt att erhålla<br>• Autentiseringstyp: Aktiverar eller inaktiverar Basic autentisering. Om Basic autentisering är aktiverad ange |  |
| För att lägga till en till IP-kamera klicka på (<br>Klicka på(<br>).                                                                                                                                                                                                                                                                                                                                                                                                          | ) och sedan på symbolen (<br>); annars, för att avsluta sessionen,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  |

I det här avsnittet kan du se vad du hittills har skapat, anpassade händelser, aktiveringslägen, scenarier, sektioner etc.

# **Tillkopplingslägen**

På den här sidan kan du skapa aktiveringslägen för områden som därefter kommer att tilldelas "Scenarier". Scenarierna kommer i sin tur att vara förknippade med specifika "händelser".

För att programmera tillkopplingslägen, klicka på ikonen ( ) och sedan på symbolen ( ). Ange ett namn för varje tillkopplingsläge (t ex Frånkopplat, Tillkopplat, Hemmaläge osv.) Och ställ in de färger som identifierar områdets status.

Färgerna är uppdelade enligt följande:

- **Vit:** Ingen åtgärd. När läget är aktiverat ändras inte områdets status.
- **Gul:** Tllkoppling med fördröjning. När läget är aktiverat är området tillkopplat med fördröjning (in- och utgångsfördröjning är aktiverat (sektioner som är programmerade som fördröjda).
- **Röd:** Tllkoppling utan fördröjning. När läget är aktiverat är området tillkopplat utan fördröjning (in- och utgångsfördröjning är deaktiverat (sektioner som är programmerade som fördröjda är direktlarmande).
- **Blå:** Växlande. När läget är aktiverat, är området tillkopplat. När den aktiveras igen är området frånkopplat och vice versa**.**

**Obs! Växlande läget kan användas flera gånger; Det är med andra ord möjligt att utföra till och frånkopplingscykler för områden med ett enda scenario (t ex TILL, FRÅN, TILL etc.). Om området programmeras med fördröjning kommer den endast att vara tillkopplat med fördröjning (det går inte att byta till tillkoppling utan fördrörjning).**

![](_page_28_Figure_11.jpeg)

**I det här exemplet är följande:**

- **Input 1: Område** 1 och 4 **är tillkopplade med fördröjning**. O**mråde** 2 och 3 **tillkopplade utan fördröjning.**
• **Input 2: Område** 1 och 4 **tillkopplade utan fördröjning.**

- Statusen för område 2 och 3 ändras ej (om de tidigare var tillkopplade skulle de förbli tillkopplade).
- **Input 3**: Alla områden frånkopplas-
- **Input 4: Område** 2 och 3 **tillkopplade utan fördröjning**. Statusen för område 4 ändras ej. Om område 1 var frånkopplat, skulle det nu tillkopplas och vice versa.

#### **Utgångar**

För att programmera utgångarna, klicka på ikonen ( ) och sedan på symbolen ( ). Ange sedan de olika parametrarna:

- **Beskrivning:** Namnet som ges till enheten (t ex vardagsrum, kök etc.)
- **Hashtags:** Se avsnittet Hashtags (sida 19). Det är möjligt att associera flera hashtags.
- Den här funktionen är användbar när du vill aktivera flera utgångar med en händelse. (t.ex. du vill aktivera utgång 1, utgång 2 och utgång 3, alla med Hashtag "#utomhusbelysning". På scenarierna måste du skapa ett scenario "utomhusbelysning" och sedan "Åtgärder" Typ: " Utgång "Underyp:" Utgångsaktivering "Enhet:" #utomhusbelysning ". Detta scenario kommer att associeras med en händelse (t.ex. områdeslarm). Se avsnittet" Scenarier " (sida 41).
- **Områden:** det område (eller områden) som kameran är associerad med (till exempel för att begränsa övervakning till vissa användare, t.ex. i ett system som är inbyggt i en parhus)

# **Länk utgångar till enheter**

I detta avsnitt visas hur man länkar utgångar till plintar på centralapparaten eller till plintar i expansionskorten (trådbundna, trådlösa) som tidigare programmerats under Busstillbehör eller trådlösa enheter.

Tillgängliga utgångar är:

**1. Välj enhetstyp.**

Välj typ av enhet som utgången ska associeras till.

- **• lares:** "m1" and "m2"skruvterminaler på lares 4.0.
- **• auxi:** Alla skruvterminaler på expansionskortet. Ej giltig för auxi10!
- **• auxi relä/auxi-L:** Alla skruvterminaler på expansionskort på auxi relä/auxi L.
- **• ergo-rev.0/ergo:** "m1" och "m2" skruvterminaler på ergo manöverpanel. Ej tillgänglig för ergo S och ergo M.
- **• duo:** "m1" och "m2" -skruvterminaler på duo repeater. Ej tillgänglig om duo är programmerad som en repeater.
- **• radius:** Det går att koppla utgången till lysdioden och summern eller bara till lysdioden.
- **• imago:** Det är möjligt att koppla utgången till LED blixten och summern, eller bara till LED blixten eller endast till de extra lysdioderna (vanligtvis används för att visa systemets tillkopplingsstatus).
- **• auxiwls:** "o1" och "o2" skruvterminaler på den trådlösa auxi.
- **• imago wls:** Det är möjligt att koppla utgången till LED blixten och summern, eller bara till LED blixten eller bara till de extra lysdioderna (vanligtvis används för att visa systemets tillkopplingsstatus).

#### **Notering: Om imago wls drivs genom att ansluta ett icke uppladdningsbart batteri (KSI7207580.000) kommer utgångar att hanteras oberoende av programmering som sker på följande sätt:**

- **Larmutgång:** Monostabil med en tid lika med den maximala larmtiden som fastställts i programmering (standard: 3 min).
- **Power LED-utgång:** Monostabil med maximal tid lika med 30 sekunder. **Aux LED-utgång:** Monostabil med maximal tid lika med 30 sekunder; Detta driftläge används för att spara batteriets livslängd. Om den trådlösa imago drivs av en 12Vdc extern strömförsörjning och ett laddningsbart batteri, hanteras utgångarna enligt programmering.
- **Virtuell:** Med hänsyn till den traditionella lares-plattformen så finns inte längre timers, men dessa har ersatts av virtuella utgångar, kombinerat med "utgång PÅ" och "utgång AV" -händelser. En virtuell utgång är inte associerad med någon enhet.

#### **2. Välj enheten.**

Välj vilket tillbehör som en utgång ska tillhöra, se punkt nr. 1. Det här alternativet är inte alltid tillgängligt (om t ex en utgång redan är associerad med en utgång på moderkortet).

Exempel: En utgång ska tillhöra "m1" -plinten på ett auxi expansionskort. Efter att ha programmerat in alla enheter (sidan 20), välj auxi, enligt beskrivningen i punkt nr 1 i detta avsnitt. Välj sedan den inlärda enheten i rullgardinsmenyn.

# **3. Välj terminal**

Med den här menyn kan du koppla utgången till tillbehörets plintar. Endast de tillgängliga utgångarna visas. Om ingen terminal visas, betyder det att det inte längre är möjligt att utnyttja de tillgängliga utgångarna för det här tillbehöret.

#### **Läge**

- **Monostabil:** En utgång som aktiveras för en programmerad tid (Aktiv tid) när en händelse inträffar och återgår sedan automatiskt till viloläge.
- **Bistabil:** En utgång som följer status för en händelse eller som kan aktiveras av en händelse och deaktiveras av en annan.
- **Tillkopplingsläge:** Följer tillkopplingsstatus för det område (eller områden) som den är associerad med. Om området är tillkopplat aktiveras utgången och vice versa.
- **Larm:** Det aktiveras när ett område (eller områden) som den är associerad med genererar ett larm. Aktiv tid ställs in under "områden" "cykel" (min).
- **Sabotage:** Det aktiveras när ett område (eller områden) som den är associerad med genererar ett sabotagelarm. (Aktiv tid är lika med områdets cyklisk tid).
- **Larm och Sabotage:** Det aktiveras när ett område (eller områden) som den är associerad med genererar ett larm och sabotagehändelse och är lika med områdets cyklisk tid.
- **Fel:** Aktiveras när ett fel inträffar (t ex felaktigt batteri i centralapparat). Den blir inaktiverad när felet är återställt.

# **Styra via APP**

- **Ej synligt:** Om det här alternativet är valt kommer inte utgången att visas i APP och i webbservern på sidan med realtidsutgångar.
- **Med kod (lokal) Med kod (fjärr):** I detta fall hanteras utgången lokalt med kod, och via fjärr med kod.
- **Med kod (lokal) Ej styrbar (fjärr):** I detta fall hanteras utgången lokalt med kod, men det går inte att styra via fjärr (även om det visas).
- **Utan kod (lokal) Utan kod (fjärr):** I detta fall kommer utgången att hanteras lokalt utan kod, och via fjärr utan kod.
- **Utan kod (lokal) Ej styrbar (fjärr):** I detta fall hanteras utgången lokalt utan PIN-kod, men det går inte att styra via fjärr (även om det visas).
- **Utan kod (lokal) Med kod (fjärr):** I detta fall hanteras utgången lokalt utan kod, men kod krävs för styra via fjärr.

# **Polaritet**

- **Normalt öppen NO:** Välj det här alternativet om utgång ska vara NO (normalt öppen) i viloläge och sluta till jord vid aktivering eller om du vill att reläkontakten (t.ex. auxi relä) ska vara öppen**.**
- **Normalt stängd NC:** Välj det här alternativet om utgång ska vara NC (normalt stängd) i viloläge och bryta från jord vid aktivering eller om du vill att reläkontakten (t.ex. auxi relä) ska vara stängd**.**

#### **Aktiveringstid (sek)**

Tid i sekunder för en utgång som programmeras som monostabil att aktiveras när en händelse inträffar.

**Obs! Det här alternativet visas bara om du ställer in en monostabil utgång.**

#### **Inaktiveringstid (sek)**

Inaktiveringstid är summan av aktiveringstid och minimitiden för vilken utgången ska vara deaktiverad.

- **Aktivera endast om systemet är tillkopplat:** Utgången är endast aktiverad om området (eller områdena) som är associerad med den är tillkopplat.
**Notering: Det här alternativet är endast tillgängligt om du ställer in "sabotage" eller "larm och sabotage"**

#### **Valbara balanseringsvärden**

I det här avsnittet kan anpassade balanseringsvärden skapas för att anpassa om andra mostånd än 4,7Kohm ska användas.

Det är möjligt att ändra varje gränsvärde på ingången (kortsluten, normal, larm, övertäckning / fel, sabotage), med utgångspunkt från den grundprogrammerade standardbalanseringen.

På den här sidan, bredvid knapparna för sessionshantering, visas följande knapp: ( )

Genom att klicka på det här alternativet kan du öppna ett Excel-kalkylblad som gör att du enkelt kan bestämma tröskelvärdena som ska appliceras i enlighet med de installerade slutmotstånden.

# **Sektioner**

På den här sidan kan du skapa sektioner som kommer att kopplas till olika enheter (central, auxi etc.). Obs! Det kan hända att vissa parametrar (t ex pulser, pulslängd, balansering etc.) inte är tillgängliga på vissa enheter (t ex på trådlösa enheter, det är inte möjligt att ställa in balanseringen, antalet pulser etc.). För enkelhets skull kommer alla tillgängliga parametrar att visas.

För att programmera sektioner klickar du på ikonen ( ) och sedan på symbolen ( ). Här kan följande parametrar programmeras för sektioner:

- **Beskrivning:** Namnet som ges till sektionen (t ex IR-vardagsrum, IR-kök etc.)
- **Hashtags:** Se avsnittet Hashtags på (sidan 19) i manualen. Du kan associera flera hashtags.
- **Områden:** Det område (eller områden) som kameran är associerad med (till exempel för att begränsa övervakning till vissa användare, t.ex. i ett system som är inbyggt i ett parhus)

Om en centralapparat hanterar ett parhus där en magnetkontakt (t.ex. sektion 2) är installerad på en gemensam dörr som leder till ingångarna för respektive lägenheten. Lägenheterna är i sin tur förknippade med skiljeväggar (t ex lägenhet 1 och lägenhet 2). Om magnetkontakten tillhör 2 områden och om båda områden vara tillkopplade och om sektionen påverkas, kommer ett larm att utlösas; annars kommer inget larm att utlösas.

- **Kamera:** Välj från vilken IP-kamera som bilder ska skickas i ett e-postmeddelande vid larm. Samma ögonblicksbilder kommer också att sparas i händelseloggen under "Bild".
- **Trigger kamera:** Välj händelser som är relaterad till sektionen som ska aktivera funktionen för att skicka ögonblicksbilderna. Tre händelser är tillgängliga och flera val kan göras:
	- **Larm på sektion.**
	- **Sabotage på sektion.**
	- **Övertäckningslarm på sektion.**

#### **Länka sektioner till enheter**

För att länka sektioner till skruvplintar i centralapparat eller till skruvplintar i något av tillbehören (trådbundna och trådlösa tillbehör) som tidigare programmerats in under busstillbehör eller trådlösa enheter.

Tillgängliga funktioner är:

#### **1. Välj enhetstyp**

Typ av enheter som sektionen ska associeras till.

- **• lares:** Alla skruvplintar på lares 4.0.
- **• auxi/auxi 10in:** Alla skruvplintar på expansionskort.
- **• ergo-rev.0/ergo: "m1"** and **"m2"** skruvplintar på manöverpaneler. Inte möjlig på **ergoS** eller **ergoM**.
- **• duo: "m1"** and **"m2"** skruvplintar på duo repeaters. Inte möjlig om duo är programmerad som repeater.
- **• poli:** Internt reedelement eller skruvplintar på ingångarna **"m1"** and **"m2"**.
- **• nanus:** Internt reedelement .
- **• velum**.
- **• nebula**.
- **• auxi wls: i1** och **i2** skruvplintar.

#### **2. Välj enhet**

Välj den enhet som den ska tillhöra som tidigare valts vid punkt nr. 1.

Det här alternativet är inte alltid tillgängligt (t ex om sektionen är redan associerad med centralapparaten). Efter att ha programmerat alla enheter (se sidan 20), välj "auxi" / "auxi10", som beskrivs i punkt nr 1 i det här avsnittet. Välj sedan den programmerade enheten i rullgardinsmenyn.

#### **3. Välj plint**

Med den här menyn kan du koppla sektionen till en av enhetens plintar. Endast de tillgängliga ingångarna visas. Om ingen terminal visas, betyder att det inte finns lediga plintar är tillgängliga för den här enheten.

# **Bearbetningsläge**

Efter att ha associerat sektionen med enheten bestäms typen av analys av signalen som krävs för att utlösa ett larm. Obs! Det går inte att använda vissa lägen beroende på vilken typ av enhet som valts (t.ex. på lares 4.0-kortet, endast standard- och kommandolägen är möjlig)! För enkelhetens skull kommer alla tillgängliga konfigurationer att visas.

#### **Det finns fyra lägen:**

1. **Standard:** Kan kombineras med magnetkontakter, detektorer etc.

- **Notering: inte möjlig för unum WLS, velum WLS, nebula WLS, auxi WLS.**
2. **Aktivera scenario:** Den här sektionen kan inte generera några larm men används endast för att aktivera scenarier. Associerar de områden som som ska vara tillkopplade / frånkopplad med sektionen. Därefter associerar på händelsesidan att realtidslarm ska aktivera ett scenario. Om alla områden som hanteras av det scenariot inte är associerade, kommer endast de valda områden tillkopplas / frånkopplas. Om det här alternativet är aktiverat är det möjligt att direkt hantera en utgång (eller en grupp av utgångar som använder en Hashtag) utan att skapa ett scenario. I det här fallet visas följande ytterligare konfigurationer:

- a. **Styr utgång:** Här kan man välja en utgång (eller en grupp av utgångar med hjälp av Hashtag) det som ska styras med hjälp av en styringång.
- b. **Typ av aktivering:** I den här menyn är det möjligt att välja vilken typ av åtgärd som ska utföras på utgången: Aktivering, deaktivering, växling (med avseende på aktuell status)
- c. **Kommando:** För att välja typ av funktion Knapp (aktivering av utgång kommer endast att utföras när sektionen öppen) och Omkoppling (aktivering av utgång kommer att ske både när sektionen öppnas och stängs)

**Notering: Denna funktion är inte tillgänglig för WLS, velum WLS, nebula WLS, auxi WLS.**

- 3. **Inertia/Glaskross:** För att kombineras med interia, glaskrossdetektorer etc.
- Ej tillgänglig för lares, ergo-rev.0, duo, unum WLS, nanus WLS, velum WLS, nebula WLS, auxi WLS.
- 4. **Jalusier:** att kombineras med detektorer för jalusier.
	- Ej tillgänglig för lares, ergo-rev.0, duo, unum WLS, nanus WLS, velum WLS, nebula WLS, auxi WLS.
- **Test:** Om det här alternativet är valt, spåras endast händelser i händelseloggen utan att larm genereras.

#### **Ingångsfördröjning med nivå:**

- Magnetkontakt på entredörr ska vara fördröjd och inpasseringsfördröjd med nivå 1.
- Första IR-detektor innanför entredörr som ska vara inpasseringsfördröjd ska programmeras nivå 1.
- Nästa IR-detektor innanför entredörr som ska vara inpasseringsfördröjd ska programmeras nivå 2.
- Ytterliggare IR-detektor innanför entredörr som ska vara inpasseringsfördröjd ska programmeras nivå 3.
- **Till exempel, när områden är tillkopplade, om du programmerar tre nivåer, får du följande beteende:**
- 1. **Innan inpasseringsvarning har startat:** Det är möjligt att påverka sektioner med nivå 1; inpasseringsvarning startar när första sektionen (magnetkontakt eller IR-detektor) påverkas.
- 2. U**nder inpasseringsvarning:** Är möjligt att påverka sektioner en nivå högre än den sista påverkade sektionen.

![](_page_32_Figure_23.jpeg)

Bilden visar en hypotetisk situation för ingången till ett hus där manöverpanel endast kan nås efter att passerat flera rum med detektorer. Specifikt måste den IR-detektorn märkt med (1) vara den som påverkas först för att larm inte ska utlösas. Sedan kan nummer (2) och nummer (3) påverkas för att larm inte ska utlösas.

**OBS: För korrekt funktion måste de sektioner i samma inpasseringsväg ha minst ett område gemensamt. Dvs Magnetkontakt på dörr och IR-detektor innanför dörr ska vara nr 1, nästa IR ska vara nummer 2.**

# **Utpasseringslogik**

Programmering av logik för sektioner under utgångstiden.

#### **Det finns tre lägen:**

- 1. **Omedelbar:** Om en sektion är påverkad under utpasseringstiden kommer sektionen att utlösa larm.
- 2. **Fördröjd:** Sektionen kommer inte att utlösa några larm under utpasseringstiden.
- 3. **Sista ut:** Om den här är den sista sektionen som påverkas under utpassering (vanligtvis MK på entredörr), så återställs utgångstiden automatiskt. Alltid med hänvisning till bild (sid 33) måste sektioner markerade med 1, 2 och 3 markeras som utgångsfördröjning och nummer 1 som "sista ut".
- **Alltid aktiv:** Om det här alternativet väljs, utlöses larm direkt när sektionen påverkas, oavsett om område är tillkopplat elller inte som tillhör sektionen (t ex 24 timmarssektion)
- **Varning:** Om det här alternativet är valt, när en sektionen påverkas och om område är frånkopplat, kommer en ljudsignal att genereras i manöverpaneler som har "varning" aktiverad och är associerade med samma områden med som sektionen.

# **Förbikoppling**

Det är möjligt att hantera förbikoppling av sektion i fyra olika lägen:

- 1. **Ej förbikopplingsbar:** Om det här alternativet är valt kan användaren inte förbikoppla sektionen.
- 2. **Förbikopplingsbar:** Om det här alternativet är valt kan användaren förbikoppla sektionen. En förbikopplad sektion utlöser inte larm. Sabotage och fel/övertäckning kommer dock utlösa larm, om såvidare inte "även förbikopplad sabotage" är aktiverat.
- 3. **Automatisk förbikopplingsbar:** Om det här alternativet så valt så förbikopplas sektionen automatiskt om den är påverkad vid tillkoppling. Automatisk förbikoppling förbikopplar aldrig sabotage och övertäckning, om såvidare inte alternativet "även förbikopplad sabotage" är aktiverat. Sektion inkopplas in automatiskt vid nästa frånkoppling.
- 4. **Automatisk förbikopplingsbar med återinkoppling:** Om det här är alternativet är valt så förbikopplas sektionen automatiskt om den påverkad vid tillkoppling, men så fort den är åter i normalläge, återställs den automatiskt och är aktiv igen.

#### **Balansering**

Centralapparaten har 8 ingångar och 2 programmerbara I / O-terminaler som kan konfigureras som ingångar eller utgångar. Både på centralapparat och expansionskort auxi kan varje ingång programmeras till åtta olika typer av valfria balanseringstyper.

Följande tabell visar hur centralapparat tolkar motståndsvärdena för olika balanseringskonfigurationer:

#### 1. **Normalt stängd (NC)**

| Band 0  | Band 1    | Band 2    | Band 3   | Band 4    |  |
|---------|-----------|-----------|----------|-----------|--|
| 0-1.8KΩ | 2.2-4.1KΩ | 4.2-6.8KΩ | 7.2-14KΩ | ∞ (öppen) |  |
| Normal  | Larm      |           |          |           |  |
|         |           |           |          |           |  |

#### 2. **Normalt öppen (NO):**

| Band 0  | Band 1    | Band 2    | Band 3   | Band 4    |
|---------|-----------|-----------|----------|-----------|
| 0-1.8KΩ | 2.2-4.1KΩ | 4.2-6.8KΩ | 7.2-14KΩ | ∞ (öppen) |
|         | Normal    |           |          |           |
|         |           |           |          |           |

#### 3. **Enkelbalanserad (10K):**

| Band 0  | Band 1    | Band 2    | Band 3   | Band 4    |
|---------|-----------|-----------|----------|-----------|
| 0-1.8KΩ | 2.2-4.1KΩ | 4.2-6.8KΩ | 7.2-14KΩ | ∞ (öppen) |
|         | Sabotage  |           | Normal   | Sabotage  |

## **4. Dubbelbalanserad (4.7K + 4,7K):**

| Band 0   | Band 1    | Band 2    | Band 3   | Band 4    |
|----------|-----------|-----------|----------|-----------|
| 0-1.8KΩ  | 2.2-4.1KΩ | 4.2-6.8KΩ | 7.2-14KΩ | ∞ (öppen) |
| Sabotage | Normal    |           | Larm     | Sabotage  |

**Bild på inkoppling ovan visar Ksenia´s förslag på inkoppling med 2 motstånd på 10K parallellt, denna inkoppling motsvarar nedanstående inkoppling med 2 motstånd på 4,7K i serie istället:**

![](_page_34_Figure_5.jpeg)

#### **5. Dubbelbalanserad (10K + 10K):**

| Band 0   | Band 1    | Band 2    | Band 3   | Band 4    |
|----------|-----------|-----------|----------|-----------|
| 0-1.8KΩ  | 2.2-4.1KΩ | 4.2-6.8KΩ | 7.2-14KΩ | ∞ (öppen) |
| Sabotage |           | Normal    | Larm     | Sabotage  |

#### **6. Trippelbalanserad (parallell 3 x 10K):**

| Band 0   | Band 1    | Band 2    | Band 3        | Band 4    |
|----------|-----------|-----------|---------------|-----------|
| 0-1.8KΩ  | 2.2-4.1KΩ | 4.2-6.8KΩ | 7.2-14KΩ      | ∞ (öppen) |
| Sabotage | Normal    | Larm      | Övertäckning* | Sabotage  |

#### **7. Övertäckning (10K):**

| Band 0<br>Band 1 |           | Band 2    | Band 3   | Band 4       |
|------------------|-----------|-----------|----------|--------------|
| 0-1.8KΩ          | 2.2-4.1KΩ | 4.2-6.8KΩ | 7.2-14KΩ | ∞ (Sabotage) |
|                  | Fel       |           | Normal   | Fel          |

#### **8. Sabotage (10K):**

| Band 0   | Band 1    | Band 2    | Band 3   | Band 4    |  |  |
|----------|-----------|-----------|----------|-----------|--|--|
| 0-1.8KΩ  | 2.2-4.1KΩ | 4.2-6.8KΩ | 7.2-14KΩ | ∞ (öppen) |  |  |
| Sabotage |           |           | Normal   | Sabotage  |  |  |

#### **9. Specialbalansering**

**När denna inställning väljs, aktiveras en undermeny som tillåter att associera en anpassad balansering som definierats i föregående avsnitt till sektionen.**

#### **Antal pulser**

Det är antalet pulser som krävs innan en sektion utlöser larm. Det kan ställas för "Standard" eller "Styr scenrio" sektion, men är fasta värden för "jalusier" eller "Inertia"-sektioner.

#### **Larmfönster**

Det är tidsfönstret inom vilket antalet programmerade pulser måste uppstå för att larm ska utlösas.

#### **Pulslängd**

Längd för varje enskild puls på ingång (uttryckt i ms.). Detta värde bestämmer tiden för vilken sektion måste vara påverkad för att detektera en giltig puls och gäller för alla bearbetningslägen. Om man t ex. programmerar en sektion som "jalusier"så kommer larm att utlösas om ett programmerat antal snabba pulser uppfylls (jalusirörelse) eller om kontakten förblir öppen för den tid som programmeras i det här fönstret (avbrott). När det gäller en sektion som är programmerad som "jalusier"med inställning till 0, så utförs endast snabbpulsanalysen utan att utlösa ett larm om kontakten förblir öppen.

#### **Larmcykel**

Det är det maximala antalet larm som kan genereras av en sektion: Efter att ha överskridit de inställda larmcykler så kommer sektionen inte att utlösa sektion. Larmcyklerna återställs varje gång sektion blir tillkopplad. Om den är inställd på 0, kan sektion generera oändliga larm när området den tillhör är tillkopplad.

#### **Inaktivitet**

Om området som sektioner ingår i är frånkopplad, och sektionen aldrig har påverkats under denna programmerade tiden (uttryckt i minuter), kommer en händelse "inaktivitetslarm" att genereras (passiv kontroll av övertäckning eller ingen detektering). Minsta tid är 10 minuter och maximal tid är 2500 minuter (ungefär 41 timmar).

#### **Användare**

För att programmera "Användare", klicka på ikonen ( ) och sedan på symbolen ( ). Följande parametrar kan ändras:

#### **Allmänt**

- **Beskrivning:** Användarens namn.
- **Användartyper:** Följande typer kan väljas: Huvudanvändare, Standard, Gäst, Patrullering, Endast tillkoppling och Endast bricka.

Följande egenskaper kan väljas.

![](_page_36_Figure_6.jpeg)

#### **Standardkod**

- Huvudmeny
	- Återställa larm
	- Områdesstatus
	- Sektionsstatus
	- Ändra kod
		- (ändra huvudkod)
	- Ergo alternativ:
		- Belysning:
			- minimun / normal / maximum
		- Volym:
			- tyst / låg/ medium / normal / max
		- Varning:
		- PÅ / AV
		- Känslighet:
		- låg / medium / hög
	- Avancerad meny:
		- Händelselogg
		- När du bläddrar visas detaljerna i händelsen
		- Datum och tid
		- Nätverk
		- IP Address / Subnet Mask. / Gateway
	- Felstatus
	- GSM status
	- GSM-operatör / SIM-saldo / SIM-utgångsdatum
	- Återställ larmöverföring (kommunikation)

#### **Gästkod**

- Huvudmeny
	- Återställa larm
	- Områdesstatus
	- Sektionsstatus
	- Ändra kod
		- (ändra huvudkod)
	- Ergo alternativ:
		- Belysning:
			- minimun / normal / maximum
			- Volym:
			- tyst / låg/ medium / normal / max
			- Varning:
			- PÅ / AV
			- Känslighet:
			- låg / medium / hög
	- Avancerad meny:
		- Händelselogg
			- När du bläddrar visas detaljerna i händelsen
			- Datum och tid
			- Nätverk:
				- IP Address / Subnet Mask. / Gateway
	- Felstatus
	- GSM status
		- GSM-operatör / SIM-saldo / SIM-utgångsdatum
	- Återställ larmöverföring (kommunikation)

 **Obs! Gästkoden kan inte hantera systemet via "lares 4.0" APP!**

- **Rondering:** Om det här alternativet väljs kommer koden, brickan eller fjärrkontrollen som är associerad med den att kunna frånkoppla systemet, men områdena kommer att tillkopplas automatiskt vid slutet av ronderingen som programmerats på sidan "Områden". Det är möjligt att "tvinga" tillkoppling utan att vänta till på slutet av tiden för ronderingen. Manöverpanel och läsare måste vara aktiverade vid frånkoppling.
- **Endast tillkoppling:** Om det här alternativet är valt, kan koden, brickan eller fjärrkontrollen som är associerad med denna funktion endast kunna tillkoppla systemet.
- **Öppna dörr:** Om det här alternativet är valt, när koden används, eller om brickan används på läsaren, så aktiveras endast scenariot som motsvarar den igenkända koden och / eller igenkänd brickhändelse (programmerad på sidan "Händelser"), utan att tillåta aktivering av scenarierna som hör samman med manöverpanelen eller läsaren eller åtkomst till menyer (eller om den är i närheten av manöverpanelen). Det här alternativet är mycket användbart om du vill använda brickan för att bara göra en åtgärd (t ex aktivering av en utgång för att öppna en dörr eller ett visst scenario).
- **Telefon:T**telefonnumret som kommer att ringas av centralapparaten.
- **E-post:** E-postadress som notfieringar ska skickas till.
- **Områden:** områden som kan hanteras av användaren. På detta sätt är det möjligt att skapa en fleranvändaråtkomst på APP (t.ex. ett parhus som hanteras av en enda centralapparat: användaren A kan hantera endast sin lägenhet, men kan inte hantera områden som är associerade med användaren B).

**Hashtags:** den grupp som användaren tillhör (t ex anställda).

Det är möjligt att skapa ett scenario som aktiverar eller inaktiverar alla användare med hashtag "anställda".

- **Prioritetskanal:** För varje nummer är det möjligt att programmera vilken kommunikationskanal som ska användas som prioriterad kanal. Den andra kanalen kommer automatiskt att användas som backup. Om exempelvis GSM är vald som prioritet, och det blir något problem med GSM-modulen, så skickas samtalen istället via PSTN .
# **Notifikationer**

- **Samtal:** Aktiverar eller inaktiverar funktionen för att skicka röstsamtal (via GSM eller PSTN) till användaren.
- **SMS:** Aktiverar eller inaktiverar funktionen för att skicka SMS-meddelandet.
- **Email:** Aktiverar eller inaktiverar funktionen för att skicka e-postmeddelanden.

### **Konfiguration av åtkomst till centralapparat**

- **Kod:** ange användarkod.
- **Bricka:** för varje RFID-bricka sparas en unik kod. När brickan lärs via systemet visas den här koden i det här fältet.
- **• Kod:** aktiverar eller inaktiverar användningen av koden på manöverpanel och i APP. Om det här alternativet är inaktiverat och koden används på manöverpanelen, visas meddelandet "Fel kod!". Om du anger koden på appen visas meddelandet "Inloggning misslyckades".
- **• Fjärrkontroll:** aktiverar eller inaktiverar användningen av fjärrkontrollen.

# **Fjärrkontrollalternativ**

**Serienummer:** I detta fält ska serienumeret som finns på fjärrkontrollens etikett anges. När serienumeret har angetts visas följande alternativ:

- **Bekräfta med vibration:** Aktiverar eller inaktiverar fjärrkontrollens vibrationsfunktion för att bekräfta när ett scenario utförs när man trycket på en knapp.
- **Långt tryck på (i) -knappen:** Aktiverar eller inaktiverar de funktioner som är associerade med långtryck på ( i ) knappen. Vilken åtgärd programmeras på sidan "Händelser".
- **Långt tryck på tillkoppling ( ):** Aktiverar eller inaktiverar funktionerna som är associerade med långtryck på den total tillkoppling. Vilken åtgärd programmeras på sidan "Händelser".
- **Långt tryck på frånkoppling ( ):** Aktiverar eller inaktiverar funktionerna som är associerade med långtryck på den frånkoppling. Vilken åtgärd programmeras på sidan "Händelser".
- **Långt tryck på deltillkoppling ( ):** Aktiverar eller inaktiverar funktionerna som är associerade med långtryck på den deltillkoppling. Vilken åtgärd programmeras på sidan "Händelser".

#### **Contact ID mottagare**

För att programmera "Contact ID-mottagare", klicka på ikonen ( ) och sedan på symbolen ( ). Följande parametrar kan programmeras:

- **Beskrivning:** Namnet på Contact-ID mottagaren.
- **Primär telefonnr:** Telefonnumret till den Contact ID-mottagare som centralapparaten ska ringa till.
- **Huvud kod:** Den fyrsiffriga koden som identifierar kunden. Det tillhandahålls av larmcentralen.
- **Sekundär telefonnr:** Telefonnumret till den Contact ID-mottagare som centralapparaten ska ringa till.
- **Backup kod:** den fyrsiffriga koden som identifierar kunden. Det tillhandahålls av larmcentralen.

#### **SIA IP mottagare**

För att programmera "SIA IP-mottagare", klicka på ikonen ( ) och sedan på symbolen ( ). För varje mottagare skapas också en eventuell backupmottagare, på vilken signalerna skickas till vid kommunikationsfel med huvudmottagaren. Ange följande parametrar:

- **Beskrivning:** Namnet är associerat med SIA-IP-mottagaren.
- **Aktivera Eth / GPRS-övervakning:** Genom att välja det här alternativet skickas övervakningspaket till mottagaren med hjälp av båda tillgängliga kommunikationskanalerna om det finns tillgång till både Ethernet-anslutning och GPRS.
- **Överför över TCP:** Om du väljer det här alternativet sätts användningen av TCP istället för UDP-protokollet för att skicka signaler.
- **Använd Tidsstämpel:** Om det är valt, så skickas information om datum och timme med i datapaketet.
- **Kommunikationstidsavbrott:** Väntetid i sekunder som krävs för att få bekräftelse på signalen som skickats till mottagaren innan centralapparaten gör ett ytterligare försök (standard 5, max 60).
- **Ethernet-port:L**lokal port där centralapparaten lyssnar använder för att meddelandet via Ethernet.
- **GPRS-port:** Lokal port där centralapparaten lyssnar använder för att meddelandet via GPRS.
- **Eth (sek) övervakningsintervall:** Tidsintervallet i sekunder mellan ett kontrollpaket och det andra via Ethernetkanalen.
- **GPRS-övervakningsintervall:** Tidsintervallet i sekunder mellan ett kontrollpaket och det andra via GPRS-kanalen.
- **Övervakningsläge:** Välj vilka mottagare som ska övervakas (Välj alternativet "Endast ett" om du vill övervaka endast huvudmottagaren och "Alla" om du vill övervaka båda)
- **Protokoll:** Protokoll som används för att formatera datafältet i transportprotokollet SIAIP DC09 (SiaLevel3, KS-PROT för kompatibilitet med Vigilo-mottagaren).
- **Application Status ID:** ID för centralapparatens applikationsprotokoll som används med nuvarande mottagare.
- **Transport av lagyer ID:** SIA-IP DC09 ID för centralapparaten som används med nuvarande mottagare, maximalt 12 hexadecimala siffror.

Centralapparaten skickar signaler till en primärmottagare, och eventuellt till en valfri sekundär mottagare. Följande data gäller för båda mottagarna, men endast obligatorisk för den primära mottagaren.

- **Ethernet IP:** mottagarens IP-adress som ska användas när ett meddelande skickas via Ethernet.
- **Ethernet-port:** porten genom vilken mottagaren lyssnar på när en signal skickas via Ethernet
- **GPRS IP:** mottagarens IP-adress som ska användas när ett meddelande skickas via GPRS.
- **GPRS port:** porten genom vilken mottagaren lyssnar på när en signal skickas via GPRS.
- **Mottagar-ID:** SIA-IP DC09 ID för mottagaren, max 6 hexadecimala siffror.

## **Scenarier**

Beroende på storlek av centralapparat kan upp till 512 scenarier konfigureras, vilka alla kan hanteras på distans (vilket överstiger gränsen på 10 för lares plattformen).

Scenarierna är en uppsättning upp till 16 åtgärder som kan hantera utgångar (aktivering, deaktivering, växling), sektioner (förbikoppling, återinkoppling, växling), användare (aktivering, inaktivering) och, ingångslägen.

För att konfigurera "Scenarier" klicka på ( ) och sedan på symbolen ( ) . Följande parametrar kan programmeras:

- **Beskrivning:** Detta är namnet som är associerat med scenariot (t ex larm och belysning.)
- **Områden:** Scenariot hanterar ingångar, utgångar, användare etc. i samband med områden.
- **Scenariohantering via APP:**
- **Ej synligt:** Om det här alternativet är valt kommer inte utgången att visas i APP och i webbservern på sidan av med realtidsutgångar.
- **Med kod (lokal) Med kod (fjärr):** I detta fall hanteras utgången lokalt med kod och det styras via APP på samma sätt.
- **Med kod (lokal) Ej styrbar (fjärr):** I detta fall hanteras utgången lokalt med, kod men det går inte att styras det via APP (även om det visas).
- **Utan kod (lokal) Utan kod (fjärr):** I detta fall kommer utgången att hanteras lokalt utan kod och styras via APP på samma sätt.
- **Utan kod (lokal) Ej styrbar (fjärr):** I detta fall hanteras utgången lokalt utan PIN-kod, men det går inte att styras det via APP (även om det visas).
- **Utan kod (lokal) Med kod (fjärr):** I detta fall hanteras utgången lokalt utan kod, men kod måste anges för att styras via APP.

**Åtgärder:** I det här avsnittet är åtgärderna associerade med scenariot. När ett nytt scenario skapas, är inte åtgärderna programmerade. Följande meny visas:

För att konfigurera "Åtgärder" klickar du på symbolen ( ) . Det kommer att visas tre alternativ att konfigurera: **• Typ:** Identifierar den grupp som ska hanteras (t.ex. sektioner, område, utgång, etc.). **• Undertyp:** Är den åtgärd som påverkar parametervärdet i "Typ" (t ex typ: sektion - förbikoppling). **• Enhet:** Anger i detalj sektionen, området, enheten, användaren etc. som hanteras. Efter att ha tillämpat de tre parametrarna som tidigare beskrivits klickar du på ( ). För att fortsätta att konfigurera åtgärderna klickar du på symbolen( ) .

**I exemplet nedan och på nästa sida har tre åtgärder programmerats. När scenariot inträffar, förbikopplas sektion 1, utgången för grön lysdiod ska aktiveras och användarkonto nr 2 ska aktiveras (om detta var tidigare aktiverat så ändras inget).**

| Actions     |           | 4 | > | 17 |
|-------------|-----------|---|---|----|
| Bypass Zone | IN 1      |   |   |    |
| Output On   | Green LED |   |   |    |
| Enable User | Account 2 |   |   |    |

För att radera en enda åtgärd (t ex för att radera förbikoppling av sektion 1 som visas i exemplet) klickar du på den åtgärd du vill radera och sedan på symbolen ( ) .

Genom att klicka på en åtgärd och pilarna bredvid symbol ( ), kan du flytta åtgärden upp och ner. Typ av notifikation anges under <"Undertyper":

## Typ: **Sektion**

De tillgängliga undertyperna är:

- **Förbikoppling av sektion:** En sektion förbikopplas.
- **Inkoppling av sektion:** En tidigare förbikopplad sektion inkopplas igen.
- **Sektionsförbikoppling/återinkoppling:** Om det här alternativet är aktiverat förbikopplas/återinkopplas en sektion igen och vice versa.

**Obs! Denna undertyp har ingen effekt på sektioner med attributet "ej förbikopplingsbar".**

- Typ: **Utgång**
De tillgängliga undertyperna är:

- **Utgångsaktivering: U**tgången är aktiverad.
- **Utgångsdeaktivering:** Utgången är deaktiverad.
- **Utgångsväxling:** Utgång växlas (aktiveras/deaktiveras) och vice versa.

**Obs! Denna undertyp påverkar även utgångar med attributen "ej styrbara (lokalt)" och "ej styrbara (fjärr)". Om en utgång är programmerad med attributet "kod (lokal)" eller "med kod (fjärr)", hanteras det av scenariot utan att behöva en kod.**

- Typ: **Tillkopplingslägen**
Tillgängliga tillkopplingslägen är:

- **• Kompatibel med EN50131:** Om systemet inte är klart för tillkoppling så kommer systemet inte att tillkopplas och händelsen "Fel vid tillkoppling" att genereras.
Notering! Om det finns öppna sektioner som är programmerade som "Förbikopplingsbar" eller "Ej Förbikopplingsbar" vid tillkoppling kommer detta att visas på manöverpanelen, då dessa inte förbikopplas. Vilket innebär att systemet inte kan tillkopplas. Sektioner med funktion "Automatisk förbikoppling" som är öppna vid tillkoppling, kommer att förbikopplas och kommer inte att utlösa larm även dessa sektioner återgår till normalläge: dessa kommer att återinkopplas när systemet frånkopplas. Sektioner med funktion "Automatisk inkoppling" som är öppna vid tillkoppling, kommer att förbikopplas och kommer inte att utlösa larm. Om de återgår till normalläge kommer dessa att återinkopplas omgående och kan utlösa larm igen.

- **Manuell förbikoppling:** Om systemet inte är klart för tillkoppling så visas alla öppna sektioner på manöverpanelen, med möjlighet att manuellt att förbikoppla sektioner.
**Notering**! Om det finns öppna sektioner med funktion "Ej förbikopplingsbar", kommer det att visas på manöverpanelen men dessa kan inte förbikopplas. Sektioner som har funktion "Automatisk förbikoppling" och om de är öppna vid tillkoppling, kommer att automatisk förbikopplas och kommer inte att utlösa larm även om sektionerna återgår till normalläge, dessa kommer att återinkopplas när systemet frånkopplas.

Sektioner med funktion "Automatisk inkoppling", som är öppna vid tillkoppling kommer att förbikopplas och kommer inte att utlösa larm. Om de går tillbaka kommer de att återinkopplas och kan utlösa larm igen. Sektioner med funktion "Förbikopplingsbar" som är öppna vid tillkoppling, kommer att visas på manöverpanelen och kan inte förbikopplas.

- **Larm utlöses vid öppna sektioner:** Om systemet inte är klart för tillkoppling (öppna sektioner finns) när det tillkopplas kommer larm att utlösas.
**Notering**! Om det finns påverkade sektioner med funktion "Ej förbikopplingsbar" kan inte dessa sektioner förbikopplas utan kommer att utlösa larm istället. Om sektioner med funktion "Automatisk förbikoppling" som är öppna under tillkoppling så kommer dessa att automatiskt förbikopplas och kommer inte att utlösa larm, dessa kommer att återinkopplas när systemet frånkopplas. Sektioner med funktion "Automatisk inkoppling", som är öppna vid tillkoppling kommer att förbikopplas och kommer inte att utlösa larm. Om de återgår till normalläge kommer dessa att återinkopplas omgående och kan utlösa larm igen.

### • **Tvingad förbikoppling: Om sektioner är öppna vid tillkoppling, kommer sektioner att förbikopplas.**

Notering! Om det finns öppna sektioner med funktion "Ej förbikopplingsbar", vid tillkoppling, kommer sektioner inte att förbikopplas och larm kommer att utlösas.

Sektioner med funktion "Förbikopplingsbar" och "Automatisk förbikoppling"som är öppna vid tillkoppling, kommer att förbikopplas och kommer inte att generera larm även om de återvänder till normalläge, dessa kommer att återinkopplas vid frånkoppling. Sektioner med funktion "Automatisk inkoppling", som är öppna vid tillkoppling kommer att förbikopplas och kommer inte att generera larm. Om de återgår till normalläge kommer dessa att återinkopplas omgående och kan utlösa larm igen.

# Typ: **Utgångar**

De tillgängliga undertyperna är:

- **Aktivera användare:** Användarens konto (inklusive kod, bricka eller fjärrkontroll), om den är inaktiv, är nu aktiverad**.**
- **Inaktivera användare:** Användarens konto (inklusive kod, bricka eller fjärrkontroll) är nu inaktiverad.
- Type: **Övrigt**

De tillgängliga undertyperna är:

- **Radera telefonkö:** Avbryter pågående samtal och alla samtal som ligger i kö..
- **Återställning av utgångar:** Alla utgångar som hör samman med ett larm eller en sabotagehändelse återställs.

#### **Händelser**

Den här sidan länkar händelser (larm, sabotage, etc.) med olika scenarier.

För att konfigurera "Händelser", dvs utförandet av de programmerade scenarierna (tillkoppling, aktivering av utgångar etc.) klicka på ( ) ikonen och sedan på symbolen ( ). Följande parametrar kan programmeras:

- **Typ:** Identifierar gruppen som genererar en händelse (t ex sektion, område, utgång, etc.).
- **Undertyp:** Åtgärden relaterad till föregående parameter (t ex Typ: sektionsundertyp sektionslarm). Det går att lägga upp till 15 objekt.

När du har angett de tidigare beskrivna två parametrarna klickar du på ( ). Vid denna tidpunkt är det nödvändigt att ställa in två andra parametrar:

- **Enhet:** Sektion, område, tillbehör, användare etc. som genererar händelsen.
- **Scenario:** Ange det tidigare programmerade scenariot, vilket aktiveras när händelsen som genereras av den valda enheten inträffar.

Notifikationer visas under <"Undertyper".

- Typ: **Sektion**
De tillgängliga undertyperna är:

- **Larm:** Aktiverar ett scenario när sektionen utlöser ett larm.
- **Larmåterställning:** Aktiverar ett scenario när sektionen är återställd efter ett larm.
- **Sabotage:** Aktiverar ett scenario när sektioner utlöser ett sabotagelarm.
- **Sabotageåterställning:** Aktiverar ett scenario när sabotagelarm är återställd.
- **Förbikopplad:** Aktiverar ett scenario när sektion är förbikopplad.
- **Återinkopplad:** Aktiverar ett scenario när sektion är återinkopplad.
- **Övertäckning:** Aktiverar ett scenario när en detektor utlöser övertäckningslarm.
- **Övertäckning återställd:** Aktiverar ett scenario när en detektor som har utlöst övertäckningslarm blir återställd.
- **Aktiverad i realtid:** Aktiverar ett scenario när sektionen är aktiverad i realtid, om området är frånkopplat.
- **Aktiverad i realtid återställd:** Aktiverar ett scenario när sektionen som har är aktiverad i realtid blir återställd, om området är frånkopplat.

#### Typ: **Område**

Tillgängliga undertyper är:

- **Larm:** Aktiverar ett scenario när området som utlöser larm.
- **Tillkoppling:** Aktiverar ett scenario när området tillkopplas.
- **Sabotage:** Aktiverar ett scenario när området utlöser ett sabotagelarm.
- **Frånkoppling:** Aktiverar ett scenario när området frånkopplas.
- **Varning:** Aktiverar ett scenario när ett område ulöser varning.
- **Varning återställs:** Aktiverar ett scenario när ett område som har utlöst varning återställs.
- **Rondering påbörjad:** Aktiverar ett scenario när en rondering påbörjas efter en frånkoppling.
- **Rondering avslutad:** Aktiverar ett scenario när en rondering avslutas vid en tillkoppling.
- **Inpasseringstid startad:** Aktiverar ett scenario när inpasseringstid startar i ett område som är tillkopplat.
- **Inpasseringstid avslutad:** Aktiverar ett scenario när inpasseringstid avslutas i ett område som är tillkopplat.
- **Utpasseringstid startad:** Aktiverar ett scenario vid tillkoppling när utpassering startar.
- **Utpasseringstid avslutad:** Aktiverar ett scenario vid tillkoppling när utpassering avslutas.
- **Ej tillkopplad:** Aktiverar ett scenario när tid för ej tillkopplad avslutas (om programmerad under **"Områdes"**) sidan.
- **Fel vid tillkoppling:** Aktiverar ett scenario när centralapparaten inte kan utföra en tillkoppling (t ex. närvaro i utrymmen under tillkoppling som hindrar scenario att utföra tillkoppling enligt EN5013 eller manuell förbikopplings attribut.
- Typ: **Utgång**

Tillgängliga undertyper är:

- **Aktivering:** utför scenario när utgång är aktiverad (manuellt av APP eller via en händelse, t ex scenario).
- **Deaktivering:** utför scenarionär utgång är deaktiverad (manuellt av APP eller via en händelse, t ex scenario).
- Typ: **Tillbehör**

De tillgängliga undertyperna är:

- **Sabotage (BUSS):** Aktiverar ett scenario när bussenheter generar sabotagelarm (t ex en manöverpanel öppnas).
- **Sabotage återställt (BUSS):** Aktiverar ett scenario när bussenheter generar en återställning av sabotagelarm.
- **Sabotage (radio):** Aktiverar ett scenario när trådlösa enheter generar sabotagelarm (t ex en magnetkontakt poli öppnas)
- **Sabotage återställt (radio):** Aktiverar ett scenario när trådlösa enheter generar återställning av sabotagelarm
- **Bortfall (BUSS):** Aktiverar ett scenario när bussenheter inte längre kan detekteras av centralapparat (t ex. kabelbrott eller tillbehörsfel).
- **Bortfall återställt (BUSS):** Aktiverar ett scenario när bussenheter återställs (t ex, kabelbrott åtgärdat eller felaktigt tillbehör återställt).
- **Bortfall (radio):** Aktiverar ett scenario när centralapparaten inte längre erhåller några periodiska rapporter från trådlösa tillbehör.
- **Bortfall återställt (radio):** Aktiverar ett scenario när centralapparaten kommunicerar igen med trådlösa tillbehör som har slutat att skicka periodiska rapporter..
- Typ: **Manöverpanel**
- **Knapp 0:** Aktiverar ett scenario när knapp (0) på manöverpanelen trycks ned.
- **Knapp 1:** Aktiverar ett scenario när knapp (1) på manöverpanelen trycks ned.
- **Knapp 2:** utför ett scenario när knapp (2) på manöverpanelen trycks ned.
- **Knapp 3:** Aktiverar ett scenario när knapp (3) på manöverpanelen trycks ned.
- **Knapp 4:** Aktiverar ett scenario när knapp (4) på manöverpanelen trycks ned.
- **Knapp 5:** Aktiverar ett scenario när knapp (5) på manöverpanelen trycks ned.
- **Knapp 6:** Aktiverar ett scenario när knapp (6) på manöverpanelen trycks ned.
- **Knapp 7:** Aktiverar ett scenario när knapp (7) på manöverpanelen trycks ned..
- **Knapp 8:** Aktiverar ett scenario när knapp (8) på manöverpanelen trycks ned.
- **Knapp 9:** Aktiverar ett scenario när knapp (9) på manöverpanelen trycks ned.

#### Typ: **Läsare**

Tillgängliga undertyper är:

- **Grön lysdiod:** Aktiverar scenario när den gröna lysdioden på läsaren är vald och lyser.
- **Röd lysdiod:** Aktiverar scenario när den röda lysdioden på läsaren är vald och lyser.
- **Vit lysdiod:** Aktiverar scenario när den vita lysdioden på läsaren är vald och lyser.
- **Blåa lysdiod:** Aktiverar scenario när den blåa lysdioden på läsaren är vald och lyser.
- **Gula lysdiod:** Aktiverar scenario när den gula lysdioden på läsaren är vald och lyser.

#### Typ: **Kommunikation**

#### Tillgängliga undertyper är:

- **Kommunikation startad:** Aktiverar scenario när centralapparaten initierar PSTN/GSM/E-post samtal etc.
- **Kommunikationfel:** Aktiverar scenario när det blir fel vid PSTN/GSM/E-post samtal etc.
- **Inkommande samtal:** Aktiverar scenario när centralapparaten tar emot ett samtal.
- **Contact ID kommunikation utförd:** Aktiverar scenario när centralapparaten ringer ett Contact-ID samtal.
- **Contact ID kommunikationsfel:** Aktiverar scenario när det blir fel vid ett Contact-ID samtal.
- **SIA kommunikation utförd:** Aktiverar scenario när centralapparaten skickar ett larm med SIA protokoll.
- **SIA kommunikationsfel:** Aktiverar scenario när det blir ett fel när larm ska skickas med SIA protokoll.

Avsnittet "Enhet" indikerar vad/vem (t ex användarkod, bricka) eller vad (t.ex. enhet, sektion, område, etc.) genererar händelsen. T ex. Om en "Enhet" med område 1 och undertyp larm, så kommer centralapparaten att utföra scenariot (tidigare programmerat på när område 1 genererar ett larm. Du kan välja flera enheter: Om du vill markera alla enheter (t ex områden) för en viss händelse, välj "Alla".

#### Typ: **Strömförsörjning**

Tillgängliga undertyper är::

- **• Nätfel:** Aktiverar scenario vid nätfel i centralapparat **lares 4.0**, i trådlösa repeater duo eller strömförsöjning "**opis"**.
- **• Nätfel återställt:** Aktiverar scenario vid återställning vid nätfel i centralapparat **lares 4.0**, i trådlösa repeater duo eller strömförsöjning **opis**.
- **• Låg batteri:** Aktiverar scenario när batterispänning sjunker under tröskel 11V, (sker oftast när nätspänning försvinner).
- **• Låg batteri återställt:** Aktiverar scenario när batterispänning är återställd (sker oftast när nätspänning kommer tillbaka).
- **• Batterifel:** Aktiverar scenario när centralapparat **lares 4.0**, imago siren, trådlösa tillbehör och strömförsörjning **"opis"** inte klarar batteritest.
- **• Låg spänning:** Aktiverar scenario när inkommande spänning till centralapparat **lares 4.0** sjunker under tröskel 14.4V, eller inkommande spänning till **"opis"** sjunker under tröskel 13.1V.
- **• Låg spänning återställd:** Aktiverar scenario när inkommande spänning till centralapparat **lares 4.0** är över tröskel 14.4V, eller inkommande spänning till **"opis"** är över tröskel 13.1V.
- **• Batteriladdningsfel:** Aktiverar scenario när centralapparat **lares 4.0** och/eller **"opis"** misslyckas med att leverera nödvändig ström till systemet.
- **• Batteriladdningsfel återställt:** Aktiverar scenario när batteriladdningsfel är återställt i centralapparat **lares 4.0** och/eller **"opis"**.
- **• Säkringsfel:** Aktiverar scenario när det blir säkringsfel i centralapparat **lares 4.0** och/eller **"opis"** (t ex. vid kortslutning).
- **• Säkringsfel återställd:** Aktiverar scenario när det blir säkringsfel är återställd i centralapparat **lares 4.0** och/eller **"opis"** (t ex. vid kortslutning är åtgärdat).

**Obs! Om CPU-fönstret visas i enhetsfönstret, så beror händelserna som genererar kommunikationen att det gäller fel i centralapparaten lares 4.0.**

### Type: **Fjärrkontroll**

Tillgängliga undertyper är:

- **Frånkoppling:** Aktiverar scenario när knappen Frånkoppling trycks ner på fjärrkontroll (kort tryck).
- **Hemmatillkoppling:** Aktiverar scenario när knappen hemmatillkoppling trycks ner på fjärrkontroll (kort tryck).
- **Tillkoppling:** Aktiverar scenario när knappen Tillkoppling trycks ner på fjärrkontroll (kort tryck).
- **Lång tryck på Frånkoppling:** Aktiverar scenario när knappen Frånkoppling trycks ner på fjärrkontroll (långt tryck).
- **Lång tryck på Hemmatillkoppling:** Aktiverar scenario när knappen hemmatillkoppling trycks ner på fjärrkontroll (långt tryck).
- **Lång tryck på Tillkoppling:** Aktiverar scenario när knappen Tillkoppling trycks ner på fjärrkontroll (långt tryck).
- **Lång tryck på Info knapp:** Aktiverar scenario när knappen Info knapp trycks ner på fjärrkontroll (långt tryck).

## Typ: **kod ID**

Tillgängliga undertyper är:

- **Kod igenkänd:** Aktiverar scenario när en kod är igenkänd. Kan giltig kod på manöverpanel eller i APP.
- **Bricka igenkänd:** Aktiverar scenario när en bricka är igenkänd. Kan giltig bricka på manöverpanel eller läsare

# Type: **Moderkort**

- **Sabotage:** Aktiverar scenario när det blir ett sabotagelarm i centralapparatens kapsling (dörren öppnas och/eller bortbrytning fråm vägg) detekteras genom att sabotagekontakter anslutna till T kontakter på kretskort lares.
- **Sabotage återställt:** Aktiverar scenario när det blir ett sabotagelarm är återställt i centralapparatens kapsling
- **Start av underhåll:** Aktiverar scenario när en ny programmering utförs.
- **Slut av underhåll:** Aktiverar scenario när en programmering avslutas, via portal och installatörsapp är genomförd.
- **Periodisk test:** Aktiverar scenario när ett periodiskt testhändelse sker.
- **Fel kod:** Aktiverar scenario efter 3 inkorrekta koder har angets på manöverpanelen. Efter 4 felslagna koder blockeras manöverpanelen i 90 sekunder.
- **Installatörskod används:** Aktiverar scenario när installatörskoden har använts.
- **Centralapparat stänger ner:** Aktiverar scenario när systemet stänger ner, händer vid nätfel och batteriet är urladdat. Det sker för att skydda batteriet för en total urladdning.
- **Omstart av centralapparat:** Aktiverar scenario när centralapparat startar om på grund av att spänning har återställts eller på grund av ett systemfel eller på grund av en firmwareuppdatering.
- **Ethernet nätverksfel:** Aktiverar scenario när Ethernet-kabeln är bortkopplad (eller när routern / switchen är avstängd).
- **Ethernet nätverksfel återställt:** Aktiverar scenario när Ethernet-kabeln är åter ansluten (eller när routern / switchen är aktiv igen).
- **PSTN telelinjefel:** Aktiverar scenario när telefonlinje är borta (kabelbrott eller telelinjefel).
- **PSTN telelinjefel återställt:** Aktiverar när scenario när telefonlinje är ok igen (kabel inkopplad eller telelinje ok).
- **Inget GSM nätverk:** Aktiverar scenario när GSM nätverk saknas (ingen signal, fel GSM mast/operatör eller att underhåll sker, SIM kort inaktivt eller inte längre aktiv på nätverket eller hos mobiloperatören).
- **GSM nätverk återställt:** Aktiverar scenario när GSM nätverk är återställt.
- **Fel på övervakning IP mottagare**: Aktiverar scenario när IP mottagare inte kan kommunicera för övervakningsrapporter.
- **IP mottagare återställd:** Aktiverar scenario när IP mottagare kan kvittera övervakningsrapporter.
- **Radiostörning:** Aktiverar scenario när radiostörning detekteras av centralapparat på 868Mhz bandet.
- **Radiostörning återställd:** Aktiverar scenario när radiostörning inte längre kan detekteras.

### **Kontaktlista**

För att programmera "Kontaktlistor", det vill säga de grupper av användare som tar emot larmmeddelanden (samtal, SMS, e-post, etc.), klicka på ( ) ikonen och sedan på symbolen ( ). Följande parametrar kan programmeras:

- **Beskrivning:** Identifierar en grupp kontakter (t ex anställda).
- **Alternativ:** Välj vilken typ av kommunikation som ska skickas för en viss kontaktlista. Det är möjligt att göra ett flervalsalternativ:
	- **Röstsamtal:** Skicka röstsamtal via GSM eller PSTN.
	- **SMS:** Skicka SMS.
	- **E-post:** Skicka det detaljerade e-postmeddelandet om händelsen.
	- **Contact-ID:** Skicka ett meddelande via Contact-ID-protokollet.
- **Kontakter:** Välj användare som ska ta emot larmmeddelanden.
- **Contact-ID:** Välj Contact-mottagare.

#### **Meddelanden**

På den här sidan länkar man "Meddelande" (samtal, SMS, etc.) med olika händelser.

För att programmera "Notifieringar", dvs meddelanden (samtal, SMS, e-post etc. som ska skickas), klicka på ( ) ikonen och sedan på symbolen ( ). Följande parametrar kan programmeras:

- **Typ:** Identifierar gruppgenererande notifieringar (t ex sektion, område, utgång, etc.).
- **Undertyp:** Är händelsen relaterad till föregående parameter (t ex typ: sektion undertyp: sektionslarm). Det är möjligt att göra ett multipelval med upp till 15 objekt.

När du har angett de tidigare beskrivna två parametrarna klickar du på ( ).

Nu är det nödvändigt att ställa in två andra parametrar:

- **Enhet:** Område, enhet, användare etc. som genererar meddelande.
- **Contact list:** välj en tidigare programmerad kontaktlista, som tar emot samtal, textmeddelanden, e-postmeddelanden och Contact-ID-meddelandet.

Notifikationerna är listade under<**"Undertyper"**.

- Typ: **Sektion**
- **Larm:** Skickar ett meddelande när en sektion genererar ett larm.
- **Återställning:** Skickar ett meddelande när en sektion blir återställd efter ett utlöst larm.
- **Sabotage:** Skickar ett meddelande när en sektion genererar ett sabotage larm.
- **Sabotageåterställning:** Skickar ett meddelande när en sektion blir återställd efter ett sabotagelarm.
- **Förbikopplad:** Skickar ett meddelande när en sektion är förbikopplad.
- **Återinkoppling:** Skickar ett meddelande när en sektion är återinkopplad.
- **Övertäckning:** Skickar ett meddelande när en detektor har utlöst ett övertäckningslarm.
- **Övertäckningslarm återställd:** Skickar ett meddelande när en detektor blir återställd efter ett övertäckningslarm.
- **Real tid larm:** Skickar ett meddelande när en sektion är i larmläge, om området är frånkopplat.
- **Real time återställning:** Skickar ett meddelande när en sektion ok, om området är frånkopplat.

#### Typ: **Områden**

Tillgängliga undertyper är:

- **Larm:** Skickar när ett område genererar ett larm.
- **Tillkopplad:** Skickar ett meddelande när ett område är tillkopplad.
- **Sabotage:** Skickar ett meddelande när ett område utlöser sabotagelarm.
- **Återinkopplad:** Skickar ett meddelande när ett område är återinkopplad.
- **Varning:** Skickar ett meddelande när varning i område är aktiverad.
- **Varning återställd:** Skickar ett meddelande när varning i område är deaktiverad.
- **Rondering:** Skickar ett meddelande när ronderingsstiden börjar.
- **Rondering avslutad:** Skickar ett meddelande när ronderingsstiden avslutas: systemet är tillkopplat igen.
- **Tillkopplingstid startas:** Skickar ett meddelande när tillkopplingstid påbörjas för ett område.
- **Tillkopplingstid avslutas:** Skickar ett meddelande när tillkopplingstid avslutas efter tillkoppling för ett område.
- **Utpasseringstid startas:** Skickar ett meddelande när utgångstiden påbörjas när systemet tillkopplas.
- **Utpasseringstid avslutad:** Skickar ett meddelande när utgångstiden avslutas vid tillkoppling; system är nu tillkopplad.
- **• Ej tillkopplad:** Skickar ett meddelande om systemet ej tillkopplas (om den är programmerad på sidan "Områden").
- **Tillkopplingsfel:** Skickar ett meddelande när centralapparaten avbryter en tillkoppling t ex om det är aktivitet i objektet under tillkoppling och det scenario som hanterar tillkoppling är programmerad som EN5013 eller manuell förbikoppling.

#### Typ: **Utgång**

Tillgängliga undertyper är:

- **Aktivering:** Skickar ett meddelande när en utgång är aktiverad (manuellt av APP eller via en händelse, t ex ett scenario).
- **Deaktivering:** Skickar ett meddelande när en utgång är inaktiverad (manuellt av APP eller via en händelse, t ex ett scenario).

#### Typ: **Tillbehör**

Tillgängliga undertyper är:

- **Sabotage (BUSS):** Skickar ett meddelande när en bussenhet genererar ett sabotagelarm (t ex öppning av manöverpanel).
- **Sabotage återställd (BUSS):** Skickar ett meddelande när en bussenhet genererar ett sabotagelarm som är återställd.
- **Sabotage (radio):** Skickar ett meddelande när en trådlös detektor genererar ett sabotagelarm.
- **Sabotage återställd (radio):** Skickar ett meddelande när en trådlös detektor genererar ett sabotagelarm som är återställd.
- **Tillbehör saknas (buss):** Skickar ett meddelande när en bussenhet inte längre kan detekteras av centralapparaten (t ex kabelbrott eller tillbehörsfel).
- **Tillbehör återställd (buss):** Skickar ett meddelande när en bussenhet åter kan detekteras av centralapparaten (t ex kabel åter inkopplad eller tillbehör återställd).
- **Tillbehör saknas (radio):** Skickar ett meddelande när ett radiobaserad detektor inte längre kan detekteras av centralapparaten (t ex dålig mottagning eller störning).
- **Tillbehör återställd (radio):** Skickar ett meddelande när en radiobaserad detektor åter kan detekteras av centralapparaten.

#### Typ: **Manöverpanel**

- **Knapp 0:** Skickar ett meddelande när knappen (0) trycks på manöverpanelen.
- **Knapp 1:** Skickar ett meddelande när knappen (1) trycks på manöverpanelen.
- **Knapp 2:** Skickar ett meddelande när knappen (2) trycks på manöverpanelen.
- **Knapp 3:** Skickar ett meddelande när knappen (3) trycks på manöverpanelen.
- **Knapp 4:** Skickar ett meddelande när knappen (4) trycks på manöverpanelen.
- **Knapp 5:** Skickar ett meddelande när knappen (5) trycks på manöverpanelen.
- **Knapp 6:** Skickar ett meddelande när knappen (6) trycks på manöverpanelen.
- **Knapp 7:** Skickar ett meddelande när knappen (7) trycks på manöverpanelen.
- **Knapp 8:** Skickar ett meddelande när knappen (8) trycks på manöverpanelen.
- **Knapp 9:** Skickar ett meddelande när knappen (9) trycks på manöverpanelen.

#### Typ: **Läsare**

Tillgängliga undertyper är:

- **Grön lysdiod:** Utför scenario när den gröna lysdioden på läsaren är vald och lyser.
- **Röd lysdiod:** Utför scenario när den röda lysdioden på läsaren är vald och lyser.
- **Vit lysdiod:** Utför scenario när den vita lysdioden på läsaren är vald och lyser.
- **Blåa lysdiod:** Utför scenario när den blåa lysdioden på läsaren är vald och lyser.
- **Gula lysdiod:** Utför scenario när den gula lysdioden på läsaren är vald och lyser.

#### Typ: **Kommunikation**

Tillgängliga undertyper är:

- **Kommunikation startad:** Utför scenario när centralapparaten initerar PSTN/GSM/E-post samtal etc.
- **Kommunikationfel:** Utför scenario när det blir fel vid PSTN/GSM/E-post samtal etc.
- **Inkommande samtal:** Utför scenario när centralapparaten tar emot ett samtal.
- **Contact ID kommunikation utförd:** Utför scenario när centralapparaten ringer ett Contact-ID samtal.
- **Contact ID kommunikationsfel:** Utför scenario när det blir fel vid ett Contact-ID samtal.
- **SIA kommunikation utförd:** Utför scenario när centralapparaten skickar ett larm med SIA protokoll.
- **SIA kommunikationsfel:** Utför scenario när det blir ett fel när larm ska skickas med SIA protokoll.

Avsnittet "Enhet" indikerar vem (t ex användarkod, bricka) eller vad (t.ex. enhet, sektion, område, etc.) genererar händelsen. T ex. att vi har valt att område 1 och undertyp larm, så kommer centralapparaten att utföra scenariot (tidigare programmerat på när område 1 genererar ett larm. Du kan välja flera enheter: Om du vill markera alla enheter (t ex områden) för en viss händelse, välj "Alla".

#### Typ: **Strömförsörjning**

Tillgängliga undertyper är::

- **• Nätfel:** Utför scenario vid nätfel i centralapparat **lares 4.0**, i trådlösa repeater duo eller strömförsörjning **opis**.
- **• Nätfel återställt:** Utför scenario vid återställning vid nätfel i centralapparat **lares 4.0**, i trådlösa repeater duo eller strömförsöjning **opis**.
- **• Låg batteri:** Utför scenario när batterispänning sjunker under tröskel 11V, (sker oftast när nätspänning försvinner).
- **• Låg batteri återställt:** Utför scenario är batterispänning är återställd (sker oftast när nätspänning kommer tillbaka).
- **• Batterifel:** Utför scenario när centralapparat **lares 4.0**, imago siren, trådlösa tillbehör och strömförsörjning **"opis"** inte klarar battertest.
- **• Låg spänning:** Utför scenario när inkommande spänning till centralapparat **lares 4.0** sjunker under tröskel 14.4V, eller inkommande spänning till **"opis"** sjunker under tröskel 13.1V.
- **• Låg spänning återställd:** Utför scenario när inkommande spänning till centralapparat **lares 4.0** är över tröskel 14.4V, eller inkommande spänning till **"opis"** är över tröskel 13.1V.
- **• Batteriladdningsfel:** Utför scenario när centralapparat **lares 4.0** och/eller **"opis"** misslyckas med att leverera nödvändig ström till systemet.
- **• Batteriladdningsfel återställt:** Utför scenario när batteriladdningsfel är återställt i centralapparat **lares 4.0** och/eller **"opis"**.
- **• Säkringsfel:** Utför för scenario när det blir säkringsfel i centralapparat **lares 4.0** och/eller **"opis"** (t ex. vid kortslutning).
- **• Säkringsfel återställd:** Utför scenario när det blir säkringsfel är återställd i centralapparat **lares 4.0** och/eller **"opis"** (t ex. vid kortslutning är åtgärdat).

#### **Obs! Om CPU-fönstret visas i enhetsfönstret, så beror händelserna som genererar kommunikationen att det gäller fel i centralapparaten lares 4.0.**

## Type: **Fjärrkontroll**

Tillgängliga undertyper är:

- **Frånkoppling:** Utför scenario när knappen Frånkoppling trycks på fjärrkontroll (kort tryck).
- **Hemmatillkoppling:** Utför scenario när knappen hemmatillkoppling trycks på fjärrkontroll (kort tryck).
- **Tillkoppling:** Utför scenario när knappen Tillkoppling trycks på fjärrkontroll (kort tryck).
- **Långt tryck på Frånkoppling:** Utför scenario när knappen Frånkoppling trycks på fjärrkontroll (långt tryck).
- **Långt tryck på Hemmatillkoppling:** Utför scenario när knappen hemmatillkoppling trycks på fjärrkontroll (långt tryck).
- **Långt tryck på Tillkoppling:** Utför scenario när knappen Tillkoppling trycks på fjärrkontroll (långt tryck).
- **Långt tryck på Infoknapp:** Utför scenario när knappen Info trycks på fjärrkontroll (långt tryck).

#### Typ: **kod ID**

Tillgängliga undertyper är:

- **Kod igenkänd:** Utför scenario när en kod som är igenkänd används på manöverpanel eller i APP.
- **Bricka igenkänd:** Utför scenario när en bricka är igenkänd används på manöverpanel eller läsare.

#### Type: **Moderkort**

- **Sabotage:** Utför scenario när det blir ett sabotagelarm i centralapparatens kapsling (dörren öppnas och/eller bortbrytning fråm vägg) detekteras genom att sabotagekontakter anslutna till T kontakter på kretskort lares.
- **Sabotage återställt:** Utför scenario när ett sabotagelarm blir återställt i centralapparatens kapsling.
- **Underhåll startad:** Utför scenario när en ny programmering utförs.
- **Underhåll asvlutad:** Utför scenario när en programmering avslutas, via portal och installatörsapp är genomförd.
- **Periodisk test:** Utför scenario när ett periodiskt testhändelse sker.
- **Fel kod:** Utför scenario efter 3 inkorrekta koder har angets på manöverpanelen. Efter 4 felslagna koder blockeras manöverpanelen i 90 sekunder.
- **Installatörskod används:** Utför scenario när installatörskoden har använts.
- **Centralapparat stänger ner:** Utför scenario när systemet stänger ner, händer vid nätfel och batteriet är urladdat. Det sker för att skydda batteriet för en total urladdning.
- **Omstart av centralapparat:** Utför scenario när centralapparat startar om på grund av att spänning har återställts eller på grund av ett systemfel eller på grund av en firmwareuppdatering.
- **Ethernet nätverksfel:** Utför scenario när Ethernet-kabeln är bortkopplad (eller när routern / switchen är avstängd).
- **Ethernet nätverksfel återställt:** Utför scenario när Ethernet-kabeln är åter ansluten (eller när routern / switchen är aktiv igen).
- **PSTN telelinjefel:** Utför scenario när telefonlinje är borta (kabelbrott eller telelinjefel).
- **PSTN telelinjefel återställt:** Utför scenario när telefonlinje är ok igen (kabel inkopplad eller telelinje ok).
- **Inget GSM nätverk:** Utför scenario när GSM nätverk saknas (ingen signal, fel GSM mast/operatör eller att underhåll sker, SIM kort inaktivt eller inte längre aktiv på nätverket eller hos mobilopratören).
- **GSM nätverk återställt:** Utför scenario när GSM nätverk är återställt.
- **Fel på övervakning IP mottagare**: Utför scenario när IP mottagare inte kan kommunicera för övervakningsrapporter.
- **IP mottagare återställd:** Utför scenario när IP mottagare kan kvittera övervakningsrapporter.
- **Radiostörning:** Utför scenario när radiostörning detekteras av centralapparat på 868Mhz bandet.
- **Radiostörning återställd:** Utför scenario när radiostörning inte längre kan detekteras.

| Realtid                                                                                                                                                        |                                                         |  |  |  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|--|--|--|
| På realtidssidorna är det möjligt att kontrollera systemets status.<br>En realtidsstatusvisning av alla enheter anslutna till centralapparaten är tillgänglig. |                                                         |  |  |  |
| • Realtidssektioner:                                                                                                                                           |                                                         |  |  |  |
|                                                                                                                                                                |                                                         |  |  |  |
|                                                                                                                                                                | är i normalläge                                         |  |  |  |
| För att förbikoppla en sektion, använd "knappen" bredvid statusikonen:                                                                                         |                                                         |  |  |  |
| inkopplad                                                                                                                                                      |                                                         |  |  |  |
| är förbikopplad                                                                                                                                                |                                                         |  |  |  |
|                                                                                                                                                                |                                                         |  |  |  |
|                                                                                                                                                                | Förbikopplad sektion (statusikonen blir ogenomskinlig). |  |  |  |
|                                                                                                                                                                |                                                         |  |  |  |
|                                                                                                                                                                | Sektionen i larmläge                                    |  |  |  |
|                                                                                                                                                                |                                                         |  |  |  |
|                                                                                                                                                                | Sektionen är i sabotage och sabotagelarm pågår          |  |  |  |
|                                                                                                                                                                |                                                         |  |  |  |
|                                                                                                                                                                |                                                         |  |  |  |
|                                                                                                                                                                | Sektionen är i sabotage och sabotageminne finns         |  |  |  |
|                                                                                                                                                                |                                                         |  |  |  |
|                                                                                                                                                                | Sektionsfel (övertäckning) och fellarm pågår            |  |  |  |
|                                                                                                                                                                |                                                         |  |  |  |
|                                                                                                                                                                |                                                         |  |  |  |
|                                                                                                                                                                | Sektion ok, men felminne finns                          |  |  |  |
|                                                                                                                                                                |                                                         |  |  |  |

![](_page_51_Figure_0.jpeg)

|                                                                             | Område tillkopplat                                                                                                                                                                                             |
|-----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                             | Område tillkopplat och larm pågår                                                                                                                                                                              |
| • Realtid för användargränssnitt (manöverpaneler, läsare) anslutna på buss: | I det här avsnittet är enheterna indelade i grupper (ergo, läsare, etc.). Välj önskad grupp för att visa status för enheterna.<br>Ansluten och fungerande enhet på buss. Serienr och firmwareversion<br>visas. |
|                                                                             | Tillbehör i sabotage                                                                                                                                                                                           |
|                                                                             | Tillbehör saknas.                                                                                                                                                                                              |

Informationen ovan gäller är likadan för alla bussenheter.

#### **Realtid för bussirener:**

Bussirenerna visar samma information som de andra kringutrustningen med den enda skillnaden att i detta fall visas även spänning för kretskort och backupbatteriet (t ex siren radius)

![](_page_53_Figure_2.jpeg)

**Realtid för trådlösa repeaters (ska kontrolleras eftersom det inte ska finnas en "duo" i repeater-läge och kan därför inte utföra andra tester):** Trådlös repeater är programmerad men inte kommunicerar med systemet. Aktuell spänning Batterispänning **Realtid för trådlösa detektorer ("unum", "poli" etc.) och trådlösa I/O-moduler ("auxi wls"):** Trådlös enhet ("unum") och den relaterade statusen för radiosignalen. Den visar: datumet, tiden för den sista överföringen och vilken mottagare som den kommunicerar med. Trådlös detektor inlärd men kommunicerar inte med systemet. Trådlös detektor ("unum") i sabotage och detekteras av den interna mottagaren). Radiosignal Radiosignal 1 (högre än -76db) Radiosignal 2 (mellan -90db och -76db) Radiosignal 3 (mellan -100db och -91db) Radiosignal 4 (lägre än -101db) Spänningsinformationen

# **Talmeddelanden**

Från webbserverns installatör 1.5.1-version är det möjligt att generera talmeddelanden även med lokal anslutning med centralapparaten, vilket inte är möjligt med tidigare versioner som krävde Online-anslutning med Secureweb-portalen. Om du redan har en Loquendo USB-minne, lägg bara till några filer genom att hämta dem från det kseniasecurity.com Loquendo_lares4.zip). När filen har laddats ner måste den komprimeras upp på USB-minne: Nu är USB-minne klar för användas med lares 4.0 och denna åtgärd får inte upprepas igen.

#### **Lyssna**

Huvudfönstret visar de talmeddelanden som genereras och som delas upp i underkategorier (händelser, sektioner, områden etc.)

![](_page_55_Picture_4.jpeg)

Talmeddelande är tillgängligt för nedladdning.

Talmeddelande har laddats ner och redo att lyssnas på.

# **Generera**

För att skapa talmeddelanden via Secureweb-portalen måste du ha en aktiverad Loquendo-licens, som finns på ett skraplicensskort.

- För att generera talmeddelanden i peer-to-peer-läget med centralapparaten måste du istället utföra följande steg:
	- 1. Öppna centralapparaten via en lokal anslutning, i okrypterat läge (så i http istället för https). För att ändra standardinställningen behöver du komma åt konfigurationen av centralapparaten och i avsnittet "Alternativ" "Nätverk" och sedan i avsnittet "Webbserver" och under "Protokoll" välj "Ingen" läget (port 80).
	- 2. Stäng webbläsaren.
	- 3. Anslut USB-minnet till datorn, stäng av brandväggen som kan förhindra kommunikation med USB-minnet. Öppna filmappen på USB-minnet och som är extraherad från .zip-filen. Starta servern manuellt genom att dubbelklicka på lares-4-win i Windows eller lares-4 mac på en MAC.
	- 4. Logga in på centralapparaten med en lokal anslutning igen.
	- 5. I avsnittet talmeddelanden finns meny för generering av talmeddelanden.
	- 6. När generering av talmeddelanden är klart bör man återställa anslutningen till det krypterade läget igen.

Rubrikmeddelanadet ställs in under "Alternativ" "talmeddelanden".

Följande kan väljas:

![](_page_55_Picture_18.jpeg)

Programmeringen har ändrats, skapa talmeddelanden nu.

Visas när talmeddelanden ännu inte har genererats eller har skapats tidigare, men under tiden har konfiguratione ändrats. Så här skapar du talmeddelanden:

- 1. Välj en röst (kräver en Loquendo-licens).
2. Klicka på ( )

Grattis, alla talmeddelanden är utförda.

Detta visas så snart alla talmeddelanden har skapats korrekt. Du behöver inte generera dem igen om så vidare du inte gör några konfigurationsändringar (sektioner, områden etc.)

Installationen av dessa enheter måste utföras med goda tekniska kunskaper, i enlighet med gällande bestämmelser. Dessa enheter har utvecklats enligt kriterierna för kvalitet, tillförlitlighet och prestanda som antogs av Ksenia Security. Det rekommenderas att kontrollera systemets korrekta funktion minst en gång i månaden. Testprocedurerna beror på systemkonfigurationen. Kontakta nstallatören för mer information.. Ksenia Security Srl avvisar allt ansvar i händelse av att utrustningen ändras av obehörig personal. Innehållet i denna manual kan komma att ändras utan föregående meddelande och representerar inte ett åtagande från KSENIA SECURITY.

#### **Avfall och återvinngsinformation för användare (WEEE-direktiv)**

#### Varning! För att kassera den här enheten, använd inte en vanlig soptunna!

Använd elektrisk och elektronisk utrustning måste hanteras separat och i enlighet med lagstiftningen som kräver korrekt bearbetning, återvinning och återvinning av ovannämnda produkter. Som ett resultat av de bestämmelser som genomförts av medlemsstaterna kan enskilda invånare i EU ge använd elektrisk och elektronisk utrustning till utsedda återvinningscentraler * eller till en lokal återförsäljare som kan dra in utan kostnad om användaren köper en annan ny produkt av liknande typ .

Om elektrisk eller elektronisk utrustning används har batterier eller ackumulatorer, måste användaren kassera dem separat i förväg i enlighet med lokala föreskrifter. Korrekt bortskaffande av denna produkt kommer att bidra till att avfallet utsätts för behandling, återvinning och återvinning som är nödvändig för att förhindra dess potentiella negativa inverkan på miljön och människors hälsa, vilket kan vara en följd av otillräcklig avfallshantering. Mycket höga sanktioner förutses vid oegentligheter i enlighet med lagdekret 151/05.

* För mer information kontakta berörd myndighet.

#### **RESPEKT FÖR MILJÖ OCH HÄLSA**

**lares 4.0 har konstruerats och byggts med följande egenskaper för att minska miljöpåverkan:**

- 1. PVC-fri
- 2. Halogenfria laminat och blyfria kretskort
- 3. Låg absorption
- 4. Förpackningar gjordes huvudsakligen med återvunna fibrer och material från förnybara källor

![](_page_57_Picture_6.jpeg)

![](_page_57_Picture_7.jpeg)