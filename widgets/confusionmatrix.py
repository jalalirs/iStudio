# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/confusionmatrix.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5 import QtWidgets, QtGui

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import sys
import numpy as np

class ConfuisionMatrix(FigureCanvas):
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

    def plot(self,labels,colors,values):
        N = len(labels)
        ind = np.arange(N)    # the x locations for the groups
        width = 0.35       # the width of the bars: can also be len(x) sequence
        plots = []
        ax = self.fig.gca()
        ax.set_facecolor("#eeefef")
        for v in values:
            p = ax.barh(ind,v, height=0.35)
            plots.append(p)
        
        ax.set_yticks(ind)
        ax.set_yticklabels(labels)
        self.fig.subplots_adjust(top = 1, wspace = 0)
