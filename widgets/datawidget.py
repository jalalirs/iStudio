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
import json
from .paintingwidget import PaintingWidget

class ImageDataItem:
	def __init__(self,name,path,width=None,height=None,uri=None,datecaptured=None):
		self._name = name
		self._path = path
		self._image =  Image.open(path)
		self._width = width
		self._height = height
		self._uri = uri
		self._datecaptured = datecaptured
class CocoDataset:
	def __init__(self,datasetpath):
		self._path = datasetpath
		self._name = self._path.split("/")[-1]
		self._images = None
		self._annotations = None
		self._categories = None
		self._data = {}
		self._challenges = ["Classification","Detection","Segmentation","Keypoints","Captioning"]
		self._detectionColors = ['r','b','g','b']
	def load_(self):
		folders = ["%s/%s" % (self._path,x) for x in ["train","val","test"]]
		annotations = "%s/annotation" % (self._path)

		def open_section(section):
			with open("%s/%s/instances_%s2017.json" % (annotations,section,section)) as f:
				td = json.load(f)
				s_annotation = pd.DataFrame(td["annotations"])
				s_images = pd.DataFrame(td["images"])
				s_categories = pd.DataFrame(td["categories"])

				s_annotation["section"] = section
				s_images["section"] = section
				s_categories["section"] = section

				s_images["dir"] = "%s/%s" % (self._path,section)

				s_images["id"] = s_images["id"].astype(int)
				s_annotation["image_id"] = s_annotation["image_id"].astype(int)
			return s_images,s_annotation,s_categories
		
		tr_im, tr_ann, tr_cat = open_section("train")
		va_im, va_ann, va_cat = open_section("val")

		self._images = pd.concat([tr_im,va_im])
		self._annotations = pd.concat([tr_ann,va_ann])
		self._categories = pd.concat([tr_cat,va_cat])	

		self._images = self._images.set_index("id",drop=False)
		categories = self._annotations.groupby("image_id")["category_id"].apply(list)
		self._images.categories = categories
		self._images.categories.fillna(-1,inplace=True)
		catdict = self._categories.set_index("id").to_dict()["name"]

		def id_to_value(x):
			if x == -1:
				return []
			elif type(x) == list:
				return [catdict[d] for d in x]
			else:
				return [catdict[d]]
		self._images["categories_value"] = self._images.categories.apply(id_to_value)		
	@property
	def sections_names(self):
		return self._images.section.unique().tolist()
	@property
	def labels(self):
		return self._categories.name.unique().tolist()
	def get_label(self,imgid,challenge="classification"):
		if challenge == 'classification':
			cat = self.get_categories(imgid)
			return ",".join(cat)
	def __getitem__(self,index):
		if type(index) == str:
			index = int(index) 

		if index in self._images.id.values:
			if index not in self._data.keys():
				md = self._images.loc[index]
				self._data[index] = ImageDataItem(md.file_name,"%s/%s" % (md.dir,md.file_name),
					md.width,md.height,md.coco_url,md.date_captured)
				
			return self._data[index]
	def get_categories(self,imgid):
		if type(imgid) == str:
			imgid = int(imgid)
		categories = self._annotations[self._annotations["image_id"]==imgid].category_id.unique().tolist()
		return np.unique(self._categories[self._categories["id"].isin(categories)].name.values).tolist()
	def get_bboxes(self,imgid):
		if type(imgid) == str:
			imgid = int(imgid)
		boxes = self._annotations[self._annotations["image_id"]==imgid].bbox.tolist()
		return boxes
	def get_data_list(self,labels=None):
		df = self._images.copy()
		if labels:
			def filter_fn(row):
				cats = row.categories_value
				if type(cats) == float:
					return cats in labels
				for c in cats:
					if c in labels:
						return True
				return False		
			df = df[df.apply(filter_fn, axis=1)]

		return df[['section','id']].groupby("section")["id"].apply(list).to_dict()
	def get_challenges(self):
		return self._challenges
	def apply_challenge(self,challenge,item,guiplaceholders):
		if challenge == "Classification":
			guiplaceholders["label"].setText(self.get_label(item))
		if challenge == "Detection":
			for i,value in enumerate(self.get_bboxes(item)):
				x,y,width,height = value
				color = self._detectionColors[i%len(self._detectionColors)]
				guiplaceholders["image"].paint_rectangle(x,y,width,height,color)

	@staticmethod
	def load(datasetpath):
		print(datasetpath)
		_data = CocoDataset(datasetpath)
		_data.load_()
		
		return _data
class ScikitLearnDataset:
	def __init__(self,datasetpath):
		self._path = datasetpath
		self._data = {}
		self._labels = []
		self._sections = {}
		self._data_df = None
		self._name = self._path.split("/")[-1]
		self._challenges = ["Classification"]
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
	def get_challenges(self):
		return self._challenges
	def datanames_in(self,s):
		return self._data_df[self._data_df["new_section"] == s]["new_name"].tolist()
	def load_(self):
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
	def publish(self,path):
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
	def get_data_list(self,labels = None):
		df = self._data_df.copy()
		if labels:
			df = df[df["label"].isin(labels)]

		return df[['new_section','new_name']].groupby("new_section")["new_name"].apply(list).to_dict()
	def apply_challenge(self,challenge,item,guiplaceholders):
		if challenge == "Classification":
			guiplaceholders["label"].setText(self.get_label(item))
	@staticmethod
	def load(datasetpath):
		_data = ScikitLearnDataset(datasetpath)
		_data.load_()
		
		return _data
class Dataset:
	@staticmethod
	def load(datasetpath,protocol="scikitlearn"):
		if protocol == "scikitlearn":
			return ScikitLearnDataset.load(datasetpath)
		elif protocol == "coco":
			return CocoDataset.load(datasetpath)
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
		self._currentItemId = None
		self._paintingWidget = PaintingWidget(self.paintingWidget,
			self.paintingWidget.width(),self.paintingWidget.height())
		self.paintingLayout.addWidget(self._paintingWidget)
		self._currentChallenge = None
		self.cmbChallenge.currentIndexChanged.connect(self.on_challenge_changed)
	def on_challenge_changed(self):
		self._currentChallenge = self.cmbChallenge.currentText()
		self.apply_challenge(self._currentChallenge)
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
		protocol = self.cmbProtocol.currentText()
		dataset = self._databank.create(path,protocol)
		dname = dataset._name
		if dname not in self._datasetnames:
			self.cmbDataset.addItems([dataset._name])
			if self.cmbDataset.currentIndex() == -1:
				self.cmbDataset.setCurrentIndex(self.cmbDataset.count() - 1)
		self.cmbDataset.setEnabled(True)
		self._currentDataset = self._databank[self.cmbDataset.currentText()]
		self.cmbChallenge.clear()
		self.cmbChallenge.addItems(dataset.get_challenges())
		self.cmbChallenge.setEnabled(True)
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
			section = selected[0]
			selecteditem = section.text(0)
			item = self._currentDataset[selecteditem]
			self._currentItem = item
			self._currentItemId = selecteditem
			self._paintingWidget.paint_img(item._path)
			self._paintingWidget.update()
			self.lblInstancelName.setText(item._name)
			self.lblInstanceLabel.setText(self._currentDataset.get_label(selecteditem))
			if item._width:
				self.lblInstanceWidth.setText(str(item._width))
			else:
				self.lblInstanceWidth.setText("")
			if item._height:
				self.lblInstanceHeight.setText(str(item._height))
			else:
				self.lblInstanceHeight.setText("")
			if item._uri:
				self.lblInstanceURI.setText(item._uri)
			else:
				self.lblInstanceURI.setText("")
			if item._datecaptured:
				self.lblInstanceDate.setText(item._datecaptured)
			else:
				self.lblInstanceDate.setText("")
			self.apply_challenge(self.cmbChallenge.currentText())
	def pbLabelClicked(self):
		expansion = self.memorize_expansion()
		self._color_selected_labels()
		labels = self._selected_labels()
		self._filter_by_label(labels)
		self.expand(expansion)
	def _set_edit_widgets(self,enabled=True):
		self.pbUpdateSingle.setEnabled(enabled)
		self.pbDeleteSingle.setEnabled(enabled)
		self.labelLabel.setEnabled(enabled)
		self.sourceLabel.setEnabled(enabled)
		self.nameLable.setEnabled(enabled)
	def _update_data_list(self,data):
		"""TODO: find some way to delegate getting the items and the sections to the dataset"""
		self.dataTreeWidget.clear()
		self._qtreeWidgetItems = []
		headerItem  = QTreeWidgetItem()
		item    = QTreeWidgetItem()
		for section,items in data.items():
			parent = QTreeWidgetItem(self.dataTreeWidget)
			parent.setText(0, section)
			parent.setFlags(parent.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
			
			for n in items:
				child = QTreeWidgetItem(parent)
				child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
				child.setText(0, str(n))
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
		for l in labels:
			lblButton = QtWidgets.QPushButton(l)
			lblButton.setCheckable(True)
			lblButton.setChecked(True)
			lblButton.clicked.connect(self.pbLabelClicked)
			lblButton.setEnabled(True)
			self.labelButtonsLayout.addWidget(lblButton)
		self.labelButtonsLayout.addStretch(1)
		self._color_selected_labels()
	def _filter_by_label(self,labels):	
		data = self._currentDataset.get_data_list(labels=labels)
		self._update_data_list(data)
	def _refresh_view(self):
		print(self._currentDataset.get_data_list())
		self._update_data_list(self._currentDataset.get_data_list())
		self._update_labels(self._currentDataset.labels)
	def apply_challenge(self,challenge):
		target_placeholders = {
		"image": self._paintingWidget,
		"caption": None,
		"label": self.lblInstanceLabel
		}
		self._currentDataset.apply_challenge(challenge,self._currentItemId,target_placeholders)


if __name__ == '__main__':

	data = Dataset.load("/home/jalalirs/code/ihm/dataset/WOPR/")
