# -*- coding: utf-8 -*-

from .neuralnetwork_ui import Ui_NeuralNetwork
from .nnlayerwidget import NNLayerWidget
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


class NeuralNetworkWidget(QWidget,Ui_NeuralNetwork):
	def __init__(self,parent):
		QWidget.__init__(self,parent)
		self.setupUi(self)


		self.horizontalLayout_4.addWidget(NNLayerWidget(self,0))
		self.horizontalLayout_4.addWidget(NNLayerWidget(self,1))
		self.horizontalLayout_4.addWidget(NNLayerWidget(self,2))