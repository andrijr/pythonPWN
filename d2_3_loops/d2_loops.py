# WHILE ELSE
import time
from random import randint, sample, choice

services = ["GitHub", "Google", "Facebook"]
servicesEmpty = []
i = 0
while i < len(services):
    print(services[i])
    i += 1
else:
    print("...services")

i = 0
while i < len(servicesEmpty): # fragment kody wykonywany warunkowo
    print(servicesEmpty[i])
    i += 1
else:
    print("...servicesEmpty") # fragment kody wykonywany zawsze


# FOR IN - OBLICZ ŚREDNIĄ ARYTMETYCZNĄ 1000 losowych wartości z przedziału od 1-10
suma = 0
for liczba in range(0,10000):
    suma += randint(1,10)
print(suma/10000)


# PRZYPISZ 12 osób do 4 grup - w każdej grupie wylosuj jednego lidera
osoby = set(["AN","TSz", "MP","ZJ","PM","AP","FŚ","MT","AR","IS","MS","MK"])
group_dict = {}
i = 1
while len(osoby) > 0:
    grupa = sample(osoby, 3)
    for osoba in grupa:
        group_dict[osoba] = str(i)
        osoby.discard(osoba)
    group_dict[choice(grupa)] = str(i)+"L"
    i += 1
print(group_dict)

#P55
c_to_f = {}

for temp_c in reversed(range(-20, 45, 1)):
    c_to_f[temp_c] = (9/5) * temp_c + 32
    if(temp_c != 0):
        print("%+4iC | %5.1fF" % (temp_c, c_to_f[temp_c]))
    else:
        print("%4iC | %5.1fF" % (temp_c, c_to_f[temp_c]))

tC = 16
print("%i stopni Celsiusza to %.1f stopni Farenhaita" % (tC, c_to_f[tC]))

# CONTINUE & BREAK
i = 0
for liczba in range(1,10,1):
    print("Obieg:" + str(i + 1))
    if(liczba == 5):
        print("XXX")
        break
    i += 1


#
# while(True):
#     if(input("Co chcesz zrobić??? Q-wyjście").upper() == "Q"):
#         print("Przerwanie")
#         break


lista = range(-10,10,1)
los = sample(set(lista),5)
licznik = 5.5
for i in los:
    print("Wylosowana wartość: %i" % i)
    if(i == 0):
        print("Nie można dzielić przez zero")
        continue
    print("Wynik operacji: %.2f" % (licznik/i))

for i in los:
    print("Wylosowana wartość: %i" % i)
    try:
        print("Wynik operacji: %.2f" % (licznik/i))
    except:
        print("Błąd dzielenia przez 0")



#P50
# produkty do kupienia
products = {
        1 : ["A", 49.99, 5],
        2 : ["B", 13.99, 4],
        3 : ["C", 16.99, 9]
            }
# kaoszyk zakupowy
order = {2: ["B",13.99, 1]}

"""
1. Menu zamówień (while ... )
2. Zamówienie produktu po ID w określonej ilości
3. Gdy zamówienie może być dodane do koszyka to zmiejszamy stan magazynowy
4. Eksport paragonu wraz z kwotą do zapłaty
"""

print(len(products))
print(products)
print(time.strftime("%d.%m.%Y %H:%M", time.localtime()))

isClosed = False                                        # zmienna decydująca o zakończeniu programu
orderNo = 1
while(isClosed == False):
    print("Wybierz produkt podając jego ID")
    print("%3s | %20s | %5s | %3s" % ("ID","NAZWA","CENA","ILOŚC"))
    for key in products.keys():                             # pętla wypisująca zawartość słownika products gdy są na magazynie
        if(products[key][2] != 0):
            print("%3i | %20s | %5.2f | %3i" % (key,products[key][0],products[key][1],products[key][2], ))
    try:
        decision = int(input("Wybierz produkt 0-wyjście"))  # wybór użytkownika -> klucz produktu
        if(decision == 0):                                  # wyjście z programu
            sum = 0
            for key in order.keys():                        # pętla obliczająca sumę do zapłaty na podstawie
                sum += order[key][1] * order[key][2]        # słownika order
            print("Do zapłaty: " + str(sum) + "zł")
            isClosed = True
        elif(decision in products.keys()):                  # wybór produktu
            amount = int(input("Podaj ilość"))              # wybór użytkownika -> ilość zamawiana produktu
            if(products[decision][2] < amount):             # porównanie ilości z magazynem -> za dużo jest zamawiane
                print("Brak takiej ilości w magazynie")
            else:                                           # porównanie ilości z magazynem -> zamówienie przyjęte
                print("Dodano do koszyka")
                order[orderNo] = [products[decision][0],products[decision][1],amount] # dodanie zamówienia do koszyka
                orderNo += 1
                print("Twój koszyk")
                for key in order.keys():                    # pętla wypisująca zawartość koszyka
                    print("%3i | %20s | %5.2f | %3i" % (key, order[key][0], order[key][1], order[key][2]))
                products[decision][2] = products[decision][2] - amount
        else:                                               # błąd użytkownika
            print("Błędny wybór")
    except:
        print("Błąd! Musisz podać wartość całkowitą")







