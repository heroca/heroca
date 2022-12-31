try:
    archi1=open("datos.txt","w") 
    archi1.write("Primer línea.\n") 
    archi1.write("Segunda línea.\n") 
    archi1.write("Tercer línea.\n")  
    archi1.write(3334)
except TypeError:
    print("No se puede grabar un entero con write")    
finally:
    archi1.close() 
    print("Se cerró el archivo")