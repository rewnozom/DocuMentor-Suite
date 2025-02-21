# TurretCam user manual

Updated October 26, 2023

![](_page_0_Picture_2.jpeg)

**TurretCam** is an IP camera with smart infrared (IR) backlight and an object recognition function. The user can view archived and live videos in the Ajax apps. To store the captured data, install a microSD card or connect the camera to NVR with an installed hard disk.

The device is compatible with all [.](https://ajax.systems/products/hubs/) Connection to , , andis not supported. hubs radio signal range extenders [ocBridge Plus](https://ajax.systems/products/ocbridgeplus/) uartBridge

The camera connects to the network via Ethernet, using the appropriate connector. A hub is only required for adding TurretCam to the Ajax system.

The camera is available in several versions:

- TurretCam (5 Mp/2.8 mm);
- TurretCam (8 Mp/2.8 mm);
- TurretCam (5 Mp/4 mm);
- TurretCam (8 Mp/4 mm).

#### [Buy TurretCam](https://ajax.systems/products/turretcam/)

# Functional elements

![](_page_1_Picture_4.jpeg)

![](_page_1_Picture_5.jpeg)

- **1.** Camera holder.
- **2.** Camera enclosure.
- **3.** Camera lens.
- **4.** IR backlight. Used to record videos in dark and low-light conditions.
- **5.** Faceted lens. Covers the infrared LEDs and diffuses the rays.
- **6.** Microphone.
- **7.** Holes for attaching the camera to the surface.
- **8.** Slot for microSD card.
- **9.** Reset button.
- **10.** QR code with the device ID. Used to add TurretCam to an Ajax system.
- **11.** Cable connector.

# Operating principle

TurretCam is an IP camera that uses artificial intelligence (AI) for object recognition. Its algorithms can identify moving objects, distinguishing between humans, animals, or vehicles.

The device features a smart IR backlight, ensuring the capture of high-quality images even in low-light conditions. The camera automatically adjusts the backlight intensity in real time to prevent overexposure, enabling clear visibility of objects that are either far away or too close to the camera in low-light conditions.

![](_page_2_Picture_8.jpeg)

TurretCam has an IP65 protection class, making it suitable for outdoor installation. Its robust metal enclosure protects the device against sabotage.

You can install a microSD card with a memory capacity of up to 256 GB (not included in the complete set of the camera). Additionally, the device can operate without a memory card or via NVR.

TurretCam enables you to:

- **1.** Watch video in real-time with the ability to zoom in for a closer look.
- **2.** Access archived videos, navigating through them based on recording chronology and calendar (this feature is available if a microSD memory card is installed in the camera, or it is connected to NVR with an installed hard disk).
- **3.** Configure motion detection zones and adjust sensitivity level.
- **4.** View the **Videowall** that combines images from all connected cameras.

- **5.** that send a short video from the selected camera to the Ajax app when the security detector is triggered. [Create video scenarios](https://support.ajax.systems/en/manuals/videoscenarios/)
# Video scenarios

The Ajax system offers the capability to use IP cameras for alarm verification. Video scenarios enable the substantiation of alarm triggers with corresponding video from cameras installed at the facility.

Cameras can be configured to respond to alarms from a single device, multiple devices, or all connected devices. Combined detectors can register various types of alarms, allowing you to configure responses to a wide range of alarm types, whether it's just one, several, or all of them.

#### [Learn more](https://support.ajax.systems/en/manuals/videoscenarios/)

# Videowall

The user can manage videos on the **Videowall** tab, accessible once at least one camera has been added. This feature ensures quick access to all connected cameras, displayed in accordance with privacy settings.

The user can:

- **1.** Switch between cameras.
- **2.** Search for the desired camera by name.
- **3.** Receive updates on camera previews.
- **4.** Change the display order (in progress).

# Privacy settings

The user can configure access to view videos from shared cameras, extending this capability to other users and the security company. The user can specify the conditions that permit video viewing: at any time, when shared devices are armed, or exclusively within a designated timeframe following the alarm.

# Selecting the installation site

When choosing the optimal location to install TurretCam, consider the camera's viewing angle and any potential obstacles that might obstruct its view.

Consider the placement recommendations when designing the security system project for your object. The security system should be designed and installed by professionals. A list of recommended partners is . available here

#### The camera should not be installed

- **1.** In indoor or outdoor locations where the temperature and humidity levels do not align with the specified operating parameters.
- **2.** In locations where objects or structures might obstruct the camera's view.

# Installation and connection

- **1.** Using the bundled hexagon key (Ø 2 mm), loosen the two screws and detach the camera enclosure from the holder. Ensure to support the enclosure to prevent the camera from falling.
- **2.** Remove the screws holding the QR code cover. Insert a microSD card (not included) into the appropriate slot. Replace the QR code cover and tighten the screws.

![](_page_4_Picture_10.jpeg)

- **3.** Use the mounting template to mark the locations for the drill holes on the surface where you plan to mount the camera. Secure the template to the chosen installation location with tape, and drill three holes as indicated on the template.
- **4.** Route the cable through the camera holder and secure the holder to the surface using the bundled screws.

![](_page_5_Picture_2.jpeg)

- **5.** Place the camera enclosure in the holder, ensuring that the camera lens faces the protected area. Secure it in place by tightening the two screws in the holder using the bundled hexagon key (Ø 2 mm).
- **6.** Connect the Ethernet cable to the camera. If it is powered by PoE, no external power supply is needed; otherwise, connect both the external power supply and the Ethernet cable. Install a waterproof connector if the camera will be used in indoor areas with humidity levels outside the operating parameters, or outdoors.

![](_page_5_Picture_5.jpeg)

- **7.** Turn on the power supply of the camera. The LED indicator on the cable connector lights up green, indicating a successful connection to Ajax Cloud.
## Adding to the system

# Before adding a device

- **1.** Install the [Ajax app](https://ajax.systems/software/) and log in to your account.
- **2.** Add a hub to your app, configure its settings, and create at least one . [virtual](https://support.ajax.systems/en/manuals/hub-2-plus/#block10) [room](https://support.ajax.systems/en/manuals/hub-2-plus/#block10)
- **3.** Ensure the hub is disarmed.

## How to add TurretCam

**Without NVR in the system:**

**With NVR in the system:**

### Icons

The icons in the app display some device states. To access them:

- **1.** Select a hub in the Ajax app.
- **2.** Go to the **Devices** tab.
- **3.** Find **TurretCam** in the list.

| Icon | Value                                                       |
|------|-------------------------------------------------------------|
|      | Live view is available.                                     |
|      | Live view is not available.                                 |
|      | Other users have access to view camera video.<br>Learn more |

| The camera has an archive.                                                                  |
|---------------------------------------------------------------------------------------------|
| The microSD card is not installed.                                                          |
| The microSD card is installed.                                                              |
| Malfunction of the microSD card is detected. Formatting the microSD card is<br>recommended. |
| The microSD card is being formatted.                                                        |
| The new firmware version is available.                                                      |
| An error was detected during the firmware update.                                           |

# States

The states display information about the device and its operating parameters. You can find out about the states of the video recorder in Ajax apps:

- **1.** Select a hub in the Ajax app.
- **2.** Go to the **Devices** tab.
- **3.** Select **TurretCam** from the list of devices. If TurretCam is connected to the video recorder, select **NVR** and then click **Cameras**.

| Parameter         | Value                                                                                                        |
|-------------------|--------------------------------------------------------------------------------------------------------------|
|                   | The camera connection status to the internet<br>via Ethernet:                                                |
|                   | Online — the camera is connected to the<br>network. Normal state.                                            |
| Connection        | Offl<br>ine — the camera is not connected to the<br>network. Please check your wired internet<br>connection. |
|                   | Clicking the icon<br>displays the network<br>parameters.                                                     |
| Connection to NVR | Displayed when the camera is connected to<br>NVR.                                                            |

|                  | The camera connection status to NVR:<br>Online — the camera is connected to the<br>network via NVR. Normal state.<br>Offl<br>ine — the camera is not connected to the<br>network via NVR. Please check your wired<br>internet connection. |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                  | Clicking the icon<br>displays the network<br>parameters.                                                                                                                                                                                  |
|                  | Displays the list of storage devices connected<br>to the camera:<br>Cloud (in progress);                                                                                                                                                  |
| Storage Location | Memory card — data is recorded on a<br>memory card (not included) installed in the<br>camera.<br>NVR hard drive — data is recorded on the                                                                                                 |
|                  | NVR hard disk.<br>Clicking the icon<br>displays the network<br>parameters.                                                                                                                                                                |
|                  | The memory card connection status to the<br>camera:                                                                                                                                                                                       |
|                  | OK — the memory card is communicating<br>with the camera. Normal state.<br>Not installed — the memory card is not                                                                                                                         |
| Memory Card      | installed in the camera.                                                                                                                                                                                                                  |
|                  | Requires formatting — the memory card<br>formatting is recommended. If the memory<br>card contains data, it will be permanently<br>deleted.                                                                                               |
|                  | Formatting… — the memory card is being<br>formatted.                                                                                                                                                                                      |
| Resolution       | The current camera resolution.                                                                                                                                                                                                            |
| Frame Rate       | The current camera frame rate.                                                                                                                                                                                                            |
| Bit Rate         | The current camera bit rate.                                                                                                                                                                                                              |

|                            | The current video codec:                                                                                               |
|----------------------------|------------------------------------------------------------------------------------------------------------------------|
| Video Codec                | H.265;                                                                                                                 |
|                            | H.264.                                                                                                                 |
|                            | The Motion Detection function status:                                                                                  |
| Motion Detection           | On;                                                                                                                    |
|                            | Off.                                                                                                                   |
|                            | The Object Detection function status:                                                                                  |
| Object Detection           | On;                                                                                                                    |
|                            | Off.                                                                                                                   |
|                            | Displays the number of users who have access<br>to view video from the camera.                                         |
| Camera Access Available to | Clicking the icon<br>displays the list of users,<br>installers, and companies with access under<br>certain conditions. |
|                            | Learn more                                                                                                             |
| Firmware                   | Firmware version of the camera.                                                                                        |
| ID                         | TurretCam ID/Serial Number. Also available on<br>the back part of the casing and the packaging.                        |

# Settings

To change video recorder settings, in an Ajax app:

- **1.** Go to the **Devices** tab.
- **2.** Select **TurretCam** from the list. If TurretCam is connected to the video recorder, select **NVR** and click **Cameras**.
- **3.** Go to **Settings** by clicking on the gear icon .
- **4.** Set the required parameters.
- **5.** Click **Back** to save the new settings.

| Settings              | Value                                                                                                                 |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------|
|                       | Camera name. Displayed in the list of hub<br>devices, SMS text, and notifications in the<br>events feed.              |
| Name                  | To change the camera name, click on the text<br>field.                                                                |
|                       | The name can contain up to 12 Cyrillic<br>characters or up to 24 Latin characters.                                    |
|                       | Selection of the camera virtual room.                                                                                 |
| Room                  | The room name is displayed in SMS text and<br>notifications in the events feed.                                       |
| Arm in Night Mode     | When this option is enabled, the camera will<br>switch to the armed mode whenever the system<br>is set to Night Mode. |
|                       | Learn more                                                                                                            |
| Recording Preferences | Selection of the storage device where the<br>camera will save the recorded data:                                      |
|                       | Cloud (in progress);                                                                                                  |
|                       | SD card;                                                                                                              |
|                       | NVR.                                                                                                                  |
|                       | Selection of the Recording Mode for each<br>storage device:                                                           |
|                       | On Detection or Scenario;                                                                                             |
|                       | Continuous;                                                                                                           |
|                       | Never.                                                                                                                |

|                                   | Selection of the armed mode when the camera<br>records video:                                                                                                                                           |  |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
|                                   | When Armed;                                                                                                                                                                                             |  |
|                                   | Always.                                                                                                                                                                                                 |  |
| Notifications by camera detectors | When the Notify When Camera Detects Motion<br>toggle is enabled, the user receives a<br>notification upon any detected motion by the<br>camera.                                                         |  |
|                                   | When the Notify When Camera Detects Object<br>toggle is enabled, the user receives a<br>notification upon specific object motion<br>detection by the camera:                                            |  |
|                                   | If a human is detected;                                                                                                                                                                                 |  |
|                                   | If a pet is detected;                                                                                                                                                                                   |  |
|                                   | If a vehicle is detected.                                                                                                                                                                               |  |
|                                   | The setting also allows the user to specify the<br>duration of the movement and select the armed<br>mode that triggers the notifications.                                                               |  |
| Camera settings                   |                                                                                                                                                                                                         |  |
| Detectors                         | When the Motion Detection toggle is enabled,<br>the camera detects motion using its built-in<br>software.                                                                                               |  |
|                                   | When the Object Detection toggle is enabled,<br>the camera distinguishes between specific<br>objects. In the camera video, a human, a pet,<br>and a vehicle are highlighted with colored<br>rectangles. |  |
|                                   | The setting also allows the user to define the<br>active zone where the camera detects motion.<br>When triggered, the system sends a notification<br>to the user.                                       |  |
| Video Stream                      | Settings for mainstream and substream<br>parameters.                                                                                                                                                    |  |
| Image Preferences                 | Settings for camera image quality.                                                                                                                                                                      |  |

| On-Screen Display (OSD)                 | Allows the user to customize the display of<br>additional information on the camera image:<br>Camera name;<br>Timestamp;<br>Parameters of the displayed text.                       |  |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| Audio                                   | When the Audio Capture and Playback toggle is<br>enabled, the camera records sound.                                                                                                 |  |
| Privacy Zones                           | Allows the user to select zones that are not<br>displayed on the camera video. Instead, the user<br>sees a black rectangle.                                                         |  |
| Image Rotation                          | Allows the user to rotate the camera video.                                                                                                                                         |  |
| Firmware Update                         | Allows the user to check for a new firmware<br>version and download it.                                                                                                             |  |
| Connection                              |                                                                                                                                                                                     |  |
| Connection Type                         | The setting for selecting the camera's<br>connection type to Ajax Cloud service via<br>Ethernet.<br>Available connection types:<br>DHCP;<br>Static.                                 |  |
| Delay of Cloud Connection Loss Alarm, s | The delay helps to reduce the risk of a false<br>event about the lost connection with the server.<br>The delay can be set in the range of 30 to 600<br>seconds.                     |  |
| NVR-Cloud Polling Interval, s           | The frequency of polling the Ajax Cloud server<br>is set in the range of 30 to 300 seconds.<br>The shorter the interval, the quicker the cloud<br>connection loss will be detected. |  |
| Memory Card                             | Selection of the maximum archive depth. It can<br>be set in the range of 1 to 360 days or can be<br>unlimited.                                                                      |  |

|                  | Allows the user to format the memory card.                              |  |
|------------------|-------------------------------------------------------------------------|--|
|                  | Time zone selection.                                                    |  |
| Service          | Set by the user and is displayed when viewing<br>video from IP cameras. |  |
| Report a Problem | Allows the user to describe a problem and send<br>a report.             |  |
| User Guide       | Opens the camera user manual.                                           |  |
| Unpair Device    | Unpairs TurretCam from the hub.                                         |  |

# Indication

The green LED indicator is placed on the cable connector.

| Event                                                     | Indication       | Note |
|-----------------------------------------------------------|------------------|------|
| The camera has power and is<br>connected to the internet. | Lights up green. |      |

# Malfunction

When the camera has a malfunction, such as a loss of internet connection, you can see it in the **Devices** tab in the Ajax app. The malfunction counter is displayed to the left of the camera icon (a white number on a red background).

All malfunctions can be seen in the camera . Fields with malfunctions will be highlighted in red. States

## Maintenance

Regularly check the functioning of the camera. If you notice any image degradation, loss of clarity, or darkening, check the camera for dirt. Clean the device's enclosure to remove dust, cobwebs, and other contaminants as they emerge. Use soft, dry wipes suitable for cleaning electronic equipment.

Avoid using substances that contain alcohol, acetone, petrol, and other aggressive solvents when cleaning the camera. Wipe the lens gently: scratches can result in poor-quality images and camera failure.

# Technical specifications

[Technical specifications for TurretCam (5 Mp/2.8 mm)](https://ajax.systems/products/specs/turretcam-5-mp-2-8-mm/)

[Technical specifications for TurretCam (5 Mp/4 mm)](https://ajax.systems/products/specs/turretcam-5-mp-4-mm/)

[Technical specifications for TurretCam (8 Mp/2.8 mm)](https://ajax.systems/products/specs/turretcam-8-mp-2-8-mm/)

[Technical specifications for TurretCam (8 Mp/4 mm)](https://ajax.systems/products/specs/turretcam-8-mp-4-mm/)

[Compliance with standards](https://ajax.systems/standards/)

# Warranty

Warranty for the Limited Liability Company "Ajax Systems Manufacturing" products is valid for 2 years after the date of purchase.

If you encounter any issues with the device's functionality, we recommend contacting Ajax Technical Support first. In most cases, technical issues can be resolved remotely.

### [Warranty obligations](https://ajax.systems/warranty)

[User Agreement](https://ajax.systems/end-user-agreement)

### **Contact Technical Support:**

- [e-mail](mailto:support@ajax.systems)
- [Telegram](https://t.me/AjaxSystemsSupport_Bot)

Subscribe to the newsletter about safe life. No spam

Email Subscribe