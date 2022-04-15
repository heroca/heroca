lista = []
suma = 0
promedio = 0
alta = 0
baja = 0
for x in range(5):
    valor = float(input('Altura: '))
    lista.append(valor)
    suma = suma + valor
promedio = suma / len(lista)
for x in range(len(lista)):
    if lista[x] > promedio:
        alta = alta + 1
    else:
        baja = baja + 1
print('promedio')
print(promedio)
print('cantidad de personas mas altas que el promedio')
print(alta)
print('cantidad de personas menos altas que el promedio')
print(baja)