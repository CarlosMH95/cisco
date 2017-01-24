from sqlalchemy import Column, Integer, String
from practica35.base import base

class Usuario(base.Base):
    __tablename__ = 'USUARIO'
    id = Column(Integer, primary_key=True)
    nombres =  Column(String(50))
    apellidos = Column(String(50))
    usuario = Column(String(15))
    contrasenia = Column(String(64))