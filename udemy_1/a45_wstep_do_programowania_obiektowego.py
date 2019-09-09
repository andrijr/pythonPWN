def szczekaj():
    print("hau hau")
def machajOgonem():
    print("machaj ogonem")

# najpierw jest ktoś lub coś a pózniej co wykonuję
# klasa to zbór informacji o bjekcie ze pies ma rase ma
# funkcje w klasach to są metody

class Dog:
    def giveVoice(self):
        print("hau hau")

# tworzymy objekty
szarik = Dog()
azor = Dog()

azor.giveVoice()
szarik.giveVoice()

