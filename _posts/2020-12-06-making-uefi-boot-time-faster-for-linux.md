---
published: true
key: '!!str'
title: Making UEFI Boot Time Faster for Linux
---
If you are experiencing very slow booting after installing manjaro linux (mine was around 10-15 sec), then do the following things:

# BIOS Tweak
1. Diable Legacy Option ROMs
   ![20201206_080501.jpg]({{site.baseurl}}/images/20201206_080501.jpg)
   
2. Disable SMART Reporting
   ![20201206_080639.jpg]({{site.baseurl}}/images/20201206_080639.jpg)

3. Disable TPM Security
   ![20201206_080758.jpg]({{site.baseurl}}/images/20201206_080758.jpg)

4. Disable Secure Boot
   ![20201206_080911.jpg]({{site.baseurl}}/images/20201206_080911.jpg)

5. Set Fast Boot to Minimal
   ![20201206_081036.jpg]({{site.baseurl}}/images/20201206_081036.jpg)

6. Set Extended Bios POST Time to 0
   ![20201206_081133.jpg]({{site.baseurl}}/images/20201206_081133.jpg)


