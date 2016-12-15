cadena = "Esto es un texto"
print(cadena[0])
print(cadena[-1])

cadena = "Esto es un \"texto\" entre comillas"
print(cadena)
cadena = "una\t\t\ttabulacion"
print(cadena)
cadena = "Primera linea\nSegunda linea"
print(cadena)
cadena = "Hola  Bienvenidos\rAdios Mundo"
print (cadena)


cadena = "Hola Mundo"
print("Mundo" in cadena)

cadena = "Hola Mundo"
print(cadena[2:7])
print(cadena[-8:-3])
print(cadena[2:7:2])
print(cadena[5:]) #Hasta el final de la cadena
print(cadena[:4]) #desde el inicio hasta la posicion final
print(cadena[::-1]) #invertir string
print(cadena[6:1:-2]) #substring invertido

print(cadena[-7:-11:-1]) #invertir string
print(cadena[:-6:-1]) #invertir string

####################################################################
print(len(cadena))
print(min("hola@mundo"))
print(max("hola@mundo"))