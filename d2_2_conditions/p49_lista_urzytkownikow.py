# Wykonaj prosty test poprawności logowania
# Jeżeli użytkownik podał login: admin i hasło: admin – przejdź do panelu administratora
# Jeżeli użytkownik podał login: user i hasło: user – przejdź do panelu użytkownika
# W przeciwnym razie wyświetl stosowny komunikat


login =     'mm'     # input("podaj login:")
password =  'mm'     #'nput("podaj password:")
# LOGOWANIE NA PODSTAWIE LISTY UŻTRKOWNIKÓW
# login, hasło, uprawnienia, aktywacja
users = [ ["mm","mm","ROLE_ADMIN",True],
          ["kk", "kk", "ROLE_USER", True],
          ["ll", "ll", "ROLE_USER", True]]

isLogged = False
for user in users:
    if(login == user[0] and password == user[1]):
        isLogged = True
        if(user[2] == "ROLE_ADMIN"):
            print("PANEL ADMINISTRATORA")
            break
        else:
            print("PANEL UŻYTKOWNIKA")
            break
print("" if isLogged else "BŁĄD LOGOWANIA")



print("##########")
# login user permission active
login =     'guest'     # input("podaj login:")
password =  'guest'     #'nput("podaj password:")
users =    [
                    ["admin", "admin", 'admin', True],
                    ["user", "user", 'user', True],
                    ["guest", "guest", 'guest', True]
                    ]
isLogged = False
for user in users:
    # print(user)
    if login == user[0] and password == user[1] :
        isLogged = True
        print("jesteś zalogowany")
        if user[1] == 'admin':
            print('Panel Administrator')
            break
        elif user[1] == 'user':
            print('Panel User')
            break
        else:
            print('Panel Guest')
            break
print('Błąd logowania' if isLogged == False else'')
