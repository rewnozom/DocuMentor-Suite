![](_page_0_Picture_0.jpeg)

# **AA A485-DTMF**

### **INSTALLATIONSANVISNING**

**Revision 1**

## **INSTALLATION 2**

#### **ALLMÄNT**

Interfacet används för att kunna koppla in läsare med 485-kommunikation till äldre central med DTMF-kommunikation.

![](_page_1_Figure_5.jpeg)

#### **TEKNISKA DATA**

|                 | Strömförsörjning: 12 - 24V DC reglerad (10.8 - 27.4). |
|-----------------|-------------------------------------------------------|
|                 | Max 23mA (vid 12V), Min 16mA (vid 24V).               |
|                 | Matning från centralenheten.                          |
| Matning läsare: | 12V DC. Om inkommande spänning faller under           |
|                 | 12V så faller även denna i motsvarande grad.          |
|                 | Avsäkrad: 200mA.                                      |
| Antal läsare:   | 1 läsare kan kopplas till varje interface.            |
| Miljökrav:      | -30 till +60 grader Celcius.                          |
|                 | 10 till 100% luftfuktighet.                           |
| Mått:           | 98x98x52 mm.                                          |
|                 |                                                       |

#### **PACKLISTA**

1 st AA A485-DTMF, Interface Aptus485 - DTMF

- 2 st Skruv med plugg
- 1 st Installationsanvisning (denna)

#### **SYSTEMBESKRIVNING**

![](_page_1_Figure_13.jpeg)

#### **MONTERING**

Enheten är avsedd för utanpåliggande montage. Lossa locket och kretskortet. Skruva sedan fast bakstycket med bilagda skruv så att kabelintag görs i underkant. På lockets insida sitter 2st tätningsbrickor som skakk tryckas in ovanför monteringsskruvarna. Tryck nu fast kretskortet i plastsnäppena.

Dra fram kablage och dra in i kapslingen. Anslut kabeln till de jackbara plintarna. Avsluta monteringen genom att skruva på locket.

#### **INKOPPLINGSANVISNING**

Använd partvinnad kabel, t.ex. av typ ELLXB 2x2x0.5 eller ELAQBY 2x2x0.6 både för anslutning till centralenhet och anslutning till läsare.

#### **Anslutning till centralenhet (J2)**

Förlägg paren enligt följande: Par 1: (Gnd, S); Par 2: (Gnd,+). **Obs!** + skall inte kopplas till dörringångens + på centralen utan till centralens matningsspänning.

Maximal kabellängd till central är 100m. Överstiger kabellängden 50m bör kabelarean vara minst 0.5mm2 för spänningsmatningen. **Anslutning till läsare (J1)**

Förlägg ett par till 485 (A+B) och spänning (12V+GND) i det andra paret.

![](_page_1_Figure_23.jpeg)

Interfacet är alltid terminerat gentemot Aptus485-bussen. Tänk dock på att terminera också i läsaren.

![](_page_2_Picture_1.jpeg)

![](_page_2_Picture_2.jpeg)

#### **LYSDIODER**

AA A485-DTMF har lysdioder för att indikera kommunikation till läsare.

| D3 | Gul | Blinkar då data tas emot från läsare. |
|----|-----|---------------------------------------|
| D4 | Röd | Blinkar då data sänds till läsare.    |

#### **INSTÄLLNINGAR**

| S1 | Modifierad | ON => Läsare modifierad. Inställningen      |
|----|------------|---------------------------------------------|
|    |            | används i de fall en dörr har både in och   |
|    |            | utläsare. I så fall skall inläsaren modifie |
|    |            | ras.                                        |
|    |            | Vid leverans: OFF.                          |

#### **SYSTEMKRAV**

MultiAccess från version 5.0. AC/TC/BC 387/500/600/700 från version F1.

#### **PROGRAMMERING**

Central och MultiAccess uppfattar 485-läsaren tillsammans med AA 485-DTMF som en helt vanlig DTMF-läsare. Programmeringen görs på sedvanligt sätt på dörren i MultiAccess. Avsluta programmeringen med att sända data.

#### **AVPROVNING**

Kontrollera en extra gång att alla signalledare är rätt inkopplade innan anläggningen spänningssätts. Kontrollera att läsare och interface kommunicerar, både röd och gul lysdiod skall blinka. Läs en nyckelbricka i läsaren och verifiera att den kommer in korrekt.

#### **GARANTI**

Aptus Elektronik AB lämnar två års garanti på material och fabrikationsfel på samtliga produkter. Övrigt enligt leveransbestämmelser NL01.

#### **SERVICE**

För service hänvisar APTUS Elektronik AB till ansvarig återförsäljare som utöver egen kompetens har kontinuerlig kontakt med APTUS Elektronik AB.