
import requests
url = "http://earthquake.usgs.gov/fdsnws/event/1/query"

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

def presentacion_datos(datos):
    for dato in datos:
        plantilla = """
*********************************************
magnitud = %s
lugar = %s
longitud = %s
latitud = %s
*********************************************
""" % (dato[10], dato[12], dato[3], dato[2])
        print(plantilla)

#############################################################################
