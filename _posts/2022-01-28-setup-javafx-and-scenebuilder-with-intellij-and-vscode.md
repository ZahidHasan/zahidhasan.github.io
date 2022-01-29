---
published: true
key: 28-01-2022
title: Setup JavaFX and SceneBuilder with Intellij
Tags:
  - JavaFX
  - Intellij
  - VSCode
  - Java
tags:
  - JavaFX
  - IntelliJ
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
9. Add a button, set id 'btn'. set 'btnClicked' in 'on action' field.
![intellij_scenebuilder_btn.png]({{site.baseurl}}/images/intellij_scenebuilder_btn.png)
10. In scenebuilder go to view->'show sample Controller Skeleton' and copy the code. Paste this code in controller class in intellij.
![intellij_scenebuilder_controller.png]({{site.baseurl}}/images/intellij_scenebuilder_controller.png)
11. In controller class, paste the following line in 'tncCicked()' method.

```ps
   @FXML
    void btncCicked(ActionEvent event) {

        String tittle = txt.getText();
        lbl.setText(tittle);
    }
```
12. Run the program by clicking the play button beside 'HelloApplication()' function. Write something in the text field and click the button, the label will change!
![intellij_fx_executable.png]({{site.baseurl}}/images/intellij_fx_executable.png)
