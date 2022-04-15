cant = 0
num = int(input('introduzca cuantos valores: '))
for x in range(num):
    valor = int(input('introduzca valor: '))
    if valor >= 1000:
        cant = cant +1
print('Cantidad de valores mayores a 1000')
print(cant)