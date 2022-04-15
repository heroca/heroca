n = int(input('Cuantos numeros enteros:'))
x = 1
pares = 0
impares = 0
while x <= n:
    valor = int(input('Valor: ' + str(x) + ': '))
    if valor%2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    x = x + 1
print('Numero de pares: ' + str(pares))
print('Numero de impares: ' + str(impares))