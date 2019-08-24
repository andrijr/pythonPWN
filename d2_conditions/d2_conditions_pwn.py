#P48
# try:
#     print("NIEPARZYSTA" if int(input("Podaj liczbę: ")) % 2 else "PARZYSTA")
# except:
#     print("TO NIE JEST LICZBA")

#P49
# login = input("podaj login:")
# password = input("podaj password:")

# login, hasło, uprawnienia, aktywacja
# users = [ ["mk","mk123","ROLE_ADMIN",True],
#           ["kk", "kk123", "ROLE_USER", True],
#           ["ll", "ll123", "ROLE_USER", True]]

# LOGOWANIE NA PODSTAWIE LISTY UŻTRKOWNIKÓW
# isLogged = False
# for user in users:
#     if(login == user[0] and password == user[1]):
#         isLogged = True
#         if(user[2] == "ROLE_ADMIN"):
#             print("PANEL ADMINISTRATORA")
#             break
#         else:
#             print("PANEL UŻYTKOWNIKA")
#             break
# print("" if isLogged else "BŁĄD LOGOWANIA")

# login, hasło, uprawnienia, aktywacja
users = [ ["mk","mk123","ROLE_ADMIN",True,0],
          ["kk", "kk123", "ROLE_USER", True,0],
          ["ll", "ll123", "ROLE_USER", True,0]]


isLogged = False
while(isLogged == False):
    print(users)
    login = input("podaj login:")
    for user in users:
        # spr. czy jest taki użytkownik
        if(login == user[0] and user[3] == True):
            password = input("podaj password:")
            # spr. czy ma poprawne hasło
            if(password == user[1]):
                isLogged = True
                # sprawdzam uprawnienia
                if (user[2] == "ROLE_ADMIN"):
                    print("PANEL ADMINISTRATORA")
                    break
                else:
                    print("PANEL UŻYTKOWNIKA")
                    break
            else:
                print("BŁĘDNE HASŁO")
                user[4] += 1
                if (user[4] == 3):
                    user[3] = False
                break
        elif(login == user[0] and user[3] == False):
            print("KONTO ZABLOKOWANE!")
            break



