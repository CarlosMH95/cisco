from spotify import buscar_musica
def presentarResultados(lista, indice):
    print(indice,".- Track: ", lista[0],"\n\t Popularidad: ",lista[1], "\n\t Duracion: ",int((lista[3]/1000)/60)," minutes ", int((lista[3]/1000)%60),"segundos\n\t Artista: " , lista[4])
    return

while True:
    resultado=buscar_musica("metallica")
    print(resultado)
    print("""
    ********************************************************
    **  SELECCIONE LA ACCION QUE DESEA REALIZAR           **
    **      1-ORDENAR POR NOMBRE DE CANCION               **
    **      2-ORDENAR POR POPULARIDAD                     **
    **      3-ORDENAR POR DURACION DE CANCION             **
    **      4-ORDENAR POR NOMBRE DE ARTISTA               **
    **      5-SALIR                                       **
    ********************************************************\n
    """)
    opcion=input("Ingrese la opcion que quiera ejecutar: ")
    if opcion =="1":
        print (len(resultado))
        print ("Entro")
        resultado.sort(key=lambda y: y[0])
        indice=0
        for x in resultado:
            indice+=1
            presentarResultados(x,indice)
        print("**********************************")

    elif opcion=="2":
        print(len(resultado))
        print("Entro")
        resultado.sort(key=lambda y: y[1])
        for x in resultado:
            print(x)
        print("**********************************")
    elif opcion=="3":
        print(len(resultado))
        print("Entro")
        resultado.sort(key=lambda y: y[3])
        for x in resultado:
            print(x)
        print("**********************************")
    elif opcion=="4":
        print(len(resultado))
        print("Entro")
        resultado.sort(key=lambda y: y[4])
        for x in resultado:
            print(x)
        print("**********************************")
    elif opcion=="5":
        break


#presentar los resultados de manera ordenada,
# ordenar de a cuerdo a cualquier criterio que el usuario elija
#convertir el timempo de ms a h:m:s
