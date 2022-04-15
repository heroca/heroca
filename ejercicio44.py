mayor = 0
menor = 0
for x in range(1,11):
    nota = int(input('Introduzca nota: '))
    if nota >= 7:
        mayor = mayor + 1
    else:
        menor = menor + 1
print('mayor a 7')
print(mayor)
print('menor a 7')
print(menor)