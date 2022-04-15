lista=[]
for x in range(5):
    valor=int(input("Ingrese valor:"))
    lista.append(valor)

mayor=lista[0]
for x in range(1,5):
    if lista[x]>mayor:
        mayor=lista[x]
repite = 0
for x in range(5):
    if mayor==lista[x]:
        repite = repite + 1
print("Lista completa")
print(lista)
print("Mayor de la lista")
print(mayor)
if repite > 1:
    print('Se repite ' + str(repite) + ' veces')