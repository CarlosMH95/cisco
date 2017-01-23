import xml.etree.ElementTree as ET
import requests

response = requests.get("http://earthquake.usgs.gov/fdsnws/event/1/query?format=xml&starttime=2016-04-16&endtime=2016-04-17")
root = ET.fromstring(response.content)

namespaces = {"xmlns":"http://quakeml.org/xmlns/bed/1.2"}

for evento in root.findall("./xmlns:eventParameters/xmlns:event", namespaces = namespaces):
    print(evento.find("./xmlns:description/xmlns:text", namespaces = namespaces).text)
    print(evento.find("./xmlns:origin/xmlns:time/xmlns:value", namespaces=namespaces).text)
    print(evento.find("./xmlns:origin/xmlns:longitude/xmlns:value", namespaces=namespaces).text)
    print(evento.find("./xmlns:origin/xmlns:latitude/xmlns:value", namespaces=namespaces).text)
    print(evento.find("./xmlns:magnitude/xmlns:mag/xmlns:value", namespaces=namespaces).text)
    print("####################################################################")