# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'l:\prueba.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(412, 321)
        self.btn_ingreso = QtWidgets.QPushButton(Dialog)
        self.btn_ingreso.setGeometry(QtCore.QRect(140, 100, 75, 23))
        self.btn_ingreso.setObjectName("btn_ingreso")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(110, 70, 113, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        self.btn_ingreso.clicked.connect(self.lineEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_ingreso.setText(_translate("Dialog", "Ingresar"))
        self.lineEdit.setText(_translate("Dialog", "Hola"))

