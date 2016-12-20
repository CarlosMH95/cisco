import requests
from ubidots import ApiClient
from datetime import date, datetime




import time

api = ApiClient(token='Sm5ihUyNjAoPy7FZMsVhgLS07VzFxp')
my_variable = api.get_variable('5851fb1476254275dcc8b27e')


response=requests.get('http://earthquake.usgs.gov/fdsnws/event/1/query?format=text&starttime=2016-04-16&endtime=2016-04-26')
data=response.text

a=0
datosSeparados=data.split("\n")
listSinOrdenar=[]
for i in datosSeparados:
    lineaDatos=i.split("|")
    for x in lineaDatos:
        if (x.find("Ecuador") != -1):
            lista=[]
            timestamp=lineaDatos[1]

            #Aqui va el codigo para hacer lo del timestamp
            time_tuple = time.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%f")
            print(time_tuple)
            dt=time.mktime(time_tuple)
            dt-=(5*60*60)
            print (dt)
            lat=lineaDatos[2]
            lon=lineaDatos[3]

            #|2016-04-25T23:54:22.710|

            a+=1
            dato=lineaDatos[10]
            magnitud=float(dato)
            lista.append(dt)
            lista.append(lat)
            lista.append(lon)
            lista.append(magnitud)
            #new_value=my_variable.save_value({'value':magnitud})
            #fecha del evento, llevar de string a Time o TimeStamp
            #Info geografica Lat, Long
            #Dashboard presentar la info geografica por medio de un mapa
            listSinOrdenar.append(lista.copy())
            print("Envio: ", a)


listSinOrdenar.reverse()
a=0
for x in listSinOrdenar:
    a+=1
    new_value=my_variable.save_value({'value':x[3], "context": {"lat": float(x[1]), "lng": float(x[2])}, "timestamp":int(x[0])*1000})
    time.sleep(2)
    print("Envio: ", a)

