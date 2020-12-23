---
published: false
key: '!!str'
title: Make Portable IntelliJ & JDK for USB PenDrive.
---
# Create Portable JAVA Environment
Inorder to create portable java we are going to use portableapps platform. Download it from [here](https://tongxai-my.sharepoint.com/:u:/g/personal/zh_2002000_xyz/Ebq_Gakg7eBMp938n5waSAcBJp8aBcS3d2Tm2yXHsv-VUA?e=DZOEUM) or from their [website.](https://portableapps.com)
Install it in your preffered drive.
![portableaApps_installation.png]({{site.baseurl}}/images/portableaApps_installation.png)
![portableaApps_installation1.png]({{site.baseurl}}/images/portableaApps_installation1.png)

Once installed, inside your choosen folder you will see `PortableApps` folder where all of your portable software will reside.

Run Start.exe file and you will notice a menu in the taskbar like this
![portableaApps_installation2.png]({{site.baseurl}}/images/portableaApps_installation2.png)
All your portable apps will be listed here. You can run the apps directly from where they are installed.

Now download portable JDK made for portableapps platform [here](https://portableapps.com/apps/utilities/OpenJDK64) or [here](https://tongxai-my.sharepoint.com/:u:/g/personal/zh_2002000_xyz/EfuXG0NbSeFPpfVNWBLMkZ0BfhS8dPUSTas0Sr7opZmcUA?e=soWHEv).

Now click `Apps` menu and select `Install a New App` and select the jDK just downloaded. Installation will begin.
![portable_jdk_install.png]({{site.baseurl}}/images/portable_jdk_install.png)

![portable_jdk_install1.png]({{site.baseurl}}/images/portable_jdk_install1.png)

After installation you will not see any entry in portable platform menu.

Now go to `D:\PortableApps\PortableApps` and you will notice a new folder named `CommonFiles` has been created.
![portable_jdk_install2.png]({{site.baseurl}}/images/portable_jdk_install2.png)

This `CommonFiles` folder contains portable JDK and all the portable apps that require jdk to run will automatically find jdk from this `CommonFiles`. Actually we no longer need the portableapps platform to run IntelliJ. 

Now we will install portable Intellij. Go to [portapps.io](https://portapps.io/app/intellij-idea-community-portable/)and download portable IntelliJ or from [here](https://tongxai-my.sharepoint.com/:u:/g/personal/zh_2002000_xyz/EQf2HMMWD-RAl4Kg8FlZ0q0BsslZzXruhLInZhhBTXeNIg?e=6498Ar).

Extract the file in desktop and copy it into portableapps folder.
![portable_intellij_installation.png]({{site.baseurl}}/images/portable_intellij_installation.png)



