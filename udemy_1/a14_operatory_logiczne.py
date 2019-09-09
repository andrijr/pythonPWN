value = int(input("Podaj liczbę: "))

if value > 10:
    if value < 20:
        print(value)
    else:
        print("błąd")
else:
    print("błąd")

if value > 10 and value < 20:
    print(value)
else:
    print("błąd")

if 10 < value < 20:
    print(value)
else:
    print("błąd")

print("Poprawnie" if 10 < value < 20 else "Nie poprawnie")

# sprawdzić czy liczba jest z przedziału od (0, 100)
# lub z przedziału [200, 300]

if 0 < value < 100 or 200 <= value <= 300:
    print(value, "Poprawnie")
else:
    print(value, "Nie poprawnie")