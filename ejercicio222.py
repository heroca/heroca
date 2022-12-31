import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        
        self.label1=tk.Label(self.ventana1,text="Ingrese primer valor:")
        self.label1.grid(column=0, row=0)
        
        self.dato1=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, width=20, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0)
        
        self.label1=tk.Label(self.ventana1,text="Ingrese segundo valor:")
        self.label1.grid(column=0, row=1)
        
        self.dato2=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, width=20, textvariable=self.dato2)
        self.entry1.grid(column=1, row=1)

        self.boton1=tk.Button(self.ventana1, text="Calcular", command=self.calcular)
        self.boton1.grid(column=1, row=2)

        self.label2=tk.Label(self.ventana1,text="RESULTADO")
        self.label2.grid(column=0, row=3)
                
        self.label3=tk.Label(self.ventana1,text="0")
        self.label3.grid(column=1,row=3)
        self.ventana1.mainloop()

    def calcular(self):
        suma=int(self.dato1.get())+int(self.dato2.get())
        self.label3.configure(text=suma)

aplicacion1=Aplicacion()