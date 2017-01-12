import datetime
f=open("l:\\log.txt", "a")
fecha_actual=datetime.datetime.now().strftime("%d - %m - %Y  %H:%M:%S")
f.write(fecha_actual+"\n")
f.close()