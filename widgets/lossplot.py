

from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5 import QtWidgets, QtGui

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import sys
import numpy as np

class LossPlot(FigureCanvas):
	def __init__(self,parent=None,width=5,height=5,back_color="#eeefef"):
		self.fig = Figure(figsize=(width,height),dpi=100)
		self.fig.patch.set_facecolor(back_color)
		FigureCanvas.__init__(self,self.fig)
		FigureCanvas.setSizePolicy(self,QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		FigureCanvas.updateGeometry(self)
		self.data = None
		self.values = None
		self.labels = None
		self.colors = None

	def plot(self,train,valid):
		ax = self.fig.gca()
		ind = np.arange(train.size)
		p1 = ax.plot(ind,train)
		p2 = ax.plot(ind,valid)
		ax.set_yticks(ind)
		ax.set_ylim(0,1.2)
		self.fig.subplots_adjust(left=0,right=0.98, wspace = 0, )