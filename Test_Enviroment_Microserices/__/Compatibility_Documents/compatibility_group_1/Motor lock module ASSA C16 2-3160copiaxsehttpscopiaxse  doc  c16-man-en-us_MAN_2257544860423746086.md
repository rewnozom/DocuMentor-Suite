![](_page_0_Picture_0.jpeg)

## Connection instructions

Updated11/26/2020

# **Motor lock module ASSA C16, 2-3160**

The C16 is used instead of the regular control unit for the Hi-O 840C, 841C and 850C series of ASSA motor locks.

![](_page_0_Picture_5.jpeg)

# C16 Motor lock module ASSA

| Description                           | 3 |
|---------------------------------------|---|
| Assembly and connection               | 3 |
| Essential function                    | 4 |
| ASSA Hi-O Setup                       | 4 |
| Information                           | 4 |
| Init Network                          | 5 |
| Uninit Network                        | 5 |
| Factory Restore                       | 5 |
| Cable Termination                     | 5 |
| Explanation of LEDs                   | 6 |
| Module LEDs                           | 6 |
| Lock housing LEDs                     | 6 |
| Replace module or motor lock          | 6 |
| Factory reset of locks                | 7 |
| Installation and configuration of C16 | 7 |
| Before you contact support            | 7 |

## Description

The C16 module is designed for use with ASSA motor locks with Hi-O 840C, 841C and 850C series.

Requires VAKA version 3.60.xx or later.

# Assembly and connection

#### In case of problems, the lock may need to be removed to see the status LED.

- 1. Power off the controller.
- 2. Mount the module at any module location in the door controller.
- 3. Mount the cable in the connector below the module. (From Axema the cable is delivered with the lock)
- 4. Power up the controller.
- 5. The LED should now flash orange once / second. If the LED flashes red, the lock is not switched on or it is faulty. Then perform a factory reset of the lock ..
- 6. Approx. 30 seconds after the module has been mounted, the menu ASSA HI-O SETUP appears on the display of the door controller.
- 7. SelectINIT NETWORK using the keypad, and the LED on the module starts flashing orange, first quickly, then slowly four times. Then the LED on the back of the lock housing goes out.
- 8. Then the LED on the module flashes green and the motor lock is then in operation.

### Essential function

Motor lock relay (B28: 18-19, B27: 14-15) closes when the motor lock bolt is fully in and opens when the motor lock bolt is fully out, which can be used foressential function.

# ASSA Hi-O Setup

Under the door controllers new menu,ASSA Hi-O SETUP, there are the settings required to configure the module and motor lock.

#### Information

Displays the status and version of hardware and software.

### Init Network

Initiates communication between module and motor lock. Init Network be initiated after mounting the module and lock and takes about ten seconds. During initialization, the orange LED flashes rapidly for five seconds, then slowly four times. When the initialization is complete, the LED flashes green.

### Uninit Network

Terminates the communication between the module and motor lock. During the process, the LED flashes orange rapidly for five seconds, then slowly orange. The LED on the lock housing lights up.

#### Uninit Network must be run before changing lock or module.

### Factory Restore

Factory restore module. After the factory reset, the module LED flashes orange quickly and the LED on the lock housing lights up. Then the module LED slowly flashes orange.

### Cable Termination

Termination in the module. The module is factory set as terminated. Termination can be konfigured in VAKA in, Doors - Connections - Motor lock.

# Explanation of LEDs

### Module LEDs

| Color | Slowly flashing                                                                                         | Fast flashing                                                                                                   |
|-------|---------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
|       | Orange The module is not configured.                                                                    | The module configures Hi-O devices by send<br>ing settings to the lock case.                                    |
| Green | The module is configured and com<br>municates with the motor lock.                                      |                                                                                                                 |
| RED   | The module cannot communicate with<br>the lock housing, alternatively the mod<br>ule is not configured. | Problems with communication between lock<br>case and module. Factory reset of the motor<br>lock is recommended. |

### Lock housing LEDs

| Off             | The lock housing is connected and during normal operation.              |  |
|-----------------|-------------------------------------------------------------------------|--|
| Red, solid lit  | The lock housing is unconnected, or the lock housing is not configured. |  |
| Flashing (2 Hz) | The motor lock is connected to another C16 module.                      |  |
| Flicker (20 Hz) | Temporarily inactivated for three minutes.                              |  |

# Replace module or motor lock

- 1. Navigate to the door controller menu,ASSA Hi-O SETUP.
- 2. Start Uninit, the module LED should first flash quickly in orange and then more slowly. The motor lock LED should lit solid red.
- 3. Power down the door controller, change the module or lock and power up the door controller again. Orange LED on the module indicates successful replacement and red light indicates an unsuccessful replacement.
- 4. If the module LED flashes red, start Factory restore, the module LED should flash fast orange for five seconds and then slower.
- 5. If the module LED still flashes red, the lock must be factory reset before the next step is performed.
- 6. Start Init network, the module LED should flash orange quickly for five seconds,. Then the module LED flashes orange four times before it starts flashing green.

### **Factory reset of locks**

- 1. Power down the lock and remove it.
- 2. Remove the door sensor (magnet) and turn on the power again.
- 3. Slide the "microswitch" back and forth 6 times within 30 seconds.
- 4. Turn the power to the lock off and on. The LED should light up on the lock and the module LED should flash orange.

![](_page_6_Picture_5.jpeg)

# Installation and configuration of C16

This manual only deals with the installation and connection of the C16.

For configuration of motor lock settings, see section Access control-> Motor lock in the commissioning manual. (https://info.axema.se?commissioning)

# Before you contact support

- l C16 requires VAKA version 3.60.xx or later.
- l If a mounted C16 module does not work, a factory reset may resolve the issue.
- l Broken CPU can be replaced without configuration.
- l It is not possible with C16 for the lock contact to open day locking
- l External magnetic contact can not be used.