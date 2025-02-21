![](_page_0_Picture_0.jpeg)

#### Manual

Updated 11/23/2020

# **Door controller VAKA B18**

Door controller VAKA B18 m,anages one door environment in a VAKA system.

![](_page_0_Picture_5.jpeg)

### Important

- l B18/B28 requires Axema VAKA version 3.7 or later. (https://info.axema.se+version) Existing systems with an earlier version should be upgraded prior to installation of B18/B28.
- l To interface intrusion panels, the B28 needs an alarm module, C20.
- l B18/B28 are compatible with older door controllers B17/B27 and B16/B26.
- l For the connectors in B18/B28, a flat 2,5 mm screwdriver is recommended.

### Mounting

To allow for installation of modules for extra functionalities, the door controller should be mounted to ensure 40 mm of free space above the unit.

# CPU module

Door controller with on-board network switch, rotary switches for node address and keypad and display for settings and system information

![](_page_1_Figure_9.jpeg)

# Node addresses

Door controller in VAKA systems without B60 must have a unique node address between 1 and 10. In VAKA systems with B60, door controllers in each domain must have a unique node address between 1 and 50.

The door controllers default IP addresses follow the node address, for example, a door controller with node address 1 has the IP address 10.0.0.201 and a door controller with the node address 4 has the IP address 10.0.0.204.

#### The node address is specified with the rotary switches and must be specified before the door control panel is installed in VAKA.

Instructions for changing the node address after the door control panel has been installed in VAKA.

- 1. Uninstall the door controller in VAKA.
- 2. Isolate the door controller from the VAKA network.
- 3. From the Main menu in the door controller, selectSYSTEM SETTINGS->CLEAR CONTROLLER.
- 4. ConfirmTHIS WILL RESTORE FACTORY DEFAULT! ARE YOU SURE? by pressing the return arrow.
- 5. When the door control panel restarts, set the correct node address and change the IP address if necessary.
- 6. Connect the door controller to the VAKA system network and install the door controller in VAKA.

# Terminal blocks

![](_page_3_Figure_1.jpeg)

#### Connector Description

| 1, 2   | Supply voltage (12-35 VDC) If the door is powered by PoE, this connector will<br>deliver 12 VDC or 24 VDC (configurable in VAKA). (Connector 1 is +) |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 - 4  | Connection for readers.                                                                                                                              |
|        | For<br>cable<br>distances,<br>See<br>manual<br>for<br>the<br>reading<br>terminal.<br>types,<br>etc.                                                  |
| 5, 6   | Output AUX, potential-free closing relay. Function is determined in VAKA, for<br>example, locking relay (NC / NO), or sum alarm.                     |
| 7, 8   | Input for exit button Closing of the input gives an unlocking.                                                                                       |
| 10, 14 | Input door contact for checking the status of the door (closed / open).                                                                              |
| 11, 14 | Input bolt piston contact for control of bolt (locked / unlocked).                                                                                   |

### Termination

See the manual for the reader that is used. (https://info.axema.se)

If A45 or A6x is used, the B18 is terminated by Install the 100 Ω resistor between 3 and 4.

# Installation and configuration

This manual only covers the installation and connection of the unit.

# Technical data

| Attribute          | B18                              |  |
|--------------------|----------------------------------|--|
| Power supply       | 12-35 VDC orr PoE+ IEEE 802.3 at |  |
| Built in switch    | Yes                              |  |
| Built in firewall  | No                               |  |
| PoE-support        | Yes                              |  |
| Maximum relay load | 10-30 VDC                        |  |
| IP-rating          | IP22                             |  |
| IP rating          | IK06                             |  |
| Temperature range  | 0° to +55C°                      |  |