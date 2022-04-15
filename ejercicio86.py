nombre=[]
nota=[]
condicion = ""
for x in range(4):
    nom=raw_input("Ingrese el nombre del alumno:")
    nombre.append(nom)
    notas=int(input("Ingrese nota:"))
    nota.append(notas)
for x in range(4):
    if nota[x] >= 8:
        condicion = 'Muy bueno'
    else:
        if nota[x] >4 and nota[x] <8:
            condicion = 'Bueno'
        else:
            condicion = 'Insuficiente'
    print(nombre[x] + ' ' + str(nota[x]) + ' ' + condicion)
