lenguajes1={"C", "Pascal", "PHP", "Python"}
lenguajes2={"C++", "Java", "Python"}
print("Lenguajes estructurados")
print(lenguajes1)
print("Lenguajes orientados a objetos")
print(lenguajes2)
x=lenguajes1.union(lenguajes2)
print("Todos los lenguajes")
print(x)
x=lenguajes1.intersection(lenguajes2)
print("Intersección de los dos conjuntos de lenguajes")
print(x)
x=lenguajes1.difference(lenguajes2)
print("Diferencia de los dos conjuntos de lenguajes")
print(x)
x=lenguajes1.symmetric_difference(lenguajes2)
print("lenguajes del conjunto lenguajes1 o del conjunto lenguajes2 pero no en ambos")
print(x)