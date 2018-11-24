# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/wellrowwidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WellRowWidget(object):
    def setupUi(self, WellRowWidget):
        WellRowWidget.setObjectName("WellRowWidget")
        WellRowWidget.resize(1608, 31)
        self.horizontalLayout = QtWidgets.QHBoxLayout(WellRowWidget)
        self.horizontalLayout.setContentsMargins(-1, 5, -1, 3)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.wellName = QtWidgets.QLabel(WellRowWidget)
        self.wellName.setMaximumSize(QtCore.QSize(100, 16777215))
        self.wellName.setObjectName("wellName")
        self.horizontalLayout.addWidget(self.wellName)
        self.widget = QtWidgets.QWidget(WellRowWidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_18 = QtWidgets.QWidget(self.widget)
        self.widget_18.setMaximumSize(QtCore.QSize(1000, 10))
        self.widget_18.setStyleSheet("background-color: rgb(92, 53, 102);")
        self.widget_18.setObjectName("widget_18")
        self.horizontalLayout_2.addWidget(self.widget_18)
        self.widget_31 = QtWidgets.QWidget(self.widget)
        self.widget_31.setMaximumSize(QtCore.QSize(1000, 10))
        self.widget_31.setStyleSheet("background-color: rgb(52, 101, 164);")
        self.widget_31.setObjectName("widget_31")
        self.horizontalLayout_2.addWidget(self.widget_31)
        self.widget_53 = QtWidgets.QWidget(self.widget)
        self.widget_53.setMaximumSize(QtCore.QSize(1000, 10))
        self.widget_53.setStyleSheet("\n"
"background-color: rgb(114, 159, 207);")
        self.widget_53.setObjectName("widget_53")
        self.horizontalLayout_2.addWidget(self.widget_53)
        self.widget_21 = QtWidgets.QWidget(self.widget)
        self.widget_21.setMaximumSize(QtCore.QSize(1000, 10))
        self.widget_21.setStyleSheet("background-color: rgb(78, 154, 6);")
        self.widget_21.setObjectName("widget_21")
        self.horizontalLayout_2.addWidget(self.widget_21)
        self.widget_61 = QtWidgets.QWidget(self.widget)
        self.widget_61.setMaximumSize(QtCore.QSize(1000, 10))
        self.widget_61.setStyleSheet("background-color: rgb(143, 89, 2);")
        self.widget_61.setObjectName("widget_61")
        self.horizontalLayout_2.addWidget(self.widget_61)
        self.widget_28 = QtWidgets.QWidget(self.widget)
        self.widget_28.setMaximumSize(QtCore.QSize(1000, 10))
        self.widget_28.setStyleSheet("background-color: rgb(193, 125, 17);")
        self.widget_28.setObjectName("widget_28")
        self.horizontalLayout_2.addWidget(self.widget_28)
        self.widget_36 = QtWidgets.QWidget(self.widget)
        self.widget_36.setMaximumSize(QtCore.QSize(1000, 10))
        self.widget_36.setStyleSheet("background-color: rgb(233, 185, 110);")
        self.widget_36.setObjectName("widget_36")
        self.horizontalLayout_2.addWidget(self.widget_36)
        self.widget_7 = QtWidgets.QWidget(self.widget)
        self.widget_7.setMaximumSize(QtCore.QSize(1000, 10))
        self.widget_7.setStyleSheet("background-color: rgb(164, 0, 0);")
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_2.addWidget(self.widget_7)
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(WellRowWidget)
        QtCore.QMetaObject.connectSlotsByName(WellRowWidget)

    def retranslateUi(self, WellRowWidget):
        _translate = QtCore.QCoreApplication.translate
        WellRowWidget.setWindowTitle(_translate("WellRowWidget", "Form"))
        self.wellName.setText(_translate("WellRowWidget", "HWYH0001"))

