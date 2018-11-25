# -*- coding: utf-8 -*-

from .datawidget_ui import Ui_DataWidget
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
				data += [(f.split(".")[0],f.split(".")[0],f.split(".")[0],
					s,s,
					self._labels[i],self._labels[i],
					os.path.join(path,f)) for f in os.listdir(path) if os.path.isfile(os.path.join(path,f)) ]
		self._data_df = pd.DataFrame(data,columns=["id","name","new_name","section","new_section","label","new_label","path"])
		self._data_df.set_index("id",inplace=True)
	@property
	def sections_names(self):
		return self._data_df.new_section.unique().tolist()
	@property
	def labels(self):
		return self._data_df.new_label.unique().tolist()
	@property
	def sections(self):
		return self._data_df.new_section.unique().tolist()
	def get_label(self,name):
		return self._data_df.loc[name].new_label
	def datanames_in(self,s):
		return self._data_df[self._data_df["new_section"] == s]["new_name"].tolist()
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
	def delete(self,items):
		if type(items) == str:
			items = [items]

		for i in items:
			if i in self._data.keys():
				del self._data[i]
		self._data_df = self._data_df.drop(items)
	def update_label(self,items,nlabel,replaceName=True,protocol="scikitlearn"):
		if type(items) == str:
			items = [items]

		self._data_df.loc[items,"new_label"] = nlabel
		if replaceName:
			if protocol == "scikitlearn":
				self._data_df.loc[items,"new_name"] = self._data_df.loc[items].name.str.replace(r'^().*_', "%s_" % nlabel)
				self._data_df.set_index(self._data_df.new_name,inplace=True)
	def update_section(self,items,nsection):
		if type(items) == str:
			items = [items]
		self._data_df.loc[items,"new_section"] = nsection
	def update_item(self,item,name,label,source=""):
		self._data_df.loc[item,"new_name"] = name
		self._data_df.loc[item,"new_label"] = label
		nname = self._data_df.loc[[item]].new_name.str.replace(r'^().*_', "%s_" % label)
		self._data_df.loc[[item],"new_name"] =  nname
		nname = nname.tolist()[0]
		self._data_df.rename(index={item:nname},inplace=True)
		#self._data_df.iloc[item,"source"] = source
		return nname
	def save_session(self,path):
		if path.split(".")[-1] != ".csv":
			path += ".csv"
		self._data_df.to_csv(path,index=True)
	def load_session(self,path):
		df = pd.read_csv(path)
		sn = set(df.name.tolist())
		cn = set(self._data_df.name.tolist())
		if sn.issubset(cn):
			self._data_df = df
	def publish(self,path,protocol="scikitlearn"):
		from shutil import copyfile
		def _mkdir(f):
			if not os.path.exists(f):
				os.makedirs(f)
		def _copy(opath,nsection,nname,nlabel):
			if not os.path.exists(opath):
				return
			ext = opath.split(".")[-1]
			jpath = "%s/%s/%d.%s/%s.%s" % (path,nsection,self._labels.index(nlabel),nlabel,nname,ext)
			copyfile(opath, jpath)
		os.makedirs(path)
		for s in self.sections:
			for i,lbl in enumerate(self.labels):
				_mkdir("%s/%s/%d.%s" % (path,s,i,lbl))
		self._data_df.apply(lambda row: _copy(row['path'], row['new_section'], row['new_name'],row['new_label']), axis=1)		
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
		self.dataTreeWidget.itemClicked.connect(self.handle_selection)
		self._qtreeWidgetItems = None
		self._currentItem = None
	def get_checked_items(self):
		selected = []
		for i in self._qtreeWidgetItems:
			if i.checkState(0) == QtCore.Qt.Checked:
				selected.append(i.text(0))
		return selected
	def get_treewidgetitem(self,item):
		for i in self._qtreeWidgetItems:
			if i.text(0) == item:
				return i
		return None
	def select(self,selected):
		for i in self._qtreeWidgetItems:
			if i.text(0) in selected:
				i.setCheckState(0,QtCore.Qt.Checked)
	def handle_selection(self):
		selected = self.get_checked_items()
		if len(selected) > 0:
			self.pbEditLabelMulti.setEnabled(True)
			self.pbDeleteMulti.setEnabled(True)
			self.pbMoveTo.setEnabled(True)
		else:
			self.pbEditLabelMulti.setEnabled(False)
			self.pbDeleteMulti.setEnabled(False)
			self.pbMoveTo.setEnabled(False)
	def memorize_expansion(self):
		expansion = {}
		root = self.dataTreeWidget.invisibleRootItem()
		child_count = root.childCount()
		for i in range(child_count):
			item = root.child(i)
			expansion[item.text(0)] = item.isExpanded()
		return expansion
	def expand(self,sections):
		root = self.dataTreeWidget.invisibleRootItem()
		child_count = root.childCount()
		for i in range(child_count):
			item = root.child(i)
			if item.text(0) in sections and sections[item.text(0)]:
				item.setExpanded(True)
	def on_pbDeleteMulti_released(self):
		expansion = self.memorize_expansion()
		selected = self.get_checked_items()
		self._currentDataset.delete(selected)
		self._refresh_view()
		self.expand(expansion)
	def on_pbEditLabelMulti_released(self):
		expansion = self.memorize_expansion()
		nlabel,checked, ok = EditLabel.getNewLabel(self,self._currentDataset.labels)
		if not ok:
			return
		selected = self.get_checked_items()
		self._currentDataset.update_label(selected,nlabel,checked)
		self._refresh_view()
		self.expand(expansion)
	def on_pbMoveTo_released(self):
		expansion = self.memorize_expansion()
		nsection, ok = MoveTo.getNewSections(self,self._currentDataset.sections)
		if not ok:
			return
		selected = self.get_checked_items()
		self._currentDataset.update_section(selected,nsection)
		self._refresh_view()
		self.expand(expansion)
	def on_pbUpdateSingle_released(self):
		expansion = self.memorize_expansion()
		selected = self.get_checked_items()
		name = self.lineName.text()
		label = self.cmbLabel.currentText()
		source = self.lineSource.text()
		nname = self._currentDataset.update_item(self._currentItem,name,label,source)
		if self._currentItem in selected:
			selected.append(nname)
		self._refresh_view()
		self.expand(expansion)
		self.select(selected)
		self._currentItem = name
		nsitem = self.get_treewidgetitem(nname)
		if nsitem:
			self.dataTreeWidget.setCurrentItem(nsitem)
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
		self.pbPublish.setEnabled(True)
		self.pbLoadSession.setEnabled(True)
		self.pbSaveSession.setEnabled(True)
	def on_pbPublish_released(self):
		path = qtutil.browse("savefile")
		if path == None or path.strip() == "":
			return	
		if os.path.exists("%s" % (path)):
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Information)
			msg.setText("%s exists. Please choose another name or another path" % path)
			msg.setWindowTitle("Cannot publish")
			return
		self._currentDataset.publish(path)
	def on_pbSaveSession_released(self):
		path = qtutil.browse("savefile")
		if path == None or path.strip() == "":
			return

		self._currentDataset.save_session(path)
	def on_pbLoadSession_released(self):
		expansion = self.memorize_expansion()
		path = qtutil.browse("openfile")
		if path == None or path.strip() == "":
			return
		self._currentDataset.load_session(path)
		self._refresh_view()
		self.expand(expansion)
	def refresh_plot(self):
		selected = self.dataTreeWidget.selectedItems()
		if selected:
			size = 128, 128
			section = selected[0]
			item = section.text(0)
			img = self._currentDataset[item]._path
			self.imgLbl.setPixmap(QtGui.QPixmap(img))
			self.lineName.setText(item)
			self.cmbLabel.clear()
			self.cmbLabel.addItems(self._currentDataset.labels)
			index = self.cmbLabel.findText(self._currentDataset.get_label(item), QtCore.Qt.MatchFixedString)
			self.cmbLabel.setCurrentIndex(index)
			self._currentItem = item
			self._set_edit_widgets(True)
	def pbLabelClicked(self):
		self._color_selected_labels()
		labels = self._selected_labels()
		self._filter_by_label(labels)
	def _set_edit_widgets(self,enabled=True):
		self.lineName.setEnabled(enabled)
		self.cmbLabel.setEnabled(enabled)
		self.lineSource.setEnabled(enabled)
		self.pbUpdateSingle.setEnabled(enabled)
		self.pbDeleteSingle.setEnabled(enabled)
		self.labelLabel.setEnabled(enabled)
		self.sourceLabel.setEnabled(enabled)
		self.nameLable.setEnabled(enabled)
	def _update_data_list(self,df):
		"""TODO: find some way to delegate getting the items and the sections to the dataset"""
		self.dataTreeWidget.clear()
		self._qtreeWidgetItems = []
		sections = df.new_section.unique().tolist()
		headerItem  = QTreeWidgetItem()
		item    = QTreeWidgetItem()
		for i,s in enumerate(sections):
			parent = QTreeWidgetItem(self.dataTreeWidget)
			parent.setText(0, s)
			parent.setFlags(parent.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
			
			items = df[df["new_section"] == s]["new_name"].tolist()
			for n in items:
				child = QTreeWidgetItem(parent)
				child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
				child.setText(0, n)
				child.setCheckState(0, Qt.Unchecked)
				self._qtreeWidgetItems.append(child)
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
		self.cmbLabel.clear()
	def _filter_by_label(self,labels):	
		df = self._currentDataset._data_df.copy()
		df = df[df["label"].isin(labels)]
		self._update_data_list(df)
	def _refresh_view(self):
		self._update_data_list(self._currentDataset._data_df)
		self._update_labels(self._currentDataset._labels)





if __name__ == '__main__':

	data = Dataset.load("/home/jalalirs/code/ihm/dataset/WOPR/")
	print(data._data_df)