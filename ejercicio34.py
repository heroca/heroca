empleados = int(input('Numero de empleados: '))
x = 1
a = 0
b = 0
total = 0
while x <= empleados:
    sueldo = float(input('Sueldo del empleado ' + str(x) + ':'))
    if sueldo >= 100 and sueldo <= 300:
        a = a + 1
    else:
        if sueldo > 300:
            b = b + 1
    total = total + sueldo
    x = x + 1
print('Empleados que cobran entre 100 y 300')
print(a)
print('Empleados que cobran mas de 300')
print(b)
print('Total de sueldos')
print(total)