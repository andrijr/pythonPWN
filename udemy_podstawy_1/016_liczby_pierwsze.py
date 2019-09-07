print(3>5)
print(type(3>5))
x = 2 < 3
print(x)

czyDzieliPrzeDwa = 8 % 2 == 0
print(czyDzieliPrzeDwa)

liczba = int(input("Podaj liczbę: "))
if liczba % 2 == 0:
    print("liczba ", liczba, " podzielna przez 2" )
if liczba % 5 == 0:
    print("liczba ", liczba, " podzielna przez 5" )
if liczba % 3 == 0:
    print("liczba ", liczba, " podzielna przez 3" )