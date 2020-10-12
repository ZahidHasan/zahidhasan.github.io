---
published: true
title: Configure SublimeText and WinPython in Windows
tags:
  - WinPython
  - Sublime Text 
  - Kite 
  - Portable 
  - IDE
  - Data Science
  - AI
  - Machine Learning
  - Sublime Linter
key: '!!str'
---
If the size of the Anaconda gives you a headache then you may use WinPython distribution which requires less space. After installing some of the ml libraries the installation size of Anaconda goes up to 12GB while WinPython takes only around 3GB. WinPython provides a way to the portable installation as well. A portable setup has some advantages. For example, if you reinstall the operating system, you don’t need to set up the environment again from scratch.

In order to setup portable python environment for machine learning we need the following things

1. Python Interpreter (WinPython)
2. Python library for ML (WinPython)
3. Code Editor (Sublime text) supporting linting, auto completion and themes.

# WinPython
WinPython includes both python interpreter and libraries for machine learning as Anaconda distribution do. However, unlike Anaconda distribution, WinPython supports portable installation.

1. Download [WinPython](https://sourceforge.net/projects/winpython/files/) and unzip it into your desired location. I unzipped it into

	>D:\AI\Programming\WinPython

	![winpython.png]({{site.baseurl}}/images/winpython.png){:width="75%"}

2. Register WinPython to the Operating System. Add the following paths into the system variables!.


	>D:\AI\Programming\WinPython\
	>D:\AI\Programming\WinPython\scripts\
	>D:\AI\Programming\WinPython\python-3.8.1.amd64\
	>D:\AI\Programming\WinPython\python-3.8.1.amd64\Scripts\
	>D:\AI\Programming\WinPython\python-3.8.1.amd64\libs

   ![winpython_path.png]({{site.baseurl}}/images/winpython_path.png)
   
3. Now start cmd and type: (if cmd is already open, restart it)
   ```ps
   Where python
   Python --version
   ```
   
   ![python_version_win.png]({{site.baseurl}}/images/python_version_win.png)
   
   The above output confirms the successful installation of WinPython. We are now ready to install some machine learning libraries using PIP command.
   
   
# SublimeText
Download and extract portable version of sublime text into your preferred location. Start sublime text and check build system as python:

```Tools > Build System > python```. Press ```ctr+B``` to run code.

![sublimetext_build.png]({{site.baseurl}}/images/sublimetext_build.png)

### Install color scheme
Install themes from package control
1. Tomorrow Night
2. Monokai pro

### Install additional packages
Install themes from package control
1. SideBar enhancement
2. A file icon
  
# Linter
Linting is the process of checking the source code for Programmatic as well as Stylistic errors. Linting highlights syntactical and stylistic problems in your Python source code, which oftentimes helps you identify and correct subtle programming errors or unconventional coding practices that can lead to errors. For example, linting detects the use of an uninitialized or undefined variable, calls to undefined functions, missing parentheses, and even more subtle issues such as attempting to redefine built-in types or functions.


### Install SublimeLinter and SublimeLinter-flake8
1. Install SublimeLinter from package control. Press ```ctr+shift+p``` to open package control and select ```package control: install package```

   ![sublimetext_install_packages.png]({{site.baseurl}}/images/sublimetext_install_packages.png)

2. Search for ``` SublimeLinter``` and ```SublimeLinter-flake8```. 

3. Install both of them.


### Install flake8
```ps
pip install flake8
sud pip install flake8
```

### Configure SublimeLinter settings
Open sublime text settings. ```preference > package settings > sublime linter > settings```. Add the following into user setting.

```bash
// SublimeLinter Settings - User
{
    "show_panel_on_save": "never",
    "gutter_theme": "Packages/Theme - Monokai Pro/Monokai Pro.gutter-theme",
    "styles": [
        {
            "mark_style": "outline",
            "priority": 1,
            "scope": "region.orangish",
            "icon": "warning",
            "types": [
                "warning"
            ]
        },
        {
            "mark_style": "squiggly_underline",
            "priority": 1,
            "scope": "region.redish",
            "icon": "error",
            "types": [
                "error"
            ]
        }
    ]
}
```

![sublimetext_sublimelinter_settings.png]({{site.baseurl}}/images/sublimetext_sublimelinter_settings.png)


# Kite: Auto-completion
Kite is an AI-based autocompletion tool for Python. It uses machine learning to help you with the suggestions for keywords while coding in Python. Kite will automatically install plugins for sublime text.

![kite.gif]({{site.baseurl}}/images/kite.gif)


# Troubleshooting 

### input() doesn’t work in sublimetext
SublimeText with input() function doesn't return any output values. 
To solve this problem we will use ```terminus``` package. 

1. Install ```terminus``` from package control.

2. Go to ```preference->browse package```. Inside ```user``` folder and create a file ```Python_Terminus.sublime-build```. Add the following code into this file

   ```bash
   {
       "target": "toggle_terminus_panel",
       "cmd": ["C:/Python37/python.exe", "-u", "$file"],
       "file_regex": "^[ ]File \"(...?)\", line ([0-9]*)",
       "auto_close": true,
       "selector": "source.python"
   }
   ```
      NOTE: use forward slash (/) in path for windows. Append extra input() method in the source code to prevent auto close of terminus output. Setting  ```"auto_close": false,``` disable sublimetext to execute second time unless sublimetext is restarted.
      
### warning "Indentation contains tabs"

```view -> Indentation -> Convert indentation to spaces```

![sublimetext_warning_tab.png]({{site.baseurl}}/images/sublimetext_warning_tab.png)

