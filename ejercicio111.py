lista1=[]
for x in range(5):
    valor=int(input("Ingrese valor:"))
    lista1.append(valor)

print("Lista original")
print(lista1)

lista2=[]
posicion=0
while posicion<len(lista1):
    if lista1[posicion]>=10:
        lista2.append(lista1.pop(posicion))
    else:
        posicion=posicion+1

print("Lista despues de borrar los elementos mayores o iguales a 10")
print(lista1)
print("Lista generada con los elementos mayores o iguales a 10")
print(lista2)