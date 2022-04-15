largo = 0
clave = raw_input('Ingrese la clave: ')
largo = len(clave)
if largo < 10 and largo > 20:
    print('Error: numero de caracteres no valido.')
else:
    print('Correcto.')