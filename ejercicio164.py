def cargar():
    agenda={}
    continua1="s"
    while continua1=="s":
        fecha=raw_input("ingrese la fecha con formato dd/mm/aa:")
        continua2="s"
        lista=[]
        while continua2=="s":
            hora=raw_input("Ingrese la hora de la actividad con formato hh:mm ")
            actividad=raw_input("Ingrese la descripcon de la actividad:")
            lista.append((hora,actividad))
            continua2=raw_input("Ingresa otra actividad para la misma fecha[s/n]:")
        agenda[fecha]=lista
        continua1=raw_input("Ingresa otra fecha[s/n]:")
    return agenda


def imprimir(agenda):
    print("Listado completa de la agenda")
    for fecha in agenda:
        print("Para la fecha:",fecha)
        for hora,actividad in agenda[fecha]:
            print(hora,actividad)


def consulta_fecha(agenda):
    fecha=raw_input("Ingrese la fecha que desea consultar:")
    if fecha in agenda:
        for hora,actividad in agenda[fecha]:
            print(hora,actividad)
    else:
        print("No hay actividades agendadas para dicha fecha")
            

# bloque principal

agenda=cargar()
imprimir(agenda)
consulta_fecha(agenda)