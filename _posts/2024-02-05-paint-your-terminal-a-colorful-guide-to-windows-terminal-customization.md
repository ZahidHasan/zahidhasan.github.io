---
published: true
key: 05-02-2024
title: 'Paint Your Terminal: A Colorful Guide to Windows Terminal Customization”'
tag:
  - Windows Terminal
  - Powershell
  - CMD
  - Colors
  - Themes
  - oh-my-posh
---
Do you ever wonder why does your terminal, cmd or powershell is so dull? Why doesnt it look like these:
<img src="https://raw.githubusercontent.com/ZahidHasan/zahidhasan.github.io/master/images/terminal-colorful-1.jpg" width="600" height="400" />

![terminal-colorful-1.jpg]({{site.baseurl}}/images/terminal-colorful-1.jpg)
![terminal-colorful-2.jpg]({{site.baseurl}}/images/terminal-colorful-2.jpg)

Lets give it a life!

You need the following:
>1. Windows Terminal Canary
>2. Powershell7
>3. oh-my-posh

## What is Wndows Terminal and oh-my-posh?
Windows Terminal is a powerful tool for developers who frequently work with command-line interfaces. Any application that has a command line interface can be run inside Windows Terminal. This includes everything from PowerShell and Command Prompt to Azure Cloud Shell and any WSL distribution such as Ubuntu or Oh-My-Zsh. 
By customizing its appearance, you can make your terminal sessions more enjoyable and efficient. In this article, we’ll explore how to add vibrant colors and stylish themes to your Windows Terminal using Oh-My-Posh.

## Installing Windows Terminal
Before we dive into themes, make sure you have Windows Terminal installed.
Download canary version from [github](https://aka.ms/terminal-canary-installer)

## Installing oh-my-posh
**Using winget**
`winget install JanDeDobbeleer.OhMyPosh`
![oh-my-posh-winget-install.png]({{site.baseurl}}/images/oh-my-posh-winget-install.png)
You can see the available themes [here](https://ohmyposh.dev/docs/themes)
![oh-my-posh-themes.png]({{site.baseurl}}/images/oh-my-posh-themes.png)


## Configuring Terminal with oh-my-posh

1. use the following PowerShell command to create a profile
```powershell
	new-item -type file -path $profile -force```
2. Add the following to the end of your PowerShell profile file to set the paradox theme. (Replace paradox with the theme of your choice.)
```powershell
oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\paradox.omp.json" | Invoke-Expression ```

Now, each new PowerShell instance will start by importing Oh My Posh and setting your command line theme.