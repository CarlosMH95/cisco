# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'l:\prueba.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Usuario(object):
    def setupUi(self, Usuario):
        Usuario.setObjectName("Usuario")
        Usuario.resize(400, 300)
        self.lv_usuario = QtWidgets.QListView(Usuario)
        self.lv_usuario.setGeometry(QtCore.QRect(80, 50, 256, 192))
        self.lv_usuario.setObjectName("lv_usuario")

        self.retranslateUi(Usuario)
        QtCore.QMetaObject.connectSlotsByName(Usuario)

    def retranslateUi(self, Usuario):
        _translate = QtCore.QCoreApplication.translate
        Usuario.setWindowTitle(_translate("Usuario", "Usuario"))

