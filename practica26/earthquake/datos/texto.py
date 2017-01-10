
import requests
from practica26.earthquake.datos.constantes import URLBASE as url

def validar_magnitud(func):
    def envoltura(evento):
        datos = func(evento)
        if datos[10] == '' or float(datos[10]) <= 6:
            return None
        else:
            return datos
    return envoltura

def preparar_url(format = "text", **kwargs):
    global url
    url += "?format=%s"%format
    argumentos = ""
    for k,v in kwargs.items():
        argumentos += "&%s=%s" % (k,v)
    url += argumentos

def realizar_requerimiento():
    response = requests.get(url)
    return response.text

def obtener_eventos(base_completa, q="ecuador"):
    eventos = base_completa.split("\n")
    resultado = []
    for evento in eventos:
        if evento.lower().find(q.lower()) >= 0:
            resultado.append(evento)
    return resultado

@validar_magnitud
def obtener_datos(evento):
    return evento.split("|")



#############################################################################
