![](_page_0_Picture_0.jpeg)

# **SPCW130**

![](_page_0_Picture_2.jpeg)

**SiWay RF-Expander for X-BUS (en) SiWay Funk-Erweiterungsmodul für X-BUS (de) Módulo de expansión RF SiWay para X-BUS (es) Transpondeur SiWay RF pour X-BUS (fr) Espansione RF SiWay per X-BUS (it) SiWay RF-uitbreiding voor X-BUS (nl) SiWay RF-expansionsenhet för X-BUS (sv)**

![](_page_0_Figure_4.jpeg)

# **English – Installation Instructions**

**WARNING** Before starting to install and work with this device, please read the *Safety Instructions*.

This device shall only be connected to power supplies compliant to EN60950-1, chapter 2.5 ("limited power source").

- When changing or installing a SPCW130 on the SPC system, ensure that all anti-static precautions are adhered to while handling connectors, wires, terminals and PCBs.
## **EC Declaration of Conformity**

Hereby, Vanderbilt International (IRL) Ltd declares that this radio equipment type is in compliance with all relevant EU Directives for CE marking. From 20/04/2016 it is in compliance with Directive 2014/30/EU (Electromagnetic Compatibility Directive) and Directive 2014/35/EU (Low Voltage Directive) . From 13/06/2016 it is also in compliance with Directive 2014/53/EU (Radio Equipment Directive). The full text of the EU declaration of conformity is available at http://pcd.vanderbiltindustries.com/doc/SPC

## **Introduction to the SPCW130**

The SPCW130 provides an interface for 868 MHz wireless detectors. The SPCW130 incorporates the following elements, as shown in Fig. 1.

 The expander should be powered up for at least 30 seconds before performing any operations.

- **1.** Front tamper switch the expander has a front tamper switch with spring. When the lid is closed the spring closes the switch.
- **2.** Tamper by-pass [J1] the jumper setting determines the operation of the tamper. The tamper operation can be overridden by fitting J1.
- **3.** Buzzer the buzzer is activated in order to locate the expander (see *SPC Configuration Manual*).
- **4.** Wireless module the module provides the wireless interface for 868 MHz devices. Please note that only Intrunet wireless devices can be enrolled on to this device.
- **5.** LED activated if wireless telegrams are received. The LED is indication the reception of all wireless telegrams. It is also indicating the reception of not valid wireless telegrams.
- **6.** X-BUS status LED the LED indicates the status of the X-BUS when the system is in FULL ENGINEER mode, as shown below:

| LED status                                             | Description                                                                         |
|--------------------------------------------------------|-------------------------------------------------------------------------------------|
| Flashes regularly                                      | The X-BUS communications status is OK.                                              |
| (once every 1.5 seconds<br>approx.)                    |                                                                                     |
| Flashes quickly<br>(once every 0.2 seconds<br>approx.) | Indicates the last in line expander (excludes star<br>and multi-drop configuration) |

- **7.** Manual addressing switches the switches allow manual setting of the ID of each expander in the system.
- **8.** Auxiliary power supply (12 V) these are used to power auxiliary devices to a maximum of 200 mA.
- **9.** Input power the expander requires 12 V DC that can be supplied directly from the SPC-series controller or from a SPC PSU expander.
- **10.** X-BUS interface the communication bus is used to connect expanders together on the SPC-series system (see section Wiring the X-BUS interface).
- **11.** Termination jumper this jumper as a default is always fitted, however, when wiring for Star configuration this fitting should be removed (see section Wiring the X-BUS interface).

## **Wiring the X-BUS Interface**

The X-BUS interface provides connection of expanders and keypads to the SPC controller. The X-BUS can be wired in a number of different configurations depending on the installation requirements.

**NOTE:** Maximum system cable length = number of expanders and keypads in the system x maximum distance for cable type.

| Cable type                   | Distance |
|------------------------------|----------|
| CQR standard alarm cable     | 200 m    |
| UTP category: 5 (solid core) | 400 m    |
| Belden 9829                  | 400 m    |
| IYSTY 2 x 2 x 0.6 (min)      | 400 m    |

Fig. 2 shows the wiring of the X-BUS to an expander/controller and the following expander/ controller in Spur configuration. Terminals 3A/3B and 4A/4B are only used for using a branch wiring technique. If using a Spur configuration, the last expander is not wired back to the controller.

## **Fig. 2: Wiring of Expanders**

**1** SPC controller

- **2** Previous expander
- **3** SPCW130
- **4** Next expander

Please refer to *SPC Configuration Manual* of connected controller for further wiring instructions, shielding, specifications and limitations.

## **X-BUS Addressing**

For addressing, reconfiguration, device location, monitoring, editing of names, X-BUS type of communication, failure timer please refer to *SPC Configuration Manual*.

## **Appendix**

|   | Fig. 3: SPCW130 Enclosure |
|---|---------------------------|
| 1 | Expander anchor points    |
| 2 | Wall spacers              |
| 3 | Cover anchor points       |
| 4 | Cable grips               |
| 5 | Mounting holes            |
| 6 | Cable entry holes         |
| 7 | Cable ties                |
| 8 | Cover hooks               |
|   |                           |

### **Fig. 4: Expander Cover**

| 1 | Front tamper guide  |
|---|---------------------|
| 2 | Cover fixing screws |

**Technical Data Operating voltage** 9.5 – 14 V DC **Current consumption** 60 mA at 12 V DC **Field bus** X-BUS on RS485 (307 kb/s) **Interfaces** X-BUS (In, Out, Branch) **Radio module** Integrated SiWay RF receiver (868 MHz) **Tamper contact** On-board front spring tamper **Operating temperature** -10 to +50 °C **Relative humidity** Max. 90 % (no condensation) **Colour** RAL 9003 **Mounting** Surface, wall-mounted **Dimensions (W x H x D)** Enclosure: 200 x 153 x 47 mm PCB: 150 x 82 x 20 mm **Weight** 0.34 kg **Housing material** ABS **Housing** Plastic enclosure **Housing protection / IP rating** IP30 **Standards** EN50131-3:2009 (Grade 3, Class II)

## **Deutsch – Anweisungen**

**WARNUNG** Lesen Sie vor der Installation und Verwendung dieses Geräts die Sicherheitshinweise.

Das Gerät darf nur an einer Stromversorgung angeschlossen werden, welche der Norm EN 60950-1 / Kapitel 2.5 ("begrenzte Stromquelle") entsprechen.

Beim Austauschen oder Installieren eines SPCW130 im SPC-System müssen während der Handhabung von Anschlüssen, Drähten, Klemmen und Platinen alle erforderlichen Antistatik-Maßnahmen getroffen werden.

## **EG-Konformitätserklärung**

Hiermit erklärt Vanderbilt International (IRL) Ltd, dass dieser Funkgerätetyp den Anforderungen aller relevanten EU-Richtlinien für die CE-Kennzeichnung entspricht. Ab dem 20.04.2016 entspricht er der Richtlinie 2014/30/EU (Richtlinie über elektromagnetische Verträglichkeit) und der Richtlinie 2014/35/EU (Niederspannungsrichtlinie). Ab dem 13.06.2016 entspricht er außerdem der Richtlinie 2014/53/EU (Richtlinie über Funkanlagen).

Der vollständige Text der EU-Konformitätserklärung steht unter http://pcd.vanderbiltindustries.com/doc/SPC zur Verfügung.

## **SPCW130 – Einführung**

Das SPCW130 stellt eine Schnittstelle für 868-MHz-Funkmelder zur Verfügung. Das SPCW130 besteht aus folgenden Komponenten, die in Abb. 1 dargestellt sind:

- Das Erweiterungsmodul sollte mindestens 30 Sekunden lang mit Strom versorgt werden, bevor irgendwelche Operationen ausgeführt werden.
- **1.** Sabotageschalter auf der Frontplatte Das Erweiterungsmodul hat einen Sabotageschalter mit Feder. Beim Schließen des Deckels schließt die Feder den Schalter.
- **2.** Tamper Bypass [J1] Die Jumper-Einstellung legt den Betrieb des Sabotagealarms fest. Der Sabotagebetrieb kann durch Stecken von Jumper J1 umgangen werden.
- **3.** Summer Der Summer wird aktiviert, um das Erweiterungsmodul zu lokalisieren (siehe Konfigurationshandbuch).
- **4.** Funkmodul Das Modul stellt eine Schnittstelle für 868-MHz-Geräte zur Verfügung. Beachten Sie, dass Sie nur drahtlose Intrunet-Geräte an diesem Funkmodul anmelden können.
- **5.** LED Leuchtet, wenn Funktelegramme empfangen werden. Die LED zeigt den Empfang aller Funktelegramme an. Sie zeigt auch den Empfang von ungültigen Funktelegrammen an.
- **6.** X-BUS-Status-LED Die LED zeigt den Status des X-BUS an, wenn sich das System wie unten dargestellt im Konfigurationsmodus befindet:

| LED-Status                                   | Beschreibung                                                                                                     |
|----------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Blinkt regelmäßig<br>(ca. alle 1,5 Sekunden) | Status der X-BUS-Kommunikation ist OK.                                                                           |
| Blinkt schnell<br>(ca. alle 0,2 Sekunden)    | Zeigt das letzte Erweiterungsmodul in<br>Reihe an (berücksichtigt keine Stern- und<br>Multidrop-Konfigurationen) |

- **7.** Schalter zum manuellen Adressieren Die Schalter ermöglichen das manuelle Einstellen der ID jedes Erweiterungsmoduls im System.
- **8.** Hilfsausgangsspannung (12 V) Wird verwendet um Hilfsausgänge mit maximal 200 mA zu versorgen.
- **9.** Versorgungsspannung Der Expander benötigt eine 12-V-DC-Versorgung, die direkt vom SPC-Controller oder einem SPC PSU-Erweiterungsmodul geliefert werden.
- **10.** X-BUS-Schnittstelle Der Kommunikationsbus verbindet die Erweiterungsmodule im SPC-System untereinander (siehe Abschnitt Verdrahtung der X-BUS-Schnittstelle.
- **11.** Abschluss-Jumper Dieser Jumper ist standardmäßig immer gesteckt, muss jedoch bei einer Sternkonfiguration entfernt werden (siehe Abschnitt Verdrahtung der X-BUS-Schnittstelle).

## **Verdrahtung der X-BUS-Schnittstelle**

Die X-BUS-Schnittstelle stellt die Verbindungen von Erweiterungsmodulen und Bedienteilen zum SPC-Controller bereit. Der X-BUS kann je nach Anforderungen der Installation auf unterschiedliche Weise verdrahtet werden.

**HINWEIS:** Maximale Systemkabellänge = Anzahl von Erweiterungsmodulen und Bedienteilen im System mal maximale Entfernung nach Kabeltyp.

| Kabeltyp                     | Abstand |
|------------------------------|---------|
| CQR Standard-Alarmkabel      | 200 m   |
| UTP Kategorie 5 (solid core) | 400 m   |
| Belden 9829                  | 400 m   |
| IYSTY 2 x 2 x 0.6 (min.)     | 400 m   |

Abb. 2 zeigt die Verdrahtung des X-Bus mit dem Erweiterungsmodul/Controller und das/den folgende/n Erweiterungsmodul/Controller in

Stichleitungskonfiguration. Die Klemmen 3A/3B und 4A/4B werden nur für Abzweigverdrahtungen verwendet. Bei einer Stichleitungskonfiguration hat das letzte Erweiterungsmodul keine Rückleitung zum Controller.

#### **Siehe Abb. 2: Verdrahtung von Erweiterungs-modulen**

- **1** SPC-Controller
- **2** Vorangegangenes Erweiterungsmodul
- **3** SPCW130
- **4** Nächstes Erweiterungsmodul

Weitere Einzelheiten zur Verdrahtung und Abschirmung sowie Spezifikationen und Einschränkungen enthält das SPC Konfigurationshandbuch des angeschlossenen Controllers.

## **X-BUS-Adressierung**

Einzelheiten zu Adressierung, Rekonfiguration, Geräteanordnung, Überwachung, Namensbearbeitung, X-BUS-Kommunikationstyp, Ausfall-Timer enthält das SPC Konfigurationshandbuch.

## **Anhang**

#### **Siehe Abb. 3: SPCW130 Gehäusespezifikation**

- **1** Befestigungspunkte des Erweiterungsmoduls
- **2** Abstandshalter
- **3** Befestigungspunkte der Abdeckung
- **4** Kabelziehklemmen
- **5** Montagelöcher
- **6** Kabeleintrittsöffnungen
- **7** Kabelbinder
- **8** Abdeckungshaken

## **Siehe Abb. 4: Abdeckung des Erweiterungsmoduls**

- **1** Führung des Alarmschalters auf der Frontplatte
- **2** Befestigungsschrauben der Abdeckung

| Technische Daten           |                                                         |  |
|----------------------------|---------------------------------------------------------|--|
| Betriebsspannung           | 9,5 -14 V Gleichspannung                                |  |
| Stromverbrauch             | 60 mA bei 12 V DC                                       |  |
| Feldbus                    | X-BUS über RS485 (307 kBit/s)                           |  |
| Schnittstellen             | X-BUS (Ein, Aus, Verzweigung)                           |  |
| Funkmodul                  | Integrierter SiWay Funkempfänger (868 MHz)              |  |
| Sabotagekontakt            | Onboard-Sabotagekontakt in der Frontplatte mit<br>Feder |  |
| Betriebstemperatur         | -10 bis +50 ºC                                          |  |
| rel. Luftfeuchtigkeit      | Max. 90% (nicht kondensierend)                          |  |
| Schutzklasse               | IP30                                                    |  |
| Farbe                      | RAL 9003                                                |  |
| Gehäuseschutzart           | Class II, innen allgemein                               |  |
| Montage                    | Wandmontage, auf Putz                                   |  |
| Abmessungen<br>(B x H x T) | Gehäuse: 200 x 153 x 47 mm                              |  |

|                    | Platine: 150 x 82 x 20 mm          |
|--------------------|------------------------------------|
| Gewicht            | 0,34 kg                            |
| Gehäusematerial    | ABS                                |
| Gehäuse            | Kunststoffgehäuse                  |
| Schutzklasse       | IP30                               |
| Standards / Normen | EN50131-3:2009 (Grad 3, Klasse II) |

## **Español – Instrucciones**

**ADVERTENCIA** Antes de instalar y usar este dispositivo, lea las Instrucciones de seguridad.

Este dispositivo únicamente se conectará a fuentes de alimentación que cumplan la norma EN60950-1, capítulo 2.5 ("Fuente de alimentación limitada").

Cuando cambie o instale un SPCW130 en el sistema SPC-series, debe tomar todas las precauciones antiestáticas al manipular conectores, cables, terminales y placas.

## **Declaración de conformidad CE**

Por la presente, Vanderbilt International (IRL) Ltd declara que este tipo de equipo de radio cumple con todas las directivas de la UE relevantes para el marcado CE. Desde el 20/04/2016 cumple con la directiva 2014/30/UE (directiva de compatibilidad electromagnética) y con la directiva 2014/35/UE (directiva sobre baja tensión). Desde el 13/06/2016 cumple también con la directiva 2014/53/UE (directiva de equipos radioeléctricos).

El texto completo de la declaración UE de conformidad está disponible en http://pcd.vanderbiltindustries.com/doc/SPC

## **Introducción al SPCW130**

El SPCW130 proporciona una interfaz para detectores vía radio de 868 MHz. El SPCW130 incorpora los siguientes elementos, como se muestra en la Fig. 1.

- El módulo de expansión debe permanecer encendido durante al menos 30 segundos antes de realizar cualquier operación.
- **1.** Interruptor de tamper delantero El módulo posee en la parte frontal un interruptor de tamper accionado por un muelle. Cuando la tapa está cerrada, el muelle cierra el interruptor.
- **2.** Anulación tamper [J1] La configuración del puente determina el funcionamiento del tamper. El tamper se puede anular colocando el puente J1.
- **3.** Zumbador El zumbador se activa para localizar el módulo de expansión (véase el Manual de configuración del sistema SPC).
- **4.** Receptor vía radio El módulo proporciona la interfaz vía radio para dispositivos de 868 MHz. Tenga en cuenta que en este dispositivo sólo se pueden registrar dispositivos vía radio de Intrunet.
- **5.** LED Se activa cuando se reciben señales vía radio. El LED indica la recepción de todas las señales vía radio. También indica la recepción de señales vía radio no válids.
- **6.** LED de estado de X-BUS El LED indica el estado del X-BUS cuando el sistema está en modo TÉCNICO COMPLETO, como se muestra a continuación:

| Estado del LED                                              | Descripción                                                                                                      |
|-------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Parpadea regularmente<br>(aprox. una vez cada 1,5 segundos) | El estado de las comunicaciones de X<br>BUS es correcto                                                          |
| Parpadea rápidamente<br>(aprox. una vez cada 0,2 segundos)  | Indica el último módulo de expansión de<br>la línea (excepto en las configuraciones<br>en estrella y multipunto) |

- **7.** Interruptores de direccionamiento manual Los interruptores permiten la configuración manual de la dirección de cada módulo de expansión existente en el sistema.
- **8.** Fuente de alimentación auxiliar (12 V) Sirve para alimentar dispositivos auxiliares hasta un máximo de 200 mA.
- **9.** Potencia de entrada El módulo de expansión se alimenta con 12 Vcc, que pueden ser suministrados directamente desde la central SPC o desde una fuente de alimentación auxiliar.
- **10.** Interfaz X-BUS El bus de comunicación sirve para conectar los módulos de expansión conjuntamente con el sistema de la serie SPC (consulte la sección Cableado de la interfaz X-BUS).
- **11.** Puente de terminación Este puente siempre está colocado por defecto; sin

embargo, cuando se realiza el cableado para la configuración en estrella, se debe retirar dicho puente (consulte la sección Cableado de la interfaz X-BUS).

## **Cableado de la interfaz X-BUS**

La interfaz X-BUS permite conectar módulos de expansión y teclados al controlador SPC. El X-BUS se puede cablear con un gran número de configuraciones diferentes según los requisitos de la instalación.

NOTA: Longitud máxima de cables del sistema = número de módulos de expansión y teclados en el sistema × distancia máxima del tipo de cable.

| Tipo de cable                    | Distancia |
|----------------------------------|-----------|
| Cable de alarma estándar CQR     | 200 m     |
| Categoría UTP: 5 (núcleo sólido) | 400 m     |
| Belden 9829                      | 400 m     |
| IYSTY 2 x 2 x 0,6 (mín.)         | 400 m     |

La Fig. 2 muestra el cableado del X-BUS a un módulo de expansión/controlador y al siguiente módulo de expansión/controlador en configuración en punta. Los terminales 3A/3B y 4A/4B sólo se utilizan para emplear una técnica de cableado de bifurcación. Si emplea una configuración en punta, el último módulo de expansión no se conecta al controlador.

#### **Véase Fig. 2: Cableado de módulos de expansión**

- **1** Controlador SPC
- **2** Módulo de expansión anterior
- **3** SPCW130
- **4** Módulo de expansión siguiente

Consulte, en el Manual de configuración de SPC del controlador conectado, otras instrucciones sobre cableado, apantallamiento, especificaciones y limitaciones de los cables.

## **Direccionamiento X-BUS**

Para información sobre direccionamiento, reconfiguración, ubicación de dispositivos, supervisión, edición de nombres, tipo de comunicación X-BUS o fallo del temporizador, consulte el Manual de configuración de SPC.

## **Apéndice**

| Véase Fig. 3: Especificaciones de la caja del módulo SPCW130 |                                           |                                                  |  |  |
|--------------------------------------------------------------|-------------------------------------------|--------------------------------------------------|--|--|
| 1                                                            | Puntos de anclaje del módulo de expansión |                                                  |  |  |
| 2                                                            | Separadores murales                       |                                                  |  |  |
| 3                                                            | Puntos de anclaje de la tapa              |                                                  |  |  |
| 4                                                            | Sujetacables                              |                                                  |  |  |
| 5                                                            | Orificios de montaje                      |                                                  |  |  |
| 6                                                            | Orificios de entrada para los cables      |                                                  |  |  |
| 7                                                            | Amarres de cables                         |                                                  |  |  |
| 8                                                            | Ganchos de la tapa                        |                                                  |  |  |
| Véase Fig. 4: Tapa del módulo de expansión                   |                                           |                                                  |  |  |
| 1                                                            | Guía de tamper frontal                    |                                                  |  |  |
| 2                                                            | Tornillos de fijación de la cubierta      |                                                  |  |  |
| Datos técnicos                                               |                                           |                                                  |  |  |
| Tensión de<br>funcionamiento                                 |                                           | 9,5 – 14 Vcc                                     |  |  |
| Consumo de corriente                                         |                                           | 60 mA a 12 Vcc                                   |  |  |
| Bus de campo                                                 |                                           | X-BUS sobre RS485 (307 kb/s)                     |  |  |
| Interfaces                                                   |                                           | X-BUS (entrada, salida, bifurcación)             |  |  |
| Módulo de radio                                              |                                           | Receptor RF SiWay integrado (868 MHz)            |  |  |
| Contacto de tamper                                           |                                           | Tamper con muelle delantero                      |  |  |
| Temperatura de<br>funcionamiento                             |                                           | -10 a +50 °C                                     |  |  |
|                                                              | Humedad relativa                          | Máx. 90% (sin condensación)                      |  |  |
| Protección de la carcasa                                     |                                           | IP30                                             |  |  |
| Color                                                        |                                           | RAL 9003                                         |  |  |
| Clase de protección de la<br>carcasa                         |                                           | Clase II Interior general                        |  |  |
| Montaje                                                      |                                           | En superficie, mural                             |  |  |
| Dimensiones (A x H x F)                                      |                                           | Caja: 200 x 153 x 47 mm<br>PCI: 150 x 82 x 20 mm |  |  |
| Peso                                                         |                                           | 0,34 kg                                          |  |  |
| Material de la carcasa                                       |                                           | ABS                                              |  |  |
| Caja                                                         |                                           | Caja de plástico                                 |  |  |
| Protección de la carcasa                                     |                                           | IP30                                             |  |  |
| Estándares                                                   |                                           | EN50131-3:2009 (Grado 3, Clase II)               |  |  |

# **Français – Instructions**

**AVERTISSEMENT** Avant d'installer et d'utiliser ce dispositif, veuillez lire les consignes de sécurité.

Cet appareil ne doit être connecté qu'à des sources d'alimentation électrique conformes à la norme EN60950-1, chapitre 2.5 (« Source d'énergie limitée »).

Lors du remplacement ou de l'installation d'un SPCW130 sur un système de

- la série SPC, assurez-vous que toutes les précautions antistatiques sont respectées lors de la manipulation des connecteurs, fils, bornes et cartes de circuit imprimé.
## **Déclaration de conformité CE**

Par la présente, Vanderbilt International (IRL) Ltd déclare que le type d'équipement radio considéré est en conformité avec toutes les directives UE applicables relatives au marquage CE. Il sera en conformité avec les directives 2014/30/UE (directive compatibilité électromagnétique (CEM)) et 2014/35/UE (directive basse tension) à compter du 20.04.2016. Il sera également en conformité avec la directive 2014/53/UE (directive dite RED relative à l'équipement radio) à compter du 13.06.2016.

Le texte intégral de la déclaration de conformité aux directives de l'Union européenne est disponible à http://pcd.vanderbiltindustries.com/doc/SPC

## **Introduction au SPCW130**

Le SPCW130 procure une interface pour les détecteurs radio 868 MHz. Le SPCW130 comprend les éléments suivants illustrés dans la fig. 1.

- Il est recommandé d'allumer le transpondeur 30 secondes avant de commencer à l'utiliser.
- **1.** Commutateur d'autosurveillance d'ouverture Le transpondeur est équipé d'un commutateur d'autosurveillance d'ouverture avec ressort. Lorsque le couvercle est fermé, le ressort ferme le commutateur.
- **2.** Tamper by-pass [J1] Le réglage de ce cavalier détermine comment opère l'autosurveillance. Le fonctionnement de l'autosurveillance peut être annulé en mettant un cavalier J1 en place.
- **3.** Buzzer Le buzzer est activé pour localiser le transpondeur (voir le manuel de configuration du SPC).
- **4.** Module radio Le module fournit l'interface radio des périphériques 868 MHz. Veuillez prendre en compte que les périphériques radio Intrunet peuvent être enregistrés sur ce périphérique.
- **5.** Témoin Activé si des télégrammes radios sont reçus. Le témoin indique que tous les télégrammes radios sont reçus. Il indique également la réception de télégrammes radios non valides.
- **6.** Témoin d'état X-BUS Le témoin indique l'état de l'X-BUS lorsque le système est en Mode Paramétrage, comme illustré ci-dessous :

| État du témoin                                                         | Description                                                                                                    |
|------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Clignotement régulier<br>(une fois toutes les 1,5 secondes<br>environ) | L'état des communications X-BUS est OK.                                                                        |
| Clignotement rapide<br>(une fois toutes les 0,2 secondes<br>environ)   | Indique le dernier transpondeur en ligne<br>(ne s'applique pas aux configurations en<br>étoile et multipoints) |
|                                                                        |                                                                                                                |

- **7.** Commutateurs d'adressage manuel Les commutateurs permettent un réglage manuel de l'ID de chacun des transpondeurs du système.
- **8.** Alimentation électrique auxiliaire (12 V) Elle est utilisée pour alimenter les périphériques auxiliaires jusqu'à une valeur maximale de 200 mA.
- **9.** Alimentation d'entrée Le transpondeur nécessite 12 V CC qui peuvent être directement fournis par les centrales de la série SPC ou par une unité d'alimentation de SPC.
- **10.** Interface X-BUS Le bus de communication est utilisé pour connecter les transpondeurs sur les systèmes de la série SPC (voir la section Câblage de l'interface X-BUS).
- **11.** Cavalier de terminaison Ce cavalier est toujours monté par défaut. Toutefois, pour une configuration en étoile, ce montage doit être retiré (voir la section Câblage de l'interface X-BUS).

## **Câblage de l'interface X-BUS**

L'interface X-BUS permet la connexion des transpondeurs et des claviers à la centrale SPC. Le X-BUS peut être câblé selon plusieurs configurations différentes en fonction des besoins d'installation.

**REMARQUE** : longueur maximale du câble système = nombre de transpondeurs et de claviers dans le système x distance maximale pour le type de câble.

| Type de câble                  | Distance |
|--------------------------------|----------|
| Câble d'alarme CQR standard    | 200 m    |
| Catégorie UTP : 5 (âme pleine) | 400 m    |
| Belden 9829                    | 400 m    |
| IYSTY 2 x 2 x 0,6 (min)        | 400 m    |

La fig. 2 montre le câblage du X-BUS sur un transpondeur/une centrale et le transpondeur/la centrale suivante dans une configuration en boucle ouverte. Les bornes 3A/3B et 4A/4B ne sont utilisées que pour un câblage en branche. Si vous utilisez une configuration en boucle ouverte, le dernier transpondeur n'est pas câblé en retour sur la centrale.

#### **Voir fig. 2 : câblage de transpondeurs**

- **1** Centrale SPC
- **2** Transpondeur précédent
- **3** SPCW130
- **4** Transpondeur suivant

Veuillez consulter le manuel de configuration de la centrale SPC pour obtenir des instructions de câblage, de blindage, des spécifications et des limitations supplémentaires

### **Adressage du X-BUS**

Pour l'adressage, la reconfiguration, la localisation du périphérique, la surveillance, l'édition des noms, le type de communication X-BUS, lee temporisations, veuillez consulter le manuel de configuration du SPC.

|                                         | Annexe                                                |  |  |  |  |
|-----------------------------------------|-------------------------------------------------------|--|--|--|--|
|                                         | Voir fig. 3 : spécifications de l'enceinte du SPCW130 |  |  |  |  |
| 1                                       | Points d'ancrage du transpondeur                      |  |  |  |  |
| 2                                       | Entretoises murales                                   |  |  |  |  |
| 3                                       | Recouvrement des points d'ancrage                     |  |  |  |  |
| 4                                       | Serre-câbles                                          |  |  |  |  |
| 5                                       | Trous de fixation murale                              |  |  |  |  |
| 6                                       | Orifices d'entrée des câbles                          |  |  |  |  |
| 7                                       | Attaches de câble                                     |  |  |  |  |
| 8                                       | Accroches de couvercle                                |  |  |  |  |
| Voir fig. 4 : couvercle du transpondeur |                                                       |  |  |  |  |
| 1                                       | Guide du ressort de l'autosurveillance                |  |  |  |  |
| 2                                       | Vis de fixation du couvercle                          |  |  |  |  |
| Caractéristiques techniques             |                                                       |  |  |  |  |
|                                         |                                                       |  |  |  |  |

| Tension de<br>fonctionnement | 9,5 - 14 V CC |
|------------------------------|---------------|
|------------------------------|---------------|

| Consommation<br>électrique       | 60 mA à 12 V CC                                                             |
|----------------------------------|-----------------------------------------------------------------------------|
| Bus de terrain                   | X-BUS sur RS-485 (307 ko/s)                                                 |
| Interfaces                       | X-BUS (entrée, sortie, branche)                                             |
| Module radio                     | Récepteur SiWay RF intégré (868 MHz)                                        |
| Contact d'antisabotage           | Dispositif intégré avant d'autosurveillance à ressort                       |
| Température de<br>fonctionnement | De -10 à +50 °C                                                             |
| Humidité relative                | 90 % max. (sans condensation)                                               |
| Couleur                          | RAL 9003                                                                    |
| Montage                          | Surface, montage mural                                                      |
| Dimensions (L x H x P)           | Enceinte : 200 x 153 x 47 mm<br>Carte de circuit imprimé : 150 x 82 x 20 mm |
| Poids                            | 0,34 kg                                                                     |
| Matériau du boîtier              | ABS                                                                         |
| Boîtier                          | Enceinte en plastique                                                       |
| Protection du boîtier            | IP30                                                                        |
| Normes                           | EN50131-3:2009 (Niveau 3, Classe II)                                        |

## **Italiano – Istruzioni**

**AVVERTENZA** Prima di procedere con l'installazione e l'utilizzo di questo dispositivo, leggete le Istruzioni di sicurezza.

Questo dispositivo può essere collegato solo ad alimentatori conforme a EN60950-1, capitolo 2.5 ("limited power source").

Quando caricate o installate un SPCW130 sul sistema serie SPC, verificate che tutte le precauzioni antistatiche siano state rispettate durante la manipolazione dei connettori, cavi, terminali e PCB.

## **Dichiarazione di conformità CE**

Con la presente Vanderbilt International (IRL) Ltd dichiara che questo tipo di apparecchio radio è conforme a tutte le relative Direttive UE per la marcatura CE. Dal 20/04/2016 è conforme alla Direttiva 2014/30/UE (Direttiva sulla compatibilità elettromagnetica) e Direttiva 2014/35/UE (Direttiva sulla bassa tensione). Dal 13/06/2016 è anche conforme con la Direttiva 2014/53/UE (Direttiva sulle apparecchiature radio).

Il testo completo della dichiarazione di conformità UE è disponibile presso http://pcd.vanderbiltindustries.com/doc/SPC

## **Introduzione al dispositivo SPCW130**

Il dispositivo SPCW130 fornisce un'interfaccia per rilevatori wireless 868 MHz. Il dispositivo SPCW130 è costituito dai seguenti elementi, come mostrato in figura 1.

- L'espansione deve essere accesa per almeno 30 secondi prima di svolgere qualsiasi operazione.
- **1.** Interruttore tamper frontale L'espansione è dotata di un interruttore tamper frontale con molla. Quando il coperchio è chiuso, la molla chiude l'interruttore.
- **2.** Bypass tamper [J1] La regolazione del jumper determina il funzionamento del tamper. Il funzionamento del tamper può essere escluso fissando il J1.
- **3.** Cicalino Il cicalino è attivato per individuare l'espansione (vedi il Manuale di configurazione SPC).
- **4.** Modulo wireless Il modulo fornisce l'interfaccia wireless per dispositivi 868 MHz. Tenete presente che su questo dispositivo è possibile registrare solo dispositivi wireless Intrunet.
- **5.** LED Attivato quando si ricevono telegrammi wireless. Il LED indica la ricezione di tutti i telegrammi wireless. Esso indica anche la ricezione di telegrammi wireless non validi.
- **6.** LED di stato X-BUS Il LED indica lo stato dello X-BUS quando il sistema è in modo INSTALLATORE COMPLETO, come mostrato di seguito:

| Stato del LED                                                | Descrizione                                                                                |
|--------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| Lampeggia regolarmente<br>(una volta ogni 1,5 secondi circa) | Lo stato delle comunicazioni X-BUS non<br>presenta problemi.                               |
| Lampeggia rapidamente<br>(una volta ogni 0,2 secondi circa)  | Indica l'ultima espansione in linea<br>(esclude la configurazione a stella e<br>multidrop) |

- **7.** Interruttore di indirizzamento manuale Gli interruttori consentono l'impostazione manuale dell'ID di ogni espansione nel sistema.
- **8.** Alimentazione ausiliaria (12 V) È utilizzata per alimentare dispositivi ausiliari ad un massimo di 200 mA.
- **9.** Ingresso alimentazione L'espansione richiede un'alimentazione di 12 V DC che può essere fornita direttamente dall'unità centrale serie SPC o da un'espansione SPC PSU.
- **10.** Interfaccia X-BUS Il bus di comunicazione è utilizzato per collegare assieme le espansioni sul sistema serie SPC (vedi sezione Cablaggio dell'interfaccia X-BUS).
- **11.** Jumper di terminazione Questo jumper è sempre installato di default, tuttavia, quando effettuate il cablaggio per la configurazione a stella, questo jumper deve essere rimosso (vedi sezione Cablaggio dell'interfaccia X-BUS).

## **Cablaggio dell'interfaccia X-BUS**

L'interfaccia X-BUS consente la connessione di espansioni e tastiere con l'unità centrale SPC. X-BUS può essere collegato in un vasto numero di configurazioni diverse a seconda dei requisiti d'installazione.

**NOTA:** Lunghezza cavo massima del sistema = numero di espansioni e tastiere nel sistema x distanza massima per tipo di cavo.

| Tipo di cavo<br>Distanza |  |
|--------------------------|--|
|--------------------------|--|

| Cavo allarme standard CQR      | 200 m |
|--------------------------------|-------|
| Categoria UTP: 5 (anima piena) | 400 m |
| Belden 9829                    | 400 m |
| IYSTY 2 x 2 x 0,6 (min)        | 400 m |

La figura 2 mostra il collegamento dello X-BUS ad un'espansione/controllore e la seguente espansione/controllore nella configurazione Spur. I terminali 3A/3B e 4A/4B sono impiegati solo per utilizzare una tecnica di cablaggio derivata. Se usate una configurazione Spur, l'ultima espansione non è collegata al controllore.

#### **Vedi Fig. 2: Cablaggio delle espansioni**

- **1** Unità centrale SPC
- **2** Espansione precedente
- **3** SPCW130
- **4** Espansione successiva

Fate riferimento al Manuale di configurazione SPC del controllore collegato per ulteriori istruzioni di cablaggio, schermatura, specifiche tecniche e limitazioni.

## **Indirizzamento X-BUS**

Per informazioni su indirizzamento, riconfigurazione, posizione del dispositivo, monitoraggio, modifica dei nomi, tipo di comunicazione X-BUS, temporizzatore di guasto, fate riferimento al manuale di configurazione SPC.

## **Appendice**

| Vedi Fig. 3: Specifiche tecniche custodia SPCW130 |  |  |  |  |  |  |
|---------------------------------------------------|--|--|--|--|--|--|
|---------------------------------------------------|--|--|--|--|--|--|

- **1** Punti di ancoraggio espansione **2** Distanziatori da parete **3** Punti di ancoraggio coperchio
- **4** Tiranti per cavi
- **5** Fori di montaggio
- **6** Fori d'ingresso per cavi
- **7** Fascette per cavi
- **8** Ganci del coperchio

## **Vedi Fig. 4: Coperchio dell'espansione**

- **1** Guida tamper frontale
- **2** Viti di fissaggio del coperchio

## **Specifiche tecniche**

| Tensione di esercizio                         | 9,5 – 14 V CC                                             |
|-----------------------------------------------|-----------------------------------------------------------|
| Consumo                                       | da 60 mA a 12 V DC                                        |
| Bus di campo                                  | X-BUS su RS485 (307 kb/s)                                 |
| Interfacce                                    | X-BUS (Ingresso, Uscita, Derivazione)                     |
| Modulo radio                                  | Ricevitore RF SiWay integrato (868 MHz)                   |
| Contatto tamper                               | Tamper a molla armadio frontale on-board                  |
| Temperatura di esercizio                      | -10 a +50 °C                                              |
| Umidità relativa                              | Max. 90 % (in assenza di condensa)                        |
| Protezione<br>alloggiamento                   | IP30                                                      |
| Colore                                        | RAL 9003                                                  |
| Categoria di protezione<br>dell'alloggiamento | Classe II Indoor General                                  |
| Montaggio                                     | Superficie, montaggio a parete                            |
| Dimensioni (L x A x P)                        | Alloggiamento: 200 x 153 x 47 mm<br>PCB: 150 x 82 x 20 mm |
| Peso                                          | 0,34 kg                                                   |
| Materiale alloggiamento                       | ABS                                                       |
| Alloggiamento                                 | Custodia in plastica                                      |
| Protezione<br>alloggiamento                   | IP30                                                      |
| Standard                                      | EN50131-3:2009 (grado 3, classe II)                       |
|                                               |                                                           |

## **Nederlands –Instructies**

**WAARSCHUWING** Lees de veiligheidsinstructies voordat u dit apparaat installeert en in gebruik neemt.

Sluit dit apparaat alleen aan op voedingseenheden die voldoen aan EN60950-1, hoofdstuk 2.5 ("limited power source").

Houdt u bij het vervangen of installeren van een SPCW130 op het SPCsysteem aan alle voorzorgsmaatregelen om de vorming van statische energie te voorkomen als u werkt met connectoren, draden, klemmen en printplaten.

## **EU-compatibiliteitsverklaring**

Hiermee verklaart Vanderbilt International (IRL) Ltd dat dit type radioapparatuur voldoet aan alle toepasselijke EU-richtlijnen voor CE-markering. Vanaf 20-04-2016 voldoet het aan richtlijn 2014/30/EU (Richtlijn Elektromagnetische compatibiliteit) en richtlijn 2014/35/EU (Laagspanningsrichtlijn). Vanaf 13-06-2016 voldoet het ook aan richtlijn 2014/53/EU (Richtlijn Radioapparatuur).

De volledige tekst van de EU-conformiteitsverklaring is beschikbaar op http://pcd.vanderbiltindustries.com/doc/SPC

## **Kennismaking met de SPCW130**

De SPCW130 biedt een interface voor 868 MHz draadloze detectoren. De volgende elementen zijn geïntegreerd in de SPCW130, zoals aangegeven in Afb. 1.

- De uitbreiding moet ten minste 30 seconden zijn ingeschakeld voordat u bewerkingen uitvoert.
- **1.** Sabotageschakelaar voorzijde De uitbreiding heeft aan de voorzijde een sabotageschakelaar met veer. Wanneer het paneel wordt gesloten, wordt de schakelaar afgesloten door de veer.
- **2.** Sabotage negeren [J1] De jumperinstelling bepaalt de werking van de sabotagefunctie. De sabotagefunctie kan worden gedeactiveerd door J1 aan te brengen.
- **3.** Zoemer De zoemer wordt geactiveerd om de uitbreiding te lokaliseren (zie SPC Configuratiehandleiding).
- **4.** Draadloze module De module biedt de draadloze interface voor 868 MHz-apparaten. Houd er rekening dat alleen draadloze Intrunet-apparaten kunnen worden geregistreerd op dit apparaat.
- **5.** LED Geactiveerd als draadloze telegrammen worden ontvangen. De LED is een indicator voor de ontvangst van alle draadloze telegrammen. De LED geeft ook de ontvangst van niet-geldige draadloze telegrammen aan.
- **6.** X-BUS status-LED De LED geeft de status van de X-BUS aan als het systeem in de volledige engineermodus is, zoals hieronder wordt aangegeven:

| LED-status                                   | Beschrijving                                                                                       |
|----------------------------------------------|----------------------------------------------------------------------------------------------------|
| Knippert langzaam                            | De X-BUS-communicatiestatus is OK.                                                                 |
| (ongeveer elke 1,5 seconde)                  |                                                                                                    |
| Knippert snel<br>(ongeveer elke 0,2 seconde) | Geeft de laatste uitbreiding op de lijn aan<br>(geldt niet voor ster- en<br>multipuntconfiguratie) |

- **7.** Schakelaars voor handmatige adressering Met de schakelaars kan de ID van elke uitbreiding in het systeem handmatig worden ingesteld.
- **8.** Hulpvoeding (12 V) Met deze uitgangen kunnen hulpapparaten worden gevoed tot een maximum van 200 mA.
- **9.** Ingangsvermogen De uitbreiding moet direct worden gevoed met 12 V DC door de controller van de SPC-serie of door een SPC PSU-uitbreiding.
- **10.** X-BUS-interface Via de communicatiebus worden uitbreidingen gezamenlijk aangesloten op het systeem van de SPC-serie (zie sectie Bedrading van X-BUS-interface).
- **11.** Afsluitjumper Deze jumper is standaard altijd aangebracht, maar bij de bedrading voor een sterconfiguratie moet de jumper worden verwijderd (zie sectie Bedrading van X-BUS-interface).

## **Bedrading van X-BUS-interface**

De X-BUS-interface verzorgt de verbinding van uitbreidingen en bediendelen met de SPC-controller. Er zijn verschillende topologieën mogelijk voor de X-BUS. Welke configuratie wordt gekozen is afhankelijk van de vereisten van de installatie. **OPMERKING:** maximale kabellengte van het systeem = aantal uitbreidingen en bediendelen in het systeem x maximumafstand voor kabeltype.

| Kabeltype                        | Afstand |
|----------------------------------|---------|
| CQR standaardalarmkabel          | 200 m   |
| UTP categorie: 5 (massieve kern) | 400 m   |
| Belden 9829                      | 400 m   |
| IYSTY 2 x 2 x 0,6 (min)          | 400 m   |

In Afb. 2 ziet u de bedrading van de X-BUS naar een uitbreiding/controller en de volgende uitbreiding/controller in kanaalconfiguratie. De aansluitingen 3A/3B en 4A/4B worden alleen gebruik voor de bedrading van een aftakking. Bij een kanaalconfiguratie wordt de laatste uitbreiding niet terug aangesloten op de controller.

#### **Zie Afb. 2: Bedrading van uitbreidingen**

- **1** SPC-controller
- **2** Vorige uitbreiding
- **3** SPCW130
- **4** Volgende uitbreiding

Zie de SPC Configuratiehandleiding van de aangesloten controller voor meer instructies voor de bekabeling, afscherming, specificaties en beperkingen.

## **Adressering van X-BUS**

Zie de SPC Configuratiehandleiding voor informatie over adressering, reconfiguratie, plaats van apparaten, bewaking, bewerken van namen, communicatietype van X-bus en de storingtimer.

## **Appendix**

|                                    | Zie Afb. 3: Specificaties SPCW130 behuizing |                                                      |  |  |
|------------------------------------|---------------------------------------------|------------------------------------------------------|--|--|
| 1                                  | Ankerpunten uitbreiding                     |                                                      |  |  |
| 2                                  | Afstandstukken wand                         |                                                      |  |  |
| 3                                  | Afdekking ankerpunten                       |                                                      |  |  |
| 4                                  | Kabelklemmen                                |                                                      |  |  |
| 5                                  | Montagegaten                                |                                                      |  |  |
| 6                                  | Kabeldoorvoer                               |                                                      |  |  |
| 7                                  | Kabelbinders                                |                                                      |  |  |
| 8                                  | Klephaakjes                                 |                                                      |  |  |
|                                    | Zie Afb. 4: Klep van uitbreiding            |                                                      |  |  |
| 1                                  | Geleider sabotage voorzijde                 |                                                      |  |  |
| 2                                  | Afdekking bevestigingsschroeven             |                                                      |  |  |
|                                    | Technische gegevens                         |                                                      |  |  |
|                                    |                                             | 9,5 – 14 V DC                                        |  |  |
| Bedrijfsspanning<br>Stroomverbruik |                                             | 60 mA bij 12 V DC                                    |  |  |
| Veldbus                            |                                             | X-BUS op RS485 (307 kb/s)                            |  |  |
| Interfaces                         |                                             | X-BUS (in, uit, aftakking)                           |  |  |
| Radiomodule                        |                                             | Geïntegreerde SiWay<br>RF-ontvanger (868 MHz)        |  |  |
| Sabotagecontact                    |                                             | Ingebouwd sabotagecontact in voorzijde<br>behuizing  |  |  |
| Bedrijfstemperatuur                |                                             | -10 tot +50 °C                                       |  |  |
| Relatieve vochtigheid              |                                             | Max. 90 % (geen condensatie)                         |  |  |
| Beveiliging van behuizing          |                                             | IP30                                                 |  |  |
| Kleur                              |                                             | RAL 9003                                             |  |  |
| Beveiligingsklasse<br>behuizing    |                                             | Klasse II binnenshuis algemeen                       |  |  |
|                                    | Bevestiging                                 | Oppervlakte, wandmontage                             |  |  |
| Afmetingen (B x H x D)             |                                             | Omhulsel: 200 x 153 x 47 mm<br>PCB: 150 x 82 x 20 mm |  |  |
| Gewicht                            |                                             | 0,34 kg                                              |  |  |
| Materiaal behuizing                |                                             | ABS                                                  |  |  |
|                                    | Behuizing                                   | Kunststofbehuizing                                   |  |  |
|                                    | Beveiliging van behuizing                   | IP30                                                 |  |  |
|                                    | Normen                                      | EN50131-3:2009 (Klasse 3, Klasse II)                 |  |  |

## **Svenska – Instruktioner**

![](_page_5_Picture_30.jpeg)

**VARNING** Innan du börjar installera och arbeta med denna anordning, var god läs Säkerhetsinstruktionerna.

Denna enhet får endast anslutas till strömkällor som uppfyller kraven för EN60950-1, kapitel 2.5 ("begränsad strömkälla").

När du byter eller installerar en SPCA130 i SPC-systemet, var noga med att vidta åtgärder för att undvika antistatisk effekt vid hantering av kontakter, ledningar, terminaler och kretskort.

## **EC Konformitetsdeklaration**

Härmed försäkrar Vanderbilt International (IRL) Ltd att denna typ av radioutrustning överensstämmer med alla relevanta EG-direktiv för CE-märkning. Från 20/04/2016 överensstämmer den med direktiv 2014/30/EG (Direktiv om elektromagnetisk kompatibilitet) och direktiv 2014/35/EG (Direktiv om lågspänning). Från 13/06/2016 överensstämmer den även med direktiv 2014/53/EG (Direktiv om radioutrustning).

Den fullständiga texten för EG-försäkran om överensstämmelse finns på http://pcd.vanderbiltindustries.com/doc/SPC

## **Introduktion till SPCW130**

SPCW130 är ett användargränssnitt för 868 MHz trådlösa detektorer. SPCW130 har följande delar, som Fig. 1 visar.

- Expansionsenheten bör startas upp åtminstone 30 sekunder innan den börjar användas.
- **1.** Främre sabotagekontakt Expansionsenheten har en främre sabotagekontakt med fjäder. När locket stängs, stänger fjädern brytaren.
- **2.** Förbikoppling av sabotagelarm (J1) Sabotagelarmets funktion bestäms av bygelinställningen. Sabotagelarmet kan åsidosättas genom att sätta i J1.
- **3.** Summer Summern aktiveras för att lokalisera expansionsenheten (se SPC konfigurationsmanual).
- **4.** Trådlös modul Modulen ger trådlöst användargränssnitt till 868 MHz enheter. Observera att endast Intrunet trådlösa enheter kan registreras på denna enhet.
- **5.** Diodlampa Aktiveras om trådlösa telegram tas emot. Lampan indikerar mottagning av alla trådlösa telegram. Den indikerar också mottagning av ogiltiga trådlösa telegram.

- **6.** X-BUS statuslampa Lysdioden indikerar X-BUS-status när systemet befinner sig i FULLT INST-läge, enligt nedanstående:

| LED status            | Beskrivning                                           |  |
|-----------------------|-------------------------------------------------------|--|
| Blinkar regelbundet   | X-BUS kommunikationsstatus är OK.                     |  |
| (ungefär var 1,5 sek) |                                                       |  |
| Blinkar snabbt        | Indikerar den sista expansionsenheten                 |  |
| (ungefär var 0,2 sek) | (gäller inte stjärn- och multi-drop<br>konfiguration) |  |

- **7.** Manuell adressomkopplare Med hjälp av omkopplarna kan man ställa in ID för varje expansionsenhet i systemet manuellt.
- **8.** Strömförsörjning till extrautrustning (12 V) Används för att ge ström till extrautrustning, maximalt 200 mA.
- **9.** Strömförsörjning Expansionsenheten kräver 12 V DC antingen direkt från SPC-kontrollenheten eller från en SPC-expansionsenhet för kraftförsörjning.
- **10.** X-BUS-gränssnitt Kommunikationsbussen används för att koppla samman expansionsenheter i SPC-systemet (se avsnittet Koppling av X-BUSgränssnittet).
- **11.** Termineringsbygling Standardinställningen är att denna bygling alltid är monterad, men vid ledningsdragning för stjärnkonfiguration bör den tas bort (se avsnittet Koppling av X-BUS-gränssnittet).

## **Koppling av X-BUS-gränssnittet**

X-BUS-gränssnittet ger anslutningar av expansionsenheter och knappsatser till SPC-kontrollenheten. Kopplingen av X-BUS kan göras på många olika sätt beroende på installationskrav.

**OBS!** Maximal längd för systemkabel = antal expansionsenheter och knappsatser i systemet x max avstånd för kabeltypen.

| Kabeltyp                       | Avstånd |
|--------------------------------|---------|
| CQR standard larmkabel         | 200 m   |
| UTP-kategori: 5 (solid ledare) | 400 m   |
| Belden 9829                    | 400 m   |
| IYSTY 2 x 2 x 0,6 (min)        | 400 m   |

Fig. 2 visar koppling av X-BUS till en expansions-/kontrollenhet och nästa expansions-/kontrollenhet i kedjekonfiguration. Terminalerna 3A/3B och 4A/4B används bara när man använder kabelförgrening. Vid användning av kedjekonfiguration kopplas den sista expansionsenheten inte tillbaka till kontrollenheten.

#### **Se Fig. 2: Koppling av expansionsenheter**

- **1** SPC-kontrollenhet
- **2** Förra expansionsenheten
- **3** SPCW130
- **4** Nästa expansionsenhet

Se SPC konfigurationsmanual för den anslutna kontrollenheten för att få ytterligare information om kablage, skärmning och begränsningar.

## **X-BUS-adressering**

Se SPC konfigurationsmanual för information om adressering, omkonfiguration, övervakning, redigering av namn, X-BUS kommunikationstyp och timerfunktion vid fel.

## **Bilaga**

| Se Fig. 3: SPCA130 Specifikationer för hölje |                                      |  |
|----------------------------------------------|--------------------------------------|--|
| 1                                            | Fästpunkter för expansionsenhet      |  |
| 2                                            | Väggdistanser                        |  |
| 3                                            | Fästpunkter för locket               |  |
| 4                                            | Dragavlastare                        |  |
| 5                                            | Monteringshål                        |  |
| 6                                            | Genomföringshål för kabel            |  |
| 7                                            | Buntband                             |  |
| 8                                            | Hakar på locket                      |  |
| Se Fig. 4: Expansionsenhetens lock           |                                      |  |
| 1                                            | Riktpunkt för främre sabotagekontakt |  |
| 2                                            | Skruvar för fastsättning av lock     |  |

| Tekniska data           |                                                      |  |
|-------------------------|------------------------------------------------------|--|
| Driftspänning           | 9.5 – 14 V DC                                        |  |
| Strömförbrukning        | 60 mA vid 12 V DC                                    |  |
| Fältbuss                | X-BUS på RS485 (307 kb/s)                            |  |
| Gränssnitt              | X-BUS (In, Ut, Förgrening)                           |  |
| Radiomodul              | Integrerad SiWay RF-mottagare (868 MHz)              |  |
| Sabotagelarmets kontakt | Sabotagekontakt med fjäder                           |  |
| Drifttemperatur         | -10 till +50 °C                                      |  |
| Relativ luftfuktighet   | Max. 90 % (ej kondenserande)                         |  |
| Kapslingsskydd          | IP30                                                 |  |
| Färg                    | RAL 9003                                             |  |
| Kapslingsskydds-klass   | Klass II inomhus allmänt                             |  |
| Montering               | Yt-, väggmontering                                   |  |
| Mått (B x H x D)        | Kapsling: 200 x 153 x 47 mm<br>PCB: 150 x 82 x 20 mm |  |

| Vikt              | 0,34 kg                           |
|-------------------|-----------------------------------|
| Kapslingsmaterial | ABS                               |
| Kåpa              | Plasthölje                        |
| Kapslingsskydd    | IP30                              |
| Standarder        | EN50131-3:2009 (grad 3, klass II) |