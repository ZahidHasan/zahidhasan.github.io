---
published: true
key: '!!str'
title: Installing IntelliJ with JavaFX
tags:
  - IntelliJ
  - Java
  - JavaFX
  - Linux
  - Manjaro
  - Windows
---
## Install IntelliJ in Windows

1. Download IntelliJ community version from their [website](https://www.jetbrains.com/idea/download/).

2. Run the installer  
   ![Capture.PNG]({{site.baseurl}}/images/Capture.PNG)
 
3. Choose installation location. Default is C and that is ok.  
   ![Capture1.PNG]({{site.baseurl}}/images/Capture1.PNG)
 
4. Check the following Options  
   ![Capture3.PNG]({{site.baseurl}}/images/Capture3.PNG)
 
5. Wait until the installation in complete  
   ![Capture3.PNG]({{site.baseurl}}/images/Capture4.PNG)
   
6. Reboot the PC  
   ![Capture5.PNG]({{site.baseurl}}/images/Capture5.PNG)
   
7. Run intelliJ, Choose Dark Theme.  
   ![Capture6.PNG]({{site.baseurl}}/images/Capture6.PNG)
   
8. Disable all plugins.  
   ![Capture8.PNG]({{site.baseurl}}/images/Capture8.PNG)
  
9. Create new project  
   ![Capture9.PNG]({{site.baseurl}}/images/Capture9.PNG)
   
10. Choose `Java` and uncheck `groovy & kotlin`  
    ![Capture10.PNG]({{site.baseurl}}/images/Capture10.PNG)
    
11. Select `create project from template`  
    ![Capture11.PNG]({{site.baseurl}}/images/Capture11.PNG)
    
12. Define project name, location and click finish.  
    ![Capture12.PNG]({{site.baseurl}}/images/Capture12.PNG)
    
13. You will see the following pre-created code  
    ![Capture13.PNG]({{site.baseurl}}/images/Capture13.PNG)
    
14. On the Left side click `project` and project structure will be visible in a panel  
    ![Capture14.PNG]({{site.baseurl}}/images/Capture14.PNG)
 
## Install IntelliJ in Linux (Manjaro)
TBD



## Customizing intelliJ

To Install Plugins go to `file -> settings -> plugins`. 
    
### Syntax Highlight
Type and install `Monokai pro`  
![Capture15.PNG]({{site.baseurl}}/images/Capture15.PNG)
    
### Colorfull Brackets    
Rainbow Brackets  
![Capture16.PNG]({{site.baseurl}}/images/Capture16.PNG)
    
### Highlighting Brackets
Highlight Brackets  
![Capture19.PNG]({{site.baseurl}}/images/Capture19.PNG)
    
### Code AutoCompletion
Kite  
![Capture17.PNG]({{site.baseurl}}/images/Capture17.PNG)
     
### Restart IntelliJ to activate these plugins
![Capture18.PNG]({{site.baseurl}}/images/Capture18.PNG)


## Configuring JavaFX

1. Download JafaFX Library version 15.0.1 from [here](https://gluonhq.com/products/javafx/). or direct [link](D:\OneDrive - Tongxiao\Programming\Java\openjfx-15.0.1_windows-x64_bin-sdk_2.zip)

2. Unzip it into c:

3. Create new project select javafx.
   ![Capture1.PNG]({{site.baseurl}}/images/Capture1.PNG)
4. Choose name and location
   ![Capture2.PNG]({{site.baseurl}}/images/Capture2.PNG)
5. Demo code will be generated
   ![Capture3.PNG]({{site.baseurl}}/images/Capture3.PNG)
6. You will notice intelij cannot find the javafx library (red underline). We have to add fx library. Go to `file -> project structure` and select `library`
  ![Capture4.PNG]({{site.baseurl}}/images/Capture4.PNG)


      