lista=[]
for x in range(5):
    valor=raw_input("Ingrese nombre: ")
    lista.append(valor)

menor=lista[0]
for x in range(1,5):
    if lista[x]<menor:
        menor=lista[x]

print("Lista completa")
print(lista)
print("Menor de la lista")
print(menor)
