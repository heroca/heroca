"""
Realizar un programa que solicite la carga de valores enteros
por teclado y los sume. Finalizar la carga al ingresar el valor -1. 
"""
valor = 0
acum = 0
while valor != -1:
    valor = int(input('valor: '))
    if valor > 0:
        acum = acum + valor
print('Suma de los valores')
#Imprime el contenido de la variable acum
print(acum)