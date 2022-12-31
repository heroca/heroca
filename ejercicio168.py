def carga():
	contactos={}
	continua="s"
	while continua=="s":
		nombre=input("nombre: ")
		telefono=input("telefono: ")
		contactos[nombre]=telefono
		continua=input("Agregar otro? s/n: ")
	return contactos

def modifica(contactos):
	nombre=input("Escriba el Nombre a modificar: ")
	if nombre in contactos:
		telefono=input("Escriba el nuevo telefono: ")
		contactos[nombre]=telefono
	else:
		print("no existe el nombre, verifique!!")

def imprime(contactos):
	print("listado")
	for nombre in contactos:
		print(nombre,contactos[nombre])

contactos = carga()
modifica(contactos)
imprime(contactos)

