import threading
import requests
from ubidots import ApiClient
import time
def obtenerInfoSismos():
    response = requests.get(
        'http://earthquake.usgs.gov/fdsnws/event/1/query?format=text&starttime=2016-04-16&endtime=2016-06-05')
    data = response.text
    a = 0
    datosSeparados = data.split("\n")
    for i in datosSeparados:
        lineaDatos = i.split("|")
        for x in lineaDatos:
            if (x.find("Ecuador") != -1):
                a += 1
                dato = lineaDatos[10]
                dato2 = float(dato)
                print(({'value': dato2}))
                time.sleep(0.5)
#obtenerInfoSismos()
t=threading.Thread(target=obtenerInfoSismos)
t.start()
print("test")
i=0
while True:
    print(i)
    i+=1
    time.sleep(0.5)