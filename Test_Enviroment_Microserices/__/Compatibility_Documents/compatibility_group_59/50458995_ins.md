# LeaksProtect User Manual

Updated December 7, 2021

![](_page_0_Picture_2.jpeg)

**LeaksProtect** is a wireless leakage detector that notifies both in case of a leak and when the water dries out. Developed only for indoor use.

LeaksProtect connects to the Ajax security system via the protected radio protocol. The communication range is up to 1300 meters in line of sight. Also, LeaksProtect can be connected to third-party security systems using the or integration modules. Jeweller Ajax uartBridge Ajax ocBridge Plus

Users can configure LeaksProtect via the for macOS, Windows, iOS, or Android. The system notifies users of all events through push notifications, SMS, and calls (if activated). Ajax app

The user can connect the Ajax security system to the central monitoring station of a security company.

Buy leakage detector LeaksProtect

## Functional Elements and Indication

![](_page_1_Picture_0.jpeg)

- **1.** LED indicator
- **2.** Water sensor contacts
- **3.** QR code with the device registration key
- **4.** On/off button

## Operating Principle

At the bottom of its body, LeaksProtect is equipped with four pairs of watersensitive contacts. If at least one contact pair gets wet, the detector immediately transmits an alarm signal to the hub, notifying the user and security company. Also, the detector notifies users if the water dries out.

When switched on, LeaksProtect is always active and monitors the situation regardless of the security mode: disarmed or armed.

If the leak is detected, LeaksProtect notifies once, and the next alarm is transmitted when the contacts have dried out and gotten wet again.

## Connecting the detector to the Ajax security system

## **Detector connection to hub**

#### **Before connecting:**

- **1.** Following the hub user manual, install the . Create an account, add the hub to the app, and create at least one room. Ajax app
- **2.** Check the internet connection (via Ethernet cable and/or GSM network).
- **3.** Check the hub status in the app: make sure that it is disarmed and does not update.

![](_page_2_Picture_6.jpeg)

Only users with administrator rights can add the device to the hub.

#### **How to pair the detector with hub:**

- **1.** Select **Add Device** in the Ajax app.
- **2.** Name the device, scan or enter the **QR Code** (located on the body and packaging), and select the location room.
- **3.** Select **Add**  the countdown will begin.
- **4.** Switch on the device.

![](_page_2_Picture_13.jpeg)

LeaksProtect has a rigid "ON" button: press it with force to switch the detector on.

For the detection and pairing to occur, the device should be located within the wireless coverage area of the hub (at the same facility).

Request for connection is transmitted for a short time at the moment of switching on the device.

If the connection failed, LeaksProtect switches off after 6 seconds. To retry the connection, you do not need to reboot the device. If LeaksProtect is paired with another hub, switch the detector off, then retry the standard adding procedure.

The detector connected to the hub is displayed in the list of devices in the app. The update of the detector status in the list depends on the device inquiry time set in the hub settings (the default value is 36 seconds).

## Connecting to the third-party security systems

To connect the detector to a third-party security central unit using the or integration module, follow the recommendations in the manual of the respective device. uartBridge ocBridge Plus

The detector is always active. When connecting LeaksProtect to third party security systems, it is appropriate to place the detector in a permanently active protection zone.

### States

- **1.** Devices
- **2.** LeaksProtect

| Parameter                | Value                                                                                                        |  |
|--------------------------|--------------------------------------------------------------------------------------------------------------|--|
| Temperature              | Temperature of the detector, measured on the<br>processor and changes gradually                              |  |
| Jeweller Signal Strength | Signal strength between the hub and detector                                                                 |  |
| Battery Charge           | Battery level of the device. Displayed as a<br>percentage<br>How battery charge is displayed in<br>Ajax apps |  |
| Lid                      | The state of the tamper, which reacts to the                                                                 |  |
|                          | body being disassembled or damaged                                                                           |  |
| ReX                      | radio signal<br>Displays the status of using a<br>range extender                                             |  |

| Connection             | Connection status between the hub and<br>detector                                                                                                                 |  |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| Leakage detected       | Alarm if the water sensor contacts wet                                                                                                                            |  |
| Temporary Deactivation | Shows the status of the device: active,<br>completely disabled by the user, or only<br>notifications about triggering of the device<br>tamper button are disabled |  |
| Firmware               | Detector firmware version                                                                                                                                         |  |
| Device ID              | Device identifier                                                                                                                                                 |  |

## Settings

- **1.** Devices
- **2.** LeaksProtect
- **3.** Settings

| Setting                                   | Value                                                                                                                                                                                                                                                                                      |  |
|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| First field                               | Detector name, can be edited                                                                                                                                                                                                                                                               |  |
| Room                                      | Selecting the virtual room to which the device is<br>assigned                                                                                                                                                                                                                              |  |
| Alert with a siren if leakage is detected | sirens<br>If active,<br>added to the system are<br>activated if leakage is detected                                                                                                                                                                                                        |  |
| Jeweller Signal Strength Test             | Switches the detector to the signal strength<br>test mode                                                                                                                                                                                                                                  |  |
| Temporary Deactivation                    | Allows the user to disconnect the device<br>without removing it from the system.<br>Two options are available:<br>Entirely — the device will not execute<br>system commands or participate in<br>automation scenarios, and the system will<br>ignore device alarms and other notifications |  |
|                                           | Lid only — the system will ignore only<br>notifications about the triggering of the<br>device tamper button                                                                                                                                                                                |  |

|               | Learn more about temporary                                        |  |
|---------------|-------------------------------------------------------------------|--|
|               | deactivation of devices                                           |  |
|               |                                                                   |  |
| User Guide    | Opens the detector User Manual                                    |  |
| Delete Device | Disconnects the detector from the hub and<br>deletes its settings |  |

## Indication

The **LeaksProtect** LED indicator may light up red or green depending on the device status.

## Indication when pressing the power button

| Event                                                  | Indication                                          |
|--------------------------------------------------------|-----------------------------------------------------|
| Pressing the power button (detector is switched<br>on) | Lights up red while the button is held down         |
| Switching on                                           | Lights up green while the device is switching<br>on |
| Switching off                                          | Initially lights up red, then blinks three times    |

## **Turned-on detector indication**

| Event                                                                        | Indication                                                       | Note                                                                  |
|------------------------------------------------------------------------------|------------------------------------------------------------------|-----------------------------------------------------------------------|
| Detector connection to the<br>hub<br>ocBridge Plus<br>,<br>and<br>uartBridge | Lights up green for a few<br>seconds                             |                                                                       |
| Hardware error                                                               | Blinks red continuously                                          | The detector requires repair,<br>Support<br>please contact<br>Service |
| Leakage detected                                                             | Lights up red for about one<br>second                            |                                                                       |
| Battery needs replacing                                                      | During the alarm, it slowly lights<br>up red and slowly goes out | Replacement of the detector<br>battery is described in the            |

## Functionality Testing

Ajax security system allows conducting tests for checking the functionality of connected devices.

The tests do not start straight away but within a period of 36 seconds when using the standard settings. The test time start depends on the settings of the detector scanning period (the paragraph on "**Jeweller**" settings in the hub settings).

Jeweller Signal Strength Test

Attenuation Test

## Selecting the Location

When selecting the device location, please take into account its remoteness from the hub (up to 1300 meters) and the absence of any obstacles between the devices hindering the radio signal transmission: walls, floors, large objects located in the room.

![](_page_6_Picture_8.jpeg)

The device developed only for indoor use.

![](_page_6_Picture_10.jpeg)

Check the Jeweller signal strength level at the installation place.

If the signal level is low (one bar), we cannot guarantee the stable operation of the device. Take all possible measures to improve the signal strength. At least, move the device: even a 20 cm shift can significantly improve the quality of signal reception.

If after moving the device still has a low or unstable signal strength, use a . radio signal range extender

Install LeaksProtect in the place of potential leakage: on the floor under the bath, sink, washing machine, etc.

### **Do not install the detector:**

- outside the premises (outdoors);
- nearby any metal objects or mirrors causing attenuation and screening of the signal;
- within any premises with the temperature beyond the range of permissible limit;
- on conductive surfaces;
- closer than 1 m to the hub.

## Detector Testing

When the liquid gets on the detector contacts, it closes the electrical circuit. It is enough to close one contact pair to activate the alarm.

- **1.** To check LeaksProtect, close one contact pair with a wet finger for 3 seconds (the delay prevents false triggering). If water is detected, the detector LED will light up red for 1 second.
- **2.** Wipe the contacts with a dry napkin. When the electrical circuit is open, LeaksProtect switches on its LED red for 1 second and notifies that water dried out.

If you drown the detector with soapy water, it may continue signal flooding after getting dry. The issue is about the soapy film closes the contacts. To eliminate the problem, wipe the detector contacts with a napkin moistened with pure water and then dry them up.

## Maintenance

Check the LeaksProtect operational capability on a regular basis. We recommend cleaning the detector contacts as it gets dirty, at least, once every 2-3 months. Use an alcohol solution for cleaning the contacts.

Clean the detector body from dust, spider webs and other contaminants as they appear: they can conduct electricity and cause false actuation. Use a soft dry napkin suitable for equipment maintenance.

Do not use any substances containing alcohol, acetone, gasoline and other active solvents for cleaning the detector body.

The batteries installed in the detector ensure up to 5 years of autonomous operation on the average (with the inquiry frequency by the hub of 1 minutes). If the detector batteries are low, the security system sends the notification and the detector LED smoothly lights up and goes out green every hour, if the device is triggered.

To replace the batteries, turn off the detector, loosen the screws and remove the LeaksProtect front panel. Change the batteries with new ones type AAA, adhering to polarity.

### How long Ajax devices operate on batteries, and what affects this

#### Battery replacement

### Tech specs

| Radio communication protocol | Jeweller<br>Learn more                                                                                                                                        |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Radio frequency band         | 866.0 – 866.5 MHz<br>868.0 – 868.6 MHz<br>868.7 – 869.2 MHz<br>905.0 – 926.5 MHz<br>915.85 – 926.5 MHz<br>921.0 – 922.0 MHz<br>Depends on the region of sale. |
| Compatibility                | hubs<br>radio signal<br>Operates with all Ajax<br>,<br>range extenders<br>ocBridge Plus<br>,<br>,                                                             |

|                                    | uartBridge                             |
|------------------------------------|----------------------------------------|
| Maximum RF output power            | Up to 20 mW                            |
| Modulation of the radio signal     | GFSK                                   |
|                                    | Up to 1,300 m (any obstacles absent)   |
| Radio signal range                 | Learn more                             |
| Power supply                       | 2 × AAA batteries                      |
| Power supply voltage               | 3 V (batteries are installed in pairs) |
| Battery life                       | Up to 5 years                          |
| Dust and moisture protection class | IP65                                   |
| Installation method                | Indoors                                |
| Operating temperature range        | From 0°С to +50°С                      |
| Operating humidity                 | Up to 100%                             |
| Overall dimensions                 | 56 × 56 × 14 mm                        |
| Weight                             | 40 g                                   |
| Service life                       | 10 years                               |

### Compliance with standards

## **Complete Set**

- **1.** LeaksProtect
- **2.** Batteries AAA (pre-installed) 2 pcs
- **3.** Quick Start Guide

## Warranty

Warranty for the "AJAX SYSTEMS MANUFACTURING" LIMITED LIABILITY COMPANY products is valid for 2 years after the purchase and does not apply to the pre-installed battery.

If the device does not work correctly, you should first contact the support service — in half of the cases, technical issues can be solved remotely!

### The full text of the warranty

User Agreement

Technical support: support@ajax.systems