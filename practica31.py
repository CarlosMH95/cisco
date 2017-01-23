import requests
import urllib
from urllib.request import urlopen
import xml.etree.ElementTree as ET

response = urllib.request.urlopen("http://earthquake.usgs.gov/fdsnws/event/1/query?format=xml&starttime=2016-04-16&endtime=2016-04-17")

#tree = ET.parse('c:\\mi_xml.xml')

tree = ET.parse(response)
root = tree.getroot() #obtengo la referencia de la raiz

for child in root:  #obtengo los hijos desde la raiz
    for item in child: #obtengo una referencia a cada uno de los items de los hijos
        if item.text is not None: #no todos los hijos tienen nodo de texto
            print(item.tag, item.text) #muestro el nodo de texto y el nombre del tag
        else:
            print(item.tag, item.attrib) #muestro un diccionario de los atributos
    print("\n")
