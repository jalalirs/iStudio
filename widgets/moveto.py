# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/editlabel.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
class MoveTo(QDialog):
    def __init__(self, parent = None,sections = []):
        super(MoveTo, self).__init__(parent)
        self.resize(400, 123)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(20, 80, 361, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(20, 10, 361, 32))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.newLbl = QtWidgets.QComboBox(self.widget)
        self.newLbl.setObjectName("newLbl")
        self.newLbl.addItems(sections)
        self.horizontalLayout.addWidget(self.newLbl)

        self.retranslateUi(self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "New Label"))

    def data(self):
        return self.newLbl.currentText()

    @staticmethod
    def getNewSections(parent = None,sections = []):
        dialog = MoveTo(parent,sections)
        result = dialog.exec_()
        nsection = dialog.data()
        return (nsection, result == QDialog.Accepted)
