# -*- coding: utf-8 -*-

from .training_ui import Ui_TrainingWidget
from .neuralnetworkwidget import NeuralNetworkWidget
from . import qt_util as qtutil
from .editlabel import EditLabel
from .moveto import MoveTo
from PyQt5.QtWidgets import QWidget,QTreeWidgetItem, QVBoxLayout,QAbstractButton
from PyQt5 import QtCore, QtWidgets,QtGui
from PyQt5.QtCore import Qt,QSize
from PyQt5.QtGui import QColor, QPen, QBrush,QPixmap,QPainter,QPalette
#from qcustomplot import QCustomPlot, QCPBars, QCP, QCPGraph, QCPScatterStyle
import numpy as np
from PIL import Image
import os
import pandas as pd

class PicButton(QAbstractButton):
    def __init__(self, pixmap, parent=None):
        super(PicButton, self).__init__(parent)
        self.pixmap = pixmap

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(event.rect(), self.pixmap)
    def sizeHint(self):
        return self.pixmap.size()


class TrainingWidget(QWidget,Ui_TrainingWidget):
	def __init__(self,parent):
		QWidget.__init__(self,parent)
		self.setupUi(self)
		
		neuralnetworkWidget = NeuralNetworkWidget(self)
		self._neuralnetworkwidget = neuralnetworkWidget
		self.neuralNetworkLayout.addWidget(neuralnetworkWidget)
		spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.neuralNetworkLayout.addItem(spacerItem1)
		self.horizontalLayout.addWidget(PicButton(QPixmap(':/images/play_button.png'),self.playWidget))

		#pix = QPixmap(":/images/play_button.png");
		#bkgnd = bkgnd.scaled(self.size(), Qt::IgnoreAspectRatio);
		#QPalette palette;
		# qpl = QPalette()
		# qpl.setBrush(QPalette.Background, pix);
		# setPalette(qpl);
		self.confusionMatrixWidget.setStyleSheet(
         "background-image:url(\":/images/qcustomtemplate.png\"); background-position: center;" );
		self.lossWidget.setStyleSheet(
			"background-image:url(\":/images/training_vs_validation.jpg\"); background-position: center;")
		self.convFilterWidget.setStyleSheet(
			"background-image:url(\":/images/conv_filter.png\"); background-position: center;")

