# P 56

# Napisz program DZIEKANAT, który:
# Wczytuje od użytkownika kolejne oceny
# Sprawdza czy wprowadzona ocena jest na liście dopuszczalnych na wydziale ocen [3,3.5,4,4.5,5]
# Jeśli ocena jest na liście dopuszczalnych na wydziale ocen, dodaje ją do listy
# Jeśli ocena nie jest na liście dopuszczalnych ocen wystosuj odpowiedni komunikat
# Jeśli wciśnięto sam Enter, oznacza to koniec wprowadzania ocen
# Program dodatkowo wyświetla wyliczoną średnią arytmetyczną dla listy wprowadzonych ocen.

# oceny = input("Podaj oceny: ").split("")
# oceny = str(oceny).split("")
# print(oceny)

listGrade = [3,3.5,4,4.5,5, 5, 5, 5, 8, 8]
setGrade = {3,3.5,4,4.5,5}
newList = []

for x in listGrade:
    if x in setGrade:
        newList.append(x)
    else:
        print(x, "Nie jest na liście ocen")
print("Lista wprowadzonych ocen" , newList)
print("średnia ocena" ,  round(sum(newList) / len(newList),2))
print()


