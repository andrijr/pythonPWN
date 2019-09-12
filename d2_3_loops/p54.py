# P 54

# Napisz program, który znajdzie i wyświetli pozycję na liście pierwszego wystąpienia określonej liczby.

liczba = 123444455687
liczba = str(liczba)
znajdz = 5

for index, element in enumerate(liczba):
    if element == str(znajdz):
        print( "Liczba" , element, "ma pozycję", index)
        break


