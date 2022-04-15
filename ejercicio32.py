x=1
mayores = 0
menores = 0
while x <= 10:
    nota=int(input('Nota:'))
    if nota >= 7:
        mayores = mayores + 1
    else:
        menores = menores + 1
    x = x + 1
print('Total Mayores')
print(mayores)
print('Total menores')
print(menores)