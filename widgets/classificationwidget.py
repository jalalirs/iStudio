
from .wellrowwidget_ui import Ui_WellRowWidget
from PyQt5.QtWidgets import QWidget,QStyle, QStyleOption
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPainter, QColor, QPen

classificationColors = {
	"SSH":(84,39,136),
	"OSH":(128,115,172),
	"UP1":(222,119,174),
	"UP2":(197,27,125),
	"UP3":(142,1,82),
	"OP1":(127,188,65),
	"OP2":(77,146,33),
	"OP3":(39,100,125),
	"PMA":(200,200,200),
	"NOE": (255,255,255)
}

class ClassificationWidget(QWidget):
	clicked = pyqtSignal(str,int)
	#entered = pyqtSignal(object)
	def __init__(self,parent,wellName,wid,classification):
		QWidget.__init__(self,parent)

		self._classification = classification
		self._id = wid
		self._wellname = wellName
		r,g,b = classificationColors[classification]
		self._r = r
		self._g = g
		self._b = b
		self._color = (r,g,b)
		self._hovered = False
		self.setMaximumSize(QtCore.QSize(1000, 30))
		self.setMinimumSize(QtCore.QSize(2, 30))
		self.unframe()
		self.setObjectName("cl%d" % wid)

	def enterEvent(self,event):
		#self.entered.emit(self)
		self.frame()
		self._hovered = True
	def leaveEvent(self,event):
		self.unframe()	
		self._hovered = False
	def mouseReleaseEvent(self, event):
		self.clicked.emit(self._wellname,self._id)
	def frame(self):
		self.setStyleSheet("background-color: rgb(%d, %d, %d); border: 2px solid black" % (self._r,self._g,self._b))
		self.refresh()
	def unframe(self):
		self.setStyleSheet("background-color: rgb(%d, %d, %d); border: 1px solid white" % (self._r,self._g,self._b))
		self.refresh()
	def refresh(self):
		self.style().unpolish(self)
		self.style().polish(self)
	

	def paintEvent(self, event):

		opt = QStyleOption()
		opt.initFrom(self)
		painter = QPainter(self)
		self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)
		