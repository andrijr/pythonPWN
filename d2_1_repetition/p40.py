# Napisz program, który zamieni całkowitą liczbę dziesiętną na odpowiadającą jej liczbę rzymską.

# P40
setNumber = {"I": 1, "II": 2, "III": 3, "IV":4, "V":5, "VI":6, "VII":7, "VIII":8, "IX":9, "X": 10}
liczba = 3 #int(input("Podaj liczbę dziesiętną: "))

for key in setNumber:
    # print(setNumber[key])
    if int(setNumber[key]) == liczba:
        print(key)
        break

