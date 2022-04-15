#usando while
mail=raw_input("Ingrese un mail:")
cantidad=0
x=0
while x<len(mail):
    if mail[x]=="@":
        cantidad=cantidad+1
    x=x+1
if cantidad==1:
    print("Contiene solo un caracter @ el mail ingresado")
else:
    print("Incorrecto")

#usando for
cantidad = 0
for n in range(len(mail)):
    if mail[n] == '@':
        cantidad = cantidad + 1
if cantidad == 1:
    print("Contiene solo un caracter @ el mail ingresado")
else:
    print("Incorrecto")
