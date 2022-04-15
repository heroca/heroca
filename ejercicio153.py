def cargar_empleados():
    empleados=[]
    for x in range(5):
        nom=raw_input("Ingresar el nombre del Empleado: ")
        sue1=int(input("Ingrese Sueldo 1: "))
        sue2=int(input("Ingrese Sueldo 2: "))
        sue3=int(input("Ingrese Sueldo 3: "))
        empleados.append([nom,(sue1,sue2,sue3)])
    return empleados


def imprimir(empleados):
    print("Empleados y su sueldo")
    for x in range(len(empleados)):
        sueldo=empleados[x][1][0]+empleados[x][1][1]+empleados[x][1][2]
        print(empleados[x][0],sueldo)


def ingreso_mayor(empleados):
    print('Empleados con sueldo mayor a 10000')
    for x in range(len(empleados)):
        suma = empleados[x][1][0]+empleados[x][1][1]+empleados[x][1][2]
        if suma>10000:
            print(empleados[x][0],suma)
    

# bloque principal

empleados=cargar_empleados()
imprimir(empleados)
ingreso_mayor(empleados)