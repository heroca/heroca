x = 1
lista1 = 0
while x <= 15:
    valor = int(input('Lista 1 Valor ' + str(x) + ': '))
    lista1 = lista1 + valor
    x = x + 1
x = 1
lista2 = 0
while x <= 15:
    valor = int(input('Lista 2 Valor ' + str(x) + ': '))
    lista2 = lista2 + valor
    x = x + 1
if lista1 > lista2:
    print('Lista 1 mayor')
else:
    if lista2 > lista1:
        print('Lista 2 mayor')
    else:
        print('Listas iguales')