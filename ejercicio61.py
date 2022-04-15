import sys
if sys.version_info.major == 2:
    nombre1=raw_input("Ingrese el primer nombre:")
    nombre2=raw_input("Ingrese el segundo nombre:")
else:
    if sys.version_info.major == 3:
        nombre1=input("Ingrese el primer nombre:")
        nombre2=input("Ingrese el segundo nombre:")
print("Listado alfabetico:")
if nombre1<nombre2:
    print(nombre1)
    print(nombre2)
else:
    print(nombre2)
    print(nombre1)