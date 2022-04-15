superficie = 0
cant = 0
num = int(input('introduzca cuantos valores: '))
for x in range(num):
    base = int(input('introduzca la base: '))
    altura = int(input('introduzca la altura: '))
    superficie = base * altura / 2
    print('Superficie:')
    print(superficie)
    if superficie > 12:
        cant = cant +1
print('Cantidad Triangulos cuya superficie es mayor a 12')
print(cant)