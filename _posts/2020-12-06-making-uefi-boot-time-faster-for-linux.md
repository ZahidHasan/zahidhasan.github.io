---
published: true
key: '16'
title: Making UEFI Boot Time Faster for Linux
tags:
  - Linux
  - Operating System
  - BIOS
  - Boot
  - UEFI
---
If you are experiencing very slow booting after installing manjaro linux (mine was around 10-15 sec), then do the following things:

# BIOS Tweak

### Legacy ROM
   Diable Legacy Option ROMs
   ![20201206_080501.jpg]({{site.baseurl}}/images/20201206_080501.jpg)

### SMART Reporting
   Disable SMART Reporting
   ![20201206_080639.jpg]({{site.baseurl}}/images/20201206_080639.jpg)

### TMP Security
   Disable TPM Security
   ![20201206_080758.jpg]({{site.baseurl}}/images/20201206_080758.jpg)

### Secure Boot
   Disable Secure Boot
   ![20201206_080911.jpg]({{site.baseurl}}/images/20201206_080911.jpg)

### Fast Boot
   Set Fast Boot to Minimal
   ![20201206_081036.jpg]({{site.baseurl}}/images/20201206_081036.jpg)

### BIOS POST Time
   Set Extended Bios POST Time to 0
   ![20201206_081133.jpg]({{site.baseurl}}/images/20201206_081133.jpg)


# Linux Tweak

1. This service you can stop, disable and mask by
   ```ps
   systemctl disable --now NetworkManager-wait-online.service
   systemctl mask NetworkManager-wait-online.service
   ```

2. If you don’t use any encrypted disks you also can stop, disable and mask lvm2-monitor.service:
   ```ps
   systemctl disable --now lvm2-monitor.service
   systemctl mask lvm2-monitor.service
   ```

3. You can stop snapd service 

   ```ps
   systemctl disable --now snapd.service
   systemctl mask snapd.service
   ```
   
Hope you will have 1 or 2 sec boot time now :)
