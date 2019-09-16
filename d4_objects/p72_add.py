# P72
# Napisz prostą klasę zawierającą pola kolorów składające się z wartości RGB.
# Przypisz do tych pól dowolne wartości wykorzystując konstruktor klasy
# Zrzutuj te parametry RGB na napis i wypisz je poza klasą.
# Dodatkowo dodaj kolor zielony i niebieski aby otrzymać kolor żółty – zastosuj operator __add__

class RGB:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    def __add__(self, other):
        color = RGB(
            255 if (self.r + other.r) > 255 else self.r + other.r,
            255 if (self.g + other.g) > 255 else self.g + other.g,
            255 if (self.b + other.b) > 255 else self.b + other.b)
        return color
    def __str__(self):
        return "RGB[%d,%d,%d]" % (self.r, self.g, self.b)

red = RGB(255,0,0)
green = RGB(0,255,0)
blue = RGB(0,0,255)
print(red,green,blue)
print(red + green)
print(green + blue)
print(green + green)


