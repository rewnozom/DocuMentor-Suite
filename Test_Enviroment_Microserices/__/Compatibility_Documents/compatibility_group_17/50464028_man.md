# KeyPad TouchScreen User manual

Updated August 16, 2023

![](_page_0_Picture_2.jpeg)

**KeyPad TouchScreen** is a wireless keypad with a touch screen designed for managing the Ajax security system. Users can authenticate using smartphones, key fobs, cards, and codes. The device is intended for indoor use. [Tag](https://ajax.systems/products/tag/) Pass

**KeyPad TouchScreen** communicates with a hub over two secure radio protocols. The keypad uses **Jeweller** to transmit alarms and events, and **Wings** to update firmware, transmit the list of groups, rooms, and other additional information. The communication range without obstacles is up to 1,700 meters.

[Learn more](https://ajax.systems/radio-range/)

#### Functional elements

![](_page_1_Picture_0.jpeg)

- **1.** Ambient light sensor for automatically adjusting the backlight brightness.
- **2.** IPS touchscreen display with a 5-inch diagonal.
- **3.** Ajax logo with an LED indicator.
- **4.** Cards/key fobs/Bluetooth reader.
- **5.** SmartBracket mounting panel. To remove the panel, slide it down.
- **6.** Perforated part of the mounting panel for triggering a tamper in case of any attempt to detach the keypad from the surface. Do not break it off.
- **7.** Perforated part of the mounting panel for routing cables through the wall.
- **8.** Built-in buzzer.

#### **9.** [Tamper button](https://support.ajax.systems/en/faqs/what-is-a-tamper/).

- **10.** QR code with the device ID for adding the keypad to the Ajax system.
- **11.** Power button.
- **12.** Terminals for connecting a third-party power supply unit. The terminals can be removed from the holders when necessary.
- **13.** Cable channel for routing the cable from the third-party power supply unit.
- **14.** Perforated part of the mounting panel for routing cables from the bottom.
- **15.** The hole for attaching the SmartBracket mounting panel with a holding screw.

#### Compatible hubs and range extenders

A compatible Ajax hub with the firmwareand higher is required for the keypad to operate. OS Malevich 2.16.1

| Hubs            | Radio signal range extenders |
|-----------------|------------------------------|
| Hub 2 (2G)      | ReX 2                        |
| Hub 2 (4G)      |                              |
| Hub 2 Plus      |                              |
| Hub Hybrid (2G) |                              |
| Hub Hybrid (4G) |                              |

### Operating principle

KeyPad TouchScreen features a built-in buzzer, a touchscreen display, and a reader for contactless authorization. The keypad can be used to control security modes and automation devices and to notify about system alarms.

The keypad can automatically adjust the backlight brightness and wakes up upon approach. Sensitivity is in the app. KeyPad TouchScreen interface is inherited from Ajax Security System app. There are dark and light interface appearances to choose from. A 5-inch diagonal touchscreen display provides access to the security mode of an object or any group and control over automation scenarios. The display also indicates system malfunctions, if present (when is enabled). adjustable system integrity check

Depending on the settings, the KeyPad TouchScreen built-in buzzer notifies about:

- alarms;
- security mode changes;
- entry/exit delays;
- triggering of the opening detectors.

The keypad operates using pre-installed batteries. It can also be powered by a third-party power supply unit with a voltage range of 10.5–14 V⎓ and an operating current of at least 0.5 A. When external power is connected, the preinstalled batteries serve as a backup power source.

#### Security control

![](_page_3_Picture_4.jpeg)

KeyPad TouchScreen can arm and disarm the entire object or specific groups, and activate **Night Mode**. Use the **Control** tab to change the security mode. You can control the security using KeyPad TouchScreen through:

- **1. Smartphones**. With the installed app and Bluetooth Low Energy (BLE) support. Smartphones can be used instead of Tag or Pass for user authorization. BLE is a low-power consumption radio protocol. The keypad supports Android and iOS smartphones with BLE 4.2 and higher. Ajax Security System
- **2. Cards or key fobs**. To quickly and securely identify users, KeyPad TouchScreen uses the DESFire® technology. DESFire® is based on the ISO 14443 international standard and combines 128-bit encryption and copy protection.

- **3. Codes**. KeyPad TouchScreen supports general, personal codes, and codes for unregistered users.
#### Access codes

- **Keypad code** is a general code set up for the keypad. When used, all events are sent to Ajax apps on behalf of the keypad.
- **User code** is a personal code set up for users connected to the hub. When used, all events are sent to Ajax apps on behalf of the user.
- **Keypad access code** is a code set up for a person who is not registered in the system. When used, events are sent to Ajax apps with a name associated with this code.

![](_page_4_Picture_5.jpeg)

Access rights and codes can be adjusted in Ajax apps. If the code is compromised, it can be changed remotely, so there is no need to call an installer to the object. If a user loses their Pass, Tag, or smartphone, an admin or a PRO with system configuration rights can instantly block the device in the app. Meanwhile, a user can use a personal code to control the system.

### Security control of the groups

![](_page_5_Picture_0.jpeg)

KeyPad TouchScreen allows controlling the groups' security (if is enabled). You can also adjust the keypad to determine which groups will be shared (keypad groups). By default, all groups are visible on the keypad display in the **Control** tab. You can learn more about group security management in . Group Mode settings this section

### Emergency buttons

![](_page_5_Picture_3.jpeg)

For emergencies, the keypad features the **Panic** tab with three buttons:

- Panic button;
- Fire;
- Auxiliary alert.

In Ajax app, an admin or a PRO with the rights to configure the system can select the number of buttons displayed in the **Panic** tab. There are two options available in the KeyPad TouchScreen : only **Panic button** (by default) or all three buttons. The text of notifications in apps and event codes transmitted to the Central Monitoring Station (CMS) depend on the selected button type. settings

You can also activate accidental press protection. In this case, the user confirms alarm transmission by pressing the **Send** button on the keypad display. The confirmation screen appears after pressing any panic button.

![](_page_6_Picture_5.jpeg)

### Scenarios management

![](_page_6_Picture_7.jpeg)

The separate keypad tab holds up to six buttons that control one  [or a group of devices. Group scenarios provide more convenient contr](https://support.ajax.systems/en/automation/)ol automation device

over multiple switches, relays, or sockets simultaneously.

Create automation scenarios in the and manage them using KeyPad TouchScreen. keypad settings

[Learn more](https://ajax.systems/scenarios/)

### Indication of malfunctions and security mode

KeyPad TouchScreen informs users about system malfunctions and security mode through:

- display;
- logo;
- sound indication.

Depending on the settings, the logo lights up red continuously or when the system or group is armed. KeyPad TouchScreen indication is shown on the display only when it is active. The built-in buzzer notifies about alarms, door openings, and entry/exit delays.

## Fire alarm muting

![](_page_7_Picture_10.jpeg)

In case of a fire alarm in the system, you can mute it using KeyPad TouchScreen.

> Pressing the **Fire** emergency button in the tab doesn't activate  [(if enabled). When sending an emergency signal from the keypad, an](https://support.ajax.systems/en/what-is-interconnected-fire-alarms/) appropriate notification will be transmitted to the app and the CMS. Panic Interconnected Fire Detectors Alarm

The screen with information about the fire alarm and the button to mute it will appear on all KeyPad TouchScreen with the **Mute Fire Alarm** feature enabled. If the mute button has already been pressed on the other keypad, a corresponding notification appears on the remaining KeyPad TouchScreen displays. Users can close the fire alarm muting screen and use other keypad features. To reopen the muting screen, press the icon on the KeyPad TouchScreen display.

![](_page_8_Picture_3.jpeg)

To instantly display the fire alarm muting screen on the KeyPad TouchScreen, enable the **Always Active Display** toggle in the KeyPad settings. Also, connect the third-party power supply.

Otherwise, the muting screen will only be displayed when the keypad wakes up.

### Duress code

KeyPad TouchScreen supports a **duress code** that allows you to simulate alarm deactivation. In this case, neither the nor the installed at the facility will reveal your actions. Still, the security company and other security system users will be alerted about the incident. Ajax app sirens

[Learn more](https://support.ajax.systems/en/faqs/what-is-duress-code/)

#### User pre-authorization

**Pre-authorization** feature is essential to prevent unauthorized access to the control panel and the current system state. The feature can be activated separately for the **Control** and **Scenarios** tabs in the keypad . settings

The screen for entering the code is displayed on the tabs for which preauthorization is activated. The user should authenticate first, either by entering a code or presenting a personal access device to the keypad. The exception is the **Alarm** tab, which allows unauthorized users to send an emergency signal.

### Unauthorized Access Auto-Lock

If an incorrect code is entered or a non-verified access device is used three times in a row within 1 minute, the keypad will lock for the time specified in its . During this time, the hub will ignore all codes and access devices, while informing the security system users about attempted unauthorized access. KeyPad TouchScreen will turn off the reader and block access to all tabs. The keypad's display will show an appropriate notification. settings

PRO or a user with system configuration rights can unlock the keypad through the app before the specified locking time expires.

### Two-Stage Arming

KeyPad TouchScreen can participate in two-stage arming, but cannot be used as a second-stage device. The two-stage arming process using Tag, Pass, or smartphone is similar to using a personal or general code on the keypad.

#### [Learn more](https://support.ajax.systems/en/system-congifure-pd-6662-2017/#block4)

#### Jeweller and Wings data transfer protocols

**Jeweller** and **Wings** are two-way wireless data transfer protocols that provide fast and reliable communication between the hub and devices. The keypad uses a Jeweller to transmit alarms and events, and Wings to update firmware, transmit the list of groups, rooms, and other additional information.

#### [Learn more](https://ajax.systems/radio-range/)

#### Sending events to the monitoring station

The Ajax system can transmit alarms to bothmonitoring app and the central monitoring station (CMS) in the formats of **SurGard (Contact ID), SIA (DC-09), ADEMCO 685**, and . PRO Desktop other protocols

#### **KeyPad TouchScreen can transmit the following events:**

- **1.** Entry of the duress code.
- **2.** Pressing the panic button. Each button has its own event code.
- **3.** Keypad lock due to an unauthorized access attempt.
- **4.** Tamper alarm/recovery.
- **5.** Loss/restoration of connection with the hub (or radio signal range extender).
- **6.** Arming/disarming the system.
- **7.** [Unsuccessful attempt to arm the security system (with the](https://support.ajax.systems/en/what-is-system-integrity-check/)  enabled). system integrity check
- **8.** Permanent deactivation/activation of the keypad.
- **9.** One-time deactivation/activation of the keypad.

When an alarm is received, the operator at the security company's monitoring station knows what happened and precisely where to dispatch a rapid response team. The addressability of Ajax devices allows sending events to PRO Desktop or the CMS, including the device type, its name, security group, and virtual room. Note that the list of transmitted parameters may vary depending on the CMS type and the selected communication protocol for the monitoring station.

![](_page_11_Picture_0.jpeg)

#### Adding to the system

**KeyPad TouchScreen** is incompatible with Hub, Hub Plus, and third-party security control panels.

To connect KeyPad TouchScreen to the hub, the keypad must be located at the same secured facility as the system (within the range of the hubs radio network). For the keypad to work via the radio signal range extender, you must first add the keypad to the hub and then connect it to ReX 2 in the range extender's settings. ReX 2

> The hub and the device must operate at the same radio frequency; otherwise, they are incompatible. The radio-frequency range of the device might vary based on the region. We recommend purchasing and using Ajax devices in the same region. You can verify the range of operating radio frequencies with the [.](mailto:support@ajax.systems) technical support service

### Before adding a device

- **1.** Install the [Ajax app](https://ajax.systems/software/).
- **2.** Create a oraccount if you don't have one. Add a compatible hub [to the app, configure necessary settings, and create at least one](https://support.ajax.systems/en/manuals/hub-2-plus/#block10)  . user PRO virtual room
- **3.** Ensure the hub is switched on and has internet access via Ethernet, Wi-Fi, and/or mobile network.
- **4.** Ensure the hub is disarmed and does not start updating by checking its status in the Ajax app.

![](_page_11_Picture_11.jpeg)

#### Connecting to the hub

- **1.** Open the [Ajax app](https://ajax.systems/software/). Select the hub where you want to add the keypad.
- **2.** Go to the **Devices** tab. Click **Add Device**.
- **3.** Name the device, scan or manually input the QR code (placed on the keypad and the package box), and select a room and a group (if is enabled). Group Mode
- **4.** Press **Add**.
- **5.** Switch on the keypad by holding the power button for 3 seconds.

If the connection fails, turn off the keypad and try again in 5 seconds. Note that if the maximum number of devices has already been added to the hub ( ), you will be notified when you try to add a new one. [depending on the hub model](https://ajax.systems/hub-compare/)

> KeyPad TouchScreen features a built-in buzzer that can notify of alarms and specific system states, but it is not a siren. You can add up to 10 such devices (including sirens) to the hub. Consider this when planning your security system.

Once connected to the hub, the keypad will appear in the list of hub devices in the Ajax app. The update frequency for device statuses in the list depends on the **Jeweller** or **Jeweller/Fibra** settings, with the default value of 36 seconds.

> **KeyPad TouchScreen** works with only one hub. When connected to a new hub, it stops sending events to the old one. Adding the keypad to a new hub does not automatically remove it from the device list of the old hub. This must be done through the Ajax app.

### Malfunctions

![](_page_13_Picture_0.jpeg)

When a KeyPad TouchScreen malfunction is detected, the Ajax app displays a malfunction counter on the device icon. All malfunctions are indicated in the keypad's states. Fields with malfunctions will be highlighted in red.

#### **A malfunction is displayed if:**

- the keypad enclosure is open (tamper is triggered);
- there is no connection with the hub or radio signal range extender via Jeweller;
- there is no connection with the hub or radio signal range extender via Wings;
- the keypad's battery is low;
- the keypad's temperature is outside acceptable limits.

#### Icons

![](_page_14_Picture_0.jpeg)

#### Icons in the app

The icons in the app display some keypad states. To access them:

- **1.** Sign in to the [Ajax app](https://ajax.systems/software/).
- **2.** Select the hub.
- **3.** Go to the **Devices** tab.

| Icon | Meaning                                                                                                                                    |
|------|--------------------------------------------------------------------------------------------------------------------------------------------|
|      | Jeweller signal strength. Displays the signal strength between the hub and the<br>device. The recommended value is 2–3 bars.<br>Learn more |
|      | The keypad battery charge level is OK or it is charging.                                                                                   |
|      | The keypad has a malfunction. The list of malfunctions is available in the<br>keypad states.<br>Learn more                                 |
|      | Displayed when the keypad Bluetooth module is enabled.                                                                                     |

| Bluetooth setup is not complete. The description is available in the keypad<br>states.                   |
|----------------------------------------------------------------------------------------------------------|
| A firmware update is available. Go to the keypad states to find the description<br>and launch an update. |
| radio signal range<br>Displayed when the keypad is operating via a<br>extender                           |
| Pass/Tag reading is enabled in KeyPad TouchScreen settings.                                              |
| Chime on opening is enabled in KeyPad TouchScreen settings.                                              |
| Device is permanently deactivated.<br>Learn more                                                         |
| Tamper alarm notifications are permanently deactivated.<br>Learn more                                    |
| Device is deactivated until the first disarming of the system.<br>Learn more                             |
| Tamper alarm notifications are deactivated until the first disarming of the<br>system.<br>Learn more     |

#### Icons on the display

Icons appear on top of the display and inform about specific system states or events.

| Icon | Meaning                                                                                                                                                                                                                      |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|      | System restoration is required after an alarm. The user can either send a<br>account type<br>request or restore the system depending on their<br>. To do so,<br>click the icon and select the required button on the screen. |

| Learn more                                                                                                                                                                                       |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| fire alarm muting screen<br>Mute fire alarm. It appears after closing the<br>Users can click the icon anytime and mute the fire alarm, including the<br>interconnected fire alarm.<br>Learn more |
| Chime on opening is disabled. Click the icon to enable.<br>settings are adjusted<br>Appears on the display when the required                                                                     |
| Chime on opening is enabled. Click the icon to disable.<br>settings are adjusted<br>Appears on the display when the required                                                                     |

#### States

![](_page_16_Picture_2.jpeg)

The states provide information about the device and its operating parameters. The states of KeyPad TouchScreen can be found in the Ajax apps:

**1.** Go to the **Devices** tab.

- **2.** Select **KeyPad TouchScreen** from the list.

| Parameter                      | Value                                                                                                                                                                                                                                                                                              |
|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Malfunction                    | Clicking on<br>opens the list of the KeyPad<br>TouchScreen malfunctions.<br>The field is displayed only if a malfunction is<br>detected.                                                                                                                                                           |
| New firmware version available | Clicking on<br>opens the instructions for<br>updating the keypad's firmware.<br>The field is displayed if a new firmware version<br>is available.                                                                                                                                                  |
| Warning                        | Clicking on<br>opens the list of the settings<br>and permissions that the app needs to be<br>granted for the correct operation of the keypad.                                                                                                                                                      |
| Jeweller Signal Strength       | Signal strength between the hub or range<br>extender and the device on the Jeweller<br>channel. The recommended value is 2–3 bars.<br>Jeweller is a protocol for transmitting KeyPad<br>TouchScreen events and alarms.                                                                             |
| Connection via Jeweller        | Connection status on the Jeweller channel<br>between the device and the hub (or the range<br>extender):<br>Online — the device is connected to the hub<br>or the range extender.<br>Offl<br>ine — the device is not connected to the<br>hub or the range extender. Check the keypad<br>connection. |
| Wings Signal Strength          | Signal strength between the hub or the range<br>extender and the device on the Wings channel.<br>The recommended value is 2–3 bars.<br>Wings is a protocol for updating a firmware and<br>transmitting the list of the groups, rooms and<br>other additional information.                          |

| Connection via Wings | Connection status on the Wings channel<br>between the hub or the range extender and the<br>device:                                                                           |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                      | Online — the device is connected to the hub<br>or the range extender.                                                                                                        |
|                      | Offl<br>ine — the device is not connected to the<br>hub or the range extender. Check the keypad<br>connection.                                                               |
|                      | Displays the selected power of the transmitter.                                                                                                                              |
| Transmitter power    | The parameter appears when the Max or<br>Attenuation option is selected in the Signal<br>Attenuation Test menu.                                                              |
|                      | The battery charge level of the device:                                                                                                                                      |
|                      | OK                                                                                                                                                                           |
|                      | Battery low                                                                                                                                                                  |
| Battery Charge       | When the batteries are low, the Ajax apps and<br>the security company will receive appropriate<br>notifications.                                                             |
|                      | After sending a low battery notification, the<br>keypad can work for up to 2 weeks.                                                                                          |
| Lid                  | The status of the keypad tamper that responds<br>to detachment or opening of the device<br>enclosure:                                                                        |
|                      | Open — the keypad was removed from the<br>SmartBracket or its integrity was<br>compromised. Check the device.                                                                |
|                      | Closed — the keypad is installed on the<br>SmartBracket mounting panel. The integrity<br>of the device enclosure and the mounting<br>panel is not compromised. Normal state. |
|                      | Learn more                                                                                                                                                                   |
| External Power       | Keypad external power supply connection<br>status:                                                                                                                           |
|                      | Connected — external power supply is<br>connected to the device.                                                                                                             |

|                                    | Disconnected — the external power is<br>disconnected. The device runs on batteries.<br>Learn more                                                                                       |
|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Always Active Display              | Displayed when the Always Active Display<br>toggle is enabled in the keypad settings and<br>external power supply is connected.                                                         |
| Alarms Sound Indication            | Shows the status of the Activate keypad buzzer<br>if an alarm in the system is detected setting.                                                                                        |
| Alarm duration                     | Duration of sound signal in case of alarm.<br>Sets in increments of 3 seconds.<br>Displayed when the Activate keypad buzzer if<br>alarm in the system is detected toggle is<br>enabled. |
| Pass/Tag Reading                   | Displays if the reader for cards and key fobs is<br>enabled.                                                                                                                            |
| Bluetooth                          | Displays if the keypad's Bluetooth module is<br>enabled for controlling the system with a<br>smartphone.                                                                                |
|                                    | Beeps Settings                                                                                                                                                                          |
| Arming/Disarming                   | When enabled, the keypad notifies about arming<br>and disarming with a short beep.                                                                                                      |
| Night Mode Activation/Deactivation | When enabled, the keypad notifies you when the<br>Night Mode<br>is switched on/off by making a<br>short beep.                                                                           |
| Entry Delays                       | delays<br>When enabled, the keypad beeps about<br>when entering                                                                                                                         |
| Exit Delays                        | delays<br>When enabled, the keypad beeps about<br>when leaving                                                                                                                          |
| Entry Delays in Night Mode         | delays<br>When enabled, the keypad beeps about<br>when entering<br>in Night Mode.                                                                                                       |
| Exit Delays in Night Mode          | delays<br>When enabled, the keypad beeps about<br>when leaving<br>in Night Mode.                                                                                                        |
| Chime on opening                   | When enabled, a siren notifies about opening<br>detectors triggering in the Disarmed system                                                                                             |

|                        | mode.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                        | Learn more                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Beep Volume            | Displayed if the notifications about<br>arming/disarming, entry/exit delay, and opening<br>are activated. Shows the buzzer volume level<br>for notifications.                                                                                                                                                                                                                                                                                       |
| Permanent Deactivation | Shows the status of the keypad permanent<br>deactivation setting:<br>No — the keypad operates in the normal<br>mode.<br>Lid only — the hub administrator has<br>disabled notifications about triggering of the<br>keypad tamper.<br>Entirely — the keypad is entirely excluded<br>from the operation of the system. The<br>device does not execute system commands<br>and does not report alarms or other events.<br>Learn more                     |
| One-Time Deactivation  | Shows the status of the keypad one-time<br>deactivation setting:<br>No — the keypad operates in the normal<br>mode.<br>Lid only — notifications on the keypad<br>tamper triggering are disabled until the first<br>disarm.<br>Entirely — the keypad is entirely excluded<br>from the operation of the system until the<br>first disarm. The device does not execute<br>system commands and does not report<br>alarms or other events.<br>Learn more |
| Firmware               | Keypad firmware version.                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ID                     | Keypad ID. Also available on the QR code on the<br>device enclosure and its package box.                                                                                                                                                                                                                                                                                                                                                            |
| Device No.             | Number of the device loop (zone).                                                                                                                                                                                                                                                                                                                                                                                                                   |

#### Settings

![](_page_21_Picture_1.jpeg)

To change the KeyPad TouchScreen settings in the Ajax app:

- **1.** Go to the **Devices** tab.
- **2.** Select **KeyPad TouchScreen** from the list.
- **3.** Go to **Settings** by clicking on the icon.
- **4.** Set the required parameters.
- **5.** Click **Back** to save the new settings.

| Setting | Value                                                                                                             |
|---------|-------------------------------------------------------------------------------------------------------------------|
| Name    | Name of the keypad. Displayed in the list of hub<br>devices, text of SMS and notifications in the<br>events feed. |
|         | To change the name of the device, click on the<br>text field.                                                     |
|         | The name can contain up to 12 Cyrillic<br>characters or up to 24 Latin characters.                                |

| Room                   | Selecting the virtual room to which KeyPad<br>TouchScreen is assigned.                                                                                                                                                                              |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                        | The room name is displayed in the text of SMS<br>and notifications in the events feed.                                                                                                                                                              |
| Access Settings        | Selecting the method of arming/disarming:<br>Keypad codes only.<br>User codes only.                                                                                                                                                                 |
|                        | Keypad and user codes.<br>To activate the Keypad Access Codes set up for<br>people who are not registered in the system,<br>select the options on the keypad: Keypad codes<br>only or Keypad and user codes.                                        |
| Keypad Code            | Selection of a general code for security control.<br>Contains 4 to 6 digits.                                                                                                                                                                        |
| Duress Code            | Selecting a general duress code for silent<br>alarm. Contains 4 to 6 digits.<br>Learn more                                                                                                                                                          |
| Screen Detection Range | Configuring a distance at which the keypad<br>reacts to approaching and turns on a display:<br>Minimum.<br>Low.<br>Normal (by default).<br>High.<br>Max.<br>Select the optimal sensitivity the keypad will<br>respond to approaching as you prefer. |
| Mute Fire Alarm        | Ajax fire<br>When enabled, users can mute<br>detectors<br>alarm (even Interconnected) with a<br>keypad.<br>Learn more                                                                                                                               |

| Pass/Tag Reading              | When enabled, the security mode can be<br>controlled with Pass and Tag access devices.                                                                                                                                                                                                                                                    |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bluetooth                     | When enabled, the security mode can be<br>controlled with a smartphone.                                                                                                                                                                                                                                                                   |
| Bluetooth Sensitivity         | Adjusting sensitivity of the keypad's Bluetooth<br>module:<br>Minimum.<br>Low.<br>Normal (by default).<br>High.<br>Max.<br>Available if the Bluetooth toggle is enabled.                                                                                                                                                                  |
| Unauthorized Access Auto-Lock | When enabled, the keypad will be locked for a<br>pre-set time if an incorrect code is entered or<br>unverified access devices are used more than<br>three times in a row within 1 minute.<br>PRO or a user with the rights to configure the<br>system can unlock the keypad through the app<br>before the specified locking time expires. |
| Auto-lock Time, min           | Selecting the device keypad lock period after<br>unauthorized attempts:<br>3 minutes.<br>5 minutes.<br>10 minutes.<br>20 minutes.<br>30 minutes.<br>60 minutes.<br>90 minutes.<br>180 minutes.<br>Available if the Unauthorized Access Auto-Lock<br>toggle is enabled.                                                                    |
| Chime managing with keypad    | When enabled, the user can activate/deactivate                                                                                                                                                                                                                                                                                            |

|                               | from the keypad display notifications about<br>triggering the opening detectors. Enable<br>additionally Chime on opening at keypad's<br>settings and for at least one bistable detector.<br>Learn more                                                                                                                                                                      |
|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Firmware Update               | Switches the device to the firmware updating<br>mode.                                                                                                                                                                                                                                                                                                                       |
| Jeweller Signal Strength Test | Switches the device to the Jeweller signal<br>strength test mode.<br>Learn more                                                                                                                                                                                                                                                                                             |
| Wings Signal Strength Test    | Switches the device to the Wings signal<br>strength test mode.<br>Learn more                                                                                                                                                                                                                                                                                                |
| Signal Attenuation Test       | Switches the device to the signal attenuation<br>test mode.<br>Learn more                                                                                                                                                                                                                                                                                                   |
| Pass/Tag Reset                | Allows deleting all hubs associated with Tag or<br>Pass from device memory.<br>Learn more                                                                                                                                                                                                                                                                                   |
| User Guide                    | Opens the KeyPad TouchScreen user manual in<br>the Ajax app.                                                                                                                                                                                                                                                                                                                |
| Permanent Deactivation        | Allows the user to disable the device without<br>removing it from the system.<br>Three options are available:<br>No — the device operates in normal mode<br>and transmits all events.<br>Entirely — the device does not execute<br>system commands and does not participate<br>in automation scenarios, and the system<br>ignores alarms and other device<br>notifications. |

|                       | Lid only — the system ignores the device<br>tamper triggering notifications.<br>Learn more                                                                                                                        |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| One-Time Deactivation | Allows the user to disable events of the device<br>until the first disarm.                                                                                                                                        |
|                       | Three options are available:                                                                                                                                                                                      |
|                       | No — the device operates in the normal<br>mode.                                                                                                                                                                   |
|                       | Lid only — notifications on the device<br>tamper triggering are disabled while the<br>armed mode is active.                                                                                                       |
|                       | Entirely — the device is completely excluded<br>from the operation of the system while the<br>armed mode is active. The device does not<br>execute system commands and does not<br>report alarms or other events. |
|                       | Learn more                                                                                                                                                                                                        |
| Unpair Device         | Unpairs the device, disconnects it from the hub,<br>and deletes its settings.                                                                                                                                     |

#### Security Management

| Setting        | Value                                                                                                                                                             |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                | Activates/deactivates security control from the<br>keypad.                                                                                                        |
| Control Screen | When disabled, the Control<br>tab is hidden<br>from the keypad display. The user cannot<br>control the security mode of the system and<br>groups from the keypad. |
| Shared Groups  | Selecting which groups will be shared and<br>available for management by all authorized<br>users.                                                                 |

|                                                          | All system groups and groups created after<br>adding KeyPad TouchScreen to the hub are<br>shared by default.<br>Group Mode<br>Available if<br>is enabled.                                                                                                                                                                            |
|----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Pre-authorization                                        | When enabled, to have access to the control<br>panel and current system state, the user should<br>authenticate first: enter a code or present a<br>personal access device.                                                                                                                                                           |
| Arming without Code                                      | When enabled, the user can arm the object<br>without entering a code or presenting the<br>personal access device.<br>If disabled, enter a code or present the access<br>device to arm the system. The screen for<br>entering code appears after pressing Arm<br>button.<br>Available if the Pre-authorization toggle is<br>disabled. |
| Easy Armed Mode Change/Assigned Group<br>Easy Management | When enabled, users can switch the armed<br>mode of the system (or group) using access<br>devices without confirmation with keypad<br>buttons.<br>Group Mode<br>Available if<br>is disabled or only 1<br>group is enabled in the Shared Groups menu.                                                                                 |
| Show malfunctions list on a screen                       | When enabled, the list of malfunctions<br>preventing arming will appear on the keypad<br>system integrity check<br>display. Enable<br>for this.<br>It may take some time to display the list. This<br>reduces the time of the keypad operation from<br>the pre-installed batteries.                                                  |

#### Automation Scenarios

| Setting | Value |
|---------|-------|

| Scenarios Management | Activates/deactivates scenarios management<br>from the keypad.<br>When disabled, the Scenarios<br>tab is hidden<br>from the keypad display. The user cannot<br>control the automation scenarios from the<br>keypad.                                                                                                                                                                                                             |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Keypad Scenarios     | The menu allows you to create up to six<br>scenarios to control one automation device or a<br>group of devices.<br>When the settings are saved, buttons for<br>managing scenarios appear on the keypad<br>display (Scenarios<br>tab).<br>A user or PRO with rights to configure the<br>system can add or delete and turn on/off<br>scenarios. Disabled scenarios don't appear on<br>the Scenarios<br>tab of the keypad display. |
| Pre-authorization    | When enabled, to have access to manage<br>scenarios, the user should authenticate first:<br>enter a code or present a personal access<br>device.                                                                                                                                                                                                                                                                                |

### Emergency Signals

| Setting                     | Value                                                                                                 |
|-----------------------------|-------------------------------------------------------------------------------------------------------|
| On-Screen Emergency Buttons | When enabled, the user can send an emergency<br>signal or call for help from the keypad Panic<br>tab. |
|                             | When disabled, the Panic<br>tab is hidden from<br>the keypad display.                                 |
| Button type                 | Selecting the number of buttons to display on<br>the Panic<br>tab. Two options are available:         |
|                             | Only the Panic button (by default).                                                                   |
|                             | Three buttons: Panic button, Fire, Auxiliary<br>alert.                                                |

| Accidental Press Protection            | When enabled, sending an alarm requires<br>additional confirmation from the user.                                                                                                                              |  |
|----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| Alert with a siren                     |                                                                                                                                                                                                                |  |
| If panic button is pressed             | When enabled, the sirens added to the system<br>are activated when the Panic button is pressed.                                                                                                                |  |
| If panic fire report button is pressed | When enabled, the sirens added to the system<br>are activated when the Fire button is pressed.<br>The toggle is displayed if an option with three<br>buttons is enabled in the Button type menu.               |  |
| If auxiliary request button is pressed | When enabled, the sirens added to the system<br>are activated when the Auxiliary alert button is<br>pressed.<br>The toggle is displayed if an option with three<br>buttons is enabled in the Button type menu. |  |

### Display Settings

| Setting                      | Value                                                                                                                                                     |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Auto Adjust                  | The toggle is enabled by default. The display<br>backlight brightness is automatically adjusted<br>depending on the ambient light level.                  |
| Manual brightness adjustment | Selecting the display backlight level: from 0 to<br>100% (0 — the backlight is minimal, 100 — the<br>backlight is maximum). Sets in increments of<br>10%. |
|                              | The backlight is on when the display is active<br>only.<br>Manual adjustment is available when the Auto<br>Adjust toggle is disabled.                     |
| Appearance                   | Interface appearance adjustment:<br>Dark (by default).                                                                                                    |

|                       | Light.                                                                                                                                                                                                                                                                                                                                                                                               |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Always Active Display | The keypad display always remains enabled<br>when the toggle is enabled and the external<br>power supply is connected.<br>The toggle is disabled by default. In this case,<br>the keypad sleeps after a certain time from the<br>last interaction with the display.                                                                                                                                  |
| Armed Mode Indication | Setting the LED indication of the keypad:<br>Off (by default) — the LED indication is off.<br>Only when armed — the LED indication turns<br>on when the system is armed, and the<br>keypad goes into sleep mode (the display<br>turns off).<br>Always — the LED indication is switched on<br>regardless of the security mode. It is<br>activated when the keypad enters sleep<br>mode.<br>Learn more |
| Language              | Configuring the keypad interface language.<br>English is set by default.<br>To change the language, select the required one<br>and click Save.                                                                                                                                                                                                                                                       |

### Sound Indication Settings

KeyPad TouchScreen has a built-in buzzer that performs the following functions depending on the settings:

- **1.** Indicates the security status and also the [Entry/Exit delays](https://support.ajax.systems/en/what-is-delay-when-entering/).
- **2.** Chimes on opening.
- **3.** Informs about alarms.

![](_page_30_Picture_0.jpeg)

We do not recommend using KeyPad TouchScreen instead of the siren. The keypad's buzzer is meant for additional notifications only.are designed to deter intruders and draw attention. A properly installed siren is more difficult to dismantle due to its elevated mounting position compared to a keypad at eye level. Ajax sirens

| Setting                                   | Value                                                                                                                                       |  |
|-------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|--|
| Beeps Settings. Beep on armed mode change |                                                                                                                                             |  |
| Arming/Disarming                          | When enabled: an audible notification is sent if<br>the security mode is changed from the keypad,<br>another device, or the app.            |  |
|                                           | When disabled: an audible notification is sent if<br>the security mode is changed from the keypad<br>only.                                  |  |
|                                           | The volume of the beep depends on the<br>configured buttons' volume.                                                                        |  |
| Night Mode Activation/Deactivation        | When enabled: an audible notification is sent if<br>the Night Mode is activated/deactivated from<br>the keypad, another device, or the app. |  |
|                                           | When disabled: an audible notification is sent if<br>the Night Mode is activated/deactivated from<br>the keypad only.                       |  |
|                                           | Learn more                                                                                                                                  |  |
|                                           | The volume of the beep depends on the<br>configured buttons' volume.                                                                        |  |
| Beep on delays                            |                                                                                                                                             |  |
| Entry Delays                              | When enabled, the built-in buzzer beeps about a<br>delay when entering.                                                                     |  |
|                                           | Learn more                                                                                                                                  |  |
| Exit Delays                               | When enabled, the built-in buzzer beeps about a<br>delay when leaving.                                                                      |  |
|                                           | Learn more                                                                                                                                  |  |

| Entry Delays in Night Mode                                   | When enabled, the built-in buzzer beeps about a<br>Night Mode<br>delay when entering in the                                                 |
|--------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
|                                                              | Learn more                                                                                                                                  |
| Exit Delays in Night Mode                                    | When enabled, the built-in buzzer beeps about a<br>Night Mode<br>delay when leaving in the<br>Learn more                                    |
|                                                              |                                                                                                                                             |
|                                                              | Beep when disarmed                                                                                                                          |
| Chime on opening                                             | When enabled, the built-in buzzer informs you<br>with a short beep that the opening detectors are<br>triggered in the Disarmed system mode. |
|                                                              | Learn more                                                                                                                                  |
| Beep Volume                                                  | Selecting the built-in buzzer volume level for<br>notifications about arming/disarming, entry/exit<br>delay, and opening:                   |
|                                                              | Quiet.                                                                                                                                      |
|                                                              | Loud.<br>Very Loud.                                                                                                                         |
| Buttons                                                      |                                                                                                                                             |
| Volume                                                       | Adjusting the buzzer notification volume for<br>interactions with the keypad display.                                                       |
| Alarms reaction                                              |                                                                                                                                             |
| Audible Alarm                                                | Setting the mode when the built-in buzzer<br>enables an alarm:                                                                              |
|                                                              | Always — an audible alarm will be activated<br>regardless of the system security mode.                                                      |
|                                                              | Only when armed — an audible alarm will be<br>activated if the system or the group a<br>keypad is assigned to is armed.                     |
| Activate keypad buzzer if alarm in the system is<br>detected | When enabled, the built-in buzzer notifies an<br>alarm in the system.                                                                       |
|                                                              |                                                                                                                                             |

| Alarm in Group Mode | Selecting the group (from the shared) which<br>alarm the keypad will notify. The All Shared<br>Groups option is set by default.    |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------|
|                     | If the keypad has only one shared group and it<br>is deleted, the setting will return to its initial<br>value.                     |
|                     | Group Mode<br>Displayed if the<br>is enabled.                                                                                      |
|                     | Duration of sound signal in case of alarm: from<br>3 seconds to 3 minutes.                                                         |
| Alarm Duration      | The connection of external power supply to the<br>keypad is recommended for an audible signal<br>duration of more than 30 seconds. |

Adjust the entry/exit delays in the appropriate detectors settings, not the keypad settings.

[Learn more](https://support.ajax.systems/en/what-is-delay-when-entering/)

### Setting the keypad response to device alarms

KeyPad TouchScreen can respond to alarms from each detector in the system with a built-in buzzer. The function is useful when you do not need to activate the buzzer for the alarm of a specific device. For example, this can be applied to the triggering ofleakage detector. LeaksProtect

By default, the keypad response is enabled for alarms of all devices in the system.

#### **To set the keypad response to a device alarm:**

- **1.** Open the [Ajax app](https://ajax.systems/software/).
- **2.** Go to the **Devices** tab.
- **3.** Select the device for which you want to configure the keypad response from the list.
- **4.** Go to the device **Settings** by clicking on the icon.
- **5.** Find the **Alert with a siren** option and select the toggles which will activate it. Enable or disable the function.
- **6.** Repeat steps 3–5 for the rest of the system devices.

#### Setting the keypad response to tamper alarm

KeyPad TouchScreen can respond to enclosure alarms from each system device with a built-in buzzer. When the function is activated, the keypad built-in buzzer will emit a sound signal upon triggering the of the device. tamper button

#### **To set the keypad response to a tamper alarm:**

- **1.** Open the Ajax app.
- **2.** Go to the **Devices** tab.
- **3.** Select the hub and go to its **Settings** .
- **4.** Select the **Service** menu.
- **5.** Go to the section **Sounds and Alerts**.
- **6.** Enable the **If lid of hub or any detector is open** toggle.
- **7.** Click **Back** to save the new settings.

![](_page_33_Picture_14.jpeg)

 reacts to opening and closing of the enclosure, regardless of the armed mode of the device or system. [Tamper button](https://support.ajax.systems/en/faqs/what-is-a-tamper/)

## Setting the keypad response to pressing the panic button in the Ajax apps

You can configure the keypad response to alarm when the panic button is pressed in the Ajax apps. To do this, follow these steps:

- **1.** Open the Ajax app.
- **2.** Go to the **Devices** tab.
- **3.** Select the hub and go to its **Settings** .
- **4.** Select the **Service** menu.
- **5.** Go to the section **Sounds and Alerts**.
- **6.** Enable the **If in-app panic button is pressed** toggle.
- **7.** Click **Back** to save the new settings.

### Setting the keypad after-alarm indication

![](_page_34_Picture_8.jpeg)

The keypad can inform about triggering in the armed system through LED indication.

#### **The option functions as follows:**

- **1.** The system registers the alarm.
- **2.** The keypad plays an alarm signal (if enabled). The duration and volume of the signal depend on the device settings.
- **3.** The keypad's LED flashes twice (once every 3 seconds) until the system is disarmed.

Thanks to this feature, system users and security company patrols can understand that the alarm has occurred.

![](_page_34_Picture_15.jpeg)

The KeyPad TouchScreen after-alarm indication does not work for always active detectors, if the detector was triggered when the system was disarmed.

#### **To enable the KeyPad TouchScreen after-alarm indication, in [:](https://ajax.systems/software/)** Ajax PRO app

- **1.** Go to hub settings:
	- Hub → Settings → Service → LED Indication.
- **2.** Specify which events KeyPad TouchScreen will inform about by double flashing of the LED indicator before the system is disarmed:
	- Confirmed intrusion/hold-up alarm.
	- Single intrusion/hold-up alarm.
	- Lid Opening.
- **3.** Select the required KeyPad TouchScreen in the **Devices** menu. Click **Back** to save the parameters.
- **4.** Click **Back**. All values will be applied.

#### How to set Chime

If **Chime on opening** is enabled, KeyPad TouchScreen notify you with a short beep if the opening detectors are triggered when the system is disarmed. The feature is used, for example, in stores to notify employees that someone has entered the building.

Notifications are configured in two stages: setting up the keypad and setting up opening detectors.provides more information about **Chime** and how to set up detectors. This article

#### **To set the keypad response:**

- **1.** Open the Ajax app.
- **2.** Go to the **Devices** tab.
- **3.** Select KeyPad TouchScreen and go to its **Settings** .
- **4.** Go to the **Sound Indication** menu → **Beep Settings**.
- **5.** Enable the **Chime on opening** toggle in the **Beep when disarmed** category.
- **6.** Set the required notifications volume.
- **7.** Click **Back** to save the settings.

If the settings are made correctly, a bell icon appears in the **Control** tab of the Ajax app. Click it to activate or deactivate chime on opening.

#### **To set the chime control from the keypad display:**

- **1.** Open the Ajax app.
- **2.** Go to the **Devices** tab.
- **3.** Select KeyPad TouchScreen and go to its **Settings** .
- **4.** Enable the **Chime managing with keypad** toggle.

If the settings are made correctly, a appears in the **Control** tab on the keypad display. Click it to activate/deactivate chime on opening. bell icon

![](_page_36_Picture_9.jpeg)

### Codes setting

**Keypad access codes**

#### Cards and key fobs adding

KeyPad TouchScreen can work with ,, and third-party devices that support DESFire® technology. Tag key fobs Pass cards

Before adding third-party devices that support DESFire®, make sure they have enough free memory to handle the new keypad. Preferably, the third-party device should be preformatted.

 provides information on how to reset **Tag** or **Pass**. [This article](https://support.ajax.systems/en/manuals/access-devices/#block8)

The maximum number of connected Passes and Tags depends on the hub model. The connected Passes and Tags do not affect the total device limit on the hub.

| Hub model       | Number of Tag or Pass devices |
|-----------------|-------------------------------|
| Hub 2 (2G)      | 50                            |
| Hub 2 (4G)      | 50                            |
| Hub 2 Plus      | 200                           |
| Hub Hybrid (2G) | 50                            |
| Hub Hybrid (4G) | 50                            |

#### How to add a Tag or Pass to the system

![](_page_38_Picture_0.jpeg)

- **1.** Open the Ajax app.
- **2.** Select the hub to which you want to add a Tag or Pass.
- **3.** Go to the **Devices** tab.

Make sure the **Pass/Tag Reading** feature is enabled in at least one keypad setting.

- **4.** Click **Add Device**.
- **5.** Select **Add Pass/Tag**.
- **6.** Specify the type (Tag or Pass), colour, device name, and user (if necessary).
- **7.** Click **Next**. After that, the hub will switch to the device registration mode.
- **8.** Go to any compatible keypad with **Pass/Tag Reading** enabled and activate it.

After activation, KeyPad TouchScreen will display a screen for switching the keypad to the access devices registration mode. Click the **Start** button.

![](_page_38_Picture_11.jpeg)

A screen updates automatically if the external power supply is connected and the **Always Active Display** toggle is enabled in the keypad settings.

The screen for switching the keypad to the registration mode will appear on all KeyPad TouchScreen of the system. When an admin or PRO with rights to configure the system starts registering Tag/Pass at one keypad, the rest will switch to their initial state.

- **9.** Present Pass or Tag with the wide side to the keypad reader for a few seconds. It is marked with wave icons on the body. Upon successful addition, you will receive a notification in the Ajax app and on the keypad display.
If the connection fails, try again in 5 seconds. Please note that if the maximum number of Tag or Pass devices has already been added to the hub, you will receive a corresponding notification in the Ajax app when adding a new device.

> Both Tag and Pass can work with several hubs at the same time. The maximum number of hubs is 13. If you try to bind a Tag or Pass to a hub that has already reached the hub limit, you will receive a corresponding notification. To bind such a key fob/card to a new hub, you will need to . reset it

If you need to add another Tag or Pass, click **Add Another Pass/Tag** in the app. Repeat steps 6–9.

### How to delete a Tag or Pass from the hub

Resetting will delete all settings and bindings of key fobs and cards. In this case, the reset Tag and Pass are only removed from the hub from which the reset was made. On other hubs, Tag or Pass are still displayed in the app but cannot be used to manage the security modes. These devices should be removed manually.

- **1.** Open the Ajax app.
- **2.** Select the hub.
- **3.** Go to the **Devices** tab.
- **4.** Select a compatible keypad from the device list.

![](_page_40_Picture_0.jpeg)

- **5.** Go to the keypad settings by clicking the icon.
- **6.** Click Pass/Tag Reset menu.
- **7.** Click **Continue**.
- **8.** Go to any compatible keypad with **Pass/Tag Reading** enabled and activate it.

After activation, KeyPad TouchScreen will display a screen for switching the keypad to the access devices resetting mode. Click the **Start** button.

![](_page_40_Picture_7.jpeg)

A screen updates automatically if the external power supply is connected and the **Always Active Display** toggle is enabled in the keypad settings.

The screen for switching the keypad to the resetting mode will appear on all KeyPad TouchScreen of the system. When an admin or PRO with rights to configure the system starts resetting Tag/Pass at one keypad, the rest will switch to the initial state.

- **9.** Put Pass or Tag with the wide side to the keypad reader for a few seconds. It is marked with wave icons on the body. Upon successful formatting, you will receive a notification in the Ajax app and on the keypad display. If the formatting fails, try again.
- **10.** If you need to reset another Tag or Pass, click **Reset another Pass/Tag** in the app. Repeat step 9.

#### Bluetooth Setting

KeyPad TouchScreen supports security modes control by presenting a smartphone to the sensor. Security management is established through a Bluetooth communication channel. This method is convenient, secure, and fast, as there is no need to enter a password, add a phone to the keypad, or use Tag or Pass that could be lost.

![](_page_41_Picture_0.jpeg)

#### To enable Bluetooth authentication in the app

- **1.** Connect KeyPad TouchScreen to the hub.
- **2.** Enable the keypad Bluetooth sensor:

**Devices** → **KeyPad Touchscreen** → **Settings** → Enable the **Bluetooth** toggle.

- **3.** Click **Back** to save the settings.
#### To set up Bluetooth authentication

- **1.** Open the Ajax Security System app and select the hub to which the KeyPad TouchScreen with enabled Bluetooth authentication is added. By default, authentication with Bluetooth is available for all users of such system.
To prohibit Bluetooth authentication for certain users:

- **1.** In the **Devices** tab select the hub and go to its settings .
- **2.** Open **Users** menu and the required user from the list.
- **3.** In the **Permissions** section, disable the **Security management via Bluetooth** toggle.
- **2.** Allow the Ajax Security System app to use Bluetooth if it was not previously granted. In this case, the warning appears at KeyPad TouchScreen **States**. Pressing the symbol opens the window with explanations of what to do. Enable the **Security management with a phone** toggle at the bottom of the opened window.

![](_page_42_Picture_0.jpeg)

Grant the app permission to find and connect to nearby devices. The popup window for Android and iOS smartphones can differ.

![](_page_42_Picture_2.jpeg)

Also, the **Security management with a phone** toggle can be enabled in the app settings:

- Click the icon in the upper left corner of the screen, select the **App Settings** menu.
- Open menu **System Settings** and enable **Security management with a phone** toggle.

![](_page_43_Picture_0.jpeg)

- **3.** We recommend configuring **Geofence** for the stable performance of Bluetooth authentication. The warning appears at KeyPad TouchScreen **States** if **Geofence** is disabled and the app is not allowed to use the smartphone location. Pressing the symbol opens the window with explanations of what to do.
![](_page_43_Picture_2.jpeg)

Bluetooth authentication can be unstable if **Geofence** function is disabled. You will need to launch and minimize the app if the system switches it to the sleep mode.

You can control the system faster via Bluetooth, when the **Geofence** function is activated and configured. All you need is to unlock the phone and present it to the keypad sensor.

[How to set up Geofence](https://support.ajax.systems/en/what-is-geofence/)

- **4.** Enable the **Keep app alive to manage security via Bluetooth** toggle. For this, go to **Devices** → **Hub** → **Settings** → **Geofence**.
- **5.** Ensure that Bluetooth is enabled on your smartphone. If it is disabled, the warning appears in the keypad **States**. Pressing the symbol opens the window with explanations of what to do.
- **6.** Enable the **Keep-Alive Service** toggle in the app settings for Android smartphones. For this, in the upper left corner of the screen, click the → **App Settings** → **System Settings**.

#### Pre-authorization

When the feature is enabled, access to the control panel and current system state is blocked. To unblock it, the user should authenticate: enter an or present a personal access device to the keypad. appropriate code

![](_page_44_Picture_5.jpeg)

If pre-authorization is enabled, the **Arming without Code** feature is unavailable in the keypad settings.

#### **You can authenticate in two ways:**

- **1.** In the **Control** tab. After login, the user will see the shared groups of the system (if Group Mode is activated). They are specified in the keypad settings: **Security Management** → **Shared Groups**. By default, all the system groups are shared.
![](_page_45_Picture_0.jpeg)

- **2.** In the **Log in** tab. After login, the user will see available groups that were hidden from the shared group list.
![](_page_45_Picture_2.jpeg)

The keypad display switches to the initial screen after 10 seconds from the last interaction with it. Enter the code or present a personal access device again to control the system with KeyPad TouchScreen.

**Pre-authorization with a keypad code**

**Pre-authorization with Tag or Pass**

**Pre-authorization with a smartphone**

#### Controlling security

Using , Tag/Pass, or a smartphone, you can control the **Night Mode** and the security of the entire object or separate groups. The user or PRO with the rights to configure the system can set up access codes. provides information on how to add Tag or Pass to the hub. To control with a smartphone, adjust the appropriate in the keypad settings. Turn on the smartphone Bluetooth, Location, and unlock the screen. codes This chapter Bluetooth parameters

> KeyPad TouchScreen is locked for the time specified in the settings if an incorrect code is entered, or an unverified access device is presented three times in a row within 1 minute. The corresponding notifications are sent to users and the monitoring station of the security company. A user or PRO with the rights to configure the system can unlock KeyPad TouchScreen in the Ajax app.

Ifis disabled, an appropriate icon on the keypad display indicates the current security mode: Group Mode

- Armed.
- Disarmed.
- Night Mode.

![](_page_47_Picture_0.jpeg)

If Group Mode is enabled, users see the security mode of each group separately. The group is armed if its button outline is white and it is marked with icon. The group is disarmed if its button outline is grey and it is marked with icon.

![](_page_47_Picture_2.jpeg)

The buttons of the groups in the **Night Mode** are framed in a white square on the keypad display.

![](_page_48_Picture_0.jpeg)

If a personal or access code, Tag/Pass, or smartphone is used, the name of the user who changed the security mode is displayed in the hub event feed and in the notifications list. If a general code is used, the name of the keypad from which the security mode was changed is displayed.

The step sequence to change the security mode with the keypad depends on whether user pre-authorization is enabled in the KeyPad TouchScreen settings.

### If pre-authorization is enabled

**Security control of the object Security control of the group Using a duress code**

#### If pre-authorization is disabled

#### Example of entering codes

| Code                                                             | Example            | Note                                                                                                                                                           |
|------------------------------------------------------------------|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Keypad code<br>Keypad duress code                                | 1234 → OK          | Incorrectly entered numbers<br>can be cleared with the<br>button.                                                                                              |
| User code<br>User duress code                                    | 2 →<br>→ 1234 → OK | user ID<br>Enter the<br>first, press<br>the<br>button, and then enter<br>a personal code.<br>Incorrectly entered numbers<br>can be cleared with the<br>button. |
| Code of unregistered user<br>Duress code of unregistered<br>user | 1234 → OK          | Incorrectly entered numbers<br>can be cleared with the<br>button.                                                                                              |

#### Easy armed mode change

**Easy armed mode change** feature allows you to change the security mode to the opposite using Tag/Pass or smartphone, without confirmation with the Arm or Disarm buttons. Go to the to enable the feature. keypad settings

#### **To change the security mode to the opposite**

- **1.** Activate the keypad by approaching it or holding your hand in front of the sensor. Perform pre-authorization if necessary.
- **2.** Present Tag/Pass or smartphone.

#### Two-stage arming

![](_page_50_Picture_1.jpeg)

KeyPad TouchScreen can participate in two-stage arming but cannot be used as a second-stage device. The two-stage arming process using Tag, Pass or smartphone is similar to using a personal or general code on the keypad.

#### [Learn more](https://support.ajax.systems/en/system-congifure-pd-6662-2017/#block4)

The system users can see whether the arming is started or incomplete on the keypad display. If Group Mode is activated, the colour of the group buttons depends on the current state:

- **Grey** disarmed, arming process not started.
- **Green** arming process started.
- **Yellow** arming is incomplete.
- **White** armed.

### Managing scenarios with the keypad

KeyPad TouchScreen allows you to create up to six scenarios to control one or a group of automation devices.

#### **To create a scenario:**

- **1.** Open the . Select the hub with at least one KeyPad TouchScreen and [.](https://support.ajax.systems/en/automation/) Add one if necessary. Ajax app automation device
- **2.** Go to the **Devices** tab.
- **3.** Select KeyPad TouchScreen from the list and go to the **Settings** menu.
- **4.** Go to the **Automation Scenarios** menu. Enable the **Scenarios Management** toggle.
- **5.** Open the **Keypad Scenarios** menu.
- **6.** Press **Add Scenario**.
- **7.** Select one or more automation devices. Press **Next**.
- **8.** Enter the scenario name in the **Name** field.
- **9.** Select device action during the scenario performance.
- **10.** Press **Save**.
- **11.** Press **Back** to return to the **Automation Scenarios** menu.
- **12.** If necessary, activate the **Pre-authorization** toggle.

Created scenarios are displayed in the app: **KeyPad TouchScreen** → **Settings** → **Automation Scenarios** → **Keypad Scenarios**. You can turn them off, adjust settings, or delete them at any time.

#### **To remove a scenario:**

- **1.** Go to the **Settings** of KeyPad TouchScreen.
- **2.** Open **Automation Scenarios** → **Keypad Scenarios** menu.
- **3.** Select the scenario you want to remove.
- **4.** Press **Next**.
- **5.** Press **Delete Scenario**.

The user can see and manage automation scenarios after authentication when the **Pre-authorization** feature is enabled. Go to the **Scenarios** tab, enter the code or present a personal access device to the keypad.

**To perform a scenario**, press an appropriate button in the **Scenarios** tab.

### Fire alarm muting

Chapter in progress

### Indication

KeyPad TouchScreen informs users about alarms, entry/exit delays, current security mode, malfunctions, and other system states with:

- display;
- logo with an LED indicator;
- built-in buzzer.

KeyPad TouchScreen indication is shown on the display only when it is active. Icons that indicate some system or keypad states are displayed in the upper part of the **Control** tab. For example, they can indicate a fire alarm, system restoration after an alarm, and chime on opening. Information about the security mode will be updated even if it is changed by another device: key fob, another keypad, or in the app.

| Event                                         | Indication                                                                                           | Note                                                                                                                                                                             |
|-----------------------------------------------|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Alarm.                                        | The built-in buzzer emits an<br>acoustic signal.                                                     | If Activate keypad buzzer if<br>alarm in the system is<br>detected toggle is enabled.<br>The duration of the acoustic<br>signal depends on the keypad<br>settings.               |
| An alarm was detected in the<br>armed system. | The LED indicator flashes<br>twice approximately every 3<br>seconds until the system is<br>disarmed. | after<br>To activate, enable the<br>alarm indication<br>in the<br>hub settings. Also, specify<br>KeyPad TouchScreen as a<br>device for informing about<br>other devices' alarms. |

|                                                                                                                                                                                                           | The indication turns on after<br>the built-in buzzer has<br>completed playing the alarm<br>signal.                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| An appropriate notification is<br>shown on the display while the<br>data is loading.                                                                                                                      |                                                                                                                                         |
| The LED indicator lights up for<br>1 second, then flashes three<br>times.                                                                                                                                 |                                                                                                                                         |
| The built-in buzzer emits a<br>short beep.                                                                                                                                                                | If notifications for<br>Arming/Disarming are<br>enabled.                                                                                |
| The built-in buzzer emits a<br>short beep.                                                                                                                                                                | If notifications for Night Mode<br>Activation/Deactivation are<br>enabled.                                                              |
| The built-in buzzer emits two<br>short beeps.                                                                                                                                                             | If notifications for<br>Arming/Disarming are<br>enabled.                                                                                |
| The LED indicator lights up red<br>for a short time every 3<br>seconds if the external power<br>is not connected.<br>The LED indicator constantly<br>lights up red if the external<br>power is connected. | If Armed Mode Indication is<br>enabled.<br>The indication turns on when<br>the keypad switches to sleep<br>mode (the display goes out). |
| An appropriate notification is<br>shown on the display.<br>The built-in buzzer emits a<br>short beep (if adjusted).                                                                                       | The beep loudness depends<br>on the configured buttons'<br>volume.                                                                      |
| An appropriate notification is<br>shown on the display.<br>The LED indicator lights up red<br>once.<br>The built-in buzzer emits a<br>long beep.                                                          | The beep loudness depends<br>on the configured buttons'<br>volume.                                                                      |
|                                                                                                                                                                                                           |                                                                                                                                         |

| Successfully added card/key<br>fob.     | An appropriate notification is<br>shown on the display.<br>The built-in buzzer emits a<br>short beep.                                                                                      | The beep loudness depends<br>on the configured buttons'<br>volume.                                                                                                                                                                                                                                                                                                                |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Low battery.                            | The LED indicator smoothly<br>lights up and goes out when<br>the tamper is triggered, an<br>alarm is activated, or the<br>system is armed or disarmed<br>(if the indication is activated). |                                                                                                                                                                                                                                                                                                                                                                                   |
| Tamper triggering.                      | The LED indicator lights up red<br>for 1 second.                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                                                   |
| Jeweller/Wings Signal<br>Strength Test. | The LED indicator lights up<br>green during the test.                                                                                                                                      | Turns on after launching an<br>appropriate test in the<br>keypad settings                                                                                                                                                                                                                                                                                                         |
| Firmware update.                        | The LED indicator periodically<br>lights up green while the<br>firmware is updating.                                                                                                       | Turns on after launching the<br>firmware update in the keypad<br>States                                                                                                                                                                                                                                                                                                           |
| Muting interconnected fire<br>alarm.    | An appropriate notification is<br>shown on the display.<br>The built-in buzzer emits an<br>acoustic signal.                                                                                |                                                                                                                                                                                                                                                                                                                                                                                   |
| The keypad is deactivated.              | An appropriate notification is<br>shown on the display.                                                                                                                                    | If Entirely option is selected<br>Permanent<br>One<br>for the<br>or<br>Time Deactivation<br>keypad settings.                                                                                                                                                                                                                                                                      |
| System restoration is required.         | An appropriate screen to<br>restore or send a request for<br>the system restoration after<br>the alarm appears on the<br>display.                                                          | Restoration After<br>The<br>Alarm feature<br>has to be<br>adjusted in the system.<br>The screen appears when<br>arming or switching the<br>system to the Night Mode if an<br>alarm or malfunction occurred<br>in the system before.<br>Admins or PROs with the<br>rights to configure the system<br>can restore the system. Other<br>users can send a request for<br>restoration. |

#### Sound notifications of malfunctions

If any device is offline or the battery is low, KeyPad TouchScreen can notify system users with an audible sound. The keypad's LED indicator will also flash. Malfunction notifications will be displayed in the events feed, SMS, or push notification.

To enable sound notifications of malfunctions, use Ajax PRO and PRO Desktop : [apps](https://ajax.systems/software/)

- **1.** Click **Devices** , choose hub and open its settings :
Click **Service** → **Sounds and Alerts**.

- **2.** Enable toggles: **If battery of any device is low** and **If any device is offline**.
- **3.** Click **Back** to save settings.

| Event                                   | Indication                                                                                                                                | Note                                              |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| If any device is offline.               | Two short sound signals, LED<br>indicator flashes twice.<br>Beep occurs once per minute<br>until all devices in the system<br>are online. | Users can delay sound<br>indication for 12 hours. |
| If KeyPad TouchScreen is<br>offline.    | Two short sound signals, LED<br>indicator flashes twice.<br>Beep occurs once per minute<br>until the keypad in the system<br>is online.   | Sound indication delay is not<br>possible.        |
| If the battery of any device is<br>low. | Three short sound signals,<br>LED indicator flashes three<br>times.<br>Beep occurs once per minute<br>until the battery is restored or    | Users can delay sound<br>indication for 4 hours.  |

Sound notifications of malfunctions appear when the keypad indication is finished. If multiple malfunctions occur in the system, the keypad will first notify about the loss of connection between the device and the hub first.

### Functionality testing

The Ajax system offers several types of tests to help select the correct installation place for the devices. Tests do not start immediately. However, the waiting time does not exceed the duration of one "hub-device" ping interval. Ping interval can be checked and configured at hub settings (**Hub** → **Settings** → **Jeweller** or **Jeweller/Fibra**).

#### **To run a test, in the Ajax app:**

- **1.** Select the required hub.
- **2.** Go to the **Devices** tab.
- **3.** Select **KeyPad TouchScreen** from the list.
- **4.** Go to **Settings** .
- **5.** Select a test:
	- **1.** [Jeweller Signal Strength Test](https://support.ajax.systems/en/what-is-signal-strenght-test/)
	- **2.** [Wings Signal Strength Test](https://support.ajax.systems/en/wings-signal-strenght-test/)
	- **3.** [Signal Attenuation Test](https://support.ajax.systems/en/what-is-attenuation-test/)
- **6.** Run the test.

### Device placement

![](_page_56_Picture_15.jpeg)

The device is designed for indoor use only.

When choosing a location for the device, consider the parameters that affect its operation:

- Jeweller and Wings signal strength.
- Distance between the keypad and the hub or range extender.
- Presence of obstacles for radio signal passage: walls, interfloor ceilings, large objects located in the room.

Consider the recommendations for placement when developing a security system project for your facility. The security system must be designed and installed by specialists. A list of recommended partners is [.](https://ajax.systems/where-to-buy/) available here

KeyPad TouchScreen is best placed indoors near the entrance. This allows disarming the system before the entry delays have expired and quickly arming the system when leaving the premises.

The recommended installation height is 1.3–1.5 meters above the floor. Install the keypad on a flat, vertical surface. This ensures KeyPad TouchScreen is securely attached to the surface and helps avoid false tamper alarms.

### Signal strength

The Jeweller and Wings signal strength is determined by the number of undelivered or corrupted data packages over a certain period of time. The icon on the **Devices** tab indicates the signal strength:

- **Three bars** excellent signal strength.
- **Two bars** good signal strength.
- **One bar** low signal strength, stable operation is not guaranteed.
- **Crossed out icon** no signal.

Check the Jeweller and Wings signal strength before final installation. With a signal strength of one or zero bars, we do not guarantee stable operation of the device. Consider relocating the device as repositioning even by 20 cm can significantly improve the signal strength. If there is still poor or unstable signal after the relocation, use radio signal range extender. **KeyPad TouchScreen is incompatible with ReX radio signal range extenders**. [ReX 2](https://ajax.systems/products/rex-2/)

#### Do not install the keypad

- **1.** Outdoors. This can lead to keypad failure.
- **2.** In places where parts of clothing (for example, next to the hanger), power cables or Ethernet wire may obstruct the keypad. This can lead to false triggering of the keypad.
- **3.** Nearby any metal objects or mirrors causing attenuation and screening of the signal.
- **4.** Inside premises with temperature and humidity outside the permissible limits. This could damage the keypad.
- **5.** Closer than 1 meter from the hub or radio signal range extender. This can lead to a loss of communication with the keypad.
- **6.** In a place with a low signal level. This may result in the loss of the connection with the hub.
- **7.** Near the glass break detectors. The built-in buzzer sound may trigger an alarm.
- **8.** In places where the acoustic signal can be attenuated (inside furniture, behind thick curtains, etc.).

## Installation

Before installing KeyPad TouchScreen, ensure that you have selected the optimal location that complies with the requirements of this manual.

#### **To mount a keypad:**

- **1.** Remove the SmartBracket mounting panel from the keypad. Unscrew the holding screw first and slide the panel down.
- **2.** Fix the SmartBracket panel using double-sided tape to the selected installation spot.

Double-sided tape can only be used for temporary installation. The device attached

![](_page_59_Picture_0.jpeg)

by the tape may come unstuck from the surface at any time. As long as the device is taped, the tamper will not be triggered when the device is detached from the surface.

![](_page_59_Picture_2.jpeg)

SmartBracket has markings on the inner side for easy installation. The intersection of two lines marks the centre of the device (not the attachment panel). Orient them when installing the keypad.

![](_page_59_Picture_4.jpeg)

- **3.** Place the keypad on SmartBracket. The device LED indicator will flash. It is a signal indicating that the enclosure of the keypad is closed.
If the LED indicator doesn't light up during placing on SmartBracket, check the tamper status in the Ajax app, the integrity of the fastening, and the tightness of the keypad fixation on the panel.

- **4.** Run the andsignal strength tests. The recommended signal strength is two or three bars. If the signal strength is low (a single bar), we do not guarantee stable operation of the device. Consider relocating the device, as repositioning even by 20 cm can significantly improve the signal [strength. If there is still poor or unstable signal after the relocation, use](https://ajax.systems/products/rex-2/)  radio signal range extender. Jeweller Wings ReX 2
- **5.** Run [.](https://support.ajax.systems/en/what-is-attenuation-test/) During the test, the signal strength can be reduced and increased to simulate different conditions at the installation location. If the installation spot is chosen correctly, the keypad will have a stable signal strength of 2–3 bars. Signal Attenuation Test
- **6.** If the tests are passed successfully, remove the keypad from SmartBracket.
- **7.** Fix the SmartBracket panel on the surface with bundled screws. Use all fixing points.

![](_page_60_Picture_2.jpeg)

- **8.** Place the keypad on the SmartBracket mounting panel.
- **9.** Tighten the holding screw on the bottom of the keypad's enclosure. The screw is needed for more reliable fastening and protection of the keypad from quick dismantling.

![](_page_60_Picture_5.jpeg)

## Connecting a third-party power supply unit

When connecting a third-party power supply unit and using KeyPad TouchScreen, follow the general electrical safety regulations for using electrical appliances, as well as the requirements of regulatory legal acts on electrical safety.

KeyPad TouchScreen is equipped with terminals for connecting a 10.5V–14 V⎓ power supply unit. Recommended electrical parameters for the power supply unit are: 12 V⎓ with a current of at least 0.5 A. The connection of the external power supply is recommended when you need to keep a display always active and to avoid rapid battery discharge.

When external power is connected, the pre-installed batteries serve as a backup power source. Do not remove them while connecting the power supply.

![](_page_60_Picture_10.jpeg)

Before installing the device, make sure to check the wires for any damage to the insulation. Use only a grounded power source. Do not disassemble the device while it's under voltage. Do not use the device with a damaged power cable.

#### **To connect a third-party power supply unit:**

- **1.** Remove the SmartBracket mounting panel. Carefully break out the perforated enclosure part to prepare the holes for the cable:
![](_page_61_Picture_2.jpeg)

1 — to output the cable through the wall.

2 — to output the cable from the bottom. It is enough to break out one of the perforated parts.

- **2.** De-energize external power supply cable.
- **3.** Connect the cable to the terminals by observing polarity (marked on the plastic).

![](_page_61_Picture_7.jpeg)

- **4.** Route the cable in the cable channel. An example of how to output the cable from the bottom of the keypad:
![](_page_62_Picture_1.jpeg)

- **5.** Turn on the keypad and place it on the mounting panel.
- **6.** Check the status of batteries and external power in the Ajax app and the overall operation of the device.

#### Maintenance

Regularly check the functioning of KeyPad TouchScreen. The optimal frequency of checks is once every three months. Clean the device enclosure of dust, cobwebs, and other contaminants as they emerge. Use soft, dry wipes suitable for equipment maintenance.

Do not use substances that contain alcohol, acetone, petrol, and other active solvents to clean the device. Gently wipe the touch screen.

The device runs for up to 1.5 years on the pre-installed batteries — a calculated value based on default settings and up to 4 daily interactions with the keypad.

The system will send an early warning when it's time to replace the batteries. When changing the security mode, the LED will slowly light up and go out.

### Technical specifications

[All technical specifications of KeyPad TouchScreen](https://ajax.systems/products/specs/keypad-touchscreen/)

#### [Compliance with standards](https://ajax.systems/standards/)

#### Warranty

Warranty for the Limited Liability Company "Ajax Systems Manufacturing" products is valid for 2 years after the purchase.

If the device does not function correctly, please contact the Ajax Technical Support first. In most cases, technical difficulties can be resolved remotely.

#### [Warranty obligations](https://ajax.systems/warranty)

[User agreement](https://ajax.systems/end-user-agreement)

#### **Contact Technical Support:**

- [e-mail](mailto:support@ajax.systems)
- [Telegram](https://t.me/AjaxSystemsSupport_Bot)

#### Subscribe to the newsletter about safe life. No spam

Email Subscribe