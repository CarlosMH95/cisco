for i in range(10,0,-1):
    print (i)
mensaje= "Hola Mundo"
for letra in mensaje:
    print(letra)
dato="carlos|21|carlos@espol.edu.ec"
datos=dato.split("|")

for elemento in datos:
    print (elemento)
numeros=[1,20,78,50]
for indice in range(len(numeros)):
    if numeros[indice]%2==0:
        print(numeros[indice], "es par")
    else:
        print(numeros[indice], "es impar")

mensaje="Esto es una cadena de texto".lower()
vocales=0
consonantes=0
vocal="aeiou"
for letra in mensaje:
    if letra in vocal:
        vocales+=1
    else:
        consonantes+=1
print("Cantidad de vocales:",vocales,"Cantidad de consonantes:", consonantes)