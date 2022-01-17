---
published: true
key: '8'
title: Accessing Windows (Host) Folder from Linux (Guest) in Virtualbox
tags:
  - VirtualBox
  - Linux
  - Manjaro
  - KDE
  - Virtualization
  - Operating System
---

Assume you installed manjaro linux as a guest in virtualbox with windows host. Now you want to access folders through them. In order to do that follow the steps:

1. Go to `Devices -> Shared Foldes -> Shared Folders Settings`.

	![Screenshot 2020-11-24 16.05.28.png]({{site.baseurl}}/images/Screenshot 2020-11-24 16.05.28.png)



2. Click `add new shared folder` icon at the right side of the setting window.

	![Screenshot 2020-11-24 16.05.58.png]({{site.baseurl}}/images/Screenshot 2020-11-24 16.05.58.png)



3. In the `folder path` add the windows folder you wanto share. Give it a meaningful name. Check `auto-mount` and `make permanent`. mount pint is where in your linux you can find that windows folder. Set it like `/mnt/C`.

	![Screenshot 2020-11-24 16.06.58.png]({{site.baseurl}}/images/Screenshot 2020-11-24 16.06.58.png)


4. Now in file browser go to `root/mnt` and you will see `C` and `D` folder. However you cannot access them now because of permission related issue.

	![Screenshot_20201124_160956.png]({{site.baseurl}}/images/Screenshot_20201124_160956.png)


5. Run in the terminal
```ps
   sudo usermod -aG vboxsf $USER
```

	![Screenshot_20201124_161132.png]({{site.baseurl}}/images/Screenshot_20201124_161132.png)


6. Now you can access windows files from linux in virtualbox.

	![Screenshot_20201124_163850.png]({{site.baseurl}}/images/Screenshot_20201124_163850.png)
