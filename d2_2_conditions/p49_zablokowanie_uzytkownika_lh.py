# logowanie na podstawie listy użytkowników z zablokowaniem konta
# login, hasło, uprawnienia, aktywacja, zliczanie prób

users = [
        ["admin", "admin", "role_admin", True, 0],
        ["user", "user", "role_user", True, 0],
        ["guest", "guest", "role_guest", True, 0],
        ]
isLogged = False
while (isLogged == False):
    login = input("Podaj login: ")
    for user in users:
        # print(user)
        if (login == user[0] and user[3] == True):
            password = input("Podaj hasło: ")
            if (password == user[1]):
                isLogged = True
                print("Zalogowano do systemu")
                if (user[2] == "role_admin"):
                    print("Panel Administratora")
                    break
                elif (user[2] == "role_user"):
                    print("Panel Użytkownika")
                    break
                else:
                    print("Panel Gościa")
                    break
            else:
                user[4] +=1
                if (user[4] ==2):
                    user[3] = False
                    break
        elif (login == user[0] and user[3] == False):
            print("Konto zablokowane zkontaktuję się z administratorem")
            break