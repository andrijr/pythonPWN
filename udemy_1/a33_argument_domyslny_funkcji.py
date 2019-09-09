def dodawaniie(a = 0 , b = 0, c =0):
    print("suma równa jest", a + b + c)
    return a + b + c


lista = []
x = float(input("Podaj kolejną liczbę a żeby zakączyć wpisz 0: "))
while x !=0:
    lista.append(x)
    x = float(input("Podaj kolejną liczbę a żeby zakączyć wpisz 0: "))

print(lista)


def suma(listaLiczb: list):
    wynik = 0
    for x in listaLiczb:
        wynik += x
    return wynik

listaLiczb = [1,2,3,4,5,6,7]
print(suma(listaLiczb))