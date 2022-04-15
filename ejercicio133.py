def carga_lista():
    li=[]
    for x in range(5):
        valor=int(input("Ingrese valor:"))
        li.append(valor)
    return li


def retornar_mayormenor(li):
    ma=li[0]
    me=li[0]
    for x in range(1,len(li)):
        if li[x]>ma:
            ma=li[x]
        else:
            if li[x]<me:
                me=li[x]
    return [ma,me]                


# bloque principal del programa
# Se puede obtener de esta manera
lista=carga_lista()
rango=retornar_mayormenor(lista)
print("Mayor elemento de la lista:",rango[0])
print("Menor elemento de la lista:",rango[1])
#Se puede obtener de esta otra manera
lista=carga_lista()
mayor, menor=retornar_mayormenor(lista)
print("Mayor elemento de la lista:",mayor)
print("Menor elemento de la lista:",menor)
