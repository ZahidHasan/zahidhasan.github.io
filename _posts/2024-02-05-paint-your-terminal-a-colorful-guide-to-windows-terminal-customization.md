---
published: true
key: 05-02-2024
title: 'Paint Your Terminal: A Colorful Guide to Windows Terminal Customization'
tag:
  - Windows Terminal
  - Powershell
  - CMD
  - Colors
  - Themes
  - oh-my-posh
---
Ever wonder why does your terminal or powershell look so dull? Why doesnt it look like these:

<img src="https://raw.githubusercontent.com/ZahidHasan/zahidhasan.github.io/master/images/terminal-colorful-1.jpg" width="600" height="300" />

<img src="https://raw.githubusercontent.com/ZahidHasan/zahidhasan.github.io/master/images/terminal-colorful-2.jpg" width="600" height="300" />


Lets give it a colorful life!

You need the following:
>1. Windows Terminal
>2. oh-my-posh

## What is Wndows Terminal and oh-my-posh?
Windows Terminal is a powerful tool for developers who frequently work with command-line interfaces. Any application that has a command line interface can be run inside Windows Terminal. This includes everything from PowerShell and Command Prompt to Azure Cloud Shell and any WSL distribution such as Ubuntu or Oh-My-Zsh. 
By customizing its appearance, you can make your terminal sessions more enjoyable and efficient. In this article, we’ll explore how to add vibrant colors and stylish themes to your Windows Terminal using Oh-My-Posh.

## Installing Windows Terminal
Before we dive into themes, make sure you have Windows Terminal installed.
Download canary version from [github](https://aka.ms/terminal-canary-installer)
Or using winget

```ps
winget install Microsoft.WindowsTerminal 
```

## Installing oh-my-posh
### Using winget

```ps
winget install JanDeDobbeleer.OhMyPosh
```

![oh-my-posh-winget-install.png]({{site.baseurl}}/images/oh-my-posh-winget-install.png)

You can see the available themes [here](https://ohmyposh.dev/docs/themes)
or see them inside Terminal:
```ps
Get-PoshThemes
```
<img src="https://raw.githubusercontent.com/ZahidHasan/zahidhasan.github.io/master/images/get-posh-themes.jpg" width="600" height="300" />

If you get error like this:

<img src="https://raw.githubusercontent.com/ZahidHasan/zahidhasan.github.io/master/images/get-poshtheme-error.png" width="600" height="300" />

then create a powershell profile as follows:

1. use the following PowerShell command to create a profile
```ps
	new-item -type file -path $profile -force
```
2. Add the following to the end of your PowerShell profile file using notepad to set the paradox theme. (Replace paradox with the theme of your choice.)
```ps
oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\paradox.omp.json" | Invoke-Expression 
```
Now, each new PowerShell instance will start by importing Oh My Posh and setting your command line theme.

## Adding Fonts and Icons
Download the fonts from [here](https://github.com/haasosaurus/nerd-fonts/blob/regen-mono-font-fix/patched-fonts/LiberationMono/complete/Literation%20Mono%20Nerd%20Font%20Complete%20Mono%20Windows%20Compatible.ttf)

Open PowerShell and select your new font 'LiberationMono NF' from the list.
You can also download and install  [Meslo LGM NF](https://github.com/ryanoasis/nerd-fonts/releases/download/v3.0.2/Meslo.zip) fonts.
Now Run the code in Powershell
```ps
Install-Module Terminal-Icons -Scope CurrentUser
```
Next, navigate to that path, and you will find a “Microsoft.PowerShell_profile.ps1” file. Open it with Notepad, add the below lines, and save the file. Now, you can close the Notepad file.

```ps
Import-Module Terminal-Icons
```
<img src="https://raw.githubusercontent.com/ZahidHasan/zahidhasan.github.io/master/images/profile.jpg" width="600" height="300" />
