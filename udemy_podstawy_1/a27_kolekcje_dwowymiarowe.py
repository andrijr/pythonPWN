
lista = [1,2,3,4,5]
newLista = [lista,lista,lista,lista, 1,2]
print(lista)
print(newLista)
print(newLista[1][1])

for i in newLista:
        print(i, end="")



for x in range(0,len(newLista)):
    continue
    for y in range(0,int(len(newLista[x]))):
        print(x,y , end="")
print()
szachownica = (
        ("a","b","c","d","e","f","g","h"),
        ("_","_","_","_","_","_","_","_"),
        ("_","_","_","_","_","_","_","_"),
        ("_","_","_","_","_","_","_","_"),
        ("_","_","_","_","_","_","_","_"),
        ("_","_","_","_","_","_","_","_"),
        ("_","_","_","_","_","_","_","_"),
        ("_","_","_","_","_","_","_","_")
        )

for wiersz in szachownica:
    for pole in wiersz:
        print(pole, end=" ")
    print()