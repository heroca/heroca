def imprimir(paises):
    for clave in paises:
        print(clave, paises[clave])


# bloque principal

paises={"argentina":40000000, "espana":46000000, "brasil":190000000, "uruguay": 3400000}
imprimir(paises)