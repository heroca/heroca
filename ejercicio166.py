def cargar():
    lista=[]
    continua="s"
    while continua=="s":
        numero=int(input("Ingrese un numero:"))
        lista.append(numero)
        continua=input("Desea cargar otro numero [s/n}:")
    return lista

def fijar_cero(li):
	for x in range(len(li)):
		if li[x] < 10:
			li[x] = 0

def listar(lista):
    for elemento in lista:
        print(elemento,"-",sep="",end="")
    print("")

# bloque principal

lista=cargar()
print ("Lista antes de modificar")
listar(lista)
fijar_cero(lista)
print ("Lista despues de modificar")
listar(lista)

