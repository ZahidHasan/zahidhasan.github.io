---
published: true
key: '!!str'
title: How to Make Portable IntelliJ
tags:
  - IntelliJ
  - Java
  - JDK
  - Portable
---
You can carry and run IntelliJ without installing JAVA in your PC.

# Configuring Portable JDK
1. Inorder to create portable java we are going to use portableapps platform. Download it from [here](https://tongxai-my.sharepoint.com/:u:/g/personal/zh_2002000_xyz/Ebq_Gakg7eBMp938n5waSAcBJp8aBcS3d2Tm2yXHsv-VUA?e=DZOEUM) or from their [website.](https://portableapps.com)

2. Install it in your preffered drive.  
   ![portableaApps_installation.png]({{site.baseurl}}/images/portableaApps_installation.png)
   
   
   ![portableaApps_installation1.png]({{site.baseurl}}/images/portableaApps_installation1.png)

   Once installed, inside your choosen folder you will see `PortableApps` folder where all of your portable software    will reside. 

3. Run Start.exe file and you will notice a menu in the taskbar like this
   ![portableaApps_installation2.png]({{site.baseurl}}/images/portableaApps_installation2.png)
   
   All your portable apps will be listed here. You can run the apps directly from where they are installed.

4. Now download portable JDK made specially for portableapps platform from their [website](https://portableapps.com/apps/utilities/OpenJDK64)    or [here](https://tongxai-my.sharepoint.com/:u:/g/personal/zh_2002000_xyz/EfuXG0NbSeFPpfVNWBLMkZ0BfhS8dPUSTas0Sr7opZmcUA?e=soWHEv).

5. Now click `Apps` menu and select `Install a New App` and select the jDK just downloaded. Installation will begin.
   ![portable_jdk_install.png]({{site.baseurl}}/images/portable_jdk_install.png)

   ![portable_jdk_install1.png]({{site.baseurl}}/images/portable_jdk_install1.png)

 

6. Now go to `D:\PortableApps\PortableApps` and you will notice a new folder named `CommonFiles` has been created.
   ![portable_jdk_install2.png]({{site.baseurl}}/images/portable_jdk_install2.png)

   This `CommonFiles` folder contains portable JDK and all the portable apps that require jdk to run will automatically find jdk from this `CommonFiles` folder. 

# Configuring Portable IntelliJ

1. Now we will install portable Intellij. Go to [portapps.io](https://portapps.io/app/intellij-idea-community-  portable/) and download portable IntelliJ or from [here](https://tongxai-my.sharepoint.com/:u:/g/personal/zh_2002000_xyz/EQf2HMMWD-RAl4Kg8FlZ0q0BsslZzXruhLInZhhBTXeNIg?e=6498Ar).

2. Extract the file into portableapps folder.
   ![portable_intellij_installation.png]({{site.baseurl}}/images/portable_intellij_installation.png)

3. In the portableapps menu click `Apps` ans `Refresh App Icons`, then you will see IntelliJ entry in the menu.
   ![portable_intellij_installation1.png]({{site.baseurl}}/images/portable_intellij_installation1.png)

4. Now run IntelliJ and click configuration
   ![portable_intellij_configuration.png]({{site.baseurl}}/images/portable_intellij_configuration.png)


5. Select `Structure for New Project`

   ![portable_intellij_configuration1a.png]({{site.baseurl}}/images/portable_intellij_configuration1a.png)
   
6. IntelliJ will not be able to find JDK at this moment.
   ![portable_intellij_configuration1.png]({{site.baseurl}}/images/portable_intellij_configuration1.png)

7. Click dropdown at `No SDK` and select `Add JDK`
   ![portable_intellij_configuration2.png]({{site.baseurl}}/images/portable_intellij_configuration2.png)

8. A new windows will open, locate `openJDK64` inside the `CommonFiles` folder in `PortableApps` folder at drive D.
   ![portable_intellij_configuration3.png]({{site.baseurl}}/images/portable_intellij_configuration3.png)

Click ok and Appply.

Now you can either
1. copy the whole PortableApps folder into the usb drive or  
2. just copy the `IntelliJ` and `CommonFile` folder and you are ready to go. 

Actually we no longer need the portableapps platform to run IntelliJ.
The complete portable package(intellij+jdk) can be downloaded from [here](https://tongxai-my.sharepoint.com/:u:/g/personal/zh_2002000_xyz/EciaVCZHLmpMqRY8NLayLdYBybMllg0zr5PfLZPAY0omeQ?e=yC8Pcb) that can be run from USB.
