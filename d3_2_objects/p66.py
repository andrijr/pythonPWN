# P66
# Napisz program, który posłuży do obliczania BMI zawodnika
# Utwórz klasę Zawodnik zawierającą metodę do obliczania BMI
# Utwórz obiekt reprezentujący zawodnika
# Wywołaj metodę klasową, która zwróci wartość BMI

class Player:
    def __init__(self, name, lastname, weight, hight):
        self.name = name
        self.lastname = lastname
        self.weight = weight
        self.hight = hight
    def calculateBmi(self):
        return self.weight/pow(self.hight/100,2)
    def __str__(self):
        return "Imię: %-15s Nazwisko: %-15s BMI: %-15.2f" % (self.name, self.lastname, self.calculateBmi())

p1 = Player("Michał", "Kruczkowski", 80, 182)
p2 = Player("Adam", "Kowalski", 85, 175)
print(p1)
print(p2)