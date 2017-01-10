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