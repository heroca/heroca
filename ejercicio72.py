lista=[100,70,300,77,200,180,95,500]
suma=0
x=0
while x<len(lista):
    if lista[x] > 100:
        suma=suma+1
    x=x+1
print("Los elementos de la lista son")
print(lista)
print("La elementos mayores a 100 es")
print(suma)  