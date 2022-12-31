from urllib import request
import json

pagina=request.urlopen("https://jsonplaceholder.typicode.com/users")
datos=pagina.read().decode("utf-8")
lista=json.loads(datos)
print(lista)
for elemento in lista:   
    print("id:",elemento['id'])
    print("name:",elemento['name'])
    print("username:",elemento['username'])
    print("email:",elemento['email'])
    print("street:",elemento["address"]["street"])
    print("suite:",elemento["address"]["suite"])    
    print("city:",elemento["address"]["city"])
    print("zipcode:",elemento["address"]["zipcode"])
    print("lat:",elemento["address"]["geo"]["lat"])
    print("lng:",elemento["address"]["geo"]["lng"])
    print("phone:",elemento['phone'])
    print("website:",elemento['website'])
    print("company name:",elemento["company"]["name"])
    print("catchPhrase:",elemento["company"]["catchPhrase"])
    print("bs:",elemento["company"]["bs"])
    print("_"*80)