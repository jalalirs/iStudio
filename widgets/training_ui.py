# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/trainingwidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TrainingWidget(object):
    def setupUi(self, TrainingWidget):
        TrainingWidget.setObjectName("TrainingWidget")
        TrainingWidget.resize(1385, 1021)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(TrainingWidget)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.hyperparamWidget = QtWidgets.QWidget(TrainingWidget)
        self.hyperparamWidget.setMaximumSize(QtCore.QSize(16777215, 110))
        self.hyperparamWidget.setObjectName("hyperparamWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.hyperparamWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.playWidget = QtWidgets.QWidget(self.hyperparamWidget)
        self.playWidget.setObjectName("playWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.playWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pbPause = QtWidgets.QPushButton(self.playWidget)
        self.pbPause.setObjectName("pbPause")
        self.horizontalLayout.addWidget(self.pbPause)
        self.pbPlay = QtWidgets.QPushButton(self.playWidget)
        self.pbPlay.setObjectName("pbPlay")
        self.horizontalLayout.addWidget(self.pbPlay)
        self.horizontalLayout_3.addWidget(self.playWidget)
        spacerItem = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.widget = QtWidgets.QWidget(self.hyperparamWidget)
        self.widget.setMinimumSize(QtCore.QSize(1000, 0))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.cmbLearningRate = QtWidgets.QComboBox(self.widget_2)
        self.cmbLearningRate.setEditable(True)
        self.cmbLearningRate.setObjectName("cmbLearningRate")
        self.cmbLearningRate.addItem("")
        self.cmbLearningRate.addItem("")
        self.cmbLearningRate.addItem("")
        self.cmbLearningRate.addItem("")
        self.cmbLearningRate.addItem("")
        self.cmbLearningRate.addItem("")
        self.cmbLearningRate.addItem("")
        self.cmbLearningRate.addItem("")
        self.cmbLearningRate.addItem("")
        self.verticalLayout.addWidget(self.cmbLearningRate)
        self.horizontalLayout_2.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.cmbActivation = QtWidgets.QComboBox(self.widget_3)
        self.cmbActivation.setEditable(True)
        self.cmbActivation.setObjectName("cmbActivation")
        self.cmbActivation.addItem("")
        self.cmbActivation.addItem("")
        self.cmbActivation.addItem("")
        self.cmbActivation.addItem("")
        self.verticalLayout_2.addWidget(self.cmbActivation)
        self.horizontalLayout_2.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.widget_4)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.cmbActivation_2 = QtWidgets.QComboBox(self.widget_4)
        self.cmbActivation_2.setEditable(True)
        self.cmbActivation_2.setObjectName("cmbActivation_2")
        self.cmbActivation_2.addItem("")
        self.cmbActivation_2.addItem("")
        self.cmbActivation_2.addItem("")
        self.verticalLayout_5.addWidget(self.cmbActivation_2)
        self.horizontalLayout_2.addWidget(self.widget_4)
        self.widget_7 = QtWidgets.QWidget(self.widget)
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.widget_7)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.cmbActivation_5 = QtWidgets.QComboBox(self.widget_7)
        self.cmbActivation_5.setEditable(True)
        self.cmbActivation_5.setObjectName("cmbActivation_5")
        self.cmbActivation_5.addItem("")
        self.cmbActivation_5.addItem("")
        self.cmbActivation_5.addItem("")
        self.cmbActivation_5.addItem("")
        self.cmbActivation_5.addItem("")
        self.cmbActivation_5.addItem("")
        self.cmbActivation_5.addItem("")
        self.cmbActivation_5.addItem("")
        self.cmbActivation_5.addItem("")
        self.verticalLayout_6.addWidget(self.cmbActivation_5)
        self.horizontalLayout_2.addWidget(self.widget_7)
        self.widget_8 = QtWidgets.QWidget(self.widget)
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_8)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.widget_8)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_7.addWidget(self.label_8)
        self.cmbActivation_6 = QtWidgets.QComboBox(self.widget_8)
        self.cmbActivation_6.setEditable(True)
        self.cmbActivation_6.setObjectName("cmbActivation_6")
        self.cmbActivation_6.addItem("")
        self.cmbActivation_6.addItem("")
        self.verticalLayout_7.addWidget(self.cmbActivation_6)
        self.horizontalLayout_2.addWidget(self.widget_8)
        self.horizontalLayout_3.addWidget(self.widget)
        self.verticalLayout_8.addWidget(self.hyperparamWidget)
        self.widget_9 = QtWidgets.QWidget(TrainingWidget)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget_10 = QtWidgets.QWidget(self.widget_9)
        self.widget_10.setMinimumSize(QtCore.QSize(250, 0))
        self.widget_10.setMaximumSize(QtCore.QSize(250, 16777215))
        self.widget_10.setObjectName("widget_10")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.widget_10)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_9 = QtWidgets.QLabel(self.widget_10)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("font: 20pt \".SF NS Text\";\n"
"font-weight: bold;\n"
"")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_11.addWidget(self.label_9)
        self.widget_11 = QtWidgets.QWidget(self.widget_10)
        self.widget_11.setObjectName("widget_11")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_11)
        self.gridLayout.setObjectName("gridLayout")
        self.label_11 = QtWidgets.QLabel(self.widget_11)
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 2)
        self.cmbDataset = QtWidgets.QComboBox(self.widget_11)
        self.cmbDataset.setMinimumSize(QtCore.QSize(140, 0))
        self.cmbDataset.setObjectName("cmbDataset")
        self.gridLayout.addWidget(self.cmbDataset, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget_11)
        self.pushButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        self.verticalLayout_11.addWidget(self.widget_11)
        self.widget_13 = QtWidgets.QWidget(self.widget_10)
        self.widget_13.setObjectName("widget_13")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget_13)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_15 = QtWidgets.QLabel(self.widget_13)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_10.addWidget(self.label_15)
        self.pbTrainingPercentage = QtWidgets.QSlider(self.widget_13)
        self.pbTrainingPercentage.setOrientation(QtCore.Qt.Horizontal)
        self.pbTrainingPercentage.setObjectName("pbTrainingPercentage")
        self.verticalLayout_10.addWidget(self.pbTrainingPercentage)
        self.verticalLayout_11.addWidget(self.widget_13)
        self.widget_12 = QtWidgets.QWidget(self.widget_10)
        self.widget_12.setObjectName("widget_12")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_12)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_10 = QtWidgets.QLabel(self.widget_12)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_9.addWidget(self.label_10)
        self.pbBatchSize = QtWidgets.QSlider(self.widget_12)
        self.pbBatchSize.setOrientation(QtCore.Qt.Horizontal)
        self.pbBatchSize.setObjectName("pbBatchSize")
        self.verticalLayout_9.addWidget(self.pbBatchSize)
        self.verticalLayout_11.addWidget(self.widget_12)
        self.widget_14 = QtWidgets.QWidget(self.widget_10)
        self.widget_14.setObjectName("widget_14")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.widget_14)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_12 = QtWidgets.QLabel(self.widget_14)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_12.addWidget(self.label_12)
        self.widget_5 = QtWidgets.QWidget(self.widget_14)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lnWidth = QtWidgets.QLineEdit(self.widget_5)
        self.lnWidth.setObjectName("lnWidth")
        self.horizontalLayout_4.addWidget(self.lnWidth)
        self.lnHeight = QtWidgets.QLineEdit(self.widget_5)
        self.lnHeight.setObjectName("lnHeight")
        self.horizontalLayout_4.addWidget(self.lnHeight)
        self.verticalLayout_12.addWidget(self.widget_5)
        self.verticalLayout_11.addWidget(self.widget_14)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem1)
        self.horizontalLayout_5.addWidget(self.widget_10)
        self.line = QtWidgets.QFrame(self.widget_9)
        self.line.setMinimumSize(QtCore.QSize(3, 0))
        self.line.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_5.addWidget(self.line)
        self.widget_6 = QtWidgets.QWidget(self.widget_9)
        self.widget_6.setObjectName("widget_6")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_18 = QtWidgets.QWidget(self.widget_6)
        self.widget_18.setMinimumSize(QtCore.QSize(0, 350))
        self.widget_18.setStyleSheet("background-color: rgb(254, 166, 8);")
        self.widget_18.setObjectName("widget_18")
        self.gridLayout_2.addWidget(self.widget_18, 1, 1, 1, 2)
        self.widget_15 = QtWidgets.QWidget(self.widget_6)
        self.widget_15.setMinimumSize(QtCore.QSize(200, 0))
        self.widget_15.setStyleSheet("background-color: rgb(252, 0, 8);")
        self.widget_15.setObjectName("widget_15")
        self.gridLayout_2.addWidget(self.widget_15, 0, 2, 1, 1)
        self.widget_17 = QtWidgets.QWidget(self.widget_6)
        self.widget_17.setStyleSheet("background-color: rgb(108, 255, 30);")
        self.widget_17.setObjectName("widget_17")
        self.gridLayout_2.addWidget(self.widget_17, 1, 0, 1, 1)
        self.neuralNetworkWidget = QtWidgets.QWidget(self.widget_6)
        self.neuralNetworkWidget.setMinimumSize(QtCore.QSize(0, 600))
        self.neuralNetworkWidget.setMaximumSize(QtCore.QSize(16777215, 600))
        self.neuralNetworkWidget.setObjectName("neuralNetworkWidget")
        self.neuralNetworkLayout = QtWidgets.QVBoxLayout(self.neuralNetworkWidget)
        self.neuralNetworkLayout.setContentsMargins(0, 0, 0, 0)
        self.neuralNetworkLayout.setObjectName("neuralNetworkLayout")
        self.gridLayout_2.addWidget(self.neuralNetworkWidget, 0, 0, 1, 2)
        self.horizontalLayout_5.addWidget(self.widget_6)
        self.verticalLayout_8.addWidget(self.widget_9)

        self.retranslateUi(TrainingWidget)
        QtCore.QMetaObject.connectSlotsByName(TrainingWidget)

    def retranslateUi(self, TrainingWidget):
        _translate = QtCore.QCoreApplication.translate
        TrainingWidget.setWindowTitle(_translate("TrainingWidget", "Form"))
        self.pbPause.setText(_translate("TrainingWidget", "Pause"))
        self.pbPlay.setText(_translate("TrainingWidget", "Play"))
        self.label.setText(_translate("TrainingWidget", "Learning Rate"))
        self.cmbLearningRate.setItemText(0, _translate("TrainingWidget", "0.00001"))
        self.cmbLearningRate.setItemText(1, _translate("TrainingWidget", "0.0001"))
        self.cmbLearningRate.setItemText(2, _translate("TrainingWidget", "0.001"))
        self.cmbLearningRate.setItemText(3, _translate("TrainingWidget", "0.03"))
        self.cmbLearningRate.setItemText(4, _translate("TrainingWidget", "0.1"))
        self.cmbLearningRate.setItemText(5, _translate("TrainingWidget", "0.3"))
        self.cmbLearningRate.setItemText(6, _translate("TrainingWidget", "1"))
        self.cmbLearningRate.setItemText(7, _translate("TrainingWidget", "3"))
        self.cmbLearningRate.setItemText(8, _translate("TrainingWidget", "10"))
        self.label_2.setText(_translate("TrainingWidget", "Activation"))
        self.cmbActivation.setItemText(0, _translate("TrainingWidget", "ReLU"))
        self.cmbActivation.setItemText(1, _translate("TrainingWidget", "Tanh"))
        self.cmbActivation.setItemText(2, _translate("TrainingWidget", "Sigmoid"))
        self.cmbActivation.setItemText(3, _translate("TrainingWidget", "Linear"))
        self.label_3.setText(_translate("TrainingWidget", "Regularization"))
        self.cmbActivation_2.setItemText(0, _translate("TrainingWidget", "None"))
        self.cmbActivation_2.setItemText(1, _translate("TrainingWidget", "L1"))
        self.cmbActivation_2.setItemText(2, _translate("TrainingWidget", "L2"))
        self.label_7.setText(_translate("TrainingWidget", "Regularization Rate"))
        self.cmbActivation_5.setItemText(0, _translate("TrainingWidget", "0.00001"))
        self.cmbActivation_5.setItemText(1, _translate("TrainingWidget", "0.0001"))
        self.cmbActivation_5.setItemText(2, _translate("TrainingWidget", "0.001"))
        self.cmbActivation_5.setItemText(3, _translate("TrainingWidget", "0.03"))
        self.cmbActivation_5.setItemText(4, _translate("TrainingWidget", "0.1"))
        self.cmbActivation_5.setItemText(5, _translate("TrainingWidget", "0.3"))
        self.cmbActivation_5.setItemText(6, _translate("TrainingWidget", "1"))
        self.cmbActivation_5.setItemText(7, _translate("TrainingWidget", "3"))
        self.cmbActivation_5.setItemText(8, _translate("TrainingWidget", "10"))
        self.label_8.setText(_translate("TrainingWidget", "Problem Type"))
        self.cmbActivation_6.setItemText(0, _translate("TrainingWidget", "Classification"))
        self.cmbActivation_6.setItemText(1, _translate("TrainingWidget", "Regression"))
        self.label_9.setText(_translate("TrainingWidget", "Data"))
        self.label_11.setText(_translate("TrainingWidget", "Select dataset from below or add your own"))
        self.pushButton.setText(_translate("TrainingWidget", "Add"))
        self.label_15.setText(_translate("TrainingWidget", "Inclusion Percentage"))
        self.label_10.setText(_translate("TrainingWidget", "Batch Size:"))
        self.label_12.setText(_translate("TrainingWidget", "Resize"))
        self.lnWidth.setStatusTip(_translate("TrainingWidget", "Width"))
        self.lnHeight.setStatusTip(_translate("TrainingWidget", "Height"))

