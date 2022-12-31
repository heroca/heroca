import random

def genera():
	numero=random.randint(1,100)
	return numero

def adivina(numero):
	valor=0
	intentos=1
	while valor != numero:
		valor=int(input("Escriba el numero: "))
		if numero > valor:
			intentos = intentos + 1
			print("el numero aleatorio es mayor!")
		if numero < valor:
			print("el numero aleatorio es menor!")
			intentos = intentos + 1
	return intentos


# bloque principal

numero=genera()
resultado=adivina(numero)
print("Ganó luego de " + str(resultado) + " intentos")


