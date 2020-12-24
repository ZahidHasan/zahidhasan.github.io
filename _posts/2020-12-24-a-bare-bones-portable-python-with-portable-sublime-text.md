---
published: false
key: '!!str'
title: A Bare-bones Portable Python and Sublime Text
---
# Portable Environment Setup (Sublime Text and Python)

[This](https://sourceforge.net/projects/portable-python/files/) is very small portable python for windows. In this tutorial we will configure sublime text to use it.

1. Extract the portable python into a folder like `Portable_PySub`.
2. Extract portable [sublime text](https://www.sublimetext.com/3) into that folder also.

   ![portable_sublime_python.png]({{site.baseurl}}/images/portable_sublime_python.png)

3. In windows Sublime Text find python path from system variables. Since we are using portable version of python, so there is no python path in system variables. We need to manually locate the path into sublime.
open `preference-> browse package` in sublimetext, got to `User` folder and create a file `Python_Portable.sublime-build`. Inside this file add the following line:
```ps
{
 "cmd": ["D:/Portable_PySub/Portable Python-3.8.6 x64/App/Python/python.exe", "-u", "$file"],
 "file_regex": "^[ ]File \"(...?)\", line ([0-9]*)",
 "selector": "source.python"
 "shell": true
} 
```
Save it and restart sublimetext. 

4. Go to `tool-> build system`.You will see new entry called `Python_portable`, select it and run.

   ![portable_sublime_python2.png]({{site.baseurl}}/images/portable_sublime_python2.png)

# Installing Additional Packages


# Running Jupyter Notebook