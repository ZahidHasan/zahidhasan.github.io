---
published: true
key: '!!str'
title: Awsome Insider Journey of Android-01
---
![Setup-ADB-and-Fastboot-on-Mac-OS-Linux-and-Chrome-OS-and-Windows-topaz-enhance-sharpen.png]({{site.baseurl}}/images/Setup-ADB-and-Fastboot-on-Mac-OS-Linux-and-Chrome-OS-and-Windows-topaz-enhance-sharpen.png)


## USB Driver
The USB (Universal Serial Bus) is a standardized interface for connecting devices to a computer. To allow communication between the computer and the device, two types of drivers are typically used: 
1. the USB host-side driver and 
1. the device-side driver.

The USB host-side driver is installed on the computer and is responsible for communicating with the USB controller. It provides a standard interface for accessing the USB devices and makes it possible for the operating system to recognize and interact with the connected device.

The device-side driver, also known as a client driver, is installed on the device itself and is responsible for communicating with the USB host-side driver. The client driver implements the specific protocols required by the device and acts as a bridge between the USB host-side driver and the device's firmware.

When a USB device is connected to a computer, the host-side driver recognizes the device and sends a request to the device-side driver to retrieve information about the device and its capabilities. The device-side driver then sends back the information to the host-side driver, which uses this information to configure the device and establish communication between the computer and the device.

In summary, the host-side driver provides a standard interface for the computer to communicate with the USB device, while the device-side driver implements the specific protocols required by the device and acts as a bridge between the host-side driver and the device's firmware.

Now come to Android. What does USB driver do here?
In Android, a USB driver is a program that controls the communication between the operating system and a USB device. When a USB device is connected to an Android device, the operating system automatically detects the device and starts the driver installation process.

The driver enables the operating system to recognize the device and interact with it by sending and receiving data. For example, when you connect a USB storage device to your Android device, the driver allows the operating system to access the storage device's files and folders.

There are two types of USB drivers in Android:

1. System-level drivers: These are built into the Android operating system and are responsible for handling common functions such as charging and file transfers.
1. Vendor-specific drivers: These are provided by device manufacturers and are specific to a particular device or product line. They enable the operating system to interact with specific hardware features that are not supported by system-level drivers.

To ensure that a USB device works correctly with an Android device, it's important to have the correct driver installed. Some devices come with their own drivers, while others may require you to download the driver from the manufacturer's website.

In conclusion, the role of the USB driver in Android is to provide the operating system with the necessary information and communication channels to interact with connected USB devices

## ADB Driver
ADB (Android Debug Bridge) is a command-line tool that allows you to communicate with an Android device. It is used to run various commands on the device, such as installing and debugging applications, copying files to and from the device, and more. The ADB driver is necessary for the ADB tool to work properly and allow communication between the computer and the Android device.

When you connect an Android device to a computer, the computer needs to recognize the device and install the necessary drivers. The ADB driver is the driver that allows the computer to recognize and communicate with the Android device. It provides a bridge between the computer and the device, allowing the ADB tool to run commands on the device.

The ADB driver is typically included in the Android SDK (Software Development Kit), which can be downloaded from the Android developer website. Once you have installed the Android SDK on your computer, you can install the ADB driver and use the ADB tool to communicate with your Android device.


ADB drivers are a type of software that allows your computer to communicate with your Android device. They are essential for debugging and developing Android apps, as they allow you to access the device's internal storage, install apps, and more. ADB drivers are available for download from the Google Play Store, or you can download them directly from the manufacturer's website. Once installed, you can use them to debug your apps and make sure they are running correctly.


A USB driver is used when you want to connect your phone to your PC so that you can transfer files back and forth, install apps, and do other things.
An ADB driver is used for development purposes. If you're a developer and you want to be able to use ADB commands to do things like pull files from your phone or push files to it, you'll need to install an ADB driver on your computer.
The main difference between USB driver and an ADB driver is that the USB driver is for connecting a physical Android device to your computer via USB cable while the ADB driver is for connecting to a virtual Android device.


## Fastboot Command
Fastboot is a protocol used to update the flash file system in Android devices over a USB connection. It is used to perform various tasks such as unlocking the bootloader, installing custom recovery, and updating the firmware.

Fastboot works by booting the device into a special boot mode called "Fastboot mode". In this mode, the device is able to communicate with the host computer over a USB connection using the fastboot protocol. The host computer then sends commands to the device, which are executed in the fastboot environment.

For example, if you want to flash a new firmware on your Android device, you would first boot it into fastboot mode. You would then connect the device to your computer and use fastboot commands to transfer the firmware image to the device's flash storage. The fastboot protocol is then used to update the firmware on the device.

Fastboot is a useful tool for developers and advanced users who want to modify their Android devices. However, it is important to use fastboot with caution, as improper use can result in bricking your device or making it unbootable.

## ADB Command
Android Debug Bridge (ADB) is a command-line tool that allows you to communicate with Android devices. It provides a bridge between the device and your development machine and enables you to transfer files, run shell commands, install and uninstall apps, and perform other actions on the device.

Here's how ADB works in a nutshell:

Installation: To use ADB, you first need to install the Android SDK on your development machine. The SDK contains the ADB executable and the required drivers.

Connecting the device: You need to connect your Android device to your development machine using a USB cable. You also need to enable USB debugging on the device from the Developer options in the device settings.

Starting ADB: Once the device is connected, you can start ADB by running the adb executable from the command line.

Issuing commands: You can issue ADB commands to perform various actions on the device. For example, you can use the ```adb shell``` command to start a shell on the device and run shell commands. You can use the ```adb push``` and ```adb pull``` commands to transfer files to and from the device.

Debugging apps: ADB can also be used for debugging Android apps. You can use the ```adb logcat``` command to retrieve the logcat output from the device, which can help you identify issues in your app.

Overall, ADB is an essential tool for any Android developer, as it provides a convenient way to interact with Android devices for testing and debugging purposes

## ADB vs FastBoot
ADB (Android Debug Bridge) and Fastboot are two essential tools for developers and advanced users to interact with Android devices. They allow you to perform various actions on the device, such as installing apps, debugging, or flashing firmware.

Here's a comparison between ADB and Fastboot:

- ADB is a versatile tool that allows you to send commands to your Android device over a USB connection or over the network.
- It is primarily used for debugging purposes, but can also be used to install apps, copy files to and from the device, and perform various other tasks.
- ADB requires the device to be in an unlocked state and have developer options enabled.
- Fastboot is a protocol used to flash firmware images to Android devices.
- It is used to flash partitions on the device, such as the bootloader, recovery, system, or vendor images.
- Unlike ADB, Fastboot requires the device to be in a bootloader or fastboot mode. This means the device must be turned off and restarted in a specific way to enter fastboot mode.
- Fastboot is often used to install custom ROMs or recover bricked devices.

In conclusion, ADB and Fastboot are two different tools used for different purposes, but they are both essential for developers and advanced users who want to customize their Android devices.


# ROM
## Stock ROM
## Custom ROM
# Recovery
## Stock Recovery
## Custom Recovery
### TWRP
### MAGISK
