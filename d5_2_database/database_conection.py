 # w terminal zainstalować  # pip install cryptography
import pymysql

class DatabaseConnector:
    def __init__(self):
        self.loginToDbServer("localhost","python_admin","admin","python_db")
        while(True):
            menu = input("(S)-select, (I)-insert, (D)-delete, (U)-update, (Q)-quit  :  ")
            if(menu.upper() == "S"):
                self.selectFromUsers()
            elif(menu.upper() == "I"):
                self.inserIntoUsers(input("imie: "),input("nazwisko: "),input("data urodzenia: "),
                                    input("pensja: "), input("płeć: "))
                decision = input("Potwierdź (T/N): ")
                if(decision.upper() == "T"):
                    # przeniesienie danych z bufora pamięci do DB
                    self.connect.commit()
                else:
                    # wycofanie wprowadzanych danych
                    self.connect.rollback()
            elif(menu.upper() == "D"):
                self.deleteUserById(input("id: "))
                decision = input("Potwierdź (T/N): ")
                if(decision.upper() == "T"):
                     self.connect.commit()
                else:
                    self.connect.rollback()
            elif(menu.upper() == "U"):
                self.updaeToUser(input("id: "), input("procent podwyzszenia pensji: "))
                decision = input("Potwierdź (T/N): ")
                if(decision.upper() == "T"):
                    self.connect.commit()
                else:
                    self.connect.rollback()
            elif(menu.upper() == "Q"):
                self.connect.close()
                break
            else:
                print("Błędny wybór")
    def loginToDbServer(self, host, user_login, user_password, db_name):
        try:
            # globalny obiekt połącznia z db
            self.connect = pymysql.connect(host,user_login,user_password,db_name)
            self.cursor = self.connect.cursor()
            print("Ustanowiono połączenie z bazą danych")
        except:
            print("Błąd połączenia z bazą danych")
    def selectFromUsers(self):
        # zapytanie SQL
        sql_query = "SELECT * FROM users"
        # metoda wykonująca zapytanie
        self.cursor.execute(sql_query)
        # zwrócenie tabelki wynikowej
        print("| %3s | %15s | %15s | %15s | %19s | %4s |"
              % ("ID", "IMIĘ", "NAZWISKO", "DATA URODZENIA", "WYNAGRODZENIE NETTO", "PŁEC"))
        for user in self.cursor.fetchall():
            print("| %3d | %15s | %15s | %15s | %17.2fzł | %4s |"
                  % (user[0], user[1], user[2], user[3], user[4], user[5]))
    def inserIntoUsers(self, name, lastname, birthdate, salary, gender):
        try:
            self.cursor.execute("INSERT INTO users VALUES (default, %s, %s, %s, %s, %s)",
                             (name, lastname, birthdate, salary, gender))
            # self.cursor.execute("INSERT INTO users VALUES (default, "+name+", "+lastname+", "+birthdate+", "+str(salary)+", "+gender+")")
        except:
            print("błąd danych!")
    def deleteUserById(self, id):
        try:
            sql = "DELETE FROM users WHERE id = %s"
            self.cursor.execute(sql, id)
            # self.connect.commit()
        except:
            print("błąd danych!")
    def updaeToUser(self, id, percent):
        try:
            sql = "UPDATE users set salary = salary * (1 + (%s/100))  WHERE id = %s"
            self.cursor.execute(sql, (percent, id ))
            # self.connect.commit()
        except:
            print("błąd danych!")

DatabaseConnector()

# p75 zadanie domowe

connect = pymysql.connect()
cursor = connect.cursor()
cursor.execute()
cursor.fetchall()
cursor.close()
connect.close()
connect.rollback()
connect.commit()
