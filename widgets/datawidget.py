# -*- coding: utf-8 -*-

from .datawidget_ui import Ui_DataWidget
from . import qt_util as qtutil
from PyQt5.QtWidgets import QWidget,QTreeWidgetItem, QVBoxLayout
from PyQt5 import QtCore, QtWidgets,QtGui
from PyQt5.QtCore import Qt,QSize
from PyQt5.QtGui import QColor, QPen, QBrush
from qcustomplot import QCustomPlot, QCPBars, QCP, QCPGraph, QCPScatterStyle
import numpy as np
from PIL import Image
import os
import pandas as pd
from PIL.ImageQt import ImageQt

class ImageDataItem:
	def __init__(self,name,path):
		self._name = name
		self._path = path
		self._image =  Image.open(path)


class Dataset:
	def __init__(self,datasetpath,protocol = "scikitlearn"):
		self._path = datasetpath
		self._protocol = protocol	
		self._data = {}
		self._labels = []
		self._sections = {}
		self._data_df = None
		self._name = self._path.split("/")[-1]
	
	def load_scikitlearn(self):
		
		sections = [name for name in os.listdir(self._path) 
			if os.path.isdir(os.path.join(self._path, name))]
		if len(sections) <= 0:
			return

		labels_dirs = [name for name in os.listdir("%s/%s" % (self._path,sections[0]))
			if os.path.isdir(os.path.join(self._path,sections[0], name))]
		
		self._labels = [name.split(".")[1] for name in labels_dirs]

		data = []
		for s in sections:
			for i,l in enumerate(labels_dirs):
				path = "%s/%s/%s" % (self._path,s,l)
				data += [ (f.split(".")[0],f.split(".")[0],s,self._labels[i],os.path.join(path,f)) for f in os.listdir(path) if os.path.isfile(os.path.join(path,f)) ]

		self._data_df = pd.DataFrame(data,columns=["id","name","section","label","path"])
		self._data_df.set_index("id",inplace=True)
	@property
	def sections_names(self):
		return self._data_df.section.unique().tolist()
	def datanames_in(self,s):
		return self._data_df[self._data_df["section"] == s]["name"].tolist()
	def load_(self):
		load_func = {
		"scikitlearn": self.load_scikitlearn
		}
		load_func[self._protocol]()
	def __getitem__(self,index):
		if type(index) == str and index in self._data_df.name:
			if index not in self._data.keys():
				md = self._data_df.loc[index]
				self._data[index] = ImageDataItem(md.name,md.path)
			
			return self._data[index]
	@staticmethod
	def load(datasetpath,protocol="scikitlearn"):
		_data = Dataset(datasetpath,protocol)
		_data.load_()
		
		return _data
class DatasetBank:
	def __init__(self):
		self._datasets = {}
	def __getitem__(self,datasetname):
		return self._datasets[datasetname]
	def add(self,datasetname,dataset):
		self._datasets[datasetname] = dataset
	def create(self,datasetpath,protocol="scikitlearn"):
		_set = Dataset.load(datasetpath,protocol)
		self._datasets[_set._name] = _set
		return _set

class DataWidget(QWidget,Ui_DataWidget):
	def __init__(self,parent):
		QWidget.__init__(self,parent)
		self.setupUi(self)
		self._databank = DatasetBank()
		self._currentDataset = None
		self._qmodels = {}
		self._datasetnames = []
		self.dataTreeWidget.itemSelectionChanged.connect(self.refresh_plot)
	
	def refresh_plot(self):
		selected = self.dataTreeWidget.selectedItems()
		if selected:
			section = selected[0]
			item = section.text(0)
			imgItem = self._currentDataset[item]
			qim = ImageQt(imgItem._image)
			pix = QtGui.QPixmap.fromImage(qim)
			self.imgLbl.setPixmap(pix)

	def on_pbLoadDataset_released(self):
		path = qtutil.browse()
		if path == None or path.strip() == "":
			return
		
		dataset = self._databank.create(path)
		dname = dataset._name
		if dname not in self._datasetnames:
			self.cmbDataset.addItems([dataset._name])
			if self.cmbDataset.currentIndex() == -1:
				self.cmbDataset.setCurrentIndex(self.cmbDataset.count() - 1)
		self.cmbDataset.setEnabled(True)
		self._currentDataset = self._databank[self.cmbDataset.currentText()]
		self._refresh_view()
		


	def _update_data_list(self,df):
		self.dataTreeWidget.clear()
		sections = df.section.unique().tolist()
		headerItem  = QTreeWidgetItem()
		item    = QTreeWidgetItem()
		for i,s in enumerate(sections):
			parent = QTreeWidgetItem(self.dataTreeWidget)
			parent.setText(0, s)
			parent.setFlags(parent.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
			
			items = df[df["section"] == s]["name"].tolist()
			for n in items:
				child = QTreeWidgetItem(parent)
				child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
				child.setText(0, n)
				child.setCheckState(0, Qt.Unchecked)
	
	def _selected_labels(self):
		labels = []
		for btn in self.labelsGroup.findChildren(QtWidgets.QPushButton):
			if btn.isChecked():
				labels.append(str(btn.text()))
		return labels
	def _color_selected_labels(self):
		for btn in self.labelsGroup.findChildren(QtWidgets.QPushButton):
			if btn.isChecked():
				btn.setStyleSheet("""
						background-color:rgb(0, 170, 127)
					""")
			else:
				btn.setStyleSheet("")

	def _update_labels(self,labels):
		vbox = QVBoxLayout()
		for l in labels:
			lblButton = QtWidgets.QPushButton(l)
			lblButton.setCheckable(True)
			lblButton.setChecked(True)
			lblButton.clicked.connect(self.pbLabelClicked)
			lblButton.setEnabled(True)
			vbox.addWidget(lblButton)
		self.labelsGroup.setLayout(vbox)
		vbox.addStretch(1)
		self._color_selected_labels()

	def _filter_by_label(self,labels):
		
		df = self._currentDataset._data_df.copy()
		df = df[df["label"].isin(labels)]
		self._update_data_list(df)

	def pbLabelClicked(self):
		self._color_selected_labels()
		labels = self._selected_labels()
		self._filter_by_label(labels)

	def _refresh_view(self):
		self._update_data_list(self._currentDataset._data_df)
		self._update_labels(self._currentDataset._labels)





if __name__ == '__main__':

	data = Dataset.load("/home/jalalirs/code/ihm/dataset/WOPR/")
	print(data._data_df)