def cadena(palabra):
    contador = 0
    for x in range(len(palabra)):
        if palabra[x] == 'a' or palabra[x] == 'A':
            contador = contador + 1
    return contador

valor = raw_input('Palabra: ')
print('cantidad de letras a o A:',cadena(valor))