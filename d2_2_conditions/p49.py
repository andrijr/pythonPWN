# P49

# Wykonaj prosty test poprawności logowania
# Jeżeli użytkownik podał login: admin i hasło: admin – przejdź do panelu administratora
# Jeżeli użytkownik podał login: user i hasło: user – przejdź do panelu użytkownika
# W przeciwnym razie wyświetl stosowny komunikat


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


try:
    if (login == 'admin' and password == 'admin' ):
        print('Jesteś w Panelu Administratora')
    if (login == 'user' and password == 'user' ):
        print('Jesteś w Panelu Urzytkownika')
    else:
        print("Błąd logowania")
except:
    print("Wprowadziełeś złą wartość zpróbój jeszcze raz")