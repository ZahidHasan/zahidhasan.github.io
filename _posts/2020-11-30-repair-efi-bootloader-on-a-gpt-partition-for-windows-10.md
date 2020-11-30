---
published: true
key: '!!str'
title: Repair EFI Bootloader on a GPT Partition for Windows 10
tags:
  - boot
  - windows
  - Operating System
---
# The Problem
![windows_boot.jpg]({{site.baseurl}}/images/windows_boot.jpg)

# The Solution without any media

### Open Command Prompt
Open Command prompt, if automatic repair doesnt fix.
 ![windows_boot_advanced.jpg]({{site.baseurl}}/images/windows_boot_advanced.jpg)

### Open diskpart
Type and run the command:
```ps
diskpart
```
### Select Hard Disk
Type and run the command:
```ps
sel disk 0
```
### Check the partitions

Type and run the command:
```ps
list vol
```
### Select EFI partition
The EFI partition should be using the FAT32 file system. It is around 100 MB. Assign a drive letter to it that is not already in use:

Type and run the command:
```ps
sel vol <number of volume>
```
```ps
assign letter=<drive letter>:
```
```ps
exit
```

### Repair the boot record:

Type and run the command:
```ps
cd /d <drive letter>:\EFI\Microsoft\Boot\
```
```ps
bootrec /FixBoot
```

If you have `access denied` then do the following:

```ps
bcdboot C:\windows /s <drive letter>
```
