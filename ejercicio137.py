def carga():
    elementos=[]
    for x in range(10):
        valor = int(input('Elemento '+str(x)+' : '))
        elementos.append(valor)
    return elementos

def generarlista(v1):
    pos=[]
    neg=[]
    for x in range(len(v1)):
        if v1[x] >=0:
            pos.append(v1[x])
        else:
            neg.append(v1[x])
    return [pos,neg]

def imprimir(v1):
    for x in range(len(v1)):
        print(v1[x])

#Inicio
elementos=carga()
positivo,negativo=generarlista(elementos)
print('elementos positivos')
imprimir(positivo)
print('elementos negativos')
imprimir(negativo)
