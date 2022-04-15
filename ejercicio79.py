lista1 = []
lista2 = []
print('Sueldos turno manana')
for x in range(8):
    if x == 4:
        print('Sueldos turno tarde')
    valor = float(input('Sueldo: '))
    if x < 4:
        lista1.append(valor)
    else:
        lista2.append(valor)
print('Turno manana')
print(lista1)
print('Turno tarde')
print(lista2)