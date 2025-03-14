---
published: true
key: '21'
title: Install KDE Desktop in Kali Linux
tags:
  - Linux
  - Kali
  - KDE
---
## KDE

With Plasma, you have a full-featured Linux desktop environment that has everything you could possibly need to use your computer. KDE is one of the largest and most active open-source communities with an ecosystem of applications for every purpose you can imagine.

![KDE-Plasma-5.19-Desktop.jpg]({{site.baseurl}}/images/KDE-Plasma-5.19-Desktop.jpg)


While idling, KDE Plasma Desktop is using 580 MB with no other applications running than the terminal application. XFCE (Ubuntu) is only using 490 MB when idle.

In addition to KDE Plasma Desktop and XFCE, you can also install a desktop environment from any official repository of your Linux distribution. Both desktop environments have easy installation options and can be found in official repositories of all popular Linux distributions.

## System Update
```ps
   sudo apt update
```
## Install KDE
```
sudo apt install kali-desktop-kde
```

##  Select Display Manager

![18.png]({{site.baseurl}}/images/18.png)

## Change Kali Desktop environment
```
sudo update-alternatives --config x-session-manager
```
