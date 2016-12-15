datos = "usuario\contraseña\correo"
datos = "fmalo\\123456\\fmalo@espol.edu.ec"

print(datos)
print(len(datos))
print("Total de backslash", datos.count("\\"))

usuario = datos[:datos.find("\\")]
print(usuario)

inicio = datos.find("\\")+1
posi = datos.find("\\",inicio)
correo = datos[posi + 1:]
print(correo)

print(correo.capitalize())
print(correo.endswith("ec"))
print(correo.startswith("fmalo"))

print(correo.lower())
print(correo.upper())

print('{:0>10}'.format('test'))

data = "0000estos0son0mis0datos000000"
data_limpia = data.strip("0")
print (data_limpia)

data_limpia = data_limpia.replace("0", " ").replace("  ", " ")
print(data_limpia)


print(datos.split("\\"))
