sueldo=int(input("Ingrese sueldo:"))
antiguedad=int(input("Ingrese antiguedad:"))
print("Sueldo a pagar")
if sueldo<500 and antiguedad>=10:
    sueldoapagar = sueldo * 1.20
else:
    if sueldo<500:
        sueldoapagar = sueldo * 1.05
    else:
        sueldoapagar=sueldo
print(sueldoapagar)