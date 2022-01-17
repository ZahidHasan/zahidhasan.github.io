---
published: true
title: Error Creating Android Virtual Device in QtCreator
tags:
  - AVD
  - Android
  - Qt
  - Java
  - Linux
  - Kali
---
![Screenshot_2021-10-22_07-17-29.png]({{site.baseurl}}/images/Screenshot_2021-10-22_07-17-29.png)

## Append the following line in each of 3 environment-variable files located in home folder

```ps
unset _JAVA_OPTIONS
export PATH="/usr/lib/jvm/jdk-17/bin:$PATH"

export PATH="/home/kali/Android/Sdk/platform-tools:$PATH"
export PATH="/home/kali/Android/Sdk/emulator:$PATH"
export PATH="/home/kali/Android/Sdk/platforms/android-30:$PATH"
```
   - .bashrc
   - .zshrc and 
   - .profile files


### Unset Java Options by adding
```ps
unset _JAVA_OPTIONS
```


### Add Java 17 bin folder in environment
```ps
export PATH="/usr/lib/jvm/jdk-17/bin:$PATH"
```

### Add platform-tool, emulator and android api level in environment.
```ps
export PATH="/home/kali/Android/Sdk/platform-tools:$PATH"
export PATH="/home/kali/Android/Sdk/emulator:$PATH"
export PATH="/home/kali/Android/Sdk/platforms/android-30:$PATH"
```
