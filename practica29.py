import threading
import requests
from ubidots import ApiClient
import time
def obtenerDatosAArchivo(nombre_archivo,fecha_inicial, fecha_final, id):
    url='http://earthquake.usgs.gov/fdsnws/event/1/query?format=text&starttime=%s&endtime=%s'%(fecha_inicial,fecha_final)
    response = requests.get(url)
    data = response.text
    a = 0
    f=open(nombre_archivo,"a")

    datosSeparados = data.split("\n")
    for i in datosSeparados:
        lineaDatos = i.split("|")
        for x in lineaDatos:
            if (len(lineaDatos)> 12):
                a += 1
                magnitud = lineaDatos[10]
                lugar= (lineaDatos[12])
                linea="Magnitud: %s, Lugar: %s Proceso %d\n"%(magnitud,lugar,id)
                f.write(linea)
    f.close()


#obtenerInfoSismos()
list_procesos=[]
list_procesos.append(threading.Thread(target=obtenerDatosAArchivo, args=("sismos.txt","2016-01-01", "2016-02-01", 1)))
list_procesos.append(threading.Thread(target=obtenerDatosAArchivo, args=("sismos.txt","2016-02-02", "2016-03-01", 2)))
list_procesos.append(threading.Thread(target=obtenerDatosAArchivo, args=("sismos.txt","2016-03-02", "2016-04-01", 3)))
for t in list_procesos:
    t.start()

