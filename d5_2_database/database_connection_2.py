import pymysql
class DatabaseConnection():
    def __init__(self):
        self.loginDatabase("localhost", "python_user", "user", "python_db")
    def loginDatabase(self, host, user_login, user_password, db_name):
        try:
            self.connect = pymysql.connect(host, user_login, user_password, db_name)
            self.cursor = self.connect.cursor()
            # print("Połączono z bazą danych")
            self.loginOk = True
        except:
            self.loginOk = False
            # print("Błąd połączenia z bazą danych")
    def selectFromUser(self):
        self.cursor.execute("SELECT * FROM users")
        print(" | %3s | %12s | %13s | %13s | %8s | %5s |" % ("ID", "Name", "Lastname", "Birthdate", "Salary", "Gender"))
        for row in self.cursor.fetchall():
            print(" | %3d | %12s |  %12s |  %12s |  %5.2f |  %5s |  " % (row[0], row[1],row[2],row[3],row[4],row[5]))
    def insertIntoUser(self, name, lastname, birthdate, salary, gender):
        try:
            self.cursor.execute("INSERT INTO users VALUES (default, %s, %s, %s, %s, %s)", (name, lastname, birthdate, salary, gender))
            decision = input("Czy zatwierdzić T/N: ")
            if (decision.upper() == "T"):
                self.connect.commit()
            else:
                self.connect.rollback()
        except:
            print("Błąd wprowadzenia danych")

    def updateSalaryToUser(self, id, percent):
        try:
            self.cursor.execute("UPDATE users SET salary = salary * (1 + (%s/100)) where id = %s", (percent, id))
            decision = input("Czy zatwierdzić T/N: ")
            if (decision.upper() == "T"):
                self.connect.commit()
            else:
                self.connect.rollback()
        except:
            print("Błąd wprowadzenia danych")
    def deleteFromUser(self, id):
        try:
            self.cursor.execute("DELETE FROM users  where id = %s", (id))
            decision = input("Czy zatwierdzić T/N: ")
            if (decision.upper() == "T"):
                self.connect.commit()
            else:
                self.connect.rollback()
        except:
            print("Błąd wprowadzenia danych")



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
