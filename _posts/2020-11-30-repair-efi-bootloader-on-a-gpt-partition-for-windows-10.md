---
published: true
key: '!!str'
title: Repair EFI Bootloader on a GPT Partition for Windows 10
---
# The Problem
![windows_boot.jpg]({{site.baseurl}}/images/windows_boot.jpg)

## Solution without any media

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
The EFI partition should be using the FAT32 file system. It is around 100 MB. Assign a drive letter to it that is not already in use:

Type and run the command:

sel vol <number of volume>

Type and run the command:

assign letter=<drive letter>:

Type and run the command:

exit
