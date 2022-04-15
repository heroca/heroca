eq = 0
es = 0
isos = 0
triangulos = int(input('Triangulos: '))
for r in range(triangulos):
    lado1 = int(input('Lado 1: '))
    lado2 = int(input('Lado 2: '))
    lado3 = int(input('Lado 3: '))
    if lado1 == lado2 and lado2 == lado3:
        eq = eq + 1
        print('Equilatero')
    else:
        if lado1 != lado2 and lado2 != lado3:
            es = es + 1
            print('Escaleno')
        else:
            isos = isos + 1
            print('Isoseles')
print('Total Isoseles')
print(isos)
print('Total Escaleno')
print(es)
print('Equilatero')
print(eq)