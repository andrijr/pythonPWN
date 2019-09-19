# P 56

# Napisz program DZIEKANAT, który:
# Wczytuje od użytkownika kolejne oceny
# Sprawdza czy wprowadzona ocena jest na liście dopuszczalnych na wydziale ocen [3,3.5,4,4.5,5]
# Jeśli ocena jest na liście dopuszczalnych na wydziale ocen, dodaje ją do listy
# Jeśli ocena nie jest na liście dopuszczalnych ocen wystosuj odpowiedni komunikat
# Jeśli wciśnięto sam Enter, oznacza to koniec wprowadzania ocen
# Program dodatkowo wyświetla wyliczoną średnią arytmetyczną dla listy wprowadzonych ocen.


setGrade = {3,3.5,4,4.5,5}
listGrade = []
newList = []
liczba = ' '
while len(liczba) != 0:
    try:
        liczba = input("Podaj kolejną liczbę , zakącz wciśnij samo ENTER ")
        if len(liczba) != 0:
            listGrade.append(int(liczba))
    except:
        print("")
else:
    # print(listGrade)
    for x in listGrade:
        if x in setGrade:
            # print(listGrade)
            newList.append(x)
        else:
            print(x, "Nie jest na liście ocen")
print("Lista wprowadzonych ocen", newList)
try:
    print("średnia ocena", round(sum(newList) / len(newList), 2) )
except:
    print("")

