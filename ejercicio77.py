lista = []
suma = 0
promedio = 0
for x in range(5):
    valor = float(input('Sueldo: '))
    lista.append(valor)
    suma = suma + valor
promedio = suma / len(lista)
print(lista)
print(promedio)