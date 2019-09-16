# P50

# Napisz program do obsługi zamówień w sklepie internetowym:
# W sklepie sprzedawane są 3 produkty: A, B, C
# Posiadają one swoje:
# ID: 1, 2, 3
# Nazwa: A, B, C
# Cenę: 3.50, 2.99, 9.99
# Ilość magazynową: 10, 5, 1
# Zaprojektuj menu zamówień w sklepie:
# Użytkownik zamawia towar po jego unikatowym ID
# Użytkownik może zamówić ilość nie większą niż dostępność na magazynie
# Użytkownik może w po zrealizowaniu zamówienia zamówić kolejne produkty
# Efektem zakończenia zamawiania produktów jest:
# Paragon zawierający informację jakie produkty zamówił użytkownik
# Kwota do zapłaty
# Pamiętaj o walidacji danych!
"""
1. Menu zamówień (while ... )
2. Zamówienie produktu po ID w określonej ilości
3. Gdy zamówienie może być dodane do koszyka to zmiejszamy stan magazynowy
4. Eksport paragonu wraz z kwotą do zapłaty
"""
products = {
        1: ["A", 49.99, 5],
        2: ["B", 13.99, 4],
        3: ["C", 16.99, 9],
        4: ["D", 20.99, 0]
            }
orders = {}
orderNo = 1
isClosed = False
while (isClosed == False):
    print("Wybierz dostępne u nas produkty z listy. Dziękujemy ")
    print("%4s | %5s | %7s | %3s"  % ("ID", "Produkt", "Cena", "Ilość"))
    for key in products.keys():
        if products[key][2] != 0:
            print("%4i | %7s | %7.2f | %3i" % (key, products[key][0],products[key][1],products[key][2] ))
    try:
        decision = int(input("Zamów podaj ID produktu, 0 - Oplać koszyk "))
        if (decision == 0):
            print("Twój koszyk: ")
            sum = 0
            for key in orders.keys():
                sum += orders[key][1] * orders[key][2]
            print("Do zapłaty", round(sum,2))
            isClosed = True
        elif (decision in products.keys()):
            amount = int(input("Podaj ilość"))
            if products[decision][2] < amount:
                print("Brak takiej ilości w magazynie wybierz dostępną ilość")
            else:
                print("Dodano do koszyka")
                orders[orderNo] = [products[decision][0], products[decision][1],amount]
                orderNo += 1
                print("Twój koszyk")
                print("%4s | %5s | %7s | %3s" % ("ID", "Produkt", "Cena", "Ilość"))
                for key in orders.keys():
                    print("%4i | %7s | %7.2f | %3i" % (key, orders[key][0],orders[key][1],orders[key][2] ))
                products[decision][2] = products[decision][2] - amount
                sum = 0
                for key in orders.keys():
                    sum += orders[key][1] * orders[key][2]
                print("Do zapłaty", round(sum,2))

        else:
            print("Błędny wybór produktu")
            print(products.keys())
    except:
        print("Błąd! Musisz podać wartość całkowitą")





# isClosed == True


