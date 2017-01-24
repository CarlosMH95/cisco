# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\interfaces\usuarios.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from practica35.usuario.Usuario import Usuario
from sqlalchemy.orm import sessionmaker
from practica35.base.creacionBaseDatos import engine


class QCustomQWidget(QtWidgets.QListWidgetItem):
    def __init__(self, parent=None):
        super(QCustomQWidget, self).__init__(parent)
        self.usuario = None

    def setUsuario(self, usuario):
        self.usuario = usuario
        self.setText(usuario.usuario)

class Ui_usuarios(object):
    def setupUi(self, usuarios):
        usuarios.setObjectName("usuarios")
        usuarios.resize(400, 474)
        self.lw_usuarios = QtWidgets.QListWidget(usuarios)
        self.lw_usuarios.setGeometry(QtCore.QRect(60, 40, 256, 192))
        self.lw_usuarios.setObjectName("lw_usuarios")
        self.contrasenia = QtWidgets.QLineEdit(usuarios)
        self.contrasenia.setGeometry(QtCore.QRect(120, 320, 113, 22))
        self.contrasenia.setObjectName("contrasenia")
        self.txt_usuario = QtWidgets.QLabel(usuarios)
        self.txt_usuario.setGeometry(QtCore.QRect(120, 270, 111, 16))
        self.txt_usuario.setText("")
        self.txt_usuario.setObjectName("txt_usuario")
        self.Actualizar = QtWidgets.QPushButton(usuarios)
        self.Actualizar.setGeometry(QtCore.QRect(130, 360, 93, 28))
        self.Actualizar.setObjectName("Actualizar")
        self.Borrar = QtWidgets.QPushButton(usuarios)
        self.Borrar.setGeometry(QtCore.QRect(130, 400, 93, 28))
        self.Borrar.setObjectName("Borrar")

        self.retranslateUi(usuarios)

        self.Actualizar.clicked.connect(self.actualizar_usuario)
        self.Borrar.clicked.connect(self.borrar_usuario)

        QtCore.QMetaObject.connectSlotsByName(usuarios)

    def retranslateUi(self, usuarios):
        _translate = QtCore.QCoreApplication.translate
        usuarios.setWindowTitle(_translate("usuarios", "Dialog"))
        self.Actualizar.setText(_translate("usuarios", "Actualizar"))

        self.listar_usuarios()
        self.mostrar_usuarios()

    def listar_usuarios(self):
        Session = sessionmaker(bind=engine)
        session = Session()
        usuarios = session.query(Usuario)

        for usuario in usuarios:
            item = QCustomQWidget()
            item.setUsuario(usuario)
            self.lw_usuarios.addItem(item)

        session.close()


    def mostrar_usuarios(self):
        self.lw_usuarios.itemDoubleClicked.connect(self.showItem)

    def showItem(self, item):
        self.txt_usuario.setText(item.usuario.usuario)

    def actualizar_usuario(self):
        item = self.lw_usuarios.selectedItems()[0]
        print(item)
        Session = sessionmaker(bind=engine)
        session = Session()

        usuario = session.merge(item.usuario)
        #cliente = session.query(Usuario).filter_by(nombres='Juanito').one()
        #print (cliente)
        usuario.contrasenia = self.contrasenia.text()
        session.commit()
    def borrar_usuario(self):
        item = self.lw_usuarios.selectedItems()[0]
        print(item)
        Session = sessionmaker(bind=engine)
        session = Session()

        usuario = session.merge(item.usuario)
        #cliente = session.query(Usuario).filter_by(nombres='Juanito').one()
        #print (cliente)
        session.delete(usuario)
        session.commit()
        session.close()
        self.lw_usuarios.update()

