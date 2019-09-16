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
    print("Wybierz dostępne produkty z listy. Dziękujemy ")
    print(" %2s | %5s | %8s | %3s |" % ("ID", "Produkt", "Cena", "Ilosć"))
    for key in products.keys():
        if products[key][2] != 0:
            print(" %2i | %7s | %8.2f | %5i |" % (key, products[key][0], products[key][1], products[key][2]))
    try:
        decision = int(input("Podaj ID wybranego produktu, 0 - zakącz "))
        if decision == 0:
            sum = 0
            for key in orders.keys():
                sum += orders[key][1] * orders[key][2]
            print("Suma twojego koszyka wynosi:", round(sum, 2))
            isClosed = True
        elif decision in products.keys():
            amount = int(input("Podaj ilość: "))
            if products[decision][2] < amount:
                print("Brak takiej ilości w magazynie")
            else:
                orders[orderNo] = [products[decision][0], products[decision][1],amount]
                products[decision][2]  = products[decision][2] - amount
                orderNo += 1
                print("Dodano do koszyka: ")
                print("Twój koszyk: ")
                print(" %2s | %5s | %8s | %3s |" % ("ID", "Produkt", "Cena", "Ilosć"))
                for key in orders.keys():
                    print(" %2i | %7s | %8.2f | %5i |" % (key, orders[key][0], orders[key][1], orders[key][2]))
                sum = 0
                for key in orders.keys():
                    sum += orders[key][1] * orders[key][2]
                print("Suma twojego koszyka wynosi:", round(sum, 2))
        else:
             print("Błędny wybór produktu ")
    except:
        print("Błąd")


