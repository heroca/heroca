def carga():
	nombres=[]
	for x in range(5):
		nom=input("Escriba el nombre: ")
		nombres.append(nom)
	return nombres
	
def ordenar(nombres):
	for y in range(4):
		for z in range(4):
			if nombres[z]>nombres[z+1]:
				aux=nombres[z]
				nombres[z]=nombres[z+1]
				nombres[z+1]=aux

def imprimir(nombres):
	for x in range(len(nombres)):
		print(nombres[x],"\n",end="")


nombres=carga()
ordenar(nombres)
imprimir(nombres)
