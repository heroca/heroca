m3 = 0
m5 = 0
for x in range(1,11):
    valor = int(input('Introduzca numero entero: '))
    if valor%3 == 0:
        m3 = m3 + 1
    if valor%5 == 0:
        m5 = m5 + 1
print('multiplo de 3')
print(m3)
print('multiplo de 5')
print(m5)