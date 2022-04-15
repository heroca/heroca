empleados=[]
sueldos=[]
cant=int(input("Cuantos empleados tiene la empresa:"))
for x in range(cant):
    nom=raw_input("Ingrese el nombre:")
    empleados.append(nom)
    su=int(input("Ingrese el importe del sueldo:"))
    sueldos.append(su)

print("Listado completo de empleados")
for x in range(len(sueldos)):
    print(empleados[x],sueldos[x])

posicion=0
while posicion<len(sueldos):
    if sueldos[posicion]>10000:
        sueldos.pop(posicion)
        empleados.pop(posicion)
    else:
        posicion=posicion+1

print("Listado de empleados que cobran 10000 o menos")
for x in range(len(sueldos)):
    print(empleados[x],sueldos[x])
