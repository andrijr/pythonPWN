from d5_2_database.p77.database_conection import *

databaseConnection = DatabaseConnection()
# print(databaseConnection.loginOk)
while(databaseConnection.loginOk):
    print("Połączono z bazą danych")
    try:
        menu = input("S - select, I - insert, U - update, D - delete, Q - wyjscie: ")
        if (menu.upper() == 'S'):
            databaseConnection.selectFromUser()
        elif (menu.upper() == 'I'):
            databaseConnection.insertIntoUser(input("Imię "), input("Nazwisko "), input("Data urodzenia "), input("Wynagrodzenie "),
                                input("Pleć "))
        elif (menu.upper() == 'U'):
            databaseConnection.updateSalaryToUser(input("Podaj ID "), input("Procen podwyżki "))
        elif (menu.upper() == 'D'):
            databaseConnection.deleteFromUser(input("Podaj ID Urzytkownika którego chcesz usunąć: "))
        elif (menu.upper() == 'Q'):
            databaseConnection.connect.close()
            print("Rozłączono z bazą danych")
            break

        else:
            print("Błędny wybór")
    except:
        print("Błąd")
else:
    print("Błąd połączenia z bazą danych.")

