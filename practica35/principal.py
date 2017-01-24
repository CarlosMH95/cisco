from practica35.interfaces.usuario.creacion_usuario import Ui_creacion_usuario
from PyQt5 import QtWidgets
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_creacion_usuario()
    ui.setupUi(Form)

    Form.show()
    sys.exit(app.exec_())


#from practica35.usuario.Usuario import Usuario
#from sqlalchemy.orm import sessionmaker
#from practica35.base.creacionBaseDatos import engine


#Session = sessionmaker(bind=engine)
#session = Session()

#usuario1 = Usuario()
#usuario1.usuario = "cmalo"
#usuario1.nombres = "Carlos"
#usuario1.apellidos = "malo"
#usuario1.contrasenia = "654123"

#session.add(usuario1)
#session.commit()



