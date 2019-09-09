

# lista  = []
# liczba = int(input("Podaj liczbę: "))
# while liczba >=0:
#     lista.append(liczba)
#     liczba = int(input("Podaj liczbę: "))
# print(lista)


lista = [0,1,2,3,4,5,6,7,8,9, 10]
suma=0
for wartosc in lista:
    suma += wartosc
print(suma)
print(suma/len(lista))
print(lista)

print(lista[len(lista)-1])
print(lista[-1])
lista.reverse()
print(lista)