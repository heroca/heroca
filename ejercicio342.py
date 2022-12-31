from urllib import request
import json
import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.label1=ttk.Label(text="Código:", width=25)
        self.label1.grid(column=0, row=0, padx=10, pady=10)
        self.label2=ttk.Label(text="", width=25)
        self.label2.grid(column=1, row=0, padx=10, pady=10)
        
        self.label3=ttk.Label(text="Descripción:", width=25)
        self.label3.grid(column=0, row=1, padx=10, pady=10)
        self.label4=ttk.Label(text="", width=25)
        self.label4.grid(column=1, row=1, padx=10, pady=10)

        self.label5=ttk.Label(text="Precio:", width=25)
        self.label5.grid(column=0, row=2, padx=10, pady=10)
        self.label6=ttk.Label(text="", width=25)
        self.label6.grid(column=1, row=2, padx=10, pady=10)

        self.boton1=ttk.Button(self.ventana1, text="Anterior", command=self.anterior, width=25)
        self.boton1.grid(column=0, row=3, padx=10, pady=10)
        self.boton2=ttk.Button(self.ventana1, text="Siguiente", command=self.siguiente, width=25)
        self.boton2.grid(column=1, row=3, padx=10, pady=10)
        self.articulos=[]
        self.recuperar_articulos()
        self.indice=0
        self.mostrar_articulo()
        self.ventana1.mainloop()

    def anterior(self):
        if self.indice>0:
            self.indice-=1
            self.mostrar_articulo()

    def siguiente(self):
        if self.indice<len(self.articulos)-1:
            self.indice+=1
            self.mostrar_articulo()

    def recuperar_articulos(self):
        pagina=request.urlopen("http://localhost/pythonya/retornararticulos.php")
        datos=pagina.read().decode("utf-8")
        self.articulos=json.loads(datos)

    def mostrar_articulo(self):
        if len(self.articulos)>0:
            self.label2.config(text=self.articulos[self.indice]['codigo'])
            self.label4.config(text=self.articulos[self.indice]['descripcion'])
            self.label6.config(text=self.articulos[self.indice]['precio'])

aplicacion1=Aplicacion()
