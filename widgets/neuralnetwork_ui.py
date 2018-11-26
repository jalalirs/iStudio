# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/neuralnetwork.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NeuralNetwork(object):
    def setupUi(self, NeuralNetwork):
        NeuralNetwork.setObjectName("NeuralNetwork")
        NeuralNetwork.resize(1005, 698)
        NeuralNetwork.setMinimumSize(QtCore.QSize(0, 500))
        self.verticalLayout = QtWidgets.QVBoxLayout(NeuralNetwork)
        self.verticalLayout.setContentsMargins(0, 0, 0, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(NeuralNetwork)
        self.widget.setMinimumSize(QtCore.QSize(0, 75))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 75))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.widget_2.setStyleSheet("QPushButton {\n"
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
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pbAddLayer = QtWidgets.QPushButton(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pbAddLayer.setFont(font)
        self.pbAddLayer.setStyleSheet("")
        self.pbAddLayer.setObjectName("pbAddLayer")
        self.horizontalLayout.addWidget(self.pbAddLayer)
        self.pbRemoveLayer = QtWidgets.QPushButton(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pbRemoveLayer.setFont(font)
        self.pbRemoveLayer.setStyleSheet("")
        self.pbRemoveLayer.setObjectName("pbRemoveLayer")
        self.horizontalLayout.addWidget(self.pbRemoveLayer)
        self.lblNumOfHiddenLayers = QtWidgets.QLabel(self.widget_2)
        self.lblNumOfHiddenLayers.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblNumOfHiddenLayers.setFont(font)
        self.lblNumOfHiddenLayers.setStyleSheet("font: 20pt \".SF NS Text\";\n"
"font-weight: bold;\n"
"")
        self.lblNumOfHiddenLayers.setText("")
        self.lblNumOfHiddenLayers.setObjectName("lblNumOfHiddenLayers")
        self.horizontalLayout.addWidget(self.lblNumOfHiddenLayers)
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 20pt \".SF NS Text\";\n"
"font-weight: bold;\n"
"")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.horizontalLayout_2.addWidget(self.widget_2)
        self.verticalLayout.addWidget(self.widget)
        self.widget_4 = QtWidgets.QWidget(NeuralNetwork)
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.line = QtWidgets.QFrame(self.widget_4)
        self.line.setStyleSheet("background-color: rgb(0, 0, 255);\n"
"")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.verticalLayout.addWidget(self.widget_4)
        self.layers = QtWidgets.QWidget(NeuralNetwork)
        self.layers.setMinimumSize(QtCore.QSize(0, 100))
        self.layers.setObjectName("layers")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layers)
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout.addWidget(self.layers)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(NeuralNetwork)
        QtCore.QMetaObject.connectSlotsByName(NeuralNetwork)

    def retranslateUi(self, NeuralNetwork):
        _translate = QtCore.QCoreApplication.translate
        NeuralNetwork.setWindowTitle(_translate("NeuralNetwork", "Form"))
        self.pbAddLayer.setText(_translate("NeuralNetwork", "+"))
        self.pbRemoveLayer.setText(_translate("NeuralNetwork", "-"))
        self.label_2.setText(_translate("NeuralNetwork", "Hidden Layers"))

