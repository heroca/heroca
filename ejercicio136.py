def carga():
    art=[]
    pre=[]    
    for x in range(5):
        valor1=raw_input('Nombre del articulo: ')
        art.append(valor1)
        valor2=float(input('Precio: '))
        pre.append(valor2)
    return [art,pre]

def imprimir(v1,v2):
    print('Listado de productos')
    print(v1,v2)

def imprimir_mayor(v1,v2):
    print('Precio mayor')
    mayor = v2[0]
    r = 0
    for x in range(1,len(v2)):
        if v2[x] > mayor:
            mayor = v2[x]
            r = r + 1
    print(v1[r],v2[r])

def precio_menor(v1,v2,menor):
    print('Precio menor a',menor)
    for x in range(len(v2)):
        if v2[x] <= menor:
            print(v1[x],v2[x])

art, pre = carga()
imprimir(art,pre)
imprimir_mayor(art,pre)
menor = float(input('Precio: '))
precio_menor(art,pre, menor)
