def retornar_superficie(lado1,lado2):
    return (lado1*lado2)/2

valor1=int(input('Lado1:'))
valor2=int(input('Lado2:'))
print('Superficie',retornar_superficie(valor1,valor2))