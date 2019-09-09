
x = -5 #int(input("Podaj liczbę ujemną: "))

# dopuki x jest większe od 0 to zawszy wykonaj to co po while
while x > 0:
    x = int(input("Podaj liczbę ujemną: "))
print(x)

liczba = 375
licznik = 1
podana = int(input("Podaj liczbę: "))
while podana != liczba:
    licznik += 1
    if podana > liczba:
        podana = int(input("podana liczba większa podaj liczbę: "))
    else:
        podana = int(input("podana liczba mniejsza podaj liczbę: "))
print(podana, "Gratulujemy to właściwa liczba zgadleś za ", licznik, "razem")