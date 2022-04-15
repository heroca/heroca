entero=int(input("Ingrese numero entero de hasta 3 cifras:"))
if entero>999:
    print('Error el numero es mayor de 3 cifras')
else:
    if entero<=9:
        print('una cifras')
    else:
        if entero<=99:
            print('dos cifras')
        else:
            print('tres cifra')