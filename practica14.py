import requests
from ubidots import ApiClient

import time

api = ApiClient(token='Sm5ihUyNjAoPy7FZMsVhgLS07VzFxp')
my_variable = api.get_variable('5851fb1476254275dcc8b27e')


response=requests.get('http://earthquake.usgs.gov/fdsnws/event/1/query?format=text&starttime=2016-04-16&endtime=2016-04-26')
data=response.text

a=0
datosSeparados=data.split("\n")
for i in datosSeparados:
    lineaDatos=i.split("|")
    for x in lineaDatos:
        if (x.find("Ecuador") != -1):
            a+=1
            dato=lineaDatos[10]
            dato2=float(dato)
            new_value=my_variable.save_value({'value':dato2})
            print("Envio: ", a)
