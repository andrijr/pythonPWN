# P77
# Napisz program przechowujący informacje dotyczące pracowników zatrudnionych w dziale rozwoju oprogramowania
# pewnej firmy takie jak: Imię, Nazwisko, Rok urodzenia, Pensja, PESEL, data zatrudnienia, itp. Funkcjonalności programu:
# Odczyt z bazy danych informacji o pracownikach i wyświetlenie ich na ekranie.
# Zapis danych do bazy.
# Modyfikacja danych znajdujących się w bazie danych.
# Dodaj do powyższego programu prosty panel logowania użytkownika.
# # W tym celu utwórz tabelę z danymi logowania, np. login i hasło i na podstawie porównania zawartości tej tabeli i danych wpisanych
# # z klawiatury program przydziela lub odbiera uprawnienia dostępu do bazy danych.
from datetime import datetime
from time import strftime

import pymysql

# from d5_2_database.p77_draft.main_user import databaseConnectionUser


class DatabaseConnection():
    def __init__(self):
        self.loginDatabase("localhost", "python_admin", "admin", "python_p77")
        # self.loginDatabase("localhost", databaseConnectionUser.admin.user_login, databaseConnectionUser.admin.user_password, "python_p77")
    def loginDatabase(self, host, user_login, user_password, name_db):
        try:
            self.connect = pymysql.connect(host, user_login, user_password, name_db)
            self.cursor = self.connect.cursor()
            self.isLogin = True
            # print("Połączono z bazą danych")
        except:
            self.isLogin = False
            # print("Błąd połączenia z bazą danych")
    def __str__(self):
        return "Połączono z bazą danych" if self.isLogin else "Błąd połączenia z bazą danych"

    def checkLoginUser(self, user_login, user_password):
        self.cursor.execute("Select login, password , permission from users")
        for row in self.cursor.fetchall():
            if row[0] == user_login and row[1] == user_password:
                if row[2] == 'role_admin':
                    print("Panel Administratora")
                    self.admin = Admin(user_login, user_password)
                    global users_role
                    users_role = 'role_admin'
                    return users_role
                elif row[2] == 'role_moderator':
                    print("Panel Moderatora")
                    self.moderator = Moderator(user_login, user_password)
                    users_role = 'role_moderator'
                    return users_role
                elif row[2] == 'role_user':
                    print("Panel Użytkownika")
                    self.user = User(user_login, user_password)
                    users_role = 'role_user'
                    return users_role
                else:
                    break
                # print(row[0], row[1], row[2])


    def selectFromEmployee(self):
        self.cursor.execute("Select * from employees")
        print("Lista pracowników")
        print("| %3s | %12s | %12s | %15s | %17s | %11s | %5s | %12s | %8s |" %
              ("ID", "Imię", "Nazwisko", "Data Urodzenia", "Data Zatrudnienia", "Pesel", "Pleć", "Wynagrodzenie", "Aktywny"))
        for row in self.cursor.fetchall():
            print("| %3s | %12s | %12s | %15s | %17s | %11s | %5s | %13.2f | %8s |" %
                  (row[0], row[1], row[2],  row[3].strftime("%Y-%m-%d"), row[4].strftime("%Y-%m-%d"), row[5], row[6], row[7], row[8]))
    def insertIntoEmployee(self, name, lastname, data_birth, pesel_no, gender, salary_net):
        try:
            self.cursor.execute("INSERT INTO employees VALUES (default, %s, %s , %s, default, %s, %s, %s, default)",
                                (name, lastname, data_birth, pesel_no, gender, salary_net ))
            decision = input("Czy zatwierdzić operacje T/N")
            if decision.upper() == 'T':
                self.connect.commit()
                print("Dodano pracownika")
            else:
                self.connect.rollback()
        except:
            print("Błąd wprowadzania danych")
    def findEmployeeByNameLastname(self, name, lastname):
        self.cursor.execute("SELECT * FROM employees where name = %s and lastname = %s", (name, lastname))
        print("| %3s | %12s | %12s | %15s | %17s | %11s | %5s | %12s | %8s |" %
              ("ID", "Imię", "Nazwisko", "Data Urodzenia", "Data Zatrudnienia", "Pesel", "Pleć", "Wynagrodzenie", "Aktywny"))
        for row in self.cursor.fetchall():
            print("| %3s | %12s | %12s | %15s | %17s | %11s | %5s | %13.2f | %8s |" %
                  (row[0], row[1], row[2],  row[3].strftime("%Y-%m-%d"), row[4].strftime("%Y-%m-%d"), row[5], row[6], row[7], row[8]))
    def updateToEmployeeById(self, id_employees,  data_birth, data_empl, pesel_no,  salary_net):
        try:
            self.cursor.execute("UPDATE employees SET data_birth = %s, data_empl = %s, pesel_no = %s, salary_net = %s where id_employees = %s",
                                (data_birth, data_empl, pesel_no, salary_net, id_employees))
            decision = input("Czy zatwierdzić operacje T/N")
            if decision.upper() == 'T':
                self.connect.commit()
                print("Zaktualizowano dane pracownika")
            else:
                self.connect.rollback()
        except:
            print("Błąd wprowadzania danych")
    def deleteToEmployeeById(self, id_employees):
        try:
            self.cursor.execute("DELETE FROM employees where id_employees = %s", (id_employees))
            decision = input("Czy zatwierdzić operacje T/N")
            if decision.upper() == 'T':
                self.connect.commit()
                print("Usunięto pracownika")
            else:
                self.connect.rollback()
        except:
            print("Błąd wprowadzania danych")



databaseConnection = DatabaseConnection()
# print(databaseConnection.isLogin)
# print(databaseConnection)
# databaseConnection.selectFromEmployee()
while (databaseConnection.isLogin==True):
    print("Witamy w systemie obsługi pracowników")
    main = input("W - wyświetl pracowników D - Dodaj pracownika Z - Znajdź pracownika A - Zaktualizuj pracownika U - Usuń pracownika  Q - zamknij ")
    if main.upper() == 'W':
        databaseConnection.selectFromEmployee()
    elif main.upper() == 'D':
        databaseConnection.insertIntoEmployee(input("Podaj imię: "), input("Podaj nazwisko: "), input("Podaj date urodzenia: "), input("Podaj pesel: "),
        input("Podaj pleć: "), input("Podaj wynagrodzenie: "))
    elif main.upper() == 'Z':
        databaseConnection.findEmployeeByNameLastname(input("Podaj imię: "), input("Podaj nazwisko: "))
    elif main.upper() == 'A':
        databaseConnection.updateToEmployeeById(input("Podaj ID: "), input("Podaj date urodzenia: "),  input("Podaj date zatrudnienia: "),  input("Podaj pesel: "),
         input("Podaj wynagrodzenie: "))
    elif main.upper() == 'U':
        databaseConnection.deleteToEmployeeById(input("Podaj ID:"))
    elif main.upper() == 'Q':
        print("Dziękujemy rozłączono z bazą danych")
        break
else:
    print("Błąd połączenia z bazą danych")

