cadena = "Anula la luz azul a la Luna"
sin_espacios = cadena.replace(" ","").lower()
al_reves = sin_espacios[::-1].lower()

if sin_espacios == al_reves :
    print ("Palabra es Palindroma")
    print ("",sin_espacios)
    print (al_reves)
else:
    print ("Palabra no es Palindroma")


import re

patron = "^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \?=.-]*)*\/?$"
valor = "http://www.google.com.ec"

if re.match(patron, valor):
    print ("Dirección Web valida")
else:
    print("Dirección Web no valida")



################################################################################


patron = "^(([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]).){3}([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
valor = "255.168.1.1"

if re.match(patron, valor):
    print ("Dirección ip valida")
else:
    print("Dirección ip no valida")


################################################################################


patron = "^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3})$"
valor = "fmalo@espol@edu.ec"

if re.match(patron, valor):
    print ("Dirección mail valida")
else:
    print("Dirección mail no valida")


edad = 50

if 10 > edad >1 :
    print ("niño")
elif 19> edad > 11:
    print ("Adolesencia")
elif 65 > edad > 19:
    print ("Madurez")
else:
    print ("Vejez")