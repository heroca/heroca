paises=[]
temperaturas=[]
promediotemp=[]

for x in range(4):
    nom=raw_input("Ingrese el nombre del pais:")
    paises.append(nom)
    temp1=int(input("Ingrese primer temperatura:"))
    temp2=int(input("Ingrese segunda temperatura:"))
    temp3=int(input("Ingrese tercer temperatura:"))
    temperaturas.append([temp1, temp2, temp3])

print("Paises y temperaturas medias de los ultimos tres meses mensuales")
for x in range(4):
    print(paises[x],temperaturas[x][0],temperaturas[x][1],temperaturas[x][2])

for x in range(4):
    pro=(temperaturas[x][0]+temperaturas[x][1]+temperaturas[x][2])//3
    promediotemp.append(pro)

print("Paises y temperaturas medias trimestrales")
for x in range(4):
    print(paises[x],promediotemp[x])

posmayor=0
for x in range(1,4):
    if promediotemp[x]>promediotemp[posmayor]:
        posmayor=x
print("Pais con temperatura media trimestral mayor:", paises[posmayor])
