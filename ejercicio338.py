from urllib import request
from urllib import error

try:
    pagina=request.urlopen("http://www.scratchya.com.ar/pythonya/ejercicio336/paginax.html")
    datos=pagina.read().decode("utf-8")
    print(datos)
except error.HTTPError as err:
    print(f"Código de respuesta HTTP devuelto por el servidor {err.code}")
    print(f"No existe el recurso {err.filename}")