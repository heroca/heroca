class Operaciones:

	def __init__(self):
		self.entero1 = int(input("Valor 1 "))
		self.entero2 = int(input("Valor 2 "))
		
	def suma(self):
		suma=self.entero1 + self.entero2
		print("suma",suma)

	def resta(self):
		resta=self.entero1-self.entero2
		print("resta",resta)
	
	def mult(self):
		mult=self.entero1*self.entero2
		print("multiplicacion",mult)
	
	def div(self):
		div=self.entero1/self.entero2
		print("division",div)

operacion1=Operaciones()
operacion1.suma()
operacion1.resta()
operacion1.mult()
operacion1.div()

