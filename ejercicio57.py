"""
Programa: ejercicio57.py
programador: Raul Herrera
Fecha Modificacion: 30/08/2021
"""
#Inicializa la variable para acumular el total
acum = 0
for x in range(10):
    #Asigna a la variable valor la cantidad capturada
    valor = int(input('Introduzca valor: '))
    acum = acum + valor
print('Total')
#Imprime el resultado de la variable acum
print(acum)