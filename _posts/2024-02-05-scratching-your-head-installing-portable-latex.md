---
published: true
key: 05-02-2024
title: Scratching Your Head Installing Portable Latex
tag:
  - Latex
  - Portable
  - Portable Latex
  - Windows
---
## The Error!
Acccording to Miketex website you have to Just download the standard installer and rename it to miktex-portable.exe. You start installaton and after few minutes encounter this error:

![portable-latex-installation-error.png]({{site.baseurl}}/images/portable-latex-installation-error.png)

## Solution-1: Command Line Installer
Download Command Line Installer from miketex site.
![miketex-commandline-installer.png]({{site.baseurl}}/images/miketex-commandline-installer.png)

Unzip and copy the "miktexsetup_standalone.exe" file into the root directory of C:\
Open Terminal and run :
```ps
C:\miktexsetup_standalone.exe --verbose --local-package-repository=D:\MikTex\packages\basic --package-set=basic download
```

![miketex-commandline-installer-2.png]({{site.baseurl}}/images/miketex-commandline-installer-2.png)

Now run:
```ps
 C:\miktexsetup_standalone.exe --verbose --local-package-repository=D:\MikTex\packages\basic --package-set=basic --portable=D:\MikTex-Portable\basic --use-registry=no --modify-path=no install
 ```