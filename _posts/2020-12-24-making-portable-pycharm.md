---
published: true
key: '19'
title: How to Make Portable PyCharm
tags:
  - PyCharm
  - Python
  - Portable
  - JDK
  - Java
---
Since Pycharm require java to run first we need to make portable java

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

   This `CommonFiles` folder contains portable JDK and all the portable apps that require jdk to run will  automatically find jdk from this `CommonFiles` folder. 
  
7. Inside `CommonFiles` folder there is another folder named `OpenJDK64`. Just rename this `OpenJDK64` to `java`.


# Configuring Portable Pycharm

1. Download portable Pycharm from [portableApps.com](https://portableapps.com/node/56602) or from [here](https://tongxai-my.sharepoint.com/:u:/g/personal/zh_2002000_xyz/EfoICvYe9RVPsgottFjRPwsBt0_tdGrnPJVkpH1k7zxEzQ?e=4RuQqc)
2. Open portableapps platform, click `Apps` menu and select `Install a New App` and select the intellij just   downloaded. Installation will begin.
   ![pycharm_portable_installation.png]({{site.baseurl}}/images/pycharm_portable_installation.png)
  
   ![pycharm_portable_installation1.png]({{site.baseurl}}/images/pycharm_portable_installation1.png)
3. After installation complete you will find in portableApps folder and a menu will be created in portableApp    platform menu

   ![pycharm_portable_installation2.png]({{site.baseurl}}/images/pycharm_portable_installation2.png)
4. Click Run and Configure Python interpreter in Pycharm
   ![pycharm_portable_installation3.png]({{site.baseurl}}/images/pycharm_portable_installation3.png)
  
   ![pycharm_portable_installation4.png]({{site.baseurl}}/images/pycharm_portable_installation4.png)


Now you can either
1. copy the whole PortableApps folder into the usb drive or  
2. just copy the `Pycharm` and `CommonFile` folder and you are ready to go. 

Actually we no longer need the portableapps platform to run IntelliJ. You can also make python portable or use winPythin.
