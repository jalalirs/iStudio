# -*- coding: utf-8 -*-

from .training_ui import Ui_TrainingWidget
from .neuralnetworkwidget import NeuralNetworkWidget
from . import qt_util as qtutil
from .editlabel import EditLabel
from .moveto import MoveTo
from PyQt5.QtWidgets import QWidget,QTreeWidgetItem, QVBoxLayout
from PyQt5 import QtCore, QtWidgets,QtGui
from PyQt5.QtCore import Qt,QSize
from PyQt5.QtGui import QColor, QPen, QBrush
#from qcustomplot import QCustomPlot, QCPBars, QCP, QCPGraph, QCPScatterStyle
import numpy as np
from PIL import Image
import os
import pandas as pd


class TrainingWidget(QWidget,Ui_TrainingWidget):
	def __init__(self,parent):
		QWidget.__init__(self,parent)
		self.setupUi(self)
		
		neuralnetworkWidget = NeuralNetworkWidget(self)
		self._neuralnetworkwidget = neuralnetworkWidget
		self.neuralNetworkLayout.addWidget(neuralnetworkWidget)
		spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.neuralNetworkLayout.addItem(spacerItem1)