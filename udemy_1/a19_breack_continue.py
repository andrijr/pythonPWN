
# for x in range(1,1000):
#     if x != 7 and x!=77 and x != 777:
#         print(x, x**2-1000)
#
#
# for x in range(1,1000):
#     if x == 7 and x == 77 and x == 777:
#         continue  # wtedy przypadek jest pominęty
#     print(x, x ** 2 - 1000)

suma = 0

while True:
    napis = "koniec" #input("Podaj tekst: ")
    if napis == "koniec":
        break   # powoduję wyjście z pętli
    if len(napis) <5:
        continue # wtedy pomijamy taki przypadek
    suma += len(napis)
    print(suma)

print("poza pętlą")

liczbaPierwsza = True
liczba = int(input("Podaj liczbę: "))
for dzielnik in range(2,liczba):
    if liczba % dzielnik ==0:
        print("Jest to liczba złożona")
        liczbaPierwsza = False
        break
if liczbaPierwsza ==True:
    print("jest to liczba pierwsza")






