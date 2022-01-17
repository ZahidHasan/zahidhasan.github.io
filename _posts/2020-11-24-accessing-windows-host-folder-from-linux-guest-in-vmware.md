---
published: true
key: '9'
title: Accessing Windows (Host) Folder from Linux (Guest) in Vmware
tags:
  - Vmware
  - Linux
  - Manjaro
  - Virtualization
  - Operating System
  - KDE
---
Assume you installed manjaro linux as a guest in virtualbox with windows host. Now you want to access folders through them. In order to do that follow the steps:

1. Goto `VM -> Settings`.
   ![Screenshot 2020-11-24 21.22.53.png]({{site.baseurl}}/images/Screenshot 2020-11-24 21.22.53.png)

2. In the setting window open `options` tab, there you find `Shared Folders` option.
   ![Screenshot 2020-11-24 21.23.36.png]({{site.baseurl}}/images/Screenshot 2020-11-24 21.23.36.png)

3. Click `add` right side of the windows, chose a windows folder in `Host Path`, click next.
   ![Screenshot 2020-11-24 21.24.12.png]({{site.baseurl}}/images/Screenshot 2020-11-24 21.24.12.png)

4. Check `Enable this share`
   ![Screenshot 2020-11-24 21.24.21.png]({{site.baseurl}}/images/Screenshot 2020-11-24 21.24.21.png)

5. Finally check `Always enabled`.
   ![Screenshot 2020-11-24 21.24.46.png]({{site.baseurl}}/images/Screenshot 2020-11-24 21.24.46.png)

6. You can find your windows folders in `/mnt/hgfs/`
   ![Screenshot_20201124_212517.png]({{site.baseurl}}/images/Screenshot_20201124_212517.png)

7. In case of any error, run in terminal
```ps
   sudo vmhgfs-fuse .host:/ /mnt/hgfs/ -o allow_other -o uid=1000
```
