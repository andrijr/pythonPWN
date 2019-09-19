# P63
# Napisz funkcję generującą kod HTML dla napisu:
# <span style="color: color_name; font-size: value; “>content</span>
#  Użytkownik może podać wartości poszczególnych parametrów, jeśli tego nie zrobi przypisywane są wartości domyślne.

content = "Tekst Nowy"

# Napisz funkcję generującą kod HTML dla napisu:
# <span style="color: color_name; font-size: value; “>content</span>

def generateHtmlSpanCode(content, color = "black", fontSize = 13, repetition =1):
        html = '<span style="color: %s ; fontSize: %s; ">%s</span>\n' % (color, fontSize, content)
        html = html * repetition
        return html
print(generateHtmlSpanCode("Test","red", 16, 5))