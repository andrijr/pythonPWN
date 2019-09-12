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

produkts = {
            "A": [1, 3.50, 10],
            "B": [2, 2.99, 5],
            "C": [3, 9.99, 1]
            }

# isClosed = False
# while (isClosed == False):
print("%5s | %3s | %7s | %3s"  % ("Produkt", "ID", "Cena", "Ilość"))
for key in produkts.keys():
    print("%7s | %3i | %7.2f | %3i" % (key, produkts[key][0],produkts[key][1],produkts[key][2] ))
    produkt = input("Pdoaj id produtu któy chcesz zamówić")
    for x in board:





# isClosed == True


