import tkinter as tk
import sys

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("prueba")
        self.boton1=tk.Button(self.ventana1, text="Varón", command=self.varon)
        self.boton1.grid(column=0, row=0)
        self.boton2=tk.Button(self.ventana1, text="Mujer", command=self.mujer)
        self.boton2.grid(column=0, row=1)        
        self.boton3=tk.Button(self.ventana1, text="Finalizar", command=self.finalizar)
        self.boton3.grid(column=0, row=2)
        #self.ventana1.resizable(False, False)
        self.ventana1.mainloop()


    def varon(self):
        self.ventana1.title("Varón")

    def mujer(self):
        self.ventana1.title("Mujer")
        
    def finalizar(self):
        sys.exit(0)

aplicacion1=Aplicacion()