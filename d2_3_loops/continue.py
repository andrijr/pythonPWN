from random import sample

lista = range(-10,10,1)
los = sample(set(lista),5)
licznik = 5.5
for i in los:
    print("Wylosowana wartość: %i" % i)
    if(i == 0):
        print("Nie można dzielić przez zero")
        continue
    print("Wynik operacji: %.2f" % (licznik/i))