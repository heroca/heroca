lista1 = []
lista2 = []
lista3 = []
print('Lista 1')
for x in range(4):
    valor = int(input('Valor: '))
    lista1.append(valor)
print('Lista 2')
for x in range(4):
    valor = int(input('Valor: '))
    lista2.append(valor)
suma = 0
print(lista1)
print(lista2)
print('Lista3')
for x in range(4):
    suma = lista1[x]+lista2[x]
    lista3.append(suma)
print(lista3)