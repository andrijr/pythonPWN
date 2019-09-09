class Car:
    def __init__(self, model, brand, number):
        self.colour = ""
        self.position = [0,0]
        self.model = model
        self.brand = brand
        self.vehileRegistrationNumber = number
        self.speed = 0

    def printInformation(self):
        print("mój kolor to ", self.colour)
        print("znajduję się w miejscu takim", self.position)
        print("mój model", self.model)
        print("moja marka", self.brand)
        print("mój numer rejestracyjny", self.vehileRegistrationNumber)
        print("jadę z prekościa", self.speed)

    def increaseSpeed(self):
        self.speed += 2

    def getSpeed(self):
        return self.speed

myCar = Car("Astra", "Opel", "AB 123456")
atnotherCar = Car("Lacos", "Daewoo", "AB 123456")

myCar.increaseSpeed()
myCar.printInformation()