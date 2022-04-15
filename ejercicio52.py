plano1 = 0
plano2 = 0
plano3 = 0
plano4 = 0
n = int(input('Cuantos puntos? '))
for x in range(n):
    x = int(input('coordenada x: '))
    y = int(input('coordenada y: '))
    if x > 0 and y > 0:
        plano1 = plano1 + 1
    else:
        if x < 0 and y > 0:
            plano2 = plano2 + 1
        else:
            if x < 0 and y < 0:
                plano3 = plano3 + 1
            else:
                plano4 = plano4 + 1
print('Total primer plano')
print(plano1)
print('Total segundo plano')
print(plano2)
print('Total tercer plano')
print(plano3)
print('Total cuarto plano')
print(plano4)