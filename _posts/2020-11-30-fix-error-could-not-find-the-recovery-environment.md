---
published: true
key: '!!str'
title: Fix Error “Could not find the recovery environment” in Windows 10
tags:
  - Windows
  - Operating System
---
![windows_recovery.png]({{site.baseurl}}/images/windows_recovery.png)

1. Check the status of the Windows Recovery Environment on the computer. To do so, open an admin Command Prompt window, and then type the following command:

  ```ps
  reagentc /info
  ```

   ![windows_recovery1.png]({{site.baseurl}}/images/windows_recovery1.png)

2. Windows RE status shows up as Disabled or if the Windows RE location is empty you need to run:
   ```ps
   reagentc /enable
   ```
   ![windows_recovery3.png]({{site.baseurl}}/images/windows_recovery3.png)

Now you should reset your PC.

