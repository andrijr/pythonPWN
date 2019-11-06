import pymysql

from d5_2_database.p77_draft import user
from d5_2_database.p77_draft.user import User, Moderator, Admin

users_role = ''
class DatabaseConnectionUser():
    def __init__(self):
        self.loginDatabaseUser("localhost", "python_admin", "admin", "python_p77")
    def loginDatabaseUser(self, host, user_login, user_password, name_db):
        try:
            self.connect = pymysql.connect(host, user_login, user_password, name_db)
            self.cursor = self.connect.cursor()
            self.isLoginUser = True
            # print("Zaczęto werefikacje")
        except:
            self.isLoginUser = False
            # print("Błąd próby werefikacji")
    def __str__(self):
        return "Zaczęto werefikacje" if self.isLoginUser else "Błąd próby werefikacji"
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



databaseConnectionUser = DatabaseConnectionUser()
while databaseConnectionUser.isLoginUser==True:
    print(databaseConnectionUser)
    user_login = input("Podaj login: ")
    user_password = input("Podaj hasło: ")
    databaseConnectionUser.checkLoginUser(user_login, user_password)
    try:
        if (users_role=='role_admin') :
            print(databaseConnectionUser.admin)
            print(databaseConnectionUser.admin.user_login)
            print(databaseConnectionUser.admin.user_password)
            break
        elif (users_role=='role_moderator') :
            print(databaseConnectionUser.moderator)
            print(databaseConnectionUser.moderator.user_login)
            print(databaseConnectionUser.moderator.user_password)
            break
        elif (users_role=='role_user') :
            print(databaseConnectionUser.user)
            print(databaseConnectionUser.user.user_login)
            print(databaseConnectionUser.user.user_password)
            break
    except:
        print('obsługa błędu')

    break

else:
    print("Bład połączenia")