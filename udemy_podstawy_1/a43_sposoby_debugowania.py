import math

# lista = [1,2,3,4,5,6,7,8,9]
#
# for x in lista:
#     suma =  sum(lista)
# lista.append(suma)
# print(lista)

lista = [1,2,3,4,5,6,7,8,9]
suma = sum(lista)
suma = 0
for x in lista:
    suma +=  x
lista.append(suma)
print(lista)

print(math.isclose(math.sqrt(2)*math.sqrt(2),2))