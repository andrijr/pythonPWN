from d5_1_files.p75.generateController import  generateController

pomiary = generateController()
while(True):
    print(pomiary)
    main = input("D - dodaj urzytkownika\nU - usuń urzytkownika\nM - wykonaj pomiar\nMM - wykonaj pomiar z nowmymi parametrami\nL - likwidój pomiar\nS - zapisz pomiary\n"
                 "A - dopisz pomiary do pliku\nW - wyświetl plik pomiarów\nQ - wyjdz z programu ")
    if main.upper() == 'D':
        login = input("Podaj login ")
        name = input("Podaj imie ")
        lastname = input("Podaj nazwisko ")
        pomiary.addUser(login, name, lastname)
    elif main.upper() == 'U':
        user_id_no = int(input("Podaj id urzytkownika "))
        pomiary.deletedUserById(user_id_no)
    elif main.upper() == 'M':
        user_id_no = int(input("Wykonaj pomiar dla id urzytkownika "))
        pomiary.addTakeMeasurementById(user_id_no)
    elif main.upper() == 'MM':
        try:
            user_id_no, from_no, to_no, n = [int(x) for x in input("Wykonaj pomiar dla id urzytkownika oraz podaj ewentualne parametry po przecinku id, from_no, to_no, n ").split(",")]
            pomiary.addTakeMeasurementById(user_id_no, from_no, to_no, n)
        except:
            print("Błedne liczby ")
    elif main.upper() == 'L':
        user_id_no = int(input("Likwidój pomiar dla id urzytkownika "))
        pomiary.deleteTakeMeasurementById(user_id_no)
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