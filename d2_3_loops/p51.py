# P51

# Napisz program, który zamieni wprowadzony przez użytkownika ciąg cyfr na formę tekstową:
# znaki nie będące cyframi mają być ignorowane
# konwertujemy cyfry, nie liczby, a zatem:
# 911 to "dziewięć jeden jeden"
# 1100 to "jeden jeden zero zero.



# slownik = {"zero": 0, "jeden": 1, "dwa": 2, "trzy": 3, "cztery": 4, "pięć": 5, "sześć": 6, "siedem": 7, "osiem": 8, "dziewięć": 9, "dziesieńc": 10}
slownik = {"0": "zero", "1": "jeden", "2": "dwa", "3": "trzy", "4": "cztery", "5": "pięć", "6": "sześć", "7": "siedem", "8": "osiem", "9": "dziewięć", "10": "dziesieńc"}

try:
    number = 4566 #int(input("Podaj liczbę: "))

except:
    print("Podaj liczbę w postacie INT")

lista = list(str(number))
# lista = str(number).split()
# lista = str(number)
for i in lista:
    # print(i)
    print(slownik[i] if i in slownik.keys() else "", end=" ")


