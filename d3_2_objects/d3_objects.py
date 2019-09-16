# klasa lub encjal
# klasa jest szablonem

class Auto:
    # # pola obiektowe
    # marka = "Audi"
    # model = "A4"
    # cena = 200000.
    def __init__(self, marka, model, cena=10000):
        self.marka = marka
        self.model = model
        self.cena = cena
    # metody obiektowe
    def getAuto(self):
        print("marka: %s model: %s cena %.2f" % (self.marka, self.model, self.cena))
    def setCena(self,nowa_cena):
        self.cena = nowa_cena

# utworzenie obiektu klasy Auto
a1 = Auto("BMW","5",150000)
a1.getAuto()
a1.setCena(180000)
a1.getAuto()
a2 = Auto("Toyota","Avensis")
a2.getAuto()

print(a1)
print(a2)

a3 = Auto("BMW","3",150000)
a4 = Auto("BMW","2",150000)

print(a3)
print(a4)

class AutoFactory:
    autos = []
    def createAuto(self, marka, model, cena):
        a = Auto(marka,model,cena)
        self.autos.append(a)
        print("Dodano auto:", end="")
        a.getAuto()
    def addAuto(self, auto):
        self.autos.append(auto)
    def changePrices(self, changePercent):
        for auto in self.autos:
            auto.setCena(auto.cena * (1 + changePercent/100))
    def showAutos(self):
        for i, auto in enumerate(self.autos):
            print(str(i+1)+" ", end="")
            auto.getAuto()
    def compareAutoPirices(self, auto1, auto2):
        print("porównujemy")
        auto1.getAuto()
        auto2.getAuto()
        if(auto1.cena >= auto2.cena):
            print("Auto: " + auto1.marka + " jest droższe")
        else:
            print("Auto: " + auto2.marka + " jest droższe")
    def getAutoFromAutos(self):
        self.showAutos()
        id = int(input("Które auto chesz pobrać?"))
        return self.autos[id-1]

factory = AutoFactory()
factory.addAuto(a1)
factory.addAuto(a2)
factory.addAuto(a3)
factory.addAuto(a4)
factory.showAutos()
factory.changePrices(10)
factory.showAutos()
factory.createAuto("XXX","XXX",100000)
factory.showAutos()

factory.compareAutoPirices(a1,Auto("Fiat", "Panda", 500000))
factory.compareAutoPirices(Auto("Fiat", "Panda", 500000), factory.getAutoFromAutos())