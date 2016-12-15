from datetime import datetime

anio_nacimiento = input("Ingrese su año de bnacimiento: ")
print(datetime.now().year - int(anio_nacimiento))