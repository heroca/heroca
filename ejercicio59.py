nombre1=raw_input("Ingrese el primer nombre:")
nombre2=raw_input("Ingrese el segundo nombre:")
if nombre1==nombre2:
    print("Ingreso dos nombre iguales")
else:
    if nombre1>nombre2:
        print(nombre1)
        print("es mayor alfabeticamente")
    else:
        print(nombre2)
        print("es mayor alfabeticamente")