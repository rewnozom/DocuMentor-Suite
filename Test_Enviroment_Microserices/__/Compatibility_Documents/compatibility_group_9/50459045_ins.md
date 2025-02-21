# MotionProtect Outdoor User Manual

Updated December 8, 2021

![](_page_0_Picture_2.jpeg)

**MotionProtect Outdoor** is a wireless outdoor motion detector for the Ajax security system. The detector communicates with the hub via protected radio protocol at a distance up to 1,700 meters in the line of sight. MotionProtect Outdoor features protection against blocking the detector view (anti-masking system) and triggering by pets (pet immunity). The motion detection distance is adjustable: from 3 up to 15 meters. Jeweller

MotionProtect Outdoor can operate both on pre-installed batteries or use an external power supply. Depending on the detector settings, the batteries' life is up to 5 years.

> MotionProtect Outdoor does not support connection via the and integration modules. ocBridge Plus uartBridge

The user can configure the detector via the for iOS, Android, macOS, and Windows. The security system notifies users of all events through push notifications, SMS, and calls (if activated). Ajax app

The Ajax security system can be connected to a central monitoring station of a security company.

### Buy outdoor motion detector MotionProtect Outdoor

# Functional Elements

![](_page_1_Picture_3.jpeg)

- **1.** Main light indicator
- **2.** Upper light indicator and masking sensor
- **3.** Upper motion sensor lens
- **4.** Masking sensor
- **5.** Lower light indicator and masking sensor
- **6.** Lower motion sensor lens
- **7.** SmartBracket attachment panel (perforated part is required for actuating the tamper button in case of any attempt to dismantle the detector)
- **8.** The hole for attaching SmartBracket panel with a screw
- **9.** "On" button
- **10.** Tamper button
- **11.** QR Code
- **12.** Connector for external power supply cable outlet
- **13.** Scrollbar for adjusting the motion detection range

# Operating Principle

When the system is armed, the detector continuously receives signals from two PIR sensors. If both sensors detect identical motion, MotionProtect Outdoor instantly transmits an alarm signal to the hub and blinks with a green LED. MotionProtect Outdoor ignores animals, birds, insects, as well as swaying plants and trees.

> By a motion alarm, the security system also can activate sirens and notify a security company if connected.

![](_page_2_Figure_5.jpeg)

The detector recognizes motion and sends the first alarm immediately, but next alarms until disarming are transmitted no more than once in 5 seconds.

If a motion is detected before the system is armed, the detector will be armed not immediately, but during the next polling by the hub.

### Learn more about the algorithm of the detector operation

## Anti-masking system

**Masking** is an attempt to block in any way the view of the detector's lens.

MotionProtect Outdoor detects the following types of masking:

- An obstacle in front of both lenses (an object on the height of the detector and at a distance of up to 20 cm in front of it)
- An obstacle in front of any of the lenses (an object at a distance of up to 10 cm in front of one of the lenses)
- Painting or pasting any of the lenses with an opaque substance
- Pasting the detector front side with an opaque substance
- Applying an aerosol or painting the detector front side with paint

If one or more types of masking are detected, the detector generates a masking alarm and lights up a green LED for 1 second.

MotionProtect Outdoor detects masking regardless of the security state: armed or disarmed.

| Masking type                                    | Active mode (detector is armed) |                       | Passive mode (detector is disarmed) |                       |
|-------------------------------------------------|---------------------------------|-----------------------|-------------------------------------|-----------------------|
|                                                 | Time to alarm, s                | Time to restore,<br>s | Time to alarm, s                    | Time to restore,<br>s |
| An obstacle in<br>front of both<br>lenses       | 2                               | 8                     | 130                                 | 10                    |
| An obstacle in<br>front of any of<br>the lenses | 130                             | 18                    | 130                                 | 10                    |
| Pasting or<br>painting any of<br>the lenses     | 130                             | 18                    | 130                                 | 10                    |
| Pasting the<br>detector front<br>side           | 130                             | 18                    | 130                                 | 10                    |

### Response time to masking

| Applying aerosol<br>or painting the<br>detector front<br>side with paint | 130 | 18 | 130 | 10 |
|--------------------------------------------------------------------------|-----|----|-----|----|
|--------------------------------------------------------------------------|-----|----|-----|----|

# Connecting

# **Before starting connection:**

- **1.** Following the hub user guide, install the . Create the account, add the hub, and create at least one room. Ajax app
- **2.** Switch on the hub and check the internet connection (via Ethernet cable and/or GSM network).
- **3.** Make sure that the hub is disarmed and does not update by checking its status in the Ajax app.

Only users with administrator rights can add the device to the hub

## **How to connect the device to the hub:**

- **1.** Select the **Add Device** option in the Ajax application.
- **2.** Name the device, scan/write manually the **QR Code** (located on the body and packaging), and select the location room.

![](_page_5_Picture_0.jpeg)

- **3.** Select **Add**  the countdown will begin.
- **4.** Switch on the device by pressing the on/off button for 3 seconds.

![](_page_5_Picture_3.jpeg)

For the detection and interfacing to occur, the detector should be located within the coverage area of the wireless network of the hub (at a single protected object). Request for connection to the hub is transmitted for a short time at the time of switching on the device.

MotionProtect Outdoor turns off automatically after 6 seconds, if it failed to connect to the hub. To retry the connection, you do not need to switch off the device. If the detector has already been assigned to another hub, turn off MotionProtect Outdoor, and then follow the standard addition procedure.

If the connection to the hub failed, repeat the connection attempt after 30 seconds.

The device connected to the hub will appear in the list of devices of the hub in the app. The update of the detector statuses in the list depends on the device ping interval set in the hub settings (the default value is 36 seconds).

> To avoid masking alarms, switch off anti-masking in the device settings before the installation!

### States

**1.** Devices

- **2.** MotionProtect Outdoor

| Parameter                | Value                                                                                       |  |
|--------------------------|---------------------------------------------------------------------------------------------|--|
| Temperature              | Temperature of the Detector. Measured on the<br>processor and changes gradually             |  |
| Jeweller Signal Strength | Signal strength between the hub and the<br>detector                                         |  |
| Connection               | Connection status between the hub and the<br>detector                                       |  |
| Battery Charge           | Battery level of the device. Two states available:<br>ОК<br>Battery discharged              |  |
|                          | How battery charge is displayed in<br>Ajax apps                                             |  |
| Lid                      | The tamper mode of the detector, which reacts<br>to the detachment of or damage to the body |  |
| Delay When Entering, sec | Delay time when entering                                                                    |  |
| Delay When Leaving, sec  | Delay period after the security system is armed                                             |  |
| ReX                      | radio signal<br>Displays the status of using a                                              |  |

|                        | range extender                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| External Power         | Displays the status of using the external power<br>supply                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Sensitivity            | Sensitivity level of the motion detector: low,<br>normal, high                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Anti-masking           | Has the anti-masking option been enabled                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Always Active          | When turned on, the motion detector always<br>detects movement                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Temporary Deactivation | Shows the status of the device temporary<br>deactivation function:<br>No — the device operates normally and<br>transmits all events.<br>Lid only — the hub administrator has<br>disabled notifications about triggering on<br>the device body.<br>Entirely — the device is completely excluded<br>from the system operation by the hub<br>administrator. The device does not follow<br>system commands and does not report<br>alarms or other events.<br>By number of alarms — the device is<br>automatically disabled when the number of<br>alarms is exceeded (specified in the settings<br>for Devices Auto Deactivation). The feature<br>is configured in the Ajax PRO app. |
| Firmware               | Detector firmware version                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Device ID              | Device identifier                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

## Settings

**1.** Devices

**2.** MotionProtect Outdoor

**3.** Settings

| Setting | Value |
|---------|-------|
|         |       |

| First field                           | Detector name, can be edited                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |  |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| Room                                  | Selecting the virtual room to which the device is<br>assigned                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |
| Delay When Entering, sec              | Selecting delay time when entering                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |
| Delay When Leaving, sec               | Delay period after the security system is armed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  |
| Delays in Night Mode                  | When enabled, the detector will experience a<br>delay in the night mode                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |  |
| Arm in Night Mode                     | When turned on, the detector will switch to<br>armed mode when using night mode                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  |
| Alarm LED indication                  | Allows you to disable the flashing of the LED<br>indicator during an alarm. Available for devices<br>with firmware version 5.55.0.0 or higher<br>How to find the firmware version or<br>the ID of the detector or device?                                                                                                                                                                                                                                                                                                                                                                                                            |  |
|                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  |
| Sensitivity                           | Sensitivity level of the motion detector.<br>The choice depends on the type of object, the<br>presence of potential sources of false alarms,<br>and the protected area:<br>Low — there are likely sources of false<br>alarms in the protected area. For example,<br>tall bushes.<br>Medium (default value) — recommended<br>value, suitable for most objects. Do not<br>change it if the detector is working correctly.<br>High — there is no interference in the<br>protected area, the maximum detection<br>range and speed of alarm detection are<br>important. For example, if the detector is<br>installed in a narrow passage. |  |
| Anti-masking                          | If active, sensor will always detect masking                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |  |
| Always active                         | When turned on, the detector always registers<br>motion                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |  |
| Alert with a siren if motion detected | sirens<br>If active,<br>added to the system are<br>activated when the motion detected                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |  |
| Jeweller Signal Strength Test         | Switches the detector to the Jeweller signal<br>strength test mode                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |

| Detection Zone Test    | Switches the detector to the detection area test:                                                                                                                        |
|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                        | General motion detector test                                                                                                                                             |
|                        | Upper motion detector test                                                                                                                                               |
|                        | Lower motion detector test                                                                                                                                               |
|                        | Masking sensor test (if anti-masking<br>function is enabled)                                                                                                             |
| Attenuation Test       | Switches the detector to the signal fade test<br>mode (available in detectors with firmware<br>version 3.50 and later)                                                   |
|                        | Allows the user to disconnect the device<br>without removing it from the system.                                                                                         |
| Temporary Deactivation | Two options are available:                                                                                                                                               |
|                        | Entirely — the device will not execute<br>system commands or participate in<br>automation scenarios, and the system will<br>ignore device alarms and other notifications |
|                        | Lid only — the system will ignore only<br>notifications about the triggering of the<br>device tamper button                                                              |
|                        | Learn more about temporary                                                                                                                                               |
|                        | deactivation of devices                                                                                                                                                  |
|                        | The system can also automatically disable<br>devices when the set number of alarms is<br>exceeded.                                                                       |
|                        | Learn more about auto deactivation<br>of devices                                                                                                                         |
|                        |                                                                                                                                                                          |
| User Guide             | Opens the detector User Guide                                                                                                                                            |
| Unpair Device          | Disconnects the detector from the hub and<br>deletes its settings                                                                                                        |

## Indication

MotionProtect Outdoor light indicator may light up red or green depending on the device status.

### Indication When Pressing the "On" button

| Event                                                  | Indication                                       |
|--------------------------------------------------------|--------------------------------------------------|
| Pressing the power button (detector is switched<br>on) | Lights up red while the button is held down      |
| Switching on                                           | Lights up green while the device is switching on |
| Switching off                                          | Initially lights up red, then blinks three times |

# Turned-on detector indication

| Event                                                                 | Indication                                                            | Note                                                                                        |
|-----------------------------------------------------------------------|-----------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| Detector connection to the hub                                        | Lights up green for a few<br>seconds                                  |                                                                                             |
| Hardware error                                                        | Blinks red continuously                                               | The detector requires repair,<br>Support<br>please contact<br>Service                       |
| Motion- and masking-triggered<br>alarm or tamper button<br>triggering | Lights up green for about one<br>second                               |                                                                                             |
| Battery needs replacing                                               | During the alarm, it slowly<br>lights up green and slowly<br>goes out | Replacement of the detector<br>battery is described in the<br>Battery replacement<br>manual |

# Functionality Testing

The Ajax security system allows conducting tests for checking the functionality of connected devices.

The tests do not start immediately but within a period of 36 seconds when using default settings. The test time start depends on the settings of the detector ping interval (the "**Jeweller**" menu in the hub settings).

Jeweller Signal Strength Test

Detection Zone Test

#### Attenuation test

According to the requirements of EN50131, the level of the radio signal sent by wireless devices is reduced during the test mode.

## Choosing an installation place

Before installing the detector, conduct the Jeweller signal strength test.

Install MotionProtect Outdoor at the height of 0.8 – 1.3 m, ensuring the upper lens axis to be parallel to the ground, and the supposed intrusion path is perpendicular to the lens axis.

When choosing the installation place, consider the maximum device detection range. It depends on the sensitivity level and the position of the regulator for adjusting the motion detection range.

| Regulator position       | Sensitivity level   | Motion detection range |
|--------------------------|---------------------|------------------------|
| Top<br>(minimum range)   | Low / Middle / High | up to 3 meters         |
| Middle<br>(middle range) | Low                 | up to 7 meters         |
|                          | Middle / High       | up to 8 meters         |
| Low<br>(maximum range)   | Low / Middle / High | up to 15 meters        |

The detection range was tested at an ambient temperature of +23°C and clear weather. In other conditions, the detection range may vary. When choosing an installation place, use the to determine the sector in which the device detects movement as accurately as possible. Detection Zone Test

To avoid false alarms due to rain or snow falling on the masking sensors, install MotionProtect Outdoor under a covering. To protect masking sensors in the open area, use . Hood for MotionProtect Outdoor cover

MotionProtect Outdoor sends an alarm to the hub only if both PIR sensors detect identical motion. The difference in time of motion detection should not exceed 1.5 seconds.

Check the detector functioning at the alleged installation place. When choosing the location of MotionProtect Outdoor, take into account the radio signal communication range.

If the signal level is low (one bar), we cannot guarantee the stable operation of the detector. Take all possible measures to improve the quality of the signal. At least, move the detector: even a 20 cm shift can significantly improve the quality of signal reception.

If after moving the device still has a low or unstable signal strength, use a . radio signal range extender

Be careful when mounting the attachment panel. Excessive force during its mounting can lead to deformation of the panel and, consequently, to the inability to install the detector or to its unreliable fixation. Attach SmartBracket with the bundled fixing tools. Using any other tools, e.g., large diameter screws may damage the attachment panel. We do not recommend using double-sided adhesive tape for permanent mounting. The tape runs dry with time, which can cause falling, false triggering, and detector malfunction.

#### **Do not install the detector:**

- Without Hood for MotionProtect Outdoor in a place without a covering.
- Opposite the trees whose leaves can be in the detection zone of the upper and lower PIR sensors of the detector.
- Opposite the bushes higher than 80 cm.
- Near metal objects and mirrors (they can shield the radio signal and lead to its attenuation).
- Closer than 1 meter from the hub.

Note that MotionProtect Outdoor does not detect movement behind the glass. Therefore, do not install the detector in locations where glass objects can obstruct the detector's view. For example, in places where a glass door can obstruct the view of the device.

#### Why motion detectors react to animals and how to avoid it

![](_page_13_Picture_1.jpeg)

Install detector at a height 0.8 to 1.3 meters so that its upper lens looks parallel to the ground. If the site is uneven, the installation height is considered from the highest point of the territory controlled by the detector.

![](_page_13_Figure_3.jpeg)

### Detector installation procedure

- **1.** Fix the SmartBracket attachment panel on the surface temporarily using bundled screws or double-sided adhesive tape. Consider the installation height: 0.8 – 1.3 meters.
![](_page_14_Picture_0.jpeg)

- **2.** Select the motion detection distance (3 to 15 m) using the adjustment scroll bar.
![](_page_14_Figure_2.jpeg)

The lower PIR sensor beam direction with the specified minimum (1) and maximum (2) detection range

- **3.** Put MotionProtect Outdoor on the SmartBracket attachment panel. Leave the detection area (horizontal detection angle — 90°) and make sure that there are no moving objects within the detection area to calibrate antimasking sensors properly.
![](_page_15_Figure_2.jpeg)

Attention! The anti-masking sensors will begin to calibrate automatically when the detector has been put on the SmartBracket attachment panel. Calibration lasts up to 30 seconds and is followed by the flashing upper and lower LED indicators.

- **4.** Conduct the Detection Zone Test for upper and lower sensors separately, both sensors simultaneously, and anti-masking test in the . If the detector does not react to motion, select the appropriate sensitivity level, detection range, and check the detector slope angle. Ajax app
- **5.** If all tests have been appropriately passed, fix the SmartBracket to the surface with screws permanently, put MotionProtect Outdoor on the attachment panel, and wait until the end of calibration. Fix the detector on the attachment panel with the bundled screw.

![](_page_16_Picture_0.jpeg)

# Connecting External Power Supply

MotionProtect Outdoor can use external power supply 5-28 V DC, 200 mA. If the external power supply is connected, there is no need to remove the pre-installed batteries. Batteries provide the detector with the backup power source.

### **To connect the external power supply:**

- **1.** Disassemble the detector body: remove the screws and open the lid.
- **2.** Break off special caps on the SmartBracket attachment panel:

![](_page_16_Picture_6.jpeg)

1. A cap for putting out the power supply wire behind the SmartBracket attachment panel

2. A cap for putting out the power supply wire below the SmartBracket attachment panel

- **3.** Run the external power supply dead wire through the attachment panel and cap.
- **4.** Connect the cable to the terminal strips observing polarity. Fix the wire with the clamp.

![](_page_17_Picture_4.jpeg)

- 3. Terminal strips on the detector board
- 4. The clamp on the back of the detector body
- **5.** Switch on the power supply. The value of the **External Power Supply** field in the detector settings will change to **Connected**.

![](_page_17_Picture_8.jpeg)

Use grounded power supply source only!

- **6.** Fix the rear of the body with screws, install the detector and wait until the end of calibration.
### Maintenance

Check the operational capability of the detector regularly. Clean the detector body from dust, spider web, and other contaminants as they appear. Use soft dry napkin suitable for tech equipment.

Do not use any substances containing alcohol, acetone, gasoline, and other active solvents to clean the detector.

The pre-installed battery ensures up to 5 years of autonomous operation (with the 3 minutes ping interval by the hub). If the detector battery is low, the system notifies the user, and the LED indicator smoothly lights up and goes off if motion is detected or the tamper is triggered.

### How long Ajax devices operate on batteries, and what affects this

### Battery replacement

# Hood Installation

Hood for MotionProtect Outdoor is a cover protecting masking sensors of the detector from rain and snow. Install it when the detector cannot be placed under the covering.

Buy Hood for MotionProtect Outdoor

Hood for MotionProtect Outdoor can be mounted even on a detector that is already installed. You don't need to detach the device from the surface for installing the hood.

### **To install Hood for MotionProtect Outdoor:**

- **1.** Remove the protective film from the Dual Lock tape, which is glued to the inner surface of the hood.
- **2.** Attach the hood to the detector part of the tape will stick to the body of the detector.
- **3.** Detach the hood from the MotionProtect Outdoor and smooth out the part of the tape that remained on the detector body.
- **4.** Put the hood back so that both parts of the tape stuck, fixing the hood on the detector.

# Tech Specs

| Sensing element                     | PIR sensor, 2 pcs                                                                                                                         |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Detection angle, horizontal         | 90°                                                                                                                                       |
| Time for motion detection           | From 0.3 to 2 m/s                                                                                                                         |
| Motion detection distance           | Adjustable, 3–15 m when the detector is<br>installed at 1 m height                                                                        |
| Protection against masking          | Yes                                                                                                                                       |
| Pet ignoring function               | Yes, height up to 80 cm when the detector is<br>installed at 1 m height<br>Why motion detectors react to<br>animals and how to avoid it > |
| Protection against false triggering | Yes, algorithmic analysis                                                                                                                 |
| Radio communication protocol        | Jeweller<br>Learn more                                                                                                                    |
| Radio frequency band                | 866.0 – 866.5 MHz<br>868.0 – 868.6 MHz<br>868.7 – 869.2 MHz                                                                               |
|                                     | 905.0 – 926.5 MHz<br>915.85 – 926.5 MHz<br>921.0 – 922.0 MHz<br>Depends on the region of sale.                                            |
| Compatibility                       | hubs<br>radio<br>Operates only with all Ajax<br>, and<br>signal range extenders                                                           |
| Maximum radio signal power          | Up to 20 mW                                                                                                                               |
| Radio signal modulation             | GFSK                                                                                                                                      |

|                             | Learn more                     |  |
|-----------------------------|--------------------------------|--|
|                             |                                |  |
| Power supply                | 2 × CR123A, 3 V                |  |
| Battery life                | Up to 5 years                  |  |
| External power              | 5 – 28 V DC, 200 mA            |  |
| Body protection level       | IP55                           |  |
| Anti-tamper switch          | Yes                            |  |
| Installation method         | Outdoors/indoors               |  |
| Operating temperature range | From -25°С to +60°С            |  |
| Operating humidity          | Up to 95%                      |  |
| Accessories                 | Hood for MotionProtect Outdoor |  |
| Overall dimensions          | 183 × 70 × 65 mm               |  |
| Weight                      | 322 g                          |  |
| Service life                | 10 years                       |  |

### Compliance with standards

# Complete set

- **1.** MotionProtect Outdoor
- **2.** SmartBracket mounting panel
- **3.** CR123A battery 2 pcs. (pre-installed)
- **4.** Installation kit
- **5.** Quick Start Guide

### Warranty

Warranty for the "AJAX SYSTEMS MANUFACTURING" LIMITED LIABILITY COMPANY products is valid for 2 years after the purchase and does not apply to the pre-installed battery.

If the device does not work correctly, you should first contact the support service—in half of the cases, technical issues can be solved remotely!

### The full text of the warranty

User Agreement

Technical support: support@ajax.systems