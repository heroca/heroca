#usando for
oracion = raw_input('Introduzca una oracion: ')
cantidad = 0
for n in range(len(oracion)):
    if oracion[n] == ' ':
        cantidad = cantidad + 1
print("total de caracteres en blanco")
print(cantidad)
