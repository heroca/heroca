def sumar(v1,v2,*lista):
    suma=v1+v2
    for x in range(len(lista)):
        suma=suma+lista[x]
    return suma


# bloque principal

print("La suma de 1+2")
print(sumar(1,2))
print("La suma de 1+2+3+4")
print(sumar(1,2,3,4))
print("La suma de 1+2+3+4+5+6+7+8+9+10")
print(sumar(1,2,3,4,5,6,7,8,9,10))



#Desempaquetar una lista o tupla
def sumar(v1, v2, v3):
    return v1 + v2 + v3

li=[2, 4, 5]
su=sumar(*li)
print(su)