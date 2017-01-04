d = {1:"test",1.1:[5,7,"otro test"],"tercer":"otra cadena",(1,0):5, (5,4):1.1}

print (d[1])
print (d[1.1])
print (d["tercer"])
print (d[1,0])

d[3] = "Nuevo elemento"
d[1] = "Remplazo de Valor"

print (d)

del d[1.1]
print (d)

print(d.keys())
print(d.values())
print(d.items())


for k in d.keys():
    print(k, "\t",d[k])

for k,v in d.items():
    print(k, "\t",v)

for k in d:
    print(k,"\t",d[k])

a = (1,0)
if a in d:
    print(d[a])
    del d[a]

k = 1
if k in d:
    print (d[k])
else:
    print ("la clave no existe")