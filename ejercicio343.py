from urllib import request
import json

pagina=request.urlopen("https://jsonplaceholder.typicode.com/posts")
datos=pagina.read().decode("utf-8")
lista=json.loads(datos)
for elemento in lista:
    print("userId:",elemento['userId'])
    print("Id:",elemento['id'])
    print("title:",elemento['title'])
    print("body:",elemento['body'])
    print("_"*80)