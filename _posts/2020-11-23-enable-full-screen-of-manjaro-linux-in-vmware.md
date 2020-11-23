---
published: true
key: '!!str'
title: Enable Full Screen Mode of Manjaro Linux in VMWare
tags: 'Manjaro, Linux, Vmware, Virtualization'
---
# The Problem
By default manjaro (20.0.3) linux cannot run in full screen mode in vmware. It will not work even though you change the display resolution in manjaro or install vmware-tool. 
After installing manjaro in vmware, you see the following low resolution screen.

![manjaro_vmware.jpg]({{site.baseurl}}/images/manjaro_vmware.jpg)



# Solution
Inorder to eable full screen mode do the following:

1. Run in terminal:
   ```bash
   sudo pacman -S open-vm-tools 
   ```
2. Update and install display driver:
   ```bash
   sudo pacman -Su xf86-input-vmmouse xf86-video-vmware mesa gtk2 gtkmm
   ```
3. Edit the config file:
   ```bash
   sudo echo needs_root_rights=yes >>/etc/X11/Xwrapper.config
   ```
4. Run the service:
   ```bash
   sudo systemctl enable vmtoolsd
   sudo systemctl start vmtoolsd
   sudo systemctl restart vmtoolsd
   ```
   
# Result

Reboot and now you will see:
![Screenshot 2020-11-24 00.06.34.png]({{site.baseurl}}/images/Screenshot 2020-11-24 00.06.34.png)
