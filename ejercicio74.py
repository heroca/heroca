lista=["luis","pedro","raul","martha","fernando"]
s=0
x=0
while x<len(lista):
    if len(lista[x]) >= 5:
        s = s + 1
    x=x+1
print('nombres:')
print(lista)
print('Nombres con 5 o mas caracteres')
print(s)