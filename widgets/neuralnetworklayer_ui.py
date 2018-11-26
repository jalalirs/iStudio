# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/neuralnetworklayer.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NNLayer(object):
    def setupUi(self, NNLayer):
        NNLayer.setObjectName("NNLayer")
        NNLayer.resize(150, 190)
        NNLayer.setMinimumSize(QtCore.QSize(150, 190))
        NNLayer.setMaximumSize(QtCore.QSize(150, 16777215))
        NNLayer.setStyleSheet("QPushButton {\n"
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
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(NNLayer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.buttonsWidget = QtWidgets.QWidget(NNLayer)
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
        self.layerWidget = QtWidgets.QWidget(NNLayer)
        self.layerWidget.setStyleSheet("border-color: black;\n"
"border-style: solid;\n"
"border-width:2px;\n"
"")
        self.layerWidget.setObjectName("layerWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layerWidget)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.shape = QtWidgets.QWidget(self.layerWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shape.sizePolicy().hasHeightForWidth())
        self.shape.setSizePolicy(sizePolicy)
        self.shape.setMinimumSize(QtCore.QSize(50, 50))
        self.shape.setMaximumSize(QtCore.QSize(50, 50))
        self.shape.setStyleSheet("border-color: black;\n"
"border-style: solid;\n"
"border-width:2px;\n"
"background-color: rgb(222, 127, 168);\n"
"border-radius:5px;")
        self.shape.setObjectName("shape")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.shape)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lblCount = QtWidgets.QLabel(self.shape)
        self.lblCount.setMaximumSize(QtCore.QSize(40, 15))
        font = QtGui.QFont()
        font.setFamily(".SF NS Text")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lblCount.setFont(font)
        self.lblCount.setStyleSheet("border:None;\n"
"font: 13pt \".SF NS Text\";\n"
"")
        self.lblCount.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCount.setObjectName("lblCount")
        self.horizontalLayout_3.addWidget(self.lblCount)
        self.horizontalLayout_2.addWidget(self.shape)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.layerWidget)

        self.retranslateUi(NNLayer)
        QtCore.QMetaObject.connectSlotsByName(NNLayer)

    def retranslateUi(self, NNLayer):
        _translate = QtCore.QCoreApplication.translate
        NNLayer.setWindowTitle(_translate("NNLayer", "Form"))
        self.pbAddNeuron.setText(_translate("NNLayer", "+"))
        self.pbRemoveNeuron.setText(_translate("NNLayer", "-"))
        self.lblCount.setText(_translate("NNLayer", "1024"))

