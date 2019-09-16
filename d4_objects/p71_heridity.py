# P71
# Napisz program wykorzystując mechanizm dziedziczenia zawierającego:
# Klasę bazową o nazwie Produkt zawierającą konstruktor i metodę wyświetlającą nazwę i cenę produktu.
# Klasę Oprogramowanie rozszerzającą klasę Produkt zawierającą konstruktor i metodę wyświetlającą nazwę, cenę, język i system.
# Klasę Szkolenia rozszerzającą klasę Oprogramowanie zawierającą konstruktor i metodę wyświetlającą nazwę, cenę, język, system i termin.
# Przetestuj działanie klas na podstawie utworzonych obiektów klasy Oprogramowanie i klasy Szkolenia.

import datetime


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return "Produkt %s kosztuje %s zł" % (self.name, self.price)

class Software(Product):
    def __init__(self, name, price, language, system):
        super().__init__(name, price)
        self.language = language
        self.system = system
    def __str__(self):
        return super().__str__() + " w języku %s i systemie %s" % (self.language, self.system)

class Studies(Software):
    def __init__(self, name, price, language, system, date):
        super().__init__(name,price,language,system)
        self.date = date
    def __str__(self):
        return super().__str__() + " z którego szkolenie jest w dniu %s" % (self.date)

print("")
print("Zadanie P71!!!111")
print("")
product = Product ("produkt1", 4)
print(product)
software = Software("Oprogramowanie",2000, "Java","Windows")
print(software)
studies = Studies("Szkolenie",5000,"JavaScript","Windows",datetime.datetime.today().strftime("%d.%m.%Yr"))
print(studies)