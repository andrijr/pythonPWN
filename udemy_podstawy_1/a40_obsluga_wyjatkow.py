try:
    file = open("plik_przykladowy_2.txt", "r", encoding="UTF-8")
    file.close()
except:
    print("Plik nie istnieje")

try:
    x = int(input("podaj liczbę: "))
except:
    print("To nie jest liczba")

