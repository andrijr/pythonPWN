lista = ['a','b', 'c']
napis = "abc"
print(lista[1])
print(napis[1])

for i in lista:
    print(i)

for i in napis:
    print(i)
print()

print(id(lista))
print(id(lista.append('d')))
print(id(napis))
