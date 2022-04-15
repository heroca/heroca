def cadena(valor):
    vocales = 0
    for x in range(len(valor)):
        if valor[x]=='a' or valor[x]=='e' or valor[x]=='i' or valor[x]=='o' or valor[x]=='u':
            vocales = vocales + 1
    print('Cantidad de vocales de la palabra ',valor,' es: ',vocales)

def inicio():
    for x in range(3):
        valor = raw_input('Cadena: ')
        cadena(valor)

inicio()