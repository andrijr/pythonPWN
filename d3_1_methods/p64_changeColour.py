# P64
# Napisz funkcję, która będzie wyświetlała przy każdym kolejnym wywołaniu na przemian nazwy dwóch kolorów: biały i czarny.

def changeColour(n, colour1 = "black",colour2="white"):
    for i in range(0,n+1):
        if i % 2 == 0:
            print(colour1)
        else:
            print(colour2)
changeColour(5)
print()
def changeColour2(n, colour1 = "black",colour2="white"):
    isColour = "black"
    for i in range(0,n+1):
        if isColour == "white":
            print(colour2)
            isColour = "black"
        else:
            isColour = "white"
            print(colour1)
changeColour2(5)
print()
#########################

posts = ["Post1","Post2","Post3","Post4"]

def generateHtmlSpanCode(posts, color = "black", fontSize = 12):
    html_content = ""
    for post in posts:
        html_content += '<h1 style="color: %s; font-size: %s;">%s</h1>\n' % (color, fontSize, post)
    return html_content

print(generateHtmlSpanCode(posts, "red", 16))

def generateHtmlSpanCodeWithBackground(posts, color = "black", fontSize = 12):
    html_content = ""
    backgroundColor = "black"
    for post in posts:
        html_content += '<h1 style="color: %s; font-size: %s; backgroundColor: %s">%s</h1>\n' % (color, fontSize,  backgroundColor, post)
        if (backgroundColor == "black"):
            backgroundColor = "white"
        else:
            backgroundColor = "black"
    return html_content

print(generateHtmlSpanCode(posts, "red"))

color = "black"
def generateDifferenceColors():
    global color
    if(color == "black"):
        color = "white"
    else:
        color = "black"
    return color

print(generateDifferenceColors())
print(generateDifferenceColors())
print(generateDifferenceColors())
print(generateDifferenceColors())
print(generateDifferenceColors())
print()

color = "black"
def generateDifferenceColors(color1 = "back", color2 = "white",):
    global color
    if(color == color1):
        color = color2
    else:
        color = color1
    return color

print(generateDifferenceColors())
print(generateDifferenceColors())
print(generateDifferenceColors())
print(generateDifferenceColors())
print(generateDifferenceColors())


