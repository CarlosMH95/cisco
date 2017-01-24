from sqlalchemy import create_engine
from practica35.base import base
from practica35.usuario.Usuario import Usuario

engine = create_engine('postgresql://postgres:1234@localhost:5432/practica35')
base.Base.metadata.create_all(engine)