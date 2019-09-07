#P48
liczba = int('2') #int(input("podaj liczbę: "))
print("parzysta" if liczba % 2 == 0 else "Nie parzysta")
print("nie parzysta" if liczba % 2  else "parzysta")

# obsługa błędów jeżeli błąd to wykonaj po except
try:
    print("nie parzysta" if liczba % 2 else "parzysta")
except:
    print("To nie jest liczba")



#P49
login = 'admin'     # input("podaj login:")
password = 'admin'  # input("podaj password:")

try:
    print("Logowanie poprawne" if login == 'admin' and password == 'admin' else "Logowanie błędne")
except:
    print("bląd")

if (login == "admin" and password == "admin"):
    print("Panel administratora")
elif (login == "user" and password == "user"):
    print("Panel urzytkownika")
else:
    print("Błąd logowania")


#############
# #logowanie na podstawie listy użytkowników
print("##########")
login =     'mm'     # input("podaj login:")
password =  'mm'     #'nput("podaj password:")

# login, hasło, uprawnienia, aktywacja
users = [ ["mm","mm","ROLE_ADMIN",True],
          ["kk", "kk", "ROLE_USER", True],
          ["ll", "ll", "ROLE_USER", True]]

# LOGOWANIE NA PODSTAWIE LISTY UŻTRKOWNIKÓW
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






##################
print("Zliczanie petla While ")

# login, hasło, uprawnienia, aktywacja
users = [ ["mm","mm","ROLE_ADMIN",True,0],
          ["kk", "kk", "ROLE_USER", True,0],
          ["ll", "ll", "ROLE_USER", True,0]]


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



