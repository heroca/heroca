def retornar_superficie(lado1,lado2):
    return (lado1*lado2)/2

def carga_datos():
    valor1=int(input('Lado1:'))
    valor2=int(input('Lado2:'))
    superficie=retornar_superficie(valor1,valor2)
    return superficie

superficie1=carga_datos()
superficie2=carga_datos()

print(superficie1,superficie2)
if superficie1 > superficie2:
    print('Superficie mayor',superficie1)
else:
    print('Superficie mayor',superficie2)

