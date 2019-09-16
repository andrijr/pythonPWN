# P67
# Wykorzystując obiektowość napisz program DZIEKANAT, który:
# Umożliwia przypisanie ocen do studenta identyfikowanego przez:
# Nr_indeksu
# Imię
# Nazwisko
# Przechowywanie tych danych w sekwencji i wykonanie takich operacji jak:
# Wprowadzanie nowego studenta
# Wyświetlanie wprowadzonych studentów
# Usuwanie studenta
# Ddaliśmy jeszcze dodawanie ocen oraz kasowanie
from d3_2_objects.p67.student_controller import StudentController

dziekanat = StudentController()
while (True):
    print("Witamy w DZIEKANACIE")
    main = input("P - pokaz dziekanat\n" + "D - dodaj studenta\n" +  "Z - znajdż studenta\n" +  "W - wprowadz oceny\n" +
                 "O - wyczyść oceny\n"  + "U - usuń studenta\n"  + "Q - zamknij program \n" )
    if main.upper() == 'D':
        name = input("Podaj imię: ")
        lastname = input("Podaj nazwisko: ")
        dziekanat.addStudent(name, lastname)
    elif main.upper() == 'P':
        print(dziekanat)
    elif main.upper() == 'Z':
        try:
            index_no = int(input("Podaj indeks szukanego studenta: "))
            dziekanat.findStudentByIndex(index_no)
            print(dziekanat.findStudentByIndex(index_no))
        except:
            print("Numer indeksu powinna być liczba ")
    elif main.upper() == 'W':
        try:
            index_no = int(input("Podaj indeks studenta aby podać oceny: "))
            grades = input("Podaj oceny po przecinku: ")
            grades = grades.split(",")
            for i, grade in enumerate(grades):
                grades[i] = int(grades[i])
            dziekanat.addGradesToStudent(index_no, grades)
        except:
            print("Numer indeksu powinna być liczba ")
    elif main.upper() == 'O':
        try:
            index_no = int(input("Podaj indeks studenta aby wyczyścić oceny: "))
            dziekanat.deleteStudentGrades(index_no)
        except:
            print("Numer indeksu powinna być liczba ")
    elif main.upper() == 'U':
        print(dziekanat)
        try:
            index_no = int(input("Podaj indeks studenta aby go usunąć: "))
            dziekanat.deleteStudentByIndex(index_no)
        except:
            print("Numer indeksu powinna być liczba ")
    elif main.upper() == 'Q':
        print("Dziękujemy ")
        break
    else:
        print("Błąd")