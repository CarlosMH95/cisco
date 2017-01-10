from practica26.earthquake.datos.texto import *
from practica26.earthquake.presentacion.presentacion import *
##Deberia poner las fucniones para que no se cargue

preparar_url(starttime="2016-04-15", endtime="2016-04-30",
             orderby="magnitude", limit="20")
base = realizar_requerimiento()
eventos = obtener_eventos(base)
data = []
for evento in eventos:
    lista = obtener_datos(evento)
    if lista is not None:
        data.append(lista)

presentacion_datos(data)
