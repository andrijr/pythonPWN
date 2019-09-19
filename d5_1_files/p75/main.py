from d5_1_files.p75.generateController import  generateController

pomiary = generateController()
while(True):
    print(pomiary)
    main = input("D - dodaj urzytkownika,  U - usuń urzytkownika,  M - wykonaj pomiar,  MM - wykonaj pomiar z nowmymi parametrami\n"
                 "L - likwidój pomiar,  S - zapisz pomiary do pliku,  "
                 "A - dopisz pomiary do pliku,  W - wyświetl plik pomiarów,  Q - wyjdz z programu ")
    if main.upper() == 'D':
        login = input("Podaj login ")
        name = input("Podaj imie ")
        lastname = input("Podaj nazwisko ")
        pomiary.addUser(login, name, lastname)
    elif main.upper() == 'U':
        try:
            user_id_no = int(input("Podaj id urzytkownika "))
            pomiary.deletedUserById(user_id_no)
        except:
            print("Błędny wybór")
    elif main.upper() == 'M':
        try:
            user_id_no = int(input("Wykonaj pomiar dla id urzytkownika "))
            pomiary.addTakeMeasurementById(user_id_no)
        except:
            print("Błędny wybór")
    elif main.upper() == 'MM':
        try:
            user_id_no, from_no, to_no, n = [int(x) for x in input("Wykonaj pomiar dla id urzytkownika oraz podaj ewentualne parametry po przecinku id, from_no, to_no, n ").split(",")]
            pomiary.addTakeMeasurementById(user_id_no, from_no, to_no, n)
        except:
            print("Błedne liczby ")
    elif main.upper() == 'L':
        try:
            user_id_no = int(input("Likwidój pomiar dla id urzytkownika "))
            pomiary.deleteTakeMeasurementById(user_id_no)
        except:
            print("Błędny wybór")
    elif main.upper() == 'S':
        name_file = str(input("Podaj nazwę pliku "))
        pomiary.writeTakeMeasurement(name_file)
    elif main.upper() == 'A':
        name_file = str(input("Podaj nazwę pliku "))
        pomiary.addwriteTakeMeasurement(name_file)
    elif main.upper() == 'W':
        name_file = str(input("Podaj nazwę pliku "))
        pomiary.readTakeMeasurement(name_file)
    elif main.upper() == 'Q':
        print('Dziękujemy możesz zawsze jeszcze raz wykonać pomiar')
        break
    else:
        print("Błędny wybór spróbój jeszcze raz")