def primeros_tres(cadena):
    return cadena[:3];


# bloque principal

meses=('enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')
for x in meses:
    print(primeros_tres(x),x)
    
# del(lista[2:5]) # eliminamos los elementos de las posiciones 2,3 y 4
