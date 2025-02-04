---
published: true
key: '!!str'
title: How to Configure Memory (RAM) in WSL Linux
tag:
  - Windows
  - Linux
  - WSL
  - RAM
  - Memory
---

## How to configure memory limits in WSL2

Building machine learning models often requires significant computing power.  My home desktop, used for side projects and experiments, recently got a RAM upgrade to 32GB, as the previous amount was insufficient.  However, after the upgrade, my WSL Linux distribution was still limited to 4GB.  This post explains how to adjust the memory allocated to WSL2 distributions, allowing you to increase or decrease it as needed.

## Memory in WSL2
Let's back up and define WSL2 before diving into configuration. The Windows Subsystem for Linux lets you run Linux on Windows without full-blown virtualization.  WSL1 used a custom-built Linux kernel, which, while innovative, had limitations.  Users quickly outgrew its capabilities.

WSL2's key improvement is using a real Linux kernel, unlocking all of Linux's features.  This does mean WSL2 is technically a virtual machine.  But don't let that scare you – it's a fast VM. Boot times are incredibly quick, and performance is generally excellent.  The one common issue?  Managing the memory limit.

WSL2, being a virtual machine, requires allocated resources.  Microsoft's defaults allow WSL2 to access all CPU and GPU cores (if WSLg is installed). Memory is capped at 50% of your system's RAM.  For example, before my RAM upgrade, WSL2 was limited to 16GB on my 32GB system.

It's important to understand that WSL2 can use up to half your RAM and all CPU/GPU cores, but it doesn't necessarily use that much all the time. Unlike traditional VMs with pre-allocated memory, WSL2's memory allocation is dynamic.  It requests more only as needed, up to the 50% limit.  Now, let's explore how to configure that memory limit.

To configure the memory limit for WSL2, create a 
.wslconfig file in your user directory (e.g., C:\Users\wme).  Then, add the desired configuration settings to this file.

```
[wsl2]
memory=16GB
```

After saving the 
.wslconfig file, restart WSL using the command wsl --shutdown.