
# from practica26.earthquake.datos.texto import preparar_url, realizar_requerimiento, \
#     obtener_eventos, obtener_datos, presentacion_datos



import practica26.earthquake.datos.geojson as g
import practica26.earthquake.datos.texto as t

from practica26.earthquake.presentacion.presentacion import presentacion_datos

t.preparar_url(starttime="2016-04-15", endtime="2016-04-30",
             orderby = "magnitude", limit = "20")

base = t.realizar_requerimiento()
eventos = t.obtener_eventos(base)
data = []

for evento in eventos:
    lista = t.obtener_datos(evento)
    if lista is not None:
        data.append(lista)

presentacion_datos(data)

print("##############################################################")

g.preparar_url(starttime="2016-04-15", endtime="2016-04-30",
             orderby = "magnitude", limit = "20")

base = g.realizar_requerimiento()
eventos = g.obtener_eventos(base, q='ecuador')
data = []

for evento in eventos:
    lista = t.obtener_datos(evento)
    if lista is not None:
        data.append(lista)

presentacion_datos(data)