import json

cadena1="""
  [
      {
          "codigo":"1",
          "descripcion":"papas",
          "precio":"12"
      },
      {
          "codigo":"2",
          "descripcion":"naranjas",
          "precio":"25"
      }
  ]
"""
print(type(cadena1))
print(cadena1)
print("_"*80)
lista=json.loads(cadena1)
print(type(lista))
print(lista)
print("_"*80)
cadena2=json.dumps(lista)
print(type(cadena2))
print(cadena2)