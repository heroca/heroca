class Persona:

    def inicializar(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Edad:",self.edad)

    def mostrar_estado(self):
        if self.edad>=18:
            print("Mayor de edad")


# bloque principal

persona1=Persona()
persona1.inicializar("diego",20)
persona1.imprimir()
persona1.mostrar_estado()

persona2=Persona()
persona2.inicializar("ana",10)
persona2.imprimir()
persona2.mostrar_estado()
