import psycopg2
def conectar(usuario="postgres", password="1234", puerto="5432", nombre_base="sismos", host="localhost"):
    db= psycopg2.connect(database=nombre_base, user=usuario, password=password, host=host, port=puerto)
    print("connected!")
    return db



def leer_registro(tabla, db):
    sql="select * from %s" %tabla
    cursor=db.cursor()
    cursor.execute(sql)
    registros=cursor.fetchall()
    return registros
def insertar_registro(tabla, datos, db):
    campos=datos.keys()
    valores=datos.values()
    sql="INSERT INTO %s(%s) VALUES (%s);" %(tabla, ",".join(campos),"'" +"','".join(valores)+"'")
    cursor = db.cursor()

    cursor.execute(sql)
    db.commit()


db=conectar()
op=-1
while op!=0:
    nombre=input("Ingrese nombre:")

    usuario=input("Ingrese usuario:")
    datos={"nombre":nombre, "usuario":usuario}
    insertar_registro("usuario",datos, db)
    print("##################################")
    op=int(input("Ingrese la opcion: "))
filas=leer_registro("usuario", db)
print (filas)