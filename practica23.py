import json

import requests

url = "http://things.ubidots.com/api/v1.6/variables/5848c8d47625422c4ec9767e/values"
parametros = {"format":"json","token":"aw3vYXYy13i9xVl75Zt1jQAsQpde8j"}
response = requests.get(url=url, params=parametros)

print (response.text)

datos = json.loads(response.text)
for resultado in datos["results"]:
    print ("Valor",resultado["value"])
    print("Creado en", resultado["created_at"])
    for k,v in resultado["context"].items():
        print (k,v)
    print ("##########################################")



    