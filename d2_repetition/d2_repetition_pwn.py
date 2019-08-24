# Sprawdzanie typów wartości
print(type("abc"),type("a"),type('a'))

# Struktury danych
global_temp = []
# Dodawanie wartości
global_temp.append(24.5)
global_temp.append(22.3)
global_temp.append(24.1)
global_temp.append("Err")
global_temp.append(False)
global_temp.append('E')
print("Actual values: " + str(global_temp))
# Wybieranie warotści zlisty
i = 1
print("Wskazanie czujnika " + str(i+1) + ": " + str(global_temp[i])+ " st.C")
# Wypisz co drugą wartość z listy
print(global_temp[::2])
# Usuwanie po wartości
global_temp.remove(False)
print(global_temp)
# Usuwanie po indeksie
index = len(global_temp) - 1
print(global_temp)
print("Usuwany element: " + global_temp.pop(index))
print(global_temp)
# Lista wielowymiarowa
board = [
          ['_','_','_'] ,
          ['_','_','_'] ,
          ['_','_','_']
        ]
board[2][1] = 'X'
board[1][2] = 'O'
print(board)
# V1
for row in board:
    print(row)
print()
# V2
for row in board:
    for value in row:
        print(value,end=' ')
    print()

# Słowniki
global_temp_current = {"C1" : 24.5, "C2" : 23.4, "C3" : 22.5}
print(global_temp_current)
# Dodawanie klucza i wartości do słownika
global_temp_current["C4"] = 21.1
global_temp_current["C5"] = 21.1
print(global_temp_current)
# global_temp_current["C5"] = 23.1
print(global_temp_current)
# Zbiór kluczy i lista wartości
print(global_temp_current.keys())
print(global_temp_current.values())
# Iterowanie po słownikach w pętli
for key in global_temp_current.keys():
    print("Sensor " + key + ": ", str(global_temp_current[key]) + "st.C")

# Słownik z wartościami w postaci listy
global_temp_current1 = {"C1" : ["Model XYZ", "Warszawa", 24.5, "+/-0.5%"],
                       "C2" : ["Model ABC", "Kraków", 22.5, "+/-0.1%"]}
print(global_temp_current1)
print(global_temp_current1["C1"])
print(global_temp_current1["C1"][2], global_temp_current1["C1"][1])

for key in global_temp_current1.keys():
    print(key, end=" ")
    for value in global_temp_current1[key]:
        print(value, end=" ")
    print()


### LICZBA LUSTRZANA ###
# liczba = input("Wprowadź liczbę: ")
# print(list(liczba) == list(reversed(liczba)))

# liczba_rev = list(liczba)
# liczba_rev.reverse()
# print(list(liczba) == liczba_rev)

### DLa DANYCH LICZB ALGORYTM ZWRACA TYLKO WARTOŚCI UNIKATOWE ###
# [1,1,2,3,4,4,4] -> [1,2,3,4]
values = [1,1,2,3,4,4,4]
uniqueValues = set(values)
print(list(uniqueValues))

uniqueValues.add(7)
print(uniqueValues)
uniqueValues.discard(7)
print(uniqueValues)

print("Contains", 1 in uniqueValues)
print("Subset", set([1,2]).issubset(uniqueValues))
print("Superset", set([1,2]).issuperset(uniqueValues))

### RÓŻNICA SYMETRYCZNA -
### WYPISZ WSZYSTKIE ELEMENTY WYSTEPUJACE W KAZDEJ Z LIST ALE NIE BEDACE ELEMENTAMI WSPOLNYMI

l1 = [1,2,3,4,5,6]
l2 = [3,4,5,6,7,8,9]

print(set(l1) ^ set(l2))
print(set(l1).symmetric_difference(set(l2)))









