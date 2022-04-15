lista=[]
for x in range(10):
    valor=int(input("Ingrese valor:"))
    lista.append(valor)

print(lista)

posicion=0
while posicion<len(lista):
    if lista[posicion]==5:
        lista.pop(posicion)
    else:
        posicion=posicion+1
    
print(lista)

lista=[10, 20, 30, 40, 50]

print(lista)

del(lista[0])
del(lista[1])
del(lista[2])

print(lista) # 20 40