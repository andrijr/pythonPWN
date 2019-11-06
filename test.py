import pymysql


class DatabaseManager:

    def __init__(self):
        self.user_id = None
        self.loginDatabase(host_db='localhost', login_db='diet_admin', password_db='admin', name_db='diet_clinic')

    def loginDatabase(self, host_db, login_db, password_db, name_db):
        try:
            self.connect = pymysql.connect(host_db, login_db, password_db, name_db)
            self.cursor = self.connect.cursor()
            self.loginDatabaseOk = True
        except:
            self.loginDatabaseOk = False

    def __str__(self):
        return "Połączono z bazą danych" if self.loginDatabaseOk else "Błąd połączenia z bazą danych"


databaseManager = DatabaseManager()
print(databaseManager.loginDatabaseOk)


