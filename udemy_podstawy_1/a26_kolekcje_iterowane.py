tuple = (1,2,3)
lista = [1,2,3]
string = "abc"

tuple2 = (1,2,3, tuple, 'x')
print(tuple2)
lista2 = [1,2,3, tuple, 'x', lista, string]
print(lista2)
print(lista2[2])
print(lista2[3])
print(lista2[3][1])
print(lista2[1:])
print(lista2[::-1])
lista2.reverse()
print(lista2)
# [start, koniec, krok]
print(lista2[::-2])
print()

newList = list(string)
print(newList)
newString = ''.join(newList)
print(newString)
