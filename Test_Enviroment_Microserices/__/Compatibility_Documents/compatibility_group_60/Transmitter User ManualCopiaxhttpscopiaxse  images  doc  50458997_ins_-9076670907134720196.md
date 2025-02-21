# Transmitter User Manual

Updated December 7, 2021

![](_page_0_Picture_2.jpeg)

**Transmitter** is a module for connecting third-party detectors to Ajax security system. It transmits alarms and warns about the activation of the external detector tamper and it is equipped with own accelerometer, which protects it from dismounting. It runs on batteries and can supply power to the connected detector.

Transmitter operates within the Ajax security system, by connecting via the protected protocol to the . It is not intended to use the device in third-party systems. Jeweller hub

![](_page_0_Picture_5.jpeg)

The communication range can be up to 1,600 meters provided that there are no obstacles and the case is removed.

Transmitter is set up via a for iOS and Android based smartphones. mobile application

#### Buy integration module Transmitter

### Functional Elements

![](_page_1_Picture_3.jpeg)

- **1.** QR code with the device registration key.
- **2.** Batteries contacts.
- **3.** LED indicator.
- **4.** ON/OFF button.
- **5.** Terminals for detector power supply, alarm and tamper signals.

# Operation procedure

Transmitter is designed to connect third-party wired sensors and devices to the Ajax security system. The integration module receives information about alarms and tamper activation through the wires connected to the clamps.

Transmitter can be used to connect panic and medical buttons, indoor and outdoor motion detectors, as well as opening, vibration, breaking, fire, gas, leakage and others wired detectors.

The type of alarm is indicated in the settings of the Transmitter. The text of notifications about alarms and events of the connected device, as well as event codes transmitted to the central monitoring panel of the security company (CMS) depend on the selected type.

#### **A total of 5 types of devices are available:**

| Type                    | Icon |
|-------------------------|------|
| Intrusion alarm         |      |
| Fire alarm              |      |
| Medical alarm           |      |
| Panic button            |      |
| Gas concentration alarm |      |

Transmitter has 2 pairs of wired zones: alarm and tamper.

A separate pair of terminals ensures power supply to the external detector from the module batteries with 3.3 V.

# Connecting to the hub

### Before starting connection:

- **1.** Following the hub instruction recommendations, install the on your smartphone. Create an account, add the hub to the application, and create at least one room. Ajax application
- **2.** Go to the Ajax application.
- **3.** Switch on the hub and check the internet connection (via Ethernet cable and/or GSM network).
- **4.** Ensure that the hub is disarmed and does not start updates by checking its status in the mobile application.

![](_page_3_Picture_8.jpeg)

Only users with administrative privileges can add the device to the hub

# **How to connect the Transmitter to the hub:**

- **1.** Select the **Add Device** option in the Ajax application.
- **2.** Name the device, scan/write manually the **QR Code** (located on the body and packaging), and select the location room.
- **3.** Select **Add**  the countdown will begin.
- **4.** Switch on the device (by pressing on/off button for 3 seconds).

![](_page_4_Picture_0.jpeg)

For the detection and interfacing to occur, the device should be located within the coverage area of the wireless network of the hub (at a single protected object).

Request for connection to the hub is transmitted for a short time at the time of switching on the device.

If the connection to the Ajax hub failed, the Transmitter will switch off after 6 seconds. You may repeat the connection attempt then.

The Transmitter connected to the hub will appear in the list of devices of the hub in the application. Update of device statuses in the list depends on the device inquiry time set in the hub settings, with the default value – 36 seconds.

#### States

The states screen contains information about the device and its current parameters. The statuses of Transmitter and the device connected to it can be found in the Ajax app:

- **1.** Go to the **Devices** tab.
- **2.** Select Transmitter from the list.

| Parameter   | Value                                      |
|-------------|--------------------------------------------|
| Temperature | Temperature of the device. Measured on the |

|                          | processor and changes gradually. Displayed in<br>1°C increment.                                                       |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------|
|                          | Acceptable error between the value in the app<br>and temperature at the installation site: 2–4°C                      |
|                          | Signal strength between the hub/range<br>extender and the Transmitter.                                                |
| Jeweller Signal Strength | We recommend installing the detector in places<br>where the signal strength is 2–3 bars                               |
|                          | Connection status between the hub/range<br>extender and device:                                                       |
| Connection               | Online — device is connected with the<br>hub/range extender                                                           |
|                          | Offl<br>ine — device has lost connection with<br>the hub/range extender                                               |
| ReX range extender name  | Indicates if Transmitter is connected via a<br>radio signal range extender                                            |
|                          | Battery level of the device. Displayed as a<br>percentage                                                             |
|                          |                                                                                                                       |
| Battery Charge           | How battery charge is displayed in                                                                                    |
|                          | Ajax apps                                                                                                             |
| Lid                      | Device tamper zone status                                                                                             |
| Delay When Entering, sec | Entry delay (alarm activation delay) is the time<br>you have to disarm the security system after<br>entering the room |
|                          | What is delay when entering                                                                                           |
|                          | Delay time when exiting. Delay when exiting                                                                           |
| Delay When Leaving, sec  | (alarm activation delay) is the time you have to<br>exit the room after arming the security system                    |
|                          | What is delay when leaving                                                                                            |

|                                                                                    | delay) is the time you have to disarm the<br>security system after entering the premises.                                                                                                                                                                                                                                                     |
|------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                    | What is delay when entering                                                                                                                                                                                                                                                                                                                   |
| Night mode When Leaving, sec                                                       | The time of Delay When Leaving in the Night<br>mode. Delay when leaving (alarm activation<br>delay) is the time you have to exit the premises<br>after the security system is armed.<br>What is delay when leaving                                                                                                                            |
| External sensor state<br>(displayed when the detector is in bistable<br>mode only) | Displays the status of the connected detector<br>alarm zone. Two statuses are available:<br>OK — the state of the connected detector<br>contacts is normal<br>Alert — the connected detector contacts are<br>in alarm mode (closed if the type of<br>contacts is normally open (NO); open if the<br>type of contacts is normally closed (NC)) |
| Alert if Moved                                                                     | It turns on the built-in accelerometer, detecting<br>device movement                                                                                                                                                                                                                                                                          |
| Always Active                                                                      | When this option is enabled, the integration<br>module is constantly armed and notifies about<br>the connected detector alarms<br>Learn more                                                                                                                                                                                                  |
| Chime activation                                                                   | When enabled, the sirens connected to the<br>system notify about the triggering of the<br>opening detectors integrated with the<br>Transmitter in the Disarmed system mode<br>What is chime and how it works                                                                                                                                  |
| Temporary Deactivation                                                             | Shows the status of the device temporary<br>deactivation function:                                                                                                                                                                                                                                                                            |
|                                                                                    | No — the device operates normally and<br>transmits all events.                                                                                                                                                                                                                                                                                |
|                                                                                    | Lid only — the hub administrator has<br>disabled notifications about triggering on<br>the device body.                                                                                                                                                                                                                                        |

|            | Entirely — the device is completely excluded<br>from the system operation by the hub<br>administrator. The device does not follow<br>system commands and does not report<br>alarms or other events.<br>By number of alarms — the device is<br>automatically disabled by the system when<br>the number of alarms is exceeded (specified<br>in the settings for Devices Auto<br>Deactivation). The feature is configured in<br>the Ajax PRO app.<br>By timer — the device is automatically<br>disabled by the system when the recovery<br>timer expires (specified in the settings for<br>Devices Auto Deactivation). The feature is<br>configured in the Ajax PRO app. |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Firmware   | Detector firmware version                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Device ID  | Device identifier                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Device No. | Number of the device loop (zone)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

# Settings

To change the Transmitter settings in the Ajax app:

- **1.** Go to the **Devices** tab.
- **2.** Select **Transmitter** from the list.
- **3.** Go to **Settings** by clicking on the .
- **4.** Set the required parameters.
- **5.** Click **Back** to save the new settings.

| Setting     | Value                                                                                                                                                                                                       |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| First field | Detector name that can be changed. The name<br>is displayed in the text of SMS and notifications<br>in the event feed.<br>The name can contain up to 12 Cyrillic<br>characters or up to 24 Latin characters |
|             |                                                                                                                                                                                                             |

| Room                                | Selecting the virtual room to which Transmitter<br>is assigned. The name of the room is displayed<br>in the text of SMS and notifications in the event<br>feed                                                                                                                                                            |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Delay When Entering, sec            | Selecting delay time when entering. Delay when<br>entering (alarm activation delay) is the time you<br>have to disarm the security system after<br>entering the room                                                                                                                                                      |
|                                     | What is delay when entering                                                                                                                                                                                                                                                                                               |
| Delay When Leaving, sec             | Selecting the delay time when exiting. Delay<br>when exiting (alarm activation delay) is the time<br>you have to exit the room after arming the<br>security system                                                                                                                                                        |
|                                     | What is delay when leaving                                                                                                                                                                                                                                                                                                |
| Arm in Night Mode                   | If active, the detector connected to the<br>integration module will switch to the armed<br>mode when using the Night mode                                                                                                                                                                                                 |
| Night mode Delay When Entering, sec | The time of Delay When Entering in the Night<br>mode. Delay when entering (alarm activation<br>delay) is the time you have to disarm the<br>security system after entering the premises.                                                                                                                                  |
|                                     | What is delay when entering                                                                                                                                                                                                                                                                                               |
| Night mode Delay When Leaving, sec  | The time of Delay When Leaving in the Night<br>mode. Delay when leaving (alarm activation<br>delay) is the time you have to exit the premises<br>after the security system is armed.                                                                                                                                      |
|                                     | What is delay when leaving                                                                                                                                                                                                                                                                                                |
| Detector power supply               | 3.3 V power-on for wired detector:                                                                                                                                                                                                                                                                                        |
|                                     | Always enabled — use if problems are<br>observed in the "Disabled if hub is not<br>armed" power mode of the external<br>detector. If the security system is armed in<br>pulse mode, signals on the ALARM terminal<br>are processed no more than once every<br>three minutes and always processed in the<br>bistable mode. |

|                                  | Disabled if disarmed — the module powers<br>off the external detector if disarmed and<br>does not process signals from the ALARM<br>terminal. Once the detector is armed, the<br>power supply resumes, but the detector<br>alarms are ignored for the first 8 seconds.<br>Always Disabled — Transmitter does not<br>use energy to power an external detector.<br>Signals from the ALARM terminal are<br>processed in both pulse and bistable<br>modes.<br>If the Always Active mode is enabled, the<br>external detector power supply is on in the<br>Always Active or Disabled if not Armed modes<br>only, regardless of the security system status. |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| External Detector Contact Status | Selection of the external detector normal<br>status:<br>Normally opened (NO)<br>Normally closed (NC)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| External Detector Type           | Selection of the external detector type:<br>Bistable<br>Pulse                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Type of event                    | Selecting the alarm type of the connected<br>detector or device:<br>Intrusion<br>Fire<br>Medical help<br>Panic button<br>Gas<br>The text of notifications in the notification feed<br>and SMS, as well as the code transmitted to the<br>monitoring station of the security company,<br>depends on the selected type of event                                                                                                                                                                                                                                                                                                                         |
| Tamper status                    | Selection of the normal tamper mod for an<br>external detector:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

|                                               | Normally opened (NO)                                                                                                                                                                                                                                                     |
|-----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                               | Normally closed (NC)                                                                                                                                                                                                                                                     |
| Alarm if moved                                | Enabling the built-in accelerometer to receive an<br>alarm in case of device movement                                                                                                                                                                                    |
| Always Active                                 | When this option is enabled, the integration<br>module is constantly armed and notifies about<br>the connected detector alarms<br>Learn more                                                                                                                             |
| Alert with a siren if alarm detected          | sirens<br>If active,<br>added to the system are<br>activated if an alarm is detected                                                                                                                                                                                     |
| Alert with a siren if accelerometer triggered | sirens<br>If active,<br>added to the system are<br>triggered if device movement is detected                                                                                                                                                                              |
| Chime settings                                | Opens the settings of Chime.<br>How to set Chime<br>What is Chime                                                                                                                                                                                                        |
| Jeweller Signal Strength Test                 | Switches the Transmitter to the Jeweller signal<br>strength test mode<br>Learn more                                                                                                                                                                                      |
| Signal Attenuation Test                       | Switches the Transmitter to the signal fade test<br>mode (available in device with firmware version<br>3.50 and later)<br>Learn more                                                                                                                                     |
| User Guide                                    | Opens the Transmitter User Manual in the Ajax<br>app                                                                                                                                                                                                                     |
| Temporary deactivation                        | Two options are available:<br>Entirely — the device will not execute<br>system commands or run automation<br>scenarios. The system will ignore device<br>alarms and notifications<br>Lid only — messages about triggering the<br>tamper button of the device are ignored |

|               | Learn more about device temporary                                                                                                                                                            |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|               | deactivation                                                                                                                                                                                 |
|               | The system can also automatically deactivate<br>devices when the set number of alarms is<br>exceeded or when the recovery timer expires.<br>Learn more about auto deactivation<br>of devices |
| Unpair Device | Disconnects the device from the hub and<br>deletes its settings                                                                                                                              |

### How to set Chime

Chime is a sound signal that indicates the triggering of the opening detectors when the system is disarmed. The feature is used, for example, in stores, to notify employees that someone has entered the building.

Notifications are configured in two stages: setting up opening detectors and setting up sirens.

#### Learn more about Chime

#### **Transmitter settings**

Before setting up the Chime feature, make sure that a wired opening detector is connected to Transmitter and the following options have been configured in the detector settings in the Ajax app:

- Detector power supply
- External Detector Contact Status
- External Detector Type
- Type of event
- Tamper status

**1.** Go to the **Devices** menu.

- **2.** Select the Transmitter.
- **3.** Go to its settings by clicking the gear icon in the upper right corner.
- **4.** Go to the **Chime Settings** menu.
- **5.** Select siren notification for the event **If external contact is open**.
- **6.** Select the chime sound: 1 to 4 beeps. Once selected, the Ajax app will play the sound.
- **7.** Click **Back** to save the settings.
- **8.** Set up the required siren.

#### How to set up a siren for Chime

### Indication

| Event                                                 | Indication                                                                                                                 |
|-------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| The Module is switched on and registered              | The LED lights up when the ON button is briefly<br>pressed.                                                                |
| Registration failed                                   | LED blinks for 4 seconds with an interval of 1<br>second, then blinks 3 times rapidly (and<br>automatically switches OFF). |
| The Module is deleted from the list of hub<br>devices | LED blinks for 1 minute with an interval of 1<br>second, then blinks 3 times rapidly (and<br>automatically switches OFF).  |
| The Module has received alarm/tamper signal           | The LED lights up for 1 second.                                                                                            |
| Batteries are discharged                              | Smoothly lights up and goes out when the<br>detector or tamper is activated.                                               |

# Performance testing

The Ajax security system allows conducting tests for checking the functionality of connected devices.

The tests do not start straight away but within a period of 36 seconds when using the standard settings. The test time start depends on the settings of the detector scanning period (the paragraph on "**Jeweller**" settings in hub settings).

#### Attenuation Test

### Connection of the Module to the wired detector

Location of the Transmitter determines its remoteness from the hub and presence of any obstacles between the devices hindering the radio signal transmission: walls, inserted floors, large-size objects located within the room.

![](_page_13_Picture_4.jpeg)

Check the signal strength level at the installation location

If the signal level is one division, we cannot guarantee stable operation of the security system. Take possible measures to improve the quality of the signal! As a minimum, move the device — even 20 cm shift can significantly improve the quality of reception.

If after moving the device still has a low or unstable signal strength, use a . radio signal range extender

The Transmitter should be encased inside the wired detector case. The Module requires a space with the following minimum dimensions: 110 × 41 × 24 mm. If the installation of the Transmitter within the detector case is impossible, then any available radiotransparent case could be used.

- **1.** Connect the Transmitter to the detector through the NC/NO contacts (choose the relevant setting in the application) and COM.
![](_page_13_Picture_10.jpeg)

The maximum cable length for connecting the sensor is 150 m (24 AWG twisted pair). The value may vary when using different type of cable.

#### **The function of the Transmitter's terminals**

![](_page_14_Figure_0.jpeg)

- **+ —** power supply output (3.3 V)
- **ALARM** alarm terminals

**TAMP** — tamper terminals

![](_page_14_Picture_4.jpeg)

IMPORTANT! Do not connect external power to the Transmitter's power outputs. This may damage the device

- **2.** Secure the Transmitter in the case. Plastic bars are included in the installation kit. It is recommendable to install the Transmitter on them.
#### **Do not install the Transmitter:**

- Near metal objects and mirrors (they can shield the radio signal and lead to its attenuation).
- Closer than 1 meter to a hub.

#### Maintenance and Battery Replacement

The device does not require maintenance when mounted in the housing of a wired sensor.

#### How long Ajax devices operate on batteries, and what affects this

#### Battery Replacement

#### Tech Specs

| Connecting a detector                                         | ALARM and TAMPER (NO/NC) terminals                                                                                                                            |
|---------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Mode for processing alarm signals from the<br>detector        | Pulse or Bistable                                                                                                                                             |
| Power                                                         | 3 × CR123A, 3V batteries                                                                                                                                      |
| Capability to power the connected detector                    | Yes, 3.3V                                                                                                                                                     |
| Protection from dismounting                                   | Accelerometer                                                                                                                                                 |
| Radio communication protocol with hubs and<br>range extenders | Jeweller<br>Learn more                                                                                                                                        |
| Radio frequency band                                          | 866.0 – 866.5 MHz<br>868.0 – 868.6 MHz<br>868.7 – 869.2 MHz<br>905.0 – 926.5 MHz<br>915.85 – 926.5 MHz<br>921.0 – 922.0 MHz<br>Depends on the region of sale. |
| Compatibility                                                 | hubs<br>radio<br>Operates only with all Ajax<br>, and<br>signal range extenders                                                                               |
|                                                               |                                                                                                                                                               |
| Maximum RF output power                                       | Up to 20 mW                                                                                                                                                   |
| Modulation                                                    | GFSK                                                                                                                                                          |
| Communication range                                           | Up to 1,600 m (any obstacles absent)                                                                                                                          |
| Ping interval for the connection with the<br>receiver         | 12–300 sec                                                                                                                                                    |
| Operating temperature                                         | From –25°С to +50°С                                                                                                                                           |
| Operating humidity                                            | Up to 75%                                                                                                                                                     |
| Dimensions                                                    | 100 × 39 × 22 mm                                                                                                                                              |
| Weight                                                        | 74 g                                                                                                                                                          |

#### Compliance with standards

### Complete Set

- **1.** Transmitter
- **2.** Battery CR123A 3 pcs
- **3.** Installation kit
- **4.** Quick Start Guide

# Warranty

Warranty for the "AJAX SYSTEMS MANUFACTURING" LIMITED LIABILITY COMPANY products is valid for 2 years after the purchase and does not apply to the pre-installed battery.

If the device does not work correctly, you should first contact the support service — in half of the cases, technical issues can be solved remotely!

The full text of the warranty

User Agreement

Technical support: support@ajax.systems