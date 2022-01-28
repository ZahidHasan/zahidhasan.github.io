---
published: true
key: 28-01-2022
title: Setup JavaFX and SceneBuilder with Intellij and VSCode
Tags:
  - JavaFX
  - Intellij
  - VSCode
  - Java
---

1. Download Java FX and Scene builder from [here](https://openjfx.io/).
2. Extract Java FX in C:\Program Files\Java\
3. Install Scenebuilder in default location.
4. In Intellij got to file->settings->plugins. Find, install and activate javafx plugins.
![intellij_javafx_plugins.png]({{site.baseurl}}/images/intellij_javafx_plugins.png)
5. Go to file->new->project choose javafx.
![intellij_javafx_newprojectWindows.png]({{site.baseurl}}/images/intellij_javafx_newprojectWindows.png)
6. Now we need to add javafx library into project. Go to file->project structures->libraries and add extracted javafx lib folder.
![intellij_javajx_lib.png]({{site.baseurl}}/images/intellij_javajx_lib.png)
7. From project pane right click hello-view.fxml file and choose open in scene builder.
![intellij_scenebuilder.png]({{site.baseurl}}/images/intellij_scenebuilder.png)
8. In scene builder, delete existing nodes in hierarchy library and add anchorpane. From control choose textfield. Give it a id 'txt'.
![intellij_scenebuilder_text.png]({{site.baseurl}}/images/intellij_scenebuilder_text.png)



