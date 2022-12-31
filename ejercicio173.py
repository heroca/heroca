def cargar():
    lista=[]
    for x in range(10):
        valor=int(input("Cargar valor: "))
        lista.append(valor)
    return lista


def retornar_mitad(lista):
    mitad=len(lista)//2
    return lista[:mitad]


def imprimir(datos):
    print("Contenido de la lista")
    print(datos)


# bloque principal

lista=cargar()
lista2=retornar_mitad(lista)
imprimir(lista)
imprimir(lista2)
