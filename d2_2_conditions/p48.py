# P48

# Napisz program, który wczyta od użytkownika liczbę całkowitą
# i bez użycia instrukcji if wyświetli informację, czy jest to liczba parzysta, czy nieparzysta.



liczba = int('2') #int(input("podaj liczbę: "))
print("parzysta" if liczba % 2 == 0 else "Nie parzysta")
print("nie parzysta" if liczba % 2  else "parzysta")

# obsługa błędów jeżeli błąd to wykonaj po except
try:
    print("nie parzysta" if liczba % 2 else "parzysta")
except:
    print("To nie jest liczba")
