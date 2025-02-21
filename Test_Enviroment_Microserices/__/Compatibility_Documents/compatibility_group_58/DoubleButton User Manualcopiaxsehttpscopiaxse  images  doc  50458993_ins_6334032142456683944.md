# DoubleButton User Manual

Updated December 9, 2021

![](_page_0_Picture_2.jpeg)

**DoubleButton** is a wireless hold-up device with advanced protection against accidental presses. The device communicates with a hub via the encrypted radio protocol and compatible only with Ajax security systems. The line-of-sight communication range is up to 1300 meters. DoubleButton operates from the pre-installed battery up to 5 years. Jeweller

DoubleButton is connected and configured via on iOS, Android, macOS, and Windows. Push notifications, SMS, and calls can notify about alarms and events. Ajax apps

Buy the DoubleButton hold-up device

### Functional elements

![](_page_1_Figure_0.jpeg)

- **1.** Alarm activation buttons
- **2.** LED indicators / plastic protective divider
- **3.** Mounting hole

# Operating principle

**DoubleButton** is a wireless hold-up device, featuring two tight buttons and a plastic divider to protect against accidental presses. When pressed, it raises an alarm (hold-up event), transmitted to users and to the security company's monitoring station.

An alarm can be raised by pressing both buttons: one-time short or long press (more than 2 seconds). If only one of the buttons is pressed, the alarm signal is not transmitted.

![](_page_2_Picture_0.jpeg)

All DoubleButton alarms are recorded in the feed. The short and long presses have different icons, but the event code sent to the monitoring station, SMS, and push notifications do not depend on the pressing manner. Ajax app's notification

DoubleButton can only operate as a hold-up device. Setting the type of alarm is not supported. Keep in mind that the device is active 24/7, so pressing the DoubleButton will raise an alarm regardless of the security mode.

![](_page_2_Picture_3.jpeg)

# Event transmission to the monitoring station

The Ajax security system can connect to the CMS and transmit alarms to the monitoring station in and protocol formats. Sur-Gard (ContactID) SIA DC-09

## Connection

![](_page_2_Picture_7.jpeg)

The device is not compatible with , , and third party security control panels. ocBridge Plus uartBridge

### Before starting connection

- **1.** Install the . Create an . Add a hub to the app and create at least one room. Ajax app account
- **2.** Check if your hub is on and connected to the Internet (via Ethernet cable, Wi-Fi, and/or mobile network). You can do this in the Ajax app or by looking at the Ajax logo on the front panel of the hub. The logo should light with white or green if the hub is connected to the network.
- **3.** Check if the hub is not armed and does not update by reviewing its status in the app.

![](_page_3_Picture_4.jpeg)

Only users with administrator permissions can connect a device to a hub.

## How to connect DoubleButton to a hub

- **1.** Open the Ajax app. If your account has access to several hubs, select the hub to which you want to connect the device.
- **2.** Go to the **Devices** tab and click **Add device**.
- **3.** Name the device, scan or enter the **QR code** (located on the package), select a room and a group (if group mode is enabled).
- **4.** Click **Add** the countdown will begin.
- **5.** Hold any of two buttons for 7 seconds. After adding DoubleButton, its LED will flash green once. DoubleButton will appear in the list of hub devices in the app.

To connect DoubleButton to a hub, it should be located on the same protected object as the system (within the hub's radio network range). If the connection fails, try again in 5 seconds.

DoubleButton can be connected to one hub only. When connected to a new hub, the device stops sending commands to the old hub. Added to a new hub,

DoubleButton is not removed from the device list of the old hub. This must be done manually in the Ajax app.

![](_page_4_Picture_1.jpeg)

Updating the device statuses in the list occurs only when DoubleButton is pressed and does not depend on the Jeweller settings.

### States

The states screen contains information about the device and its current parameters. Find the DoubleButton states in the Ajax app:

- **1.** Go to the **Devices** tab .
- **2.** Select DoubleButton from the list.

| Parameter                       | Value                                                                                                                                            |
|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Battery Charge                  | Battery level of the device. Two states available:<br>ОК<br>Battery discharged<br>How battery charge is displayed in<br>Ajax apps                |
| LED Brightness                  | Indicates the LED brightness level:<br>Off — no indication<br>Low<br>Max                                                                         |
| Works via *range extender name* | radio signal<br>Displays the status of using a<br>range extender<br>The field is not displayed if the device<br>communicates directly with a hub |
| Temporary Deactivation          | Indicates the status of the device:                                                                                                              |

|          | Active<br>Temporarily deactivated |  |
|----------|-----------------------------------|--|
|          |                                   |  |
|          | Learn more                        |  |
| Firmware | DoubleButton firmware version     |  |
| ID       | Device ID                         |  |

### Setting up

DoubleButton is set up in the Ajax app:

- **1.** Go to the **Devices** tab .
- **2.** Select DoubleButton from the list.
- **3.** Go to **Settings** by clicking on the icon.

![](_page_5_Picture_6.jpeg)

Please note that after changing the settings, you need to press **Back** to apply them.

| Parameter      | Value                                                                                                                                                                                       |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| First field    | Device name. Displayed in the list of all hub<br>devices, SMS, and notifications in the event<br>feed.<br>The name can contain up to 12 Cyrillic<br>characters or up to 24 Latin characters |
| Room           | Selecting the virtual room to which<br>DoubleButton is assigned. The name of the<br>room is displayed in SMS and notifications in<br>the event feed                                         |
| LED brightness | Adjusting LED brightness:                                                                                                                                                                   |
|                | Off — no indication                                                                                                                                                                         |
|                | Low                                                                                                                                                                                         |
|                | Max                                                                                                                                                                                         |

| Alert with a siren if button is pressed | sirens<br>When enabled, the<br>connected to your<br>security system signal about the button<br>pressing                                                                                 |
|-----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| User Guide                              | Opens the DoubleButton user manual                                                                                                                                                      |
| Temporary Deactivation                  | Allows the user to disable the device without<br>removing it from the system. A temporarily<br>deactivated device will not raise an alarm when<br>pressed<br>Learn more about temporary |
|                                         | deactivation of devices                                                                                                                                                                 |
| Unpair Device                           | Disconnects DoubleButton from a hub and<br>removes its settings                                                                                                                         |

# Alarms

A DoubleButton alarm generates an event notification sent to the security company's monitoring station and system users. The pressing maner is indicated in the event feed of the app: for a short press, a single-arrow icon appears, and for a long press, the icon has two arrows.

![](_page_6_Figure_3.jpeg)

To reduce the probability of false alarms, a security company can enable the feature. alarm confirmation

Note that the alarm confirmation is a separate event that does not cancel the alarm transmission. Whether or not the feature is enabled, DoubleButton alarms are sent to a CMS and to security system users.

### Indication

![](_page_7_Picture_2.jpeg)

DoubleButton blinks red and green to indicate command execution and battery charge status.

| Category                       | Indication                                                            | Event                                                                                                                                                     |
|--------------------------------|-----------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Pairing with a security system | The whole frame blinks green<br>6 times                               | The button is not connected to<br>a security system                                                                                                       |
|                                | The whole frame lights up<br>green for a few seconds                  | Connecting the device to a<br>security system                                                                                                             |
| Command delivery indication    | The frame part above the<br>pressed button lights up green<br>briefly | One of the buttons is pressed<br>and the command is delivered<br>to a hub.<br>When only one button is<br>pressed, DoubleButton does<br>not raise an alarm |
|                                | The entire frame lights up<br>green briefly after press               | Both buttons are pressed and<br>the command is delivered to a<br>hub                                                                                      |
|                                | The entire frame lights up red<br>briefly after press                 | One or both buttons were<br>pressed and the command                                                                                                       |

|                                                                     |                                                                                                  | was not delivered to a hub                                                                 |
|---------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| Response Indication<br>(follows the Command<br>Delivery Indication) | The whole frame lights up<br>green for half a second after<br>the command delivery<br>indication | A hub received DoubleButton<br>command and raised an alarm                                 |
|                                                                     | The whole frame lights up red<br>for half a second after the<br>command delivery indication      | A hub received DoubleButton<br>command but did not raise an<br>alarm                       |
| Battery status indication<br>(follows Feedback Indication)          | After the main indication, the<br>entire frame lights up red and<br>gradually goes out           | The battery replacement is<br>required. DoubleButton<br>commands are delivered to a<br>hub |

# Application

DoubleButton can be fixed on a surface or carried around.

![](_page_8_Picture_3.jpeg)

### How to fix DoubleButton on a surface

To fix the device on a surface (e. g. under a table), use Holder.

#### **To install the device in the holder:**

- **1.** Choose a location to install the holder.
- **2.** Press the button to test whether the commands are delivered to a hub. If not, choose another location or use a radio signal range extender.

![](_page_9_Picture_0.jpeg)

When routing DoubleButton through a radio signal range extender, keep in mind that it does not automatically switch between a range extender and a hub. You can assign DoubleButton to a hub or another range extender in the Ajax app.

- **3.** Fix Holder on the surface using the bundled screws or double-sided adhesive tape.
![](_page_9_Picture_3.jpeg)

- **4.** Put DoubleButton into the holder.
![](_page_9_Picture_5.jpeg)

![](_page_9_Picture_6.jpeg)

Please note that Holder is sold separately.

![](_page_9_Picture_8.jpeg)

### How to carry DoubleButton

The button is easy to carry around thanks to a special hole on its body. It can be worn on the wrist or neck, or be hanged on a keyring.

DoubleButton has an IP55 protection index. Which means that the device body is protected from dust and splashes. And a special protective divider, tight buttons, and the need to press two buttons at once eliminate false alarms.

![](_page_10_Picture_3.jpeg)

# Using DoubleButton with alarm confirmation enabled

**Alarm confirmation** is a separate event that a hub generates and transmits to a CMS if the hold-up device has been activated by different types of pressing (short and long) or two specified DoubleButtons have transmitted alarms within a specified time. By responding to confirmed alarms only, a security company and police reduce the risk of unnecessary reacting.

Note that the alarm confirmation feature does not disable the alarm transmission. Whether or not the feature is enabled, DoubleButton alarms are sent to a CMS and to security system users.

How to configure confirmation of a hold-up device

### How to confirm alarm with one DoubleButton

To raise a confirmed alarm (hold-up event) with the same device, you need to perform any of these to actions:

- **1.** Hold both buttons simultaneously for 2 seconds, release, and then press both buttons again briefly.
- **2.** Simultaneously press both buttons briefly, release, and then hold both buttons for 2 seconds.

![](_page_11_Picture_2.jpeg)

## How to confirm alarm with several DoubleButtons

To raise a confirmed alarm (hold-up event), you can activate one hold-up device twice (according to the algorithm described above) or activate at least two different DoubleButtons. In this case, it doesn't matter in what way two different DoubleButtons were activated — with a short or long pressing.

![](_page_11_Picture_5.jpeg)

### Maintenance

When cleaning the device body, use products suitable for technical maintenance. Do not use substances containing alcohol, acetone, gasoline, or other active solvents to clean DoubleButton.

The pre-installed battery provides up to 5 years of operation, considering one pressing per day. More frequent use may decrease battery life. You can check the battery status at any time in the Ajax app.

![](_page_12_Picture_3.jpeg)

#### How long Ajax devices operate on batteries, and what affects this

If DoubleButton cools down up to -10°C and below, the battery charge indicator in the app can show low battery status until the button heats up to above-zero temperatures. Note that the battery charge level is not updated in the background, but only by pressing DoubleButton.

When the battery charge is low, users and a security company monitoring station receive notification. The device LED smoothly lights up red and goes out after each button pressing.

#### How to replace the battery in DoubleButton

### Technical Specifications

| Number of buttons                   | 2                                                                                  |
|-------------------------------------|------------------------------------------------------------------------------------|
| LED indicating command delivery     | Available                                                                          |
| Protection against accidental press | To raise an alarm, press 2 buttons<br>simultaneously<br>Protective plastic divider |
| Radio communication protocol        | Jeweller                                                                           |

|                             | Learn more                                                                                                                                                    |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Radio frequency band        | 866.0 – 866.5 MHz<br>868.0 – 868.6 MHz<br>868.7 – 869.2 MHz<br>905.0 – 926.5 MHz<br>915.85 – 926.5 MHz<br>921.0 – 922.0 MHz<br>Depends on the region of sale. |
| Compatibility               | Ajax hubs<br>radio<br>Operates only with<br>and<br>signal range extenders<br>on OS Malevich<br>2.10 and higher                                                |
| Maximum radio signal power  | Up to 20 mW                                                                                                                                                   |
| Radio signal modulation     | GFSK                                                                                                                                                          |
| Radio signal range          | Up to 1,300 m (line-of-sight)                                                                                                                                 |
| Power supply                | 1 CR2032 battery, 3 V                                                                                                                                         |
| Battery life                | Up to 5 years (depending on the frequency of<br>use)                                                                                                          |
| Protection class            | IP55                                                                                                                                                          |
| Operating temperature range | From −10°С to +40°С                                                                                                                                           |
| Operating humidity          | Up to 75%                                                                                                                                                     |
| Dimensions                  | 47 × 35 × 16 mm                                                                                                                                               |
| Weight                      | 17 g                                                                                                                                                          |
| Service life                | 10 years                                                                                                                                                      |

#### Compliance with standards

### Complete set

- **1.** DoubleButton
- **2.** CR2032 battery (pre-installed)
- **3.** Quick Start Guide

### Warranty

The warranty for the AJAX SYSTEMS MANUFACTURING Limited Liability Company products is valid for 2 years after purchase and does not extend to the bundled battery.

If the device does not function properly, we recommend that you first contact the support service as technical issues can be resolved remotely in half of the cases!

Warranty obligations

User agreement

Technical support: support@ajax.systems