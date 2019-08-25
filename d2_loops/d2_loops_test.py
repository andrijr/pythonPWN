
#P50
# produkty do kupienia
import time

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







