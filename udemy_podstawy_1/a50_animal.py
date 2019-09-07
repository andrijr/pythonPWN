class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        print("Metoda Animal")
    def printInformation(self):
        print(self.name)
        print(self.age)
    def giveTheVoice(self):
        print("voice")

class Mammal(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, name, age)
    def go(self):
        print("go go go")
    def printInformation(self):
        Animal.giveTheVoice(self)
        print("I am marnal")

class Cat(Mammal):
    def __init__(self, name, age , breed):
        #super().__init__(name, age)
        Mammal.__init__(self, name, age)
        self.breed = breed
    def giveTheVoice(self):
        print("Miaw")
    def printInformation(self):
        Mammal.printInformation(self)
        print(self.breed)
        print("I am Cat")

class Pies(Mammal):
    def __init__(self, name, age , breed):
        #super().__init__(name, age)
        Mammal.__init__(self, name, age)
        self.breed = breed
    def giveTheVoice(self):
        print("Gaw")
    def printInformation(self):
        Mammal.printInformation(self)
        print(self.breed)
        print("I am Pies")