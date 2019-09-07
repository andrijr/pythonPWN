class czlowiek:                                     # tworzymy klase o nazwie człowiek
    imie = ""                                       # Dodajemy zmienne
    nazwisko = ""
    def predstawsie(self):                          # Tworzymy metodę
        print(self.imie, self.nazwisko)
    def zmienImie(self):
        self.imie = "Andrij" #input("Podaj nowe imię: ")
znajomy = czlowiek()                                # tworzymy objekt naszej klasy czlowiek
znajomy2 = czlowiek()

znajomy.imie = "Jan"
znajomy.nazwisko = "Kondrad"
znajomy.predstawsie()
znajomy.zmienImie()
znajomy.predstawsie()


class czlowiek:                                     # redefiniujemy klase o nazwie człowiek
    imie = ""                                       # Dodajemy zmienne
    nazwisko = ""
    def __init__(self):                             #  funkcja _init_  jest konstruktorem klasy czyli gdy tworzymy jakiś objekt naszej klasy ta funkcja zwsze się wywołuje
        self.imie = "Kondrad"
    def przedstawsie(self):
        print(self.imie)

znajomy = czlowiek()
znajomy.przedstawsie()

class czlowiek:
   # imie = ""
   # nazwisko = ""
    def __init__(self, name):
        self.imie = name
    def przedstawsie(self):
        print(self.imie)

znajomy = czlowiek("Andrzej")
znajomy.przedstawsie()
znajomy2 = czlowiek("Piotr")
znajomy2.przedstawsie()