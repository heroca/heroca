import tkinter as tk

class Aplicacion:
    def __init__(self):
        #define ventana
        self.ventana1=tk.Tk()
        #define label
        self.label1=tk.Label(self.ventana1,text="Ingrese un número:")
        self.label1.grid(column=0, row=0)
        #define entry
        self.dato=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, width=10, textvariable=self.dato)
        self.entry1.grid(column=0, row=1)
        #define boton
        self.boton1=tk.Button(self.ventana1, text="Calcular Cuadrado", command=self.calcularcuadrado)
        self.boton1.grid(column=0, row=2)
        #define label resultado
        self.label2=tk.Label(self.ventana1,text="resultado")
        self.label2.grid(column=0, row=3)
        #ejecuta ventana
        self.ventana1.mainloop()

    #define metodo
    def calcularcuadrado(self):
        valor=int(self.dato.get())
        cuadrado=valor*valor
        self.label2.configure(text=cuadrado)

aplicacion1=Aplicacion()