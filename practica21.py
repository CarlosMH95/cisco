OPCIONES = (
    ("opncion1",1),
    ("Opcion 2",2)
)

print (OPCIONES[0][1])

a = ("opncion1",1)
la = list(a)
print (la)
la[1] = 2
a = tuple(la)
print (a)

