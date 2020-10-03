---
cover: https://res.cloudinary.com/canonical/image/fetch/f_auto,q_auto,fl_sanitize,e_sharpen,w_819,h_478/https://dashboard.snapcraft.io/site_media/appmedia/2018/03/linux.png
published: true
title: Configure SublimeText and Anaconda in Linux
tags: >-
  Anaconda SublimeText Python Linux Flake8 SublimeLinter  MachineLearning
  DataScience Kite AI IDE
subtitle: Configuring SublimeText and Anaconda in Linux
key: '!!str'
---
# Why SublimeText and Linux?
You want SublimeText because you do not want to wait around for laggy code-complete windows, random 2 second hitches or dealing with poor performance due to a buggy editor. Sublime opens in less than a second, it feels nearly instant. It is the fastest text editor that you can use for writing code. It opens almost immediately and performs very quick searches. SublimeText is a native app written in C++, so its footprint is much lower.

You want Linux because you do not want to deal with having to restart pc after a bit because its performance deteriorates over time.


# Anaconda Distribution
1. Download Anaconda or Miniconda for linux from [here](https://www.anaconda.com/products/individual#linux).

2. Go to downloaded folder, open terminal here, type ```./A``` and press ```tab```. It will display anaconda file name on terminal.

   ```ps
   ./Anaconda3-2020.07-Linux-x86_64.sh
   ```

   ![anaconda_installation.png]({{site.baseurl}}/images/anaconda_installation.png)

 3. Follow on screen instructions. Set installation location to```/home/anaconda3/```.
   Dont forget to type 'yes' at the last.


# SublimeText
### Install SublimeText
Install SublimeText from package manager (pamac-manager or Add/Remove Software).

![pacman_manager_sublimetext.png]({{site.baseurl}}/images/pacman_manager_sublimetext.png)

### Configure Python Path
1. By default sublimetext use system’s default python which is ```/usr/lib/python```. To verify this run the following code in sublimetext:

   ```python
   import sys
   print(sys.path)
   ```

   you will see ```/usr/lib/python``` which is default python libraries location.

   ![st_python_path.png]({{site.baseurl}}/images/st_python_path.png)

   In order to make SublimeText use anaconda’s implementation of python, follow the steps. 

2. open ```preference-> browse package``` in sublimetext, got to ```user``` folder and create a file ```anaconda.sublime-build```. Inside this file add the following line:
   
   ```bash
   {
 	 "cmd":["path to python", "-u", "$file"],
 	 "file_regex": "^[ ]File \"(...?)\", line ([0-9]*)",
 	 "selector": "source.python"
   } 
   ```
   
   ![sublimetext_browse_package.png]({{site.baseurl}}/images/sublimetext_browse_package.png){:width="60%"}

3. To find the path of anaconda python, open terminal and type:

   ```ps
   which python
   ```
   
   ![python_path.png]({{site.baseurl}}/images/python_path.png)
 
   It will give the path of anaconda’s python binaries. Copy this path and paste in ```“cmd”: [“paste path here”]``` of ```anaconda.sublime-build``` file. The ```anaconda.sublime-build``` file will look like:
    
   ![anaconda.sublime-build.png]({{site.baseurl}}/images/anaconda.sublime-build.png){:width="60%"}

4. Save it and restart sublimetext. Go to ```tool-> build system```.You will see new entry called  ```anaconda```, select it and run the above code again. now you will see 
```/home/zahidhasan/anaconda3/lib/python38``` in the output which confirms that your sublimetext now points to the anaconda’s python.

   ![st_python_path1.png]({{site.baseurl}}/images/st_python_path1.png)

### Install Color Scheme
Install themes from package control
1. Tomorrow Night
2. Monokai pro

### Install additional Packages
Install themes from package control
1. SideBar enhancement
2. A file icon
  
  
# Linter
Linting is the process of checking the source code for Programmatic as well as Stylistic errors. For example, linting detects the use of an uninitialized or undefined variable, calls to undefined functions, missing parentheses, and even more subtle issues such as attempting to redefine built-in types or functions.


### Install SublimeLinter
1. Press ```ctr+shift+p``` to open package control and select ```package control: install package```

   ![sublimetext_install_packages.png]({{site.baseurl}}/images/sublimetext_install_packages.png)

2. Search for ``` SublimeLinter``` and install. 



### Install SublimeLinter-flake8
1. Press ```ctr+shift+p``` to open package control and select ```package control: install package```

   ![sublimetext_install_packages.png]({{site.baseurl}}/images/sublimetext_install_packages.png)

2. Search for ```SublimeLinter-flake8``` and install. 


### Install flake8
1. Since SublimeLinter always uses system's library even if we've made SublimeText use anaconda python. So, we need to install flake8 in the system. To do this we need to disable Anaconda by renaming the folder ```anaconda3```to ```anaconda3X``` and run: 
     
   ```ps
   pip install flake8
   sud pip install flake8
   ```
   
2. Finally rename ```anaconda3X``` folder back to its default name ```anaconda3```.


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
### flake8 not found 
1. Even if we've made SublimeText use anaconda python, SublimeLinter in SublimeText still use default python. If you see flake8 error at the status bar of sublimetext like:
	
   ![st_flake8_not_found.png]({{site.baseurl}}/images/st_flake8_not_found.png)
    
   That means flake8 was installed in anaconda's library not in system's library. Since SublimeLinter always uses system's library, so, we need to install flake8 in system. To do this:

2. Rename the folder ```anaconda3``` to ```anaconda3X``` and run: 
     
   ```ps
   pip install flake8
   sud pip install flake8
   ```
 
3. Rename ```anaconda3X``` folder back to its default name ```anaconda3```. 

4. Run sublimetext again.

### input() doesn’t work in sublimetext
SublimeText with input() function doesn't return any output values. 
To solve this problem we will use ```terminus``` package. 

1. Install ```terminus``` from package control.

2. Go to ```preference->browse package```. Inside ```user``` folder and create a file ```Python_Terminus.sublime-build```. Add the following code into this file

   1. For windows:
   
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
      
    2. For Linux:
    
       ```bash
       {
        "target": "toggle_terminus_panel",
        "cmd": [""\home\anaconda3\bin\python", "-u", "$file"],
        "file_regex": "^[ ]File \"(...?)\", line ([0-9]*)",
        "auto_close": true,
        "selector": "source.python"
       }
       ```

### warning "Indentation contains tabs"

```view -> Indentation -> Convert indentation to spaces```

![sublimetext_warning_tab.png]({{site.baseurl}}/images/sublimetext_warning_tab.png)
