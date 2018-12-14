#!/bin/bash


if [[ "$#" -eq 1 ]]
  then
	pyuic5 -o widgets/mainwindow.py widgets/mainwindow.ui
	pyuic5 -o widgets/gigapowers/gigapowerswidget_ui.py widgets/gigapowers/gigapowerswidget.ui
	pyuic5 -o widgets/gigapowers/wellrowwidget_ui.py widgets/gigapowers/wellrowwidget.ui   
	pyrcc5 -o resources/resources_rc.py resources/resources.qrc 
fi


python3.7 iStudio.py
