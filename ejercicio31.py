piezas=int(input('cantidad de piezas:'))
x = 1
totalpiezas=0
while x<=piezas:
    longitud=float(input('Longitud:'))
    if longitud >=1.2 and longitud <=1.30:
        totalpiezas = totalpiezas + 1
    x=x+1
print('Cantidad de piezas aptas')
print(totalpiezas)