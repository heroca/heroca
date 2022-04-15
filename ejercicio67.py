x = 0
nombre=raw_input("Ingrese oracion: ")
lower = nombre.lower()
for n in range(len(nombre)):
    if lower[n]=="a" or lower[n]=="e" or lower[n]=="i" or lower[n]=="o" or lower[n]=="u":
        x = x + 1

print(lower)
print(x)