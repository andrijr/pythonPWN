from d4_objects.p73.employeeController import EmployeeController

firma = EmployeeController()
while(True):
    print("Witamy w Naszej Firmie")
    main = input("W - wyświetl wszystkich pracowników \n" + "D - dodaj pracownika \n" + "S - zmień dane \n" + "Z - wyszukaj pracownika po imieniu i nazwisku \n"
                 + "N - wyszukaj pracownika po numerze \n" + "U - usuń pracownkia \n" + "P - dodaj powdwyżkę dla pracownika \n" + "Q - Wyjdź z programu \n"  )
    if main.upper() == 'W':
        print("Lista pracowników")
        print(firma)
    elif main.upper() == 'D':
        name = input("Podaj imie ")
        lastname = input("Podaj nazwisko ")
        firma.addEmployee(name, lastname)
    elif main.upper() == 'S':
        try:
            employee_no = int(input("Podaj numer id pracownika aby zmienić dane "))
            contract = input("Podaj rodzaj kontratu full-time albo internship ")
            salary = int(input("Podaj wynagrodzenie "))
            firma.changeContractAndSalaryEmployee(employee_no, contract, salary)
        except:
            print("Błędny wybór")
    elif main.upper() == 'Z':
        name = input("Podaj imie ")
        lastname = input("Podaj nazwisko ")
        firma.findEmployeeByNameLastname(name, lastname)
        print(firma.findEmployeeByNameLastname(name, lastname))
    elif main.upper() == 'N':
        try:
            employee_no = int(input("Podaj numer id pracownika aby wyszukać "))
            firma.findEmployeeByNumber(employee_no)
            print(firma.findEmployeeByNumber(employee_no))
        except:
            print("Błędny wybór")
    elif main.upper() == 'U':
        try:
            employee_no = int(input("Podaj numer id pracownika do usunięcia "))
            firma.deleteEmployeeByNumber(employee_no)
        except:
            print("Błędny wybór")
    elif main.upper() == 'P':
        try:
            employee_no = int(input("Podaj numer id pracownika do podwyżki "))
            percent_rice = int(input("Podaj procent podwyżki "))
            firma.addSalaryForNumber(employee_no, percent_rice)
        except:
            print("Błędny wybór")
    elif main.upper() == 'Q':
        print("Dziękujemy")
        break
    else:
        print("Błedny wybór")