paises=[]
habitantes=[]
for x in range(5):
    nom=raw_input("Ingrese el nombre del pais:")
    paises.append(nom)
    no=raw_input("Ingrese el numero de habitantes:")
    habitantes.append(no)

#Ordenado por habitantes
for k in range(4):
    for x in range(4-k):
        if paises[x]>paises[x+1]:
            aux1=habitantes[x]
            habitantes[x]=habitantes[x+1]
            habitantes[x+1]=aux1
            aux2=paises[x]
            paises[x]=paises[x+1]
            paises[x+1]=aux2

print("Lista de paises y sus habitantes ordenada alfabeticamente")
for x in range(5):
    print(paises[x],habitantes[x])

#Ordenado por paises
for k in range(4):
    for x in range(4-k):
        if habitantes[x]<habitantes[x+1]:
            aux1=habitantes[x]
            habitantes[x]=habitantes[x+1]
            habitantes[x+1]=aux1
            aux2=paises[x]
            paises[x]=paises[x+1]
            paises[x+1]=aux2

print("Lista de paises y sus habitantes ordenada de mayor a menor por habitante")
for x in range(5):
    print(paises[x],habitantes[x])

