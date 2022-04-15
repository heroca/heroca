producto=[]
precio=[]
for x in range(5):
    nom=raw_input("Ingrese el nombre del producto:")
    producto.append(nom)
    pr=int(input("Ingrese el precio:"))
    precio.append(pr)

primero = precio[0]
cantidad = 0
for x in range(1,5):
    if precio[x]>primero:
        cantidad = cantidad + 1
print(producto)
print(precio)
print('productos con precio mayor al primero')
print(cantidad)