---
published: true
key: '!!str'
title: Enable Full Screen Mode of Manjaro Linux in VMWare
tags: Manjaro  Linux  Vmware  Virtualization  'Operating System'
---
# The Problem
By default manjaro (20.0.3) linux cannot run in full screen mode in vmware. It will not work even though you change the display resolution in manjaro or install vmware-tool. 
After installing manjaro in vmware, you see the following low resolution screen.

![manjaro_vmware.jpg]({{site.baseurl}}/images/manjaro_vmware.jpg)



# Solution
Inorder to eable full screen mode do the following:

1. Run in terminal:
   ```ps
   sudo pacman -S open-vm-tools 
   ```
2. Update and install display driver:
   ```ps
   sudo pacman -Su xf86-input-vmmouse xf86-video-vmware mesa gtk2 gtkmm
   ```
3. Edit the config file:
   ```bash
   sudo echo needs_root_rights=yes >>/etc/X11/Xwrapper.config
   ```
4. Run the service:
   ```ps
   sudo systemctl enable vmtoolsd
   sudo systemctl start vmtoolsd
   sudo systemctl restart vmtoolsd
   ```
5. Sometime it doesn't work and we have to enter the command `sudo systemctl restart vmtoolsd` manually. In order to make it automatically load at startup, do the following:

	- Goto application launcher (start menu) type `auto`, you will see `autostart` item. Open it.
        ![Screenshot_20201124_172546.png]({{site.baseurl}}/images/Screenshot_20201124_172546.png)
	
    2. Click on `add application`.
        ![Screenshot_20201124_172821.png]({{site.baseurl}}/images/Screenshot_20201124_172821.png)
	
    3. Type `sudo` and check `Run in terminal`, press ok.
        ![Screenshot_20201124_173207.png]({{site.baseurl}}/images/Screenshot_20201124_173207.png)
	
    4. You will see a new enty `sudo`. click `properties`.
        ![Screenshot_20201124_173230.png]({{site.baseurl}}/images/Screenshot_20201124_173230.png)
	
    5. Give a name FullScreen. In command type 
       ```ps
       sudo -S <<< "123456" systemctl restart vmtoolsd`.
       ```
        Press ok.
      
       ![Screenshot_20201124_175812.png]({{site.baseurl}}/images/Screenshot_20201124_175812.png)
       
	6. Reboot machine
   
# Result

Reboot and now you will see full screen
![Screenshot 2020-11-24 00.06.34.png]({{site.baseurl}}/images/Screenshot 2020-11-24 00.06.34.png)
