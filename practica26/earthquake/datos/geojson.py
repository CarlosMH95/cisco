import requests
import json

from practica26.earthquake.datos.constantes import  URLBASE as URL_BASE

def validar_magnitud(func):
    def envoltura(evento):
        datos = func(evento)
        if len(datos)!= 13 or datos[10] == '':
            return None
        else:
            return datos
    return envoltura

def preparar_url(format = "geojson", **kwargs):
    global URL_BASE

    URL_BASE += "?format=%s"%format
    argumentos = ""
    for k,v in kwargs.items():
        argumentos += "&%s=%s" % (k,v)
        URL_BASE += argumentos

def realizar_requerimiento():
    response = requests.get(URL_BASE)
    return json.loads(response.text)


def obtener_eventos(base_completa, q=None):
    resultado = []
    for evento in base_completa["features"]:
        if q is not None:
            if evento["properties"]["place"].lower().find(q.lower()) >= 0:
                l = ["","",str(evento["geometry"]["coordinates"][0]),str(evento["geometry"]["coordinates"][1]),"","","","","","",str(evento["properties"]["mag"]),"",str(evento["properties"]["place"])]
                resultado.append("|".join(l))
        else:
            l = ["", "", str(evento["geometry"]["coordinates"][0]), str(evento["geometry"]["coordinates"][1]), "", "",
                 "", "", "", "", str(evento["properties"]["mag"]), "", str(evento["properties"]["place"])]
            resultado.append("|".join(l))
    return resultado

@validar_magnitud
def obtener_datos(evento):
    return evento.split("|")