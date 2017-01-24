

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from practica35.usuario.Usuario import Usuario
from sqlalchemy.orm import sessionmaker
from practica35.base.creacionBaseDatos import engine
from sqlalchemy.orm.exc import NoResultFound

class Ui_creacion_usuario(object):
    def setupUi(self, creacion_usuario):
        creacion_usuario.setObjectName("creacion_usuario")
        creacion_usuario.resize(400, 300)
        self.txt_usuario = QtWidgets.QLineEdit(creacion_usuario)
        self.txt_usuario.setGeometry(QtCore.QRect(110, 70, 211, 22))
        self.txt_usuario.setObjectName("txt_usuario")
        self.txt_contrasenia = QtWidgets.QLineEdit(creacion_usuario)
        self.txt_contrasenia.setGeometry(QtCore.QRect(110, 110, 211, 22))
        self.txt_contrasenia.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_contrasenia.setObjectName("txt_contrasenia")
        self.btn_guardar = QtWidgets.QPushButton(creacion_usuario)
        self.btn_guardar.setGeometry(QtCore.QRect(80, 170, 93, 31))
        self.btn_guardar.setObjectName("btn_guardar")
        self.label = QtWidgets.QLabel(creacion_usuario)
        self.label.setGeometry(QtCore.QRect(30, 70, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(creacion_usuario)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 61, 16))
        self.label_2.setObjectName("label_2")
        self.btn_cancelar = QtWidgets.QPushButton(creacion_usuario)
        self.btn_cancelar.setGeometry(QtCore.QRect(190, 170, 93, 31))
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.retranslateUi(creacion_usuario)

        self.btn_guardar.clicked.connect(self.grabar_usuario)

        QtCore.QMetaObject.connectSlotsByName(creacion_usuario)

    def retranslateUi(self, creacion_usuario):
        _translate = QtCore.QCoreApplication.translate
        creacion_usuario.setWindowTitle(_translate("creacion_usuario", "Crear Usuario"))
        self.btn_guardar.setText(_translate("creacion_usuario", "Guardar"))
        self.label.setText(_translate("creacion_usuario", "usuario"))
        self.label_2.setText(_translate("creacion_usuario", "contraseña"))
        self.btn_cancelar.setText(_translate("creacion_usuario", "Cancelar"))

    def grabar_usuario(self):
        Session = sessionmaker(bind=engine)
        session = Session()
        try:
            usuario = session.query(Usuario).filter_by(usuario=self.txt_usuario.text()).one()
            if usuario is not None:
                self.showdialog("Usuario", "Usuario ya existe")
                session.close()
        except NoResultFound:
            usuario = Usuario()
            usuario.usuario = self.txt_usuario.text()
            usuario.contrasenia = self.txt_contrasenia.text()
            session.add(usuario)
            session.commit()
            session.close()
            self.txt_usuario.setText("")
            self.txt_contrasenia.setText("")
            self.showdialog("Usuario", "Operación exitosa")
        except Exception as ex:

            session.rollback()
            self.showdialog("Usuario", "Error")
            session.close()



    def showdialog(self, titulo, mensaje):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText(mensaje)
        #msg.setInformativeText("This is additional information")
        msg.setWindowTitle(titulo)
        #msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        #msg.buttonClicked.connect(msgbtn)
        retval = msg.exec_()