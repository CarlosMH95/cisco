import requests
import numpy as np

response = requests.get('http://earthquake.usgs.gov/fdsnws/event/1/query?format=text&starttime=2016-04-16&endtime=2016-05-20')
data = response.text

q = "ecuador"
eventos = data.split("\n")
datos = data.splitlines()
lista =[]
for evento in eventos:
    if evento.lower().find(q.lower()) >=0:
        datos = evento.split("|")
        lista.append(datos)
matrix = np.array(lista)

magnitudes = matrix[:,10]
magnitudes = np.array(magnitudes,float)

print ("Mayor magnitud", np.max(magnitudes))
indice_max  = np.argmax(magnitudes)
print("Lugar: ",matrix[indice_max,12])


print ("Menor magnitud", np.min(magnitudes))
indice_min  = np.argmin(magnitudes)
print("Lugar: ",matrix[indice_min,12])


print (lista)