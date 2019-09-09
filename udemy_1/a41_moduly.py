import a41_moduly_2

# from udemy_1.a41_moduly_2 import multiply

aLista = []
number = int(input("podaj liczbę całkowitą dla której chcesz obliczyć jeżeli chcesz akączyć wpisz 0: "))

while number != 0:
    aLista.append(number)
    number = int(input("podaj liczbę całkowitą dla której chcesz obliczyć jeżeli chcesz akączyć wpisz 0: "))
print(aLista)
print(a41_moduly_2.add(aLista))
print(a41_moduly_2.multiply(aLista))
