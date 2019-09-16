 # P45

# Używając serii instrukcji if, sprawdź, czy wartości od 0 do 4 są równe True lub False.
# Wykonaj 5 osobnych testów i wypisz tylko te wartości dla których konwersja daje wynik True.


for x in range(0, 5):
    if (x == True):
        print(x, "Podana liczba jest równa True")
    else:
        print(x, "Podana liczba jest równa False")
print()

for x in range(0, 5):
    if (bool(x) == True):
        print(x, "Podana wartość logiczna jest równa True")
    else:
        print(x, "Podana wartość logiczna jest równa False")