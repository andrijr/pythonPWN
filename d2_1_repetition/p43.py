# Stwórz listę zawierającą krotki zawierające współrzędne wszystkich punktów
# o współrzędnych naturalnych leżących na odcinku łączącym punkty (0, 0) i (20, 10).

# P43
x = 20
y = 10
lista = []
krotka = ()
for i1 in range(0, x+1):
    for i2 in range(0, y+1):
        krotka = i1, i2
        lista.append(krotka)
        # print(krotka)
print(lista)

