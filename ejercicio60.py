import sys
opcion="si"
suma=0
while opcion=="si":
    valor=int(input("Ingrese un valor:"))
    suma=suma+valor
    if sys.version_info.major == 2:
        opcion=raw_input("Desea cargar otro numero (si/no):")
    else:
        if sys.version_info.major == 3:
            opcion=input("Desea cargar otro numero (si/no):")
print("La suma de valores ingresados es")
print(suma)