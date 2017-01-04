import requests
import numpy as np


response = requests.get('http://earthquake.usgs.gov/fdsnws/event/1/query?format=text&starttime=2016-04-16&endtime=2016-04-20')
data = response.text

eventos = data.split("\n")
lista = []
for i in range(len(eventos)):
    if i > 0 and eventos[i]:
        datos = eventos[i].split("|")
        if datos[10] == '' or float(datos[10]) <= 0:
            continue
        lista.append(datos)
matrix = np.array(lista)

print(matrix)

magnitudes = matrix[:,10]
magnitudes = np.array(magnitudes, float)

print("Mayor magnitud", np.max(magnitudes))
indice_max = np.argmax(magnitudes)
print("Lugar:", matrix[indice_max,12])


print("Menor magnitud", np.min(magnitudes))
indice_min = np.argmin(magnitudes)
print("Lugar:", matrix[indice_min,12])

indice_ord = np.argsort(magnitudes)[::-1]
matrix_ord_mag = matrix[indice_ord,:]

for registro in matrix_ord_mag:
    print ("magnitud", registro[10], "\t" ,"Lugar", registro[12])