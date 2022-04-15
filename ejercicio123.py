def promedio(v1,v2,v3):
    promedio = (v1+v2+v3) / 3
    return promedio

valor1=int(input('valor1: '))
valor2=int(input('valor2: '))
valor3=int(input('valor3: '))
res = promedio(valor1,valor2,valor3)
print('Promedio:')
print(res)