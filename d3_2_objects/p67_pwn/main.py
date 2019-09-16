#CLI - command line interface
#GUI - graphical user interface
from d3_2_objects.p67_pwn.student_controller import StudentController
# utworzenie obiektu zawierającego metody obsługi dziekanatu
dziekanat = StudentController()

while(True):
    menu = input("APLIKACJA DZIEKANAT\n"
                 "(D)-dodaj nowego studenta\n(U)-usuń studenta\n(Z)-zaktualizuj oceny\n"
                 "(O)-wyczyść listę ocen studenta\n(W)-wypisz listę studentów\n(Q)-wyjdź z programu")
    if(menu.upper()=="D"):
        name = input("podaj imię: ")
        lastname = input("podaj nazwisko: ")
        dziekanat.addStudent(name,lastname)
    elif(menu.upper()=="U"):
        print(dziekanat)
        try:
            index_no = int(input("podaj numer indeksu"))
            dziekanat.deleteStudentByIndex(index_no)
        except:
            print("Numer indeksu musi być liczbą!")
    elif(menu.upper()=="Z"):
        try:
            index_no = int(input("podaj numer indeksu"))
            grades = input("Podaj listę ocen (po przecinku)")
            grades = grades.split(",")
            # konwersja ocen do liczb całkowitych
            for i, grade in enumerate(grades):
                grades[i] = int(grades[i])
            # wywołanie metody dodającej oceny do wybranego studenta
            dziekanat.addGradesToStudent(index_no,grades)
        except:
           print("Błąd danych! Nie można wykonać konwersji lub błędny numer indeksu")
    elif(menu.upper()=="O"):
        try:
            index_no = int(input("podaj numer indeksu"))
            dziekanat.deleteStudentGrades(index_no)
        except:
            print("Błędny numer indeksu")
    elif(menu.upper()=="W"):
        print(dziekanat)
    elif(menu.upper()=="Q"):
        # przerwanie pętli while
        break
    else:
        print("Błędny wybór!")