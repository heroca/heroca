while True:
    valor1=int(input("Ingrese primer valor:"))
    valor2=int(input("Ingrese segundo valor:"))
    suma=valor1+valor2
    print("La suma es", suma)
    respuesta=input("Desea ingresar otro par de valores?[s/n]")
    if respuesta=="n":
        break