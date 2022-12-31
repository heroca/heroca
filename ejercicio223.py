import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        
        self.label1=tk.Label(self.ventana1,text="Usuario:")
        self.label1.grid(column=0, row=0)
        
        self.dato1=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, width=20, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0)
        
        self.label1=tk.Label(self.ventana1,text="Clave:")
        self.label1.grid(column=0, row=1)
        
        self.dato2=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, width=20, textvariable=self.dato2, show="*")
        self.entry1.grid(column=1, row=1)

        self.boton1=tk.Button(self.ventana1, text="Validar", command=self.validar)
        self.boton1.grid(column=1, row=2)
        
        self.ventana1.mainloop()

    def validar(self):
        if self.dato1.get()=="juan" and self.dato2.get()=="abc123":
            self.ventana1.title("Correcto")
        else:
            self.ventana1.title("Incorrecto")

aplicacion1=Aplicacion()