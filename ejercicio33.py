personas = int(input('Numero de personas:'))
x = 1
totalaltura = 0
promedio = 0
while x <= personas:
    altura = float(input('Altura de la persona ' + str(x) + ': '))
    totalaltura = totalaltura + altura
    x = x + 1
promedio = totalaltura / personas
print('Promedio de altura')
print(promedio)