## LifeQuality Jeweller User manual

Updated January 12, 2023

![](_page_0_Figure_2.jpeg)

**LifeQuality Jeweller** is a wireless air quality detector. Measures temperature, humidity, and CO (carbon dioxide) concentration in the room. Reports air pollution using an LED indicator and notifications in Ajax apps. 2

A hub is required for the detector to operate. The list of compatible hubs and range extenders is . available here

LifeQuality operates as part of the Ajax security system, communicating with the hub over two secure radio protocols: and : the detector uses Jeweller to transmit measurements, while Wings transmits data backups. The hub communication range is up to 1,700 meters without obstacles. Jeweller Wings

Buy LifeQuality Jeweller

## Functional elements

![](_page_1_Picture_0.jpeg)

- **1.** LED indicator with a touch button. Reports the air quality and other detector events.
- **2.** SmartBracket mounting panel. To remove the panel, turn it counterclockwise.
- **3.** Power button.
- **4.** Device QR code and ID (serial number). It is used to connect the device to Ajax security system.

## Operating principle

![](_page_1_Figure_6.jpeg)

**LifeQuality Jeweller** is a wireless air quality detector. The detector monitors the temperature, humidity, and CO (carbon dioxide) concentration, measuring them once a minute. 2

LifeQuality measurements are available in Ajax apps in the **Devices** tab. A can set up comfort thresholds PRO or a user with system configuration rights

of temperature, humidity, and CO (carbon dioxide). When values go beyond the specified limits, hub users receive notifications pointing out which indicator is outside the norm. This allows you to create an optimal microclimate in the room, reacting in time to the detector measurements. 2

 respond to changes in LifeQuality indicators and perform user-defined actions using . For example, turns on the heating system when the specified minimum temperature is reached. Using LifeQuality with Ajax automation devices, supply systems, humidifiers, and air conditioning, it's easy to maintain a comfortable microclimate inside. Ajax automation devices automation scenarios WallSwitch

## Temperature and humidity sensor

Temperature and humidity are measured using a built-in combined SHT40 detector with digital sensors from the Swiss manufacturer Sensirion. The detector is installed in an isolated part of the main board. This excludes the influence of other board components and ensures measurement accuracy: the temperature measurement accuracy is ±0.2°C, and humidity is ±1.8%.

LifeQuality provides more accurate temperature measurements than other Ajax devices. Therefore, if the system includes LifeQuality, the **Rooms** tab in Ajax apps displays only the temperature measured by LifeQuality. The temperature measurements of other devices are ignored. Microclimate measurements will only consider data from other LifeQuality devices added to the room.

#### CO sensor 2

CO concentration is measured using a built-in Sunrise non-dispersive infrared (NDIR) detector from the Swedish manufacturer Senseair. This detector type is protected from measurement errors that may occur due to aerosols, perfumes or vapour of other substances. 2

The operating principle of the detector is based on detecting changes in the intensity of infrared radiation. Air naturally enters the detector chamber, through which the infrared lamp transmits radiation. The chamber walls allow the infrared beam to reflect and migrate to the infrared sensor, which absorbs radiation. With a special coating technology inside the chamber, the measurement accuracy is ± (30 + 3%) ppm.

In the migration process through the chamber, the radiation intensity changes due to the absorption of radiation part by carbon dioxide molecules. When the radiation reaches the endpoint and absorbs by the infrared sensor, the detector accurately detects CO concentration in the air. 2

## Data storage

![](_page_3_Figure_2.jpeg)

The detector measures temperature, humidity level and CO concentration once every minute. In Ajax apps, users can view current LifeQuality measurements and their history. The history of measurements is presented by charts. Charts show the trend of the selected air quality value over the last hour, day, week, month, or year. Ajax security system stores this data on the Ajax Cloud server for up to 2 years. 2

LifeQuality also has built-in memory that allows the detector to store measurements for up to 72 hours if communication with the hub or radio signal range extender is lost. As soon as the connection is restored, all values are sent to Ajax apps and synchronized with the charts.

## How to view charts

## Calibration

LifeQuality features automatic calibration of the CO sensor. This feature allows the sensor continuously transmit the most accurate measurements of the carbon dioxide concentration in the room. At the same time, the temperature and humidity sensor is calibrated at the production stage and does not require additional calibration. 2

The built-in CO sensor is calibrated every 1–14 days without user or installer interaction. LifeQuality automatically selects a calibration period based on the air conditions in the room. If the detector is used in an unventilated space, it should be manually calibrated every two to three weeks. You can run the calibration manually in Ajax apps. 2

- How to run the CO2 sensor calibration manually
## Jeweller and Wings data transfer protocols

**Jeweller** and **Wings** are two-way wireless protocols for fast and reliable twosided connection between the hub and connected devices. Jeweller technology is used to transmit events and measured values. If connection is lost, Wings allows you to send data backups from the detector to the hub when connection is restored.

The protocols support floating key block encryption and device recognition on every session to prevent sabotage and spoofing.

To monitor connection with system devices and display their statuses Ajax apps have a system of hub–detector polls with a frequency of 12 to 300 seconds. The polling frequency is set by a in the hub settings. PRO or a user with system setup rights

- Learn more about Jeweller
- Learn more about Wings

## Sending events to the monitoring station

The Ajax security system can transmit events and alarms to the monitoring app as well as the Central Monitoring Station (CMS) via **SurGard (Contact ID), SIA DC-09 (ADM-CID), ADEMCO 685**, and other protocols. The list of supported protocols is . PRO Desktop available here

![](_page_4_Picture_10.jpeg)

Which CMSs Ajax connects to

Only communication loss events between LifeQuality and the hub (or the radio signal range extender) are transmitted to the CMS. Use PRO Desktop to receive all smart air quality detector events.

Addressability of Ajax devices allows you to send not only events but also the type of the device, the name, virtual room, and security group assigned to it to the PRO Desktop and to the CMS. The list of transmitted parameters may differ depending on the type of the CMS and the selected communication protocol.

![](_page_5_Picture_2.jpeg)

## Adding to the system

## Before adding a device

- **1.** Install the Ajax app.
- **2.** Create an account if you don't have one.
- **3.** Add a to your app. Set the necessary settings and create at least one . hub compatible with the detector virtual room
- **4.** Make sure that the hub is turned on and has Internet access via Ethernet, Wi-Fi, and/or mobile network. You can do this in the Ajax app or by looking at the hub LED indicator: it lights up white or green.
- **5.** Make sure that the hub is disarmed and does not start updating by checking the status in the Ajax app.

![](_page_5_Picture_10.jpeg)

LifeQuality should be within the coverage area of the hub radio network. To operate via a , connect LifeQuality to the hub first. Then connect the detector to the range extender in its settings. radio signal range extender

## How to add LifeQuality Jeweller to the hub

- **1.** Open the Ajax app.
- **2.** Select the hub if you have several of them or if you are using the PRO app.
- **3.** Go to the **Devices** tab. Click **Add Device**.
- **4.** Specify the name of the device.
- **5.** Scan the QR code or enter the ID manually. QR code is located on the enclosure and on the device packaging. The ID can be found under the QR code.
- **6.** Select a virtual room and security group (if group mode is enabled).
- **7.** Click **Add**.

![](_page_6_Picture_8.jpeg)

- **8.** Turn on LifeQuality by holding the power button for 3 seconds. The hub connection request is sent only if the detector is enabled. If the detector fails to connect to the hub, try again in 5 seconds.
The detector cannot connect to the hub if they operate on different radio frequencies. The radio frequency range of the device may vary by region. Please contact for information on the operating frequency range of your devices. technical support

Once connected, LifeQuality will appear in the device list in the Ajax app. Device status update depends on the polling interval set in the **Jeweller** or **Jeweller/Fibra** settings. The default value is 36 seconds.

LifeQuality operates with one hub only. When connected to a new hub, the detector stops transmitting data to the old hub. Once added to a new hub, LifeQuality is not removed from the list of devices of the old hub. This must be done manually in Ajax apps.

## Indication

![](_page_7_Picture_1.jpeg)

LifeQuality LED indication can report detector's status as well as air quality with a backlight.

| LED indication                           | Event                           | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------------------------------|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Lights up slowly and<br>goes out slowly. | Air pollution level<br>display. | Lights up after touching a detector's logo<br>button.<br>The color of indication depends on the CO<br>2<br>(carbon dioxide) concentration in the air:<br>Green — 0–999 ppm (normal air).<br>Yellow — 1000–1399 ppm (slightly polluted<br>air).<br>Red — 1400–1999 ppm (polluted air).<br>Purple — 2000 ppm or more (extremely<br>polluted air).<br>The detector does not respond to touches on<br>the touch button when the batteries are<br>discharged. |
| Blinks once every 5<br>seconds.          | Polluted air.                   | The color of indication depends on the CO<br>2<br>(carbon dioxide) concentration in the air:<br>Yellow — 1000–1399 ppm (slightly polluted<br>air).                                                                                                                                                                                                                                                                                                       |

|                                                                                                          |                                                              | Red — 1400–1999 ppm (polluted air).                                                                                             |
|----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                          |                                                              | Purple — more than 2000 ppm (extremely<br>polluted air).                                                                        |
|                                                                                                          |                                                              | The sensor logo briefly lights up if the Flash at<br>high CO level option is enabled in the settings.<br>2                      |
| Lights up green for 1<br>second.                                                                         | Turning the detector<br>on.                                  |                                                                                                                                 |
| Lights up red, then<br>blinks three times.                                                               | Turning the detector<br>off.                                 |                                                                                                                                 |
| Lights up red.                                                                                           | Pressing the power<br>button when the<br>detector is on.     | Appears only while the power button is pressed.<br>If the button is pressed for more than 2<br>seconds, the detector turns off. |
| Blinks red six times<br>then blinks three more<br>times but quicker.                                     | The detector has been<br>removed from the<br>hub.            | Lights up when the detector receives<br>information that it has been removed from the<br>hub.                                   |
| Lights up green for 1<br>second. Blinks red six<br>times then blinks<br>three more times but<br>quicker. | Turning on a detector<br>not added to the hub.               |                                                                                                                                 |
| Lights up red slowly<br>three times.                                                                     | Battery is low.                                              | Lights up after touching a detector's logo<br>button.                                                                           |
| Slowly lights up blue<br>with an interval of 6<br>seconds.                                               | Calibration of the CO<br>2<br>(carbon dioxide)<br>sensor.    | Calibration takes up to 2 minutes.                                                                                              |
| Lights up red for<br>about half a second.                                                                | Accelerometer is<br>triggered, the detector<br>is displaced. |                                                                                                                                 |

## Functionality testing

Ajax security system provides several tests for choosing the right installation place for the devices. **Jeweller** and **Wings signal strength tests** are available for LifeQuality. Tests determine the strength and stability of the signal at the intended location of the device.

#### **To run a test in the Ajax app:**

- **1.** Select the hub if you have several of them or if you are using the PRO app.
- **2.** Go to the **Devices** tab.
- **3.** Select **LifeQuality**.
- **4.** Go to the settings by clicking on the gear icon .
- **5.** Select the test.
- **6.** Perform the test following the tips in the app.

Tests do not start immediately, but not later than over a single hub–device ping interval (36 seconds by default). You can change the device ping interval in the **Jeweller** (or **Jeweller/Fibra**) menu in the hub settings.

## Icons

Icons show some of the LifeQuality states as well as measured air quality indicators. You can view them in Ajax apps in the **Devices**  tab.

## State icons

| Icon | Value                                                                                                                                      |
|------|--------------------------------------------------------------------------------------------------------------------------------------------|
|      | Jeweller signal strength between LifeQuality and the hub (or range extender).<br>The recommended value is two or three bars.<br>Learn more |
|      | LifeQuality battery charge level.<br>Learn more                                                                                            |
|      | Malfunction detected. The list of malfunctions is available in device states.                                                              |
|      | radio signal range extender<br>LifeQuality operates through the                                                                            |
|      | LifeQuality is temporarily disabled.                                                                                                       |
|      | Learn more                                                                                                                                 |

## Air quality indicators icons

| Air temperature in the room where LifeQuality is installed. Measured in Celsius<br>or Fahrenheit depending on the app settings.<br>In the normal state, the text is colored black. The text changes color to yellow<br>when the temperature is outside the comfort limits set in the settings.                                                                                                                              |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Humidity level in the room where LifeQuality is installed. Measured in<br>percentages.<br>In the normal state, the text is colored black. The text changes color to yellow<br>when the humidity is outside the comfort limits set in the settings.                                                                                                                                                                          |
| Level of CO (carbon dioxide) concentration in the room where LifeQuality is<br>2<br>installed. Measured in ppm (parts per million).<br>The color of the text depends on the concentration:<br>Up to 350 ppm — gray (excellent air).<br>350–999 ppm — black (normal air).<br>1000–1399 ppm — yellow (slightly polluted air).<br>1400–1999 ppm — red (polluted air).<br>More than 2000 ppm — purple (extremely polluted air). |

## States

The states include information about the device and its operating parameters. You can see LifeQuality states in Ajax apps. To access them:

- **1.** Open the Ajax app.
- **2.** Select the hub if you have several of them or if you are using the PRO app.
- **3.** Go to the **Devices** tab.
- **4.** Select LifeQuality from the list.

| Parameter     | Value                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Malfunction   | Clicking the<br>opens the list of detector<br>malfunctions.<br>The field is displayed only if a malfunction is<br>detected.                                                                                                                                                                                                                                                                                                             |
| Temperature   | Air temperature in the room where LifeQuality is<br>installed. Measured in Celsius or Fahrenheit<br>depending on the app settings.<br>In the normal state, the text is colored black.<br>The text changes color to yellow when the<br>temperature is outside the specified limits.                                                                                                                                                      |
| Humidity      | Humidity level in the room where LifeQuality is<br>installed. Measured in percentages.<br>In the normal state, the text is colored black.<br>The text changes color to yellow when the<br>humidity is outside the specified limits.                                                                                                                                                                                                     |
| CO level<br>2 | Level of CO (carbon dioxide) concentration in<br>2<br>the room where LifeQuality is installed.<br>Measured in ppm (parts per million).<br>The color of the text depends on the<br>concentration:<br>Up to 350 ppm — gray (excellent air).<br>350–999 ppm — black (normal air).<br>1000–1399 ppm — yellow (slightly polluted<br>air).<br>1400–1999 ppm — red (polluted air).<br>More than 2000 ppm — purple (extremely<br>polluted air). |

| Jeweller Signal Strength | Signal strength between LifeQuality and the hub<br>or radio signal range extender via Jeweller. The<br>recommended value is two or three bars.<br>Jeweller is a protocol for transmitting<br>LifeQuality events and alarms.                                                                                           |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Connection via Jeweller  | Connection status between LifeQuality and the<br>hub or range extender via Jeweller:<br>Online — the detector is connected to the<br>hub or range extender. Normal state.<br>Offl<br>ine — no connection between the<br>detector and hub (or range extender). Check<br>the detector connection.                       |
| Wings Signal Strength    | Signal strength between LifeQuality and the hub<br>or the range extender via the Wings channel.<br>The recommended value is two or three bars.<br>Wings is a protocol for transmitting LifeQuality<br>backup data.                                                                                                    |
| Connection via Wings     | Connection status between LifeQuality and the<br>hub or the range extender via Wings:<br>Online — the detector is connected to the<br>hub or the range extender. Normal state.<br>Offl<br>ine — no connection between the<br>detector and the hub or the range extender.<br>Check the detector connection.            |
| Battery Сharge           | The battery charge level of the device:<br>OK — batteries have sufficient charge.<br>Normal state.<br>Battery low — batteries are discharged. We<br>recommend replacing the batteries with new<br>ones.<br>When the charge level is low, the Ajax apps and<br>the security company receive a related<br>notification. |

|                                         | After receiving the low battery notification, the<br>detector can operate for several months more<br>under normal conditions. However, we<br>recommend replacing the batteries immediately<br>upon notification.<br>How the battery charge is displayed<br>Battery life calculator |
|-----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                         | Alarm status when the accelerometer is<br>triggered:<br>Yes — alarm when the accelerometer is                                                                                                                                                                                      |
| Alert if moved                          | triggered is enabled.<br>No — alarm when the accelerometer is<br>triggered is disabled.                                                                                                                                                                                            |
|                                         | The alarm is triggered if the enclosure is rotated<br>or removed from the SmartBracket mounting<br>panel.                                                                                                                                                                          |
| Name of the radio signal range extender | Displayed when the device is operating via a<br>radio signal range extender                                                                                                                                                                                                        |
|                                         | Shows the status of the device temporary<br>deactivation function:                                                                                                                                                                                                                 |
|                                         | No — the device operates in normal mode.                                                                                                                                                                                                                                           |
| Temporary Deactivation                  | Entirely — the device does not execute<br>system commands and does not participate<br>in scenarios.                                                                                                                                                                                |
|                                         | Learn more                                                                                                                                                                                                                                                                         |
| Firmware                                | LifeQuality firmware version.                                                                                                                                                                                                                                                      |
| Device ID                               | LifeQuality ID (serial number). It is also located<br>on the enclosure under the QR code and the<br>device packaging.                                                                                                                                                              |
| Device No.                              | LifeQuality loop (zone) number. Events are sent<br>to the monitoring station with this number.                                                                                                                                                                                     |

## Settings

To change LifeQuality settings in the Ajax app:

- **1.** Open the Ajax app.
- **2.** Select the hub if you have several of them or if you are using the PRO app.
- **3.** Go to the **Devices** tab.
- **4.** Select LifeQuality from the list.
- **5.** Go to **Settings** by clicking on the gear icon .
- **6.** Set the required settings.
- **7.** Click **Back** to save the new settings.

| Settings      | Value                                                                                                                                                                                                                                            |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name          | Detector name. Displayed in the list of hub<br>devices, SMS text, and notifications in the<br>events feed.<br>To change the name, click on the text field. The<br>name can contain up to 12 Cyrillic characters or<br>up to 24 Latin characters. |
| Room          | The virtual room to which LifeQuality is<br>assigned.<br>To change the room, click on the field.<br>The room name is displayed in the text of SMS<br>and notifications in the events feed.                                                       |
| Notifications | Notifications that users will receive from<br>LifeQuality:<br>When device moved — if enabled, users will<br>receive notification once the device is<br>moved or detached from mounting panel.                                                    |

|                        | Temperature — if enabled, users will receive<br>notifications once the temperature value<br>goes beyond the specified limits.                                                                                                             |  |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
|                        | Humidity — if enabled, users will receive<br>notifications once the humidity value goes<br>beyond the specified limits.                                                                                                                   |  |
|                        | CO level — if enabled, users will receive<br>2<br>notifications once the carbon dioxide<br>concentration goes beyond the specified<br>limits.                                                                                             |  |
| Air quality monitoring |                                                                                                                                                                                                                                           |  |
| Temperature            | The settings of the lower and upper limits of a<br>comfortable temperature. If the temperature<br>goes beyond these limits, users will receive<br>notifications.<br>The temperature can be set within the range<br>between 0°C and +50°C. |  |
|                        |                                                                                                                                                                                                                                           |  |
| Humidity               | The settings of the lower and upper limits of a<br>comfortable humidity level. If the humidity goes<br>beyond these limits, users will receive<br>notifications.<br>Humidity can be set within the range from 0% to                       |  |
|                        | 100%.                                                                                                                                                                                                                                     |  |
|                        | The settings of the lower and upper limits of a<br>comfortable carbon dioxide concentration in the<br>air. If the concentration goes beyond these<br>limits, users will receive notifications.                                            |  |

The concentration of CO can be set within the range from 0 ppm to 2400 ppm. 2

#### **LED indication**

CO level

2

2

Blink on high CO level If enabled, the device will blink with its LED once the CO level exceeds the specified limit. 2

![](_page_15_Picture_5.jpeg)

Enabling the option affects the battery life of the device.

| Scenarios                     | The menu for setting up automation scenarios<br>by temperature, humidity, and CO level.<br>2<br>Learn more                                                                                                                                                                                            |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Jeweller Signal Strength Test | Switches the device to the Jeweller signal<br>strength test mode.<br>The test helps to check the signal strength<br>between the device and the hub or range<br>extender to determine the optimal installation<br>place for LifeQuality.<br>The recommended value is two or three bars.<br>Learn more  |
| Wings Signal Strength Test    | Switches the device to the Wings signal<br>strength test mode.<br>The test helps to check the signal strength<br>between the device and the hub or the range<br>extender to determine the optimal installation<br>place for LifeQuality.<br>The recommended value is two or three bars.<br>Learn more |
| CO Sensor Calibration<br>2    | Starts manual calibration of the carbon dioxide<br>sensor. Calibration is required if the detector is<br>installed in an unventilated area. In this<br>conditions it should be manually calibrated<br>every two to three weeks.<br>How to run the CO sensor<br>2<br>calibration manually              |
| User Guide                    | Opens LifeQuality User Manual in the Ajax app.                                                                                                                                                                                                                                                        |
| Temporary Deactivation        | Allows to temporarily disable the device without<br>removing it from the system. Two options are<br>available:<br>No — the device operates in normal mode.                                                                                                                                            |
|                               |                                                                                                                                                                                                                                                                                                       |

|               | Entirely — the device does not execute<br>system commands and does not participate<br>in scenarios. |
|---------------|-----------------------------------------------------------------------------------------------------|
|               | Learn more                                                                                          |
| Unpair Device | Unpairs LifeQuality from the hub and deletes its<br>settings.                                       |

## How to set up scenarios

- **1.** Open the Ajax app.
- **2.** Select the hub if you have several of them or if you are using the PRO app.
- **3.** Go to the **Devices** tab.
- **4.** Select LifeQuality from the list.
- **5.** Go to **Settings** by clicking on the gear icon .
- **6.** Go to the **Scenarios** menu.
- **7.** Choose one of the indicators:
	- Temperature
	- Humidity
	- CO2
- **8.** Specify the value of the parameters:
	- **Higher Than** or **Lower Than** to define the event that runs the scenario.

To create a scenario for both options, you should create two different scenarios, one for **Higher Than** and another for **Lower Than**.

- The value upon which the scenario is triggered.
![](_page_18_Picture_0.jpeg)

- **9.** Click **Next**.
- **10.** Select the necessary automation devices that should trigger when the measurements goes beyond the specified in the scenario limit.
- **11.** Specify:
	- Name of the scenario
	- Action of the automation device
- **12.** Click **Save**.

![](_page_18_Picture_7.jpeg)

Learn more about scenarios

## How to view charts of device measurements

- **1.** Open the Ajax app.
- **2.** Select the hub if you have several of them or if you are using the PRO app.
- **3.** Go to the **Devices** tab.
- **4.** Select **LifeQuality**.
- **5.** Select an indicator:
	- Temperature
	- Humidity
	- CO2

![](_page_19_Picture_0.jpeg)

- **6.** Select an interval:
	- Hour
	- Day
	- Week
	- Month
	- Year

![](_page_19_Picture_7.jpeg)

You can also switch between detector measurements inside the screen. To do this, select the indicator in the menu above.

![](_page_20_Picture_0.jpeg)

To view the values of measurements for the specified period, click on the corresponding column of the chart.

> Charts may have gaps if at that time the connection between LifeQuality and the hub was lost for more than 72 hours or LifeQuality was disabled.

#### How to start CO sensor calibration manually 2

Locate the detector outdoors before starting the calibration. For example, take it outside or leave it by an open window.

#### **To start calibration:**

- **1.** Open the Ajax app.
- **2.** Select the hub if you have several of them or if you are using the PRO app.
- **3.** Go to the **Devices** tab.
- **4.** Select LifeQuality from the list.
- **5.** Go to **Settings** by clicking on the gear icon .
- **6.** Go to **СО Sensor Calibration** menu. **2**

- **7.** Click **Start** and wait for the calibration to finish.
CO sensor is calibrated for up to 10 minutes. After clicking the **Start** button, the timer in the app will start the countdown. Calibration ends automatically after the countdown is completed — return LifeQuality to the selected installation place. 2

![](_page_21_Picture_2.jpeg)

## Selecting the installation place

![](_page_21_Picture_4.jpeg)

The device is for indoor use only.

LifeQuality can be mounted on a vertical surface using an included installation kit. The device can also be placed on any horizontal surface without mounting. We recommend mounting the device on a vertical surface. It will prevent the device from being displaced or accidentally dropped.

We recommend installing the detector at the height of a human airway. For example, locate it in the office at the sitting person's head level or in the bedroom next to the bedhead. LifeQuality installs in every room in areas that are expected to be crowded. One detector operates effectively in one room, regardless of its size.

We recommend installing the detector in a ventilated room. If this is not possible, the CO sensor should be manually calibrated every two to three 2

weeks.

### How to run the CO2 sensor calibration manually

When choosing the location of the detector, consider the parameters that affect its operation:

- Jeweller signal strength.
- Wings signal strength.
- Distance between the detector and the hub.
- Presence of barriers for radio signal passage between devices: walls, interfloor ceilings, large objects located in the room.

Consider the placement recommendations when designing your Ajax security system for the object. The security system must be designed and installed by specialists. The list of recommended Ajax partners is . available here

## Signal strength

The Jeweller/Wings signal strength is determined by the ratio of the number of undelivered or corrupted data packets to expected ones that are exchanged between the hub and the detector within a certain period of time. Signal strength is indicated by the icon on the **Devices** tab:

- **Three bars** excellent signal strength.
- **Two bars** good signal strength.
- **One bar** low signal strength; stable operation is not guaranteed.
- **Crossed out icon** no signal; stable operation is not guaranteed.

Check the Jeweller and Wings signals strength at the installation place. We cannot guarantee stable operation if the signal strength is as low as one or zero bars. In this case, move the device. Repositioning even by 20 cm can significantly improve signal reception.

If the detector still has a low or unstable signal after it was moved, use . ReX 2

![](_page_23_Picture_0.jpeg)

## Do not install the detector

- Outdoors. This could damage the detector.
- In places with fast air circulation. For example, near fans, open windows, or doors. This can lead to incorrect measurements.
- Opposite any objects with rapidly changing temperature. For example, near electric and gas heaters. This can lead to incorrect temperature measurements.
- In places where the detector has low or unstable signal strength. This can lead to a connection loss between the detector and the hub or radio signal range extender.
- Inside premises with temperature and humidity outside the device's operation limits. This could damage the detector.
- In closed botanic gardens, greenhouses, and rooms with a large number of plants. The detector is not suitable for operation in such conditions.

## Installation

![](_page_23_Picture_10.jpeg)

#### **In order to install the detector:**

- **1.** Remove the SmartBracket mounting panel from the detector. To remove the panel, turn it counterclockwise.
- **2.** Fix the SmartBracket panel to a vertical surface using double-sided adhesive tape or other temporary fastener. The mounting panel has an UP sign, which indicates the correct position of the panel.
Use double-sided adhesive tape for temporary fixation only. The device fixed permanently with adhesive tape can peel off the surface at any time, leading to damage if the device is dropped.

- **3.** Run the and signal strength tests. The recommended value is two or three bars. Jeweller Wings
If the signal strength is a single bar or lower, we cannot guarantee the stable operation of the system. Move the device as repositioning even by 20 cm can significantly improve the signal reception. If low or unstable signal strength is still reported after relocation, use the radio signal range extender. ReX 2

- **4.** Remove the detector from the mount.
- **5.** Fasten the SmartBracket panel with bundled screws using all fixation points. If using other fasteners, ensure they do not damage or deform the mounting panel.
- **6.** Place the detector on the SmartBracket mounting panel.

## Malfunctions

If malfunction is detected (for example, there is no connection with the hub or range extender), the Ajax app displays a malfunction counter in the device field.

Malfunctions are displayed in the detector . Fields with malfunctions are highlighted in red. States

![](_page_25_Picture_0.jpeg)

The device can report malfunctions to the monitoring station of the security company, as well as to users through push notifications and SMS.

#### **LifeQuality malfunctions**

- Temperature is outside the device's operation limits.
- Humidity is outside the device's operation limits.
- CO concentration exceeds the device's range. 2
- No connection to the hub or radio signal range extender.
- The detector registered the fault of one or several built-in sensors.
- The battery charge level is low.

## Maintenance

Regularly check the functioning of the detector. The optimal frequency of checkups is once every three months. Clean the enclosure from dust, cobwebs, and other contaminants as they emerge. Use a soft dry cloth suitable for equipment care. Do not use substances that contain alcohol, acetone, gasoline, and other active solvents to clean the device.

If the detector is used in an unventilated space, it should be manually calibrated every two to three weeks. You can run the calibration manually in Ajax apps.

![](_page_26_Picture_0.jpeg)

## Technical specifications

All technical specifications of LifeQuality Jeweller

Compliance with standards

## Complete set

- **1.** LifeQuality.
- **2.** Installation kit.
- **3.** Quick Start Guide.

## Warranty

Warranty for the Limited Liability Company "Ajax Systems Manufacturing" products is valid for 2 years after the purchase.

If the device does not function correctly, please contact the Ajax Technical Support first. In most cases, technical issues can be resolved remotely.

![](_page_26_Picture_11.jpeg)

User Agreement

**Contact Technical Support:**

- e-mail
- Telegram

# Subscribe to the newsletter about safe life. No spam Email Subscribe