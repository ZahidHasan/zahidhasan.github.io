---
published: true
key: '20'
title: 'How to Update Portable JDK to the Latest Version '
tags:
  - Portable
  - JDK
  - Java
---
# Install Portable JDK

1. Download and install portable JDK made specially for portableapps platform from their [website](https://portableapps.com/apps/utilities/OpenJDK64).
2. Once installed, you will notice a new folder named CommonFiles has been created. 
   ![portable_jdk_install2.png]({{site.baseurl}}/images/portable_jdk_install2.png)
3. This CommonFiles folder contains portable JDK and all the portable apps that require jdk to run will automatically find jdk from this CommonFiles folder. Inside CommonFiles folder there is another folder named OpenJDK64. Just rename this OpenJDK64 to java.
4. To check the JDK version go to bin folder, open cmd here and type:
   ```java
      java --version
   ```
   ![jdk_version_portable.png]({{site.baseurl}}/images/jdk_version_portable.png)


# Update Portable JDK

1. Go to the this [site](https://jdk.java.net/), choose desired version, download zip file for windows/x64 and unzip it.
   ![jdk_15_portable.png]({{site.baseurl}}/images/jdk_15_portable.png)

2. Copy all of these files and folders.
3. Go to ```CommonFiles -> java```. Paste and replace those files here.
4. Now go to ```D:\PortableApps\CommonFiles\Java\bin```. open comand prompt and type:
   ```ps
      java --version
   ```
  ![jdk_15_portable_version.png]({{site.baseurl}}/images/jdk_15_portable_version.png)
 

Your JDK is updated now!
