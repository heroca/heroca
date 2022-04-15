man=0
tar=0
noc=0
proman = 0
protar = 0
pronoc = 0
for x in range(5):
    edad = int(input('Edad manana: '))
    man = man + edad
proman = man / 5
for x in range(6):
    edad = int(input('Edad tarde: '))
    tar = tar + edad
protar = tar / 6
for x in range(11):
    edad = int(input('Edad noche: '))
    noc = noc + edad
pronoc = noc / 11
print('Promedio turno de manana')
print(proman)
print('Promedio turno de tarde')
print(protar)
print('Promedio turno de noche')
print(pronoc)
print('Promedio de mayor edad')
if proman > protar and proman > pronoc:
    print('Manana')
else:
    if protar > pronoc:
        print('Tarde')
    else:
        print('Noche')