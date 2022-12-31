from urllib import request
import json

codigo=input("Ingrese el código de artículo a consultar:")
pagina=request.urlopen(f"http://localhost/pythonya/retornarunarticulo.php?codigo={codigo}")
datos=pagina.read().decode("utf-8")
lista=json.loads(datos)
if len(lista)>0:
    print(f"Descripción:{lista[0]['descripcion']}")
    print(f"Precio:{lista[0]['precio']}")
else:
    print("No existe un artículo con el código ingresado")