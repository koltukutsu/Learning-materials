
# Aesk - Modern GUI Try / PyQt6-Pyside6
# 


> **Warning**: this project was created using PySide6 and Python 3.9, using previous versions can cause compatibility problems.
> **Warning**: other requirements and versions are put into the requirements.txt file

# Temalar
![Aesk_Dracula_Dark](https://user-images.githubusercontent.com/55881663/117573165-2d59fd80-b0df-11eb-880c-f8c4f5bb506e.png)
####Yapilmadi!!
![Aesk_Dracula_Light]()

# Running
> Inside your preferred terminal run the commands below depending on your system, remembering before installing Python 3.9> and PySide6 "pip install PySide6". Of course this is for WINDOWS
> I Didnt yet make the thigns for linux 
> ## **Windows**:
```console
python main.py
```
> ## **MacOS and Linux**:
```console
python3 main.py
```
# Compiling
> ## **Windows**:
```console
python setup.py build
cx_freeze is in use
```

# Project Files And Folders
> **main.py**: application initialization file.

> **main.ui**: Qt Designer project.

> **resouces.qrc**: Qt Designer resoucers, add here your resources using Qt Designer. Use version 6 >

> **setup.py**: cx-Freeze setup to compile your application (configured for Windows).

> **themes/**: add here your themes (.qss).

> **modules/**: module for running PyDracula GUI.

> **modules/app_funtions.py**: add your application's functions here.
Up
> **modules/app_settings.py**: global variables to configure user interface.

> **modules/resources_rc.py**: "resource.qrc" file compiled for python using the command: ```pyside6-rcc resources.qrc -o resources_rc.py```.

> **modules/ui_functions.py**: add here only functions related to the user interface / GUI.

> **modules/ui_main.py**: file related to the user interface exported by Qt Designer. You can compile it manually using the command: ```pyside6-uic main.ui> ui_main.py ```.
After expoting in .py and change the line "import resources_rc" to "from. Resoucers_rc import *" to use as a module.

> **images/**: put all your images and icons here before converting to Python (resources_re.py) ```pyside6-rcc resources.qrc -o resources_rc.py```.

# Thanks to 
>the Dracula Team for the inspiration and WANDERSON M.PIMENTA for this beautiful work

>https://draculatheme.com/

>https://github.com/Wanderson-Magalhaes



