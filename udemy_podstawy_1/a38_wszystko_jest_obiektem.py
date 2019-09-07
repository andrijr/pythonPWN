def dodaj(*n):
     wynik = 0
     for x in n:
         wynik += x
     return wynik
def odejmij(*n):
    wynik = 0
    for x in n:
        wynik -= x
    return wynik
def pomnoz(*n):
    wynik = 1
    for x in n:
        wynik *= x
    return wynik
def podziel(a,b=1):
    wynik = a / b
    return wynik
def podzelCalkowicie(a,b=1):
    wynik = a // b
    return wynik
def modulo(a,b=1):
    wynik = a % b
    return wynik
listaFunkcji = [dodaj, odejmij, pomnoz, podziel, podzelCalkowicie, modulo]
listaOpisowFunkcji= ["Dodawanie", "Odejmowanie", "Mnożenie", "Dzielienie", "Dzielenie Całkowite", "Reszta z dzielenia"]
print(listaFunkcji)
print(listaOpisowFunkcji)
print()

x = float(input("podaj pierwszą liczbę: "))
y = float(input("podaj kolejną liczbę: "))

for i in range(0, len(listaFunkcji)):
    print("Wynik", listaOpisowFunkcji[i], "wynosi", listaFunkcji[i](x,y))
print()

for funkcja in listaFunkcji:
    print(funkcja(x,y))
print()

print(dodaj (4,2, 8))
tupla = (1,2)
lista = [1,2,3,4, tupla, dodaj(2,4), dodaj]
print(lista)