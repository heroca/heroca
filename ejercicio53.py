pos = 0
neg = 0
pares = 0
mult = 0
for x in range(10):
    valor = int(input('Introduzca valor entero: '))
    if valor < 0:
        neg = neg + 1
    else:
        pos = pos + 1
    if valor%2 == 0:
        pares = pares + valor
    if valor%15 == 0:
        mult = mult + 1
print('Positivos:')
print(pos)
print('Negativos:')
print(neg)
print('Multiplos de 15')
print(mult)
print('Cantidad acumulada de numeros pares:')
print(pares)
