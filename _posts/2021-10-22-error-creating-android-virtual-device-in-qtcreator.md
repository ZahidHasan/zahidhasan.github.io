---
published: true
key: '!!str'
title: Error Creating Android Virtual Device in QtCreator
tags:
  - AVD
  - Android
  - Qt
  - Java
---
![Screenshot_2021-10-22_07-17-29.png]({{site.baseurl}}/images/Screenshot_2021-10-22_07-17-29.png)

### Append the following line in 3 of your environment variable files

```ps
unset _JAVA_OPTIONS
```
   - .bashrc
   - .zshrc and 
   - .profile files

