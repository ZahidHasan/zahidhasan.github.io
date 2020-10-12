---
published: true
title: 'Install OpenCV, MinGW and Codeblocks in Windows'
comment: true
layout: article
tags: 
  - OpenCV
  - MinGW
  - Code Blocks
  - C
  - Windows
  - TDM
  - Computer Vision
  - AI
  - Machine Learning
license: false
key: '!!str'
---
Unfortunately OpenCV doesn't come with prebuilt mingw/TDM (64 bit) binaries for windows. In this tutorial, we are going to build them ourselves.

# Environment setup
1. Download the source of [OpenCV 3.2](http://opencv.org/downloads.html). Create the following folders:

    > C:\\opencv\\source\
	> C:\\opencv\\build
    
    ![windows-folder-opencv.jpg]({{site.baseurl}}/images/windows-folder-opencv.jpg){:width="75%"}
    


2. Extract the zipped opencv  to C:\\opencv\\source.

3. Download [codeblocks](http://www.codeblocks.org/downloads) without mingw. Because the default MinGW comes with codeblocks is 32 bit.

4. Download [TDM](http://tdm-gcc.tdragon.net/download) 64 bit version. Install it in C:\\ drive. it will look like  C:\\TDM-GCC-64\\. The bin folder should be registered automatically in system path during the installation process,  if not then using any path editor software you can do it manually. Set C:\\TDM-GCC-64\\bin\\ folder in the system  variable.
 Alternatively, you can use [mingw 64bit](https://sourceforge.net/projects/mingw-w64/?source=typ_redirect)

5. Download and install Cmake from [here](http://www.cmake.org/cmake/resources/software.html). Again the bin folder  of cmake installation directory should be set in system path automatically, if not do it manually.


# Making binaries

1. Open cmake, set source path to C:\\opencv\\source\\ and binary path to C:\\opencv\\build. 
	
    ![cmake-source-build.JPG]({{site.baseurl}}/images/cmake-source-build.JPG){:width="75%"}


2. Hit configure button and from the drop-down menu select ‘codeblocks – MinGW Makefiles’ and press finish. When done uncheck all python stuff ( as it didn't work on my pc). Now hit generate button.


    ![cmake-mingw.JPG]({{site.baseurl}}/images/cmake-mingw.JPG){:width="75%"}
    
    
    ![cmake-python.JPG]({{site.baseurl}}/images/cmake-python.JPG){:width="75%"}
  

3. you will find a codeblocks project file (opencv.cbp) in C:\\opencv\\build folder. Just double click it and codeblocks will load it.

4. Go to ‘*settings*‘, choose ‘*compiler’ and c*lick ‘*Toolchain executable*‘. In the ‘*compiler’s installation directory*‘ field choose the “*bin*” folder of MinGW C:\\TDM-GCC-64\\bin.
   set the following:

   > c compile: gcc.exe\
   > c++ compiler: g++.exe\
   > Linker for dynamic libs: ar.exe

    
    ![cb-toolchain.JPG]({{site.baseurl}}/images/cb-toolchain.JPG){:width="75%"}


5. Finally, from codeblocks, you just need to build it. build target should be set to ‘install’ so that you can find    all the binaries inside the ‘install’ folder of C:\\opencv\\build\\install.
   Just go to ‘build ->select target -> install’ in the codeblocks menu and then hit ‘build->build’ button.
   Go get some tea :) Its gonna take some time (2-3 hour depending on the configuration of your pc).

6. After that set the path C:\\opencv\\build\\install\\x64\\mingw\\bin using path editor.

# Running test program

1. Create a C\+\+ project ‘Test’ in codeblocks.

2. Go to settings -> compiler. Select 'search directories' and in the ‘compiler’ tab chose the followings:

	> C:\\opencv\\build\\install\\include\
	> C:\\opencv\\build\\install\\include\\opencv\
	> C:\\opencv\\build\\install\\include\\opencv2

    
    ![cb-compiler.JPG]({{site.baseurl}}/images/cb-compiler.JPG){:width="75%"}


3. Select ‘Linker’ tab and add C:\\opencv\\build\\install\\x64\\mingw\\lib
	
    
    ![cb-linker.JPG]({{site.baseurl}}/images/cb-linker.JPG){:width="75%"}


4. Under ‘Linker Settings’ tab add required libraries C:\\OpenCV\\my_build\\install\\x64\\mingw\\lib\*.dll.a

    
    ![cb-linker-settings.JPG]({{site.baseurl}}/images/cb-linker-settings.JPG){:width="75%"}



# Code

```c
#include "core.hpp";
#include "highgui.hpp"
#include "imgcodecs.hpp"
    
using namespace cv;
using namespace std;
    
int main()
{
   Mat img;
   img = imread("pic.jpg");
   imshow("Original Image", img);
   waitKey();
}
```

Enjoy!
