def cargar():
    diccionario={}
    continua="s"
    while continua=="s":
        caste=raw_input("Ingrese palabra en castellano:")
        ing=raw_input("Ingrese palabra en ingles:")
        diccionario[ing]=caste
        continua=raw_input("Quiere cargar otra palabra:[s/n]")
    return diccionario


def imprimir(diccionario):
    print("Listado completo del diccionario")
    for ingles in diccionario:
        print(ingles,diccionario[ingles])


def consulta_palabra(diccionario):
    pal=raw_input("Ingrese la palabra en ingles a consultar:")
    if pal in diccionario:
        print("En castellano significa:",diccionario[pal])


# bloque principal

diccionario=cargar()
imprimir(diccionario)
consulta_palabra(diccionario)