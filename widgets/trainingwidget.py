# -*- coding: utf-8 -*-

from .training_ui import Ui_TrainingWidget
from .neuralnetworkwidget import NeuralNetworkWidget
from . import qt_util as qtutil
from .editlabel import EditLabel
from .moveto import MoveTo
from .confusionmatrix import ConfuisionMatrix
from PyQt5.QtWidgets import QWidget,QTreeWidgetItem, QVBoxLayout,QAbstractButton
from PyQt5 import QtCore, QtWidgets,QtGui
from PyQt5.QtCore import Qt,QSize
from PyQt5.QtGui import QColor, QPen, QBrush,QPixmap,QPainter,QPalette
from qcustomplot import QCustomPlot, QCPBars, QCP
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
		# self.confusionMatrixWidget.setStyleSheet(
  #        "background-image:url(\":/images/qcustomtemplate.png\"); background-position: center;" );
		self.lossWidget.setStyleSheet(
			"background-image:url(\":/images/training_vs_validation.jpg\"); background-position: center;")
		self.convFilterWidget.setStyleSheet(
			"background-image:url(\":/images/conv_filter.png\"); background-position: center;")

		labels = ["SSH","OSH","UP1","UP2","UP3","OP1","OP2","OP3","PMA"]

		colors = {
		"SSH":(84,39,136),
		"OSH":(128,115,172),
		"UP1":(222,119,174),
		"UP2":(197,27,125),
		"UP3":(142,1,82),
		"OP1":(127,188,65),
		"OP2":(77,146,33),
		"OP3":(39,100,125),
		"PMA":(200,200,200)
		}

		values = [np.random.randint(len(labels), size=1000) for i in range(len(labels))]
		agg_values = [[v.tolist().count(i) for v in values] for i in range(len(labels))]
		#self.plot_confusion(labels,colors,agg_values)
		
		self.c = ConfuisionMatrix(self.confusionMatrixWidget,
			self.confusionMatrixWidget.width(),self.confusionMatrixWidget.height())
		self.c.fig.canvas.mpl_connect('button_press_event',self.on_confmatrix_clicked)

		labels = ["SSH","OSH","UP1","UP2","UP3","OP1","OP2","OP3","PMA"]
		colors = {
		    "SSH":(84,39,136),
		    "OSH":(128,115,172),
		    "UP1":(222,119,174),
		    "UP2":(197,27,125),
		    "UP3":(142,1,82),
		    "OP1":(127,188,65),
		    "OP2":(77,146,33),
		    "OP3":(39,100,125),
		    "PMA":(200,200,200)
		    }

		values = [np.random.randint(len(labels), size=1000) for i in range(len(labels))]
		agg_values = [[v.tolist().count(i) for v in values] for i in range(len(labels))]
		self.c.plot_confusion(labels,colors,agg_values)
		self.confLayout.addWidget(self.c)

	def on_confmatrix_clicked(self,event):
		x,y = event.xdata, event.ydata
		print(x)
		print(y)