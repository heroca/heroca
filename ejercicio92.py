elementos=[]
for x in range(5):
    valor=int(input("Ingrese valor:"))
    elementos.append(valor)

print("Lista sin ordenar")
print(elementos)
# Lista odenada de menor a mayor
for k in range(4):
    for x in range(4-k):
        if elementos[x]>elementos[x+1]:
            aux=elementos[x]
            elementos[x]=elementos[x+1]
            elementos[x+1]=aux
print("Lista ordenada de menor a mayor")
print(elementos)
#Lista ordenada de mayor a menor
for k in range(4):
    for x in range(4-k):
        if elementos[x]<elementos[x+1]:
            aux=elementos[x]
            elementos[x]=elementos[x+1]
            elementos[x+1]=aux
print("Lista ordenada de mayor a menor")
print(elementos)