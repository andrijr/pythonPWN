import random

wylosowana = random.randint(1,100)
print(wylosowana)

lista = []
for i in range(0,6):
    wylosowana = random.randint(1,49)
    if wylosowana in lista:
        continue
    lista.append(wylosowana)
print(lista)

print()

while len(lista) <6:
    wylosowana = random.randint(1, 49)
    if wylosowana in lista:
        continue
    lista.append(wylosowana)
print(lista)













