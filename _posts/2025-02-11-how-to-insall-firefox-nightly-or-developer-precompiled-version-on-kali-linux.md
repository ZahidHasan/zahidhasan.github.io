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
```
sudo tar xjf Firefox-dev.tar.bz2 -C /opt/
```

