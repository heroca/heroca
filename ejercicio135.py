def carga_sueldos():
    sueldos=[]
    for x in range(10):
        sueldo=float(input('Sueldo: '))
        sueldos.append(sueldo)
    return sueldos

def impresion(lista):
    print('Sueldos',lista)

def sueldo_superior(lista):
    ss = 0
    for x in range(len(lista)):
        if lista[x] > 4000:
            ss=ss+1
    return ss

def promedio(lista):
    promedio = 0
    for x in range(len(lista)):
        promedio = promedio + lista[x]
    return promedio / len(lista)

def debajo(lista,prom):
    for x in range(len(lista)):
        if lista[x] < prom:
            print('sueldo menor que ',prom,lista[x])

sueldos=carga_sueldos()
impresion(sueldos)
ss=sueldo_superior(sueldos)
print('Sueldos mayores a 4000',ss)
prom=promedio(sueldos)
print('sueldo promedio',prom)
debajo(sueldos,prom)
