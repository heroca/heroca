# añade contenido al final del archivo con el parametro "a" append
archi1=open("datos.txt","a")
archi1.write("nueva línea 1\n")
archi1.write("nueva línea 2\n")
archi1.close()
archi1=open("datos.txt","r")
contenido=archi1.read()
print(contenido)
archi1.close()