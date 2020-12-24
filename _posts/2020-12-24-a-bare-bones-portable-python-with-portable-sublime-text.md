---
published: true
key: '!!str'
title: A Bare-bones Portable Python and Sublime Text
tags:
  - Python
  - Sublime Text
  - Portable
---
# Portable Environment Setup 
## Sublime Text and Python

[This](https://sourceforge.net/projects/portable-python/files/) is very small portable python for windows. We will configure portable sublime text to use it.

1. Extract the portable python into a folder like `Portable_PySub.`
2. Extract portable [sublime text](https://www.sublimetext.com/3) into that folder also.

   ![portable_sublime_python.png]({{site.baseurl}}/images/portable_sublime_python.png)

3. In windows Sublime Text find python path from system variables. Since we are using portable version of python, so there is no python path in the system variables. We need to manually locate the path into sublime.
In sublimetext open `preference-> browse package`, got to `User` folder and create a file `Python_Portable.sublime-build` there. 

   ![portable_sublime_python_build_system1.png]({{site.baseurl}}/images/portable_sublime_python_build_system1.png)


   Open the file in text editor and add the following lines:

   ```ps
{
 "cmd": ["D:/Portable_PySub/Portable Python-3.8.6 x64/App/Python/python.exe", "-u", "$file"],
 "file_regex": "^[ ]File \"(...?)\", line ([0-9]*)",
 "selector": "source.python"
 "shell": true
} 
   ```

   ![portable_sublime_python_build_system2.png]({{site.baseurl}}/images/portable_sublime_python_build_system2.png)



Save it and restart sublimetext. 

4. Go to `tool-> build system`.You will see new entry called `Python_portable`, select and build it.
   ![portable_sublime_python_build_system.png]({{site.baseurl}}/images/portable_sublime_python_build_system.png)

   ![portable_sublime_python2.png]({{site.baseurl}}/images/portable_sublime_python2.png)

# Installing Additional Packages
Using `pip` in `Console-Launcher.exe` residing in portable python folder, you can install packages. 
  ![portable_sublime_python_pip.png]({{site.baseurl}}/images/portable_sublime_python_pip.png)


# Running Jupyter Notebook
After installing jupyter run the following command in `Console-Launcher.exe`
```ps
python -m jupyter notebook
```
![portable_sublime_python_jupyter.png]({{site.baseurl}}/images/portable_sublime_python_jupyter.png)

![portable_sublime_python_jupyter1.png]({{site.baseurl}}/images/portable_sublime_python_jupyter1.png)
