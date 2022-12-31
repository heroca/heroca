from urllib import request
import json

pagina=request.urlopen("http://localhost/pythonya/retornararticulos.php")
datos=pagina.read().decode("utf-8")
print(datos) # imprimimos un string
print("_"*100)
lista=json.loads(datos) # convertimos el string a una lista
print(lista) # imprimimos una lista
print("_"*100)
for elemento in lista:
    print(f"{elemento['codigo']}  {elemento['descripcion']:50}  {elemento['precio']:>12}")