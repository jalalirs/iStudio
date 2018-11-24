#!/usr/bin/env python
#
import sys
import os

from PyQt5 import QtCore, QtGui, uic

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication 

from widgets.mainwindow import Ui_MainWindow
from widgets.gigapowers import GigaPOWERSWidget
from widgets.datawidget import DataWidget
from core.config import CLASSIFIERS_PATH
import utils


DIR = os.path.abspath(os.path.dirname(__file__))
import resources.resources_rc

class iStudio(QtWidgets.QMainWindow):
	def __init__(self):
		super(iStudio,self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		stream = QFile(':/styles/iStudio.css')
		if stream.open(QIODevice.ReadOnly | QFile.Text):
			self.setStyleSheet(QTextStream(stream).readAll())

		
		dataWidget = DataWidget(self)
		self._dataWidget = dataWidget
		dataLayout = QVBoxLayout()
		dataLayout.addWidget(dataWidget)
		self.ui.pageData.setLayout(dataLayout)

		# gpWidget = GigaPOWERSWidget(self,CLASSIFIERS_PATH)
		# self._gpWidget = gpWidget
		# gplayout = QVBoxLayout()
		# gplayout.addWidget(gpWidget)
		# self.ui.pageGP.setLayout(gplayout)

		# self.on_pbData_released()
		self.ui.mainStackedWidget.setCurrentIndex(0)
		self.uncheck_and_keep(0)

		

	def uncheck_and_keep(self,keepindex):
		toolbarButtons = self.ui.toolbarWidget.findChildren(QtWidgets.QPushButton)
		for i,b in enumerate(toolbarButtons):
			if i != keepindex:
				b.setChecked(False)
			else:
				b.setChecked(True)


	def on_pbGigaPOWER_released(self):
		self.ui.mainStackedWidget.setCurrentIndex(4)
		self.uncheck_and_keep(4)
	def on_pbTest_released(self):
		self.ui.mainStackedWidget.setCurrentIndex(2)
		self.uncheck_and_keep(2)
	def on_pbTrain_released(self):
		self.ui.mainStackedWidget.setCurrentIndex(1)
		self.uncheck_and_keep(1)
	def on_pbData_released(self):
		self.ui.mainStackedWidget.setCurrentIndex(0)
		self.uncheck_and_keep(0)
	def on_pbDeploy_released(self):
		self.ui.mainStackedWidget.setCurrentIndex(3)
		self.uncheck_and_keep(3)


def except_hook(cls,exception,traceback):
	sys.__excepthook__(cls,exception,traceback)

if __name__ == '__main__':
	import sys
	sys.excepthook = except_hook
	app = QtWidgets.QApplication(sys.argv)
	form = iStudio()
	form.show()
	sys.exit(app.exec_())
