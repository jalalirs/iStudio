# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5 import Qt

class NeuronGroupWidget(QtWidgets.QWidget):
    def __init__(self,parent,maxNeurons=2):
        super(QWidget, self).__init__(parent)

        self._maxNeurons = maxNeurons
        
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        # self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(50, 50))
        self.setMaximumSize(QtCore.QSize(50, 50))
        self.setStyleSheet("border-color: black;\n"
        "border-style: solid;\n"
        "border-width:2px;\n"
        "background-color: rgb(222, 127, 168);\n"
        "border-radius:5px;")
        self.setObjectName("shape")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lblCount = QtWidgets.QLabel(self)
        #self.lblCount.setMaximumSize(QtCore.QSize(40, 15))
        font = QtGui.QFont()
        font.setFamily(".SF NS Text")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(100)
        self.lblCount.setFont(font)
        self.lblCount.setStyleSheet("border:None;\n"
        "font: 13pt \".SF NS Text\";\n"
        "")
        self.lblCount.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCount.setObjectName("lblCount")
        self.horizontalLayout_3.addWidget(self.lblCount)

        self._neurons = 0
    def isFull(self):
        return self._neurons == self._maxNeurons
    def increament(self):
        self._neurons += 1
        self.lblCount.setText(str(self._neurons))
class NNLayerWidget(QtWidgets.QWidget):
    def __init__(self,parent=None, order= 0):
        super(QWidget, self).__init__(parent)
        
        self.setObjectName("NNLayer")
        self.resize(150, 190)
        self.setMinimumSize(QtCore.QSize(150, 190))
        self.setMaximumSize(QtCore.QSize(150, 16777215))
        self.setStyleSheet("QPushButton {\n"
        " border-style: solid  ;\n"
        " border-width:1px;\n"
        " border-radius:20px;\n"
        " max-width:40px;\n"
        " max-height:40px;\n"
        " min-width:40px;\n"
        " min-height:40px;\n"
        "background-color:rgb(186, 189, 182)\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
        "        );\n"
        "    }\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-style: inset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
        "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
        "        );\n"
        "    }")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.buttonsWidget = QtWidgets.QWidget(self)
        self.buttonsWidget.setMinimumSize(QtCore.QSize(0, 80))
        self.buttonsWidget.setMaximumSize(QtCore.QSize(16777215, 80))
        self.buttonsWidget.setObjectName("buttonsWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.buttonsWidget)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pbAddNeuron = QtWidgets.QPushButton(self.buttonsWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pbAddNeuron.setFont(font)
        self.pbAddNeuron.setStyleSheet("")
        self.pbAddNeuron.setObjectName("pbAddNeuron")
        self.horizontalLayout.addWidget(self.pbAddNeuron)
        self.pbRemoveNeuron = QtWidgets.QPushButton(self.buttonsWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pbRemoveNeuron.setFont(font)
        self.pbRemoveNeuron.setStyleSheet("")
        self.pbRemoveNeuron.setObjectName("pbRemoveNeuron")
        self.horizontalLayout.addWidget(self.pbRemoveNeuron)
        self.verticalLayout_2.addWidget(self.buttonsWidget)

        self.widget_dump = QtWidgets.QWidget(self)
        self.layout_dump = QtWidgets.QHBoxLayout(self.widget_dump)
        #self.layout_dump.setContentsMargins(-1, 0, -1, 0)
        self.layout_dump.setObjectName("layout_dump")
        self.verticalLayout_2.addWidget(self.widget_dump)
        

        self.layerWidget = QtWidgets.QWidget(self)
        self.layerWidget.setMinimumSize(QtCore.QSize(50, 0))
        self.layerWidget.setMaximumSize(QtCore.QSize(50, 16777215))
        self.layerWidget.setStyleSheet("border-color: black;\n"
            "border-style: solid;\n"
            "border-width:2px;\n"
            "border-radius:4px;""")
        self.layerWidget.setObjectName("layerWidget")
        self.layerLayout = QtWidgets.QVBoxLayout(self.layerWidget)
        self.layerLayout.setContentsMargins(0, 0, 0, 0)
        self.layerLayout.setObjectName("layerLayout")
        
        self.layout_dump.addWidget(self.layerWidget)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self._neurongroups = []
        self._order = order
        self.addNewNeuronGroup()

    def on_pbAddNeuron_released(self):
        self.addNeuron()
    def addNeuron(self):
        if self._neurongroups[-1].isFull():
            self.addNewNeuronGroup()
        else:
            self._neurongroups[-1].increament()

    def addNewNeuronGroup(self): 
        Neuron = NeuronGroupWidget(self.layerWidget)
        self.layerLayout.addWidget(Neuron)
  
        Neuron.increament()
        self._neurongroups.append(Neuron)
    def retranslateUi(self, NNLayer):
        _translate = QtCore.QCoreApplication.translate
        NNLayer.setWindowTitle(_translate("NNLayer", "Form"))
        self.pbAddNeuron.setText(_translate("NNLayer", "+"))
        self.pbRemoveNeuron.setText(_translate("NNLayer", "-"))