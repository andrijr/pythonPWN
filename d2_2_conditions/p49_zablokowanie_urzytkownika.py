# logowanie na podstawie listy użytkowników z zablokowaniem konta
# login, hasło, uprawnienia, aktywacja, zliczanie prób

users = [
        ["admin", "admin", "role_admin", True, 0],
        ["user", "user", "role_user", True, 0],
        ["guest", "guest", "role_guest", True, 0],
        ]

isLogged = False
while (isLogged == False):
    print(users)
    login = input("Podaj login: ")
    password = input("Podaj hasło: ")
    for user in users:
        # print(user)
        if (login == user[0] and password == user[1] and user[3] == True):
            print('Załogowano do systemu ')
            isLogged = True
            if (user[2] == "role_admin"):
                print("Panel Administratora")
                break
            elif (user[2] == "role_user"):
                print("Panel Uzytkownika")
                break
            else:
                print("Panale Goscia")
                break
        elif (login == user[0] and password != user[1] and user[3] == True):
            user[4] += 1
            if (user[4] == 2):
                user[3] = False
                break
        elif (login == user[0]  and user[3] == False):
            print("Konto zablokowane zkontaktuję sie z administratorem")
            break
