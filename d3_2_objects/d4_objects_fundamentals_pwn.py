# struktura - model danych
from math import sqrt


class Point3D:
    # konstruktor
    def __init__(self, x = 0, y = 0, z = 0):
        # self.x - pole klasowe - dostępne dla wszystkich składowych klasy
        self.x = x
        self.y = y
        self.z = z
    # tekstowa reprezentacja obiektu
    def __add__(self, other):
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)
    def __gt__(self, other):
        if(sqrt(self.x**2 + self.y**2 + self.z**2) - sqrt(other.x**2 + other.y**2 + other.z**2) > 0):
            return True
        return False
    def __eq__(self, other):
        if(self.x == other.x and self.y == other.y and self.z == other.z):
            return True
        return False
    def __str__(self):
        return "[x=%d,y=%d,z=%d]" % (self.x,self.y,self.z)

# obsługa żądań - kontroler
class Point3DController:
    # metoda do dodawania składowych dwóch pkt
    # zwracająca nowy punkt z sumą składowych
    def sumTwoPoints(self, p1, p2):
        # utworzenie obiektu klasy Point3D
        newPoint = Point3D(p1.x + p2.x, p1.y + p2.y, p1.z + p2.z)
        return newPoint
    def multiplyByValue(self, point, value):
        return Point3D(point.x * value, point.y * value, point.z * value)
    # metoda sumująca wszystkie składowe punktów znajdujące się w liście
    # metoda przyjmuje listę punktów jako argument
    # metoda zwraca obiekt klasy Poin3D
    def sumAllPoints(self, points):
        sumPoint = Point3D(0,0,0)
        # element listy to obiekt klasy Point3D
        for point in points:
            sumPoint.x += point.x
            sumPoint.y += point.y
            sumPoint.z += point.z
        return sumPoint
    # metoda wyszukująca punkt w liście po jego składowych
    # metoda zwraca wartość typu boolean
    def findPoint(self, points, x, y, z):
        findPoint = Point3D(x,y,z)
        for point in points:
            if(point.x == findPoint.x and point.y == findPoint.y and point.z == findPoint.z):
                return True
        return False

# utworzenie obiektu klasy
point1 = Point3D(0,0,0)
point2 = Point3D(5,5,5)
# odwołanie do pól klasowych
print("Point1",point1.x, point1.y, point1.z)
print("Point2",point2.x, point2.y, point2.z)
# modyfikacja pól klasowych
point1.x = 1
point1.y = point2.y - 1
print("Point1",point1.x, point1.y, point1.z)
print("Point2",point2.x, point2.y, point2.z)
# metoda do reprezentacji tekstowej obiektu - toString()
print(point1)
print(point2)
# metoda sumująca składowe obiektów klasy Point3D
pc = Point3DController()
pointSum1 = pc.sumTwoPoints(point1,point2)
print(pointSum1)
# pointSum2 = pc.sumTwoPoints(point2,point2)
# print(pointSum2)
# skalowania składowych punktu
print(pc.multiplyByValue(point1,2))
resultPoint = pc.multiplyByValue(Point3D(9,9,9),0.5)
print(resultPoint)
print(resultPoint.x, resultPoint.y, resultPoint.z)

points = [Point3D(1,1,1), Point3D(2,2,2), Point3D(3,2,1),Point3D(0,5,11)]
print(pc.sumAllPoints(points))

print(pc.findPoint(points, 1,1,2))

print("Nazwa klasy: ", point1.__class__.__name__)
print("Nazwa klasy: ", pc.__class__.__name__)
print("Nazwa klasy: ", resultPoint.__class__.__name__)
print("Nazwa klasy: ", points.__class__)
print("Nazwa klasy: ", pc.findPoint(points, 1,1,2).__class__)
print("Typ obiektu: ", type(points))

print(Point3D(1,2,3))
print("Punkt bez argumentów:", Point3D())

# Special methods
p1 = Point3D(1,1,1)
p2 = Point3D(2,3,4)
# + wywołuje metode specjalną __add__()
print(p1 + p2)
# który punkt jest większy - czyli jeży dalej wzglęcem 0,0
print(p1 == p2)
print(p1 == p1)
print("p1 > p2",p1 > p2)
print("p1 > p1",p1 > p1)

# Cykl życia obiektu
p1 = Point3D(1,1,1)
p2 = p1
p3 = Point3D(1,1,1)
print(p1)
print(p2)
print(p3)
print("XXXXX")
p1.y = 2
print(p1)
print(p2)
print(p3)
print("XXXXX")
p1 = Point3D(1,1,1)
print(p1)
print(p2)
print(p3)

