---
published: true
key: '17'
title: Installing Linux GUI environment on Windows 11 using WSL2 and WSLg!
tags:
  - Linux
  - Windows
  - Kali Linux
  - WSL
  - WSL2
  - WSLg
---
#Introduction
It is possible for developers to run both Windows and Linux on a Windows computer at the same time. A Linux distribution (such as Ubuntu, OpenSUSE, Kali, Debian, Arch Linux, etc) can be installed into Windows with the Windows Subsystem for Linux (WSL) and Linux applications, utilities, and Bash commands can be used directly on Windows, without the overhead of a traditional virtual machine or dualboot installation.

You must be running Windows 10 version 2004 and higher (Build 19041 and higher) or Windows 11 to use the commands below.

All the components you need to run WSL can now be installed with just one command. Enter the wsl --install command in PowerShell or Windows Command Prompt in administrator mode, then restart your computer.
```ps
wsl --install
```
This command will enable the features necessary to run WSL and install the Ubuntu distribution of Linux.


