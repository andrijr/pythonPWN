# zbóre nie są iterowane
# kolejność nie jest taka jaką podajemy
# elementy zbioru są zawsze unikalne
# zbiór jest szybszy

import random
a_set = {1,2,3,4, 4, 4}
print(a_set)

# while len(lista) <6:
#     wylosowana = random.randint(1, 49)
#     if wylosowana in lista:
#         continue
#     lista.append(wylosowana)
# print(lista)


zbior = set()
while len(zbior)<6:
     zbior.add(random.randint(1,49))

print(zbior)
lista = list(zbior)
print(lista)