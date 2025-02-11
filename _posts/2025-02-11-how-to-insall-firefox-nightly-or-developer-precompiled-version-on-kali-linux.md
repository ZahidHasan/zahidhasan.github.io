---
published: true
key: '!!str'
title: 'How to Insall Firefox nightly or developer precompiled version on Kali Linux '
tag:
  - Browser
  - Firefox
  - Linux
  - WSL
---
Firefox Developer Edition is a specialized version of the Mozilla Firefox browser tailored for web developers. It comes packed with advanced tools and features to assist developers in building, testing, and debugging web applications.
In this guide, we’ll walk you through the steps to install and set up Firefox Developer Edition on a Linux system. 

## Download precompiled Firefox
Before we proceed, we need to ensure that we have administrative privileges to install the software. Also, we should establish a stable internet connection to download the Firefox Developer Edition package.

Download Firefox [Developer Edition](https://www.mozilla.org/en-US/firefox/developer/)

![firefox-web.png]({{site.baseurl}}/images/firefox-web.png)

Save it in Download Folder

## Extracting the tar Archive and move to /opt folder
Two ways you can do it. Using GUI or Terminal.
Right click on firefox downloaded file and select extract here.
![extract.png]({{site.baseurl}}/images/extract.png)

or use terminal
![untar.png]({{site.baseurl}}/images/untar.png)


To unzip a "tar.xz" file in Linux, use the command tar -xf [filename.tar.xz] in your terminal, where "[filename.tar.xz]" is the name of the file you want to extract; this will extract the contents of the compressed archive to the current directory. 
Explanation:
```
 tar: This is the command used to manipulate tar archives. 

-x: This flag tells tar to extract files from the archive. 
-f: This flag specifies the filename of the archive you want to extract. 
```
now rename the extracted folder firefox_nightly of firefox_dev to avoid confusion.
if you open the folder you will see firefox executable file right there. You can double click to open it.

![firefox_extracted.png]({{site.baseurl}}/images/firefox_extracted.png)


However, we move the extracted firefox directory to the /opt directory to make it accessible system-wide. To clarify, the /opt directory is a standard location for storing third-party applications in Linux.

open Thunar file manager as root: run in terminal
```
sudo thumar
```
cut and paste the firefox folder into /opt/ directory 
## To Enable Run Firefox from Terminal
we need to use the ln command to create a symbolic link. To explain, this link will allow us to launch Firefox Developer Edition from the terminal:


**sudo ln -s /opt/firefox_nightly/firefox /usr/local/bin/firefox_nightly**


- ln -s – this command creates links between files, and the -s option instructs ln to create a symbolic link
- /opt/firefox_nightly/firefox – represents the path to the executable file firefox found inside the extracted firefox_nightly directory 
- /usr/local/bin/firefox_nightly – constitutes the path and the name of the symbolic link to be created
