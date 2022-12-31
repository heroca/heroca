import tkinter as tk
import sys

class Aplicacion:
    def __init__(self):
        self.valor=""
        self.ventana1=tk.Tk()
        self.ventana1.title("Controles Button y Label")
        self.label1=tk.Label(self.ventana1, text=self.valor)
        self.label1.grid(column=0, row=0)
        self.label1.configure(foreground="red")

        self.boton1=tk.Button(self.ventana1, text="1", command=self.incrementar1)
        self.boton1.grid(column=0, row=1)

        self.boton2=tk.Button(self.ventana1, text="2", command=self.incrementar2)
        self.boton2.grid(column=0, row=2)

        self.boton3=tk.Button(self.ventana1, text="3", command=self.incrementar3)
        self.boton3.grid(column=0, row=3)

        self.boton4=tk.Button(self.ventana1, text="4", command=self.incrementar4)
        self.boton4.grid(column=0, row=4)

        self.boton5=tk.Button(self.ventana1, text="5", command=self.incrementar5)
        self.boton5.grid(column=0, row=5)

        self.boton6=tk.Button(self.ventana1, text="Finalizar", command=self.finalizar)
        self.boton6.grid(column=0, row=6)

        self.ventana1.mainloop()


    def incrementar1(self):
        self.valor=self.valor+"1"
        self.label1.config(text=self.valor)

    def incrementar2(self):
        self.valor=self.valor+"2"
        self.label1.config(text=self.valor)

    def incrementar3(self):
        self.valor=self.valor+"3"
        self.label1.config(text=self.valor)

    def incrementar4(self):
        self.valor=self.valor+"4"
        self.label1.config(text=self.valor)

    def incrementar5(self):
        self.valor=self.valor+"5"
        self.label1.config(text=self.valor)

    def finalizar(self):
        sys.exit(0)        


aplicacion1=Aplicacion()