
def wyswietlPlansze(mapa2D: list):
    print("   1  2  3")
    numerWiersza = 1
    for wiersz in mapa2D:
        print(numerWiersza, end='  ')
        for element in wiersz:
            print(element, end='  ')
        print()
        numerWiersza += 1

def wygrana(mapa2D):
    for x in range(0,3):
        if mapa2D[x][0] == mapa2D[x][1] == mapa2D[x][2] and mapa2D[x][2] == 'X' or mapa2D[x][2] == 'O':
            return True
    for y in range(0, 3):
        if mapa2D[0][y] == mapa2D[1][y] == mapa2D[2][y] and mapa2D[2][y] == 'X' or mapa2D[2][y] == 'O':
            return True
    if mapa2D[0][0] == mapa2D[1][1] == mapa2D[2][2] and mapa2D[2][2] == 'X' or mapa2D[2][2] == 'O':
        return True
    if mapa2D[0][2] == mapa2D[1][1] == mapa2D[2][0] and mapa2D[2][0] == 'X' or mapa2D[2][0] == 'O':
        return True
    return False

def remis(mapa2D):
    if not wygrana(mapa2D):
        for wiersz in mapa2D:
            for element in wiersz:
                if element == '*':
                    return  False
        return True
    else:
        return False

graKrzyzyk = False
pobrana = input("jeżeli zaczynają krzyżyki wpisz X jeżeli O to wpisz O: ")
if pobrana == "X":
    graKrzyzyk = True
plansza = [ ['*', '*','*' ], ['*', '*','*' ], ['*', '*','*' ] ]
#wyswietlPlansze(plansza)

while (not remis(plansza)) and (not wygrana(plansza)):
    wyswietlPlansze(plansza)
    x, y = [int(x) for x in input("Podaj współrzędne pola na któe chcesz postawić krzyżyk bądź kółko: ").split()]
    if plansza[x-1][y-2] == '*':
        if graKrzyzyk:
            plansza[x-1][y-1] = 'X'
            graKrzyzyk = False
        else:
            plansza[x-1][y-1] = 'O'
            graKrzyzyk = True

wyswietlPlansze(plansza)

if wygrana(plansza):
    if graKrzyzyk:
        print("Wygral gracz grający kólkami O")
    else:
        print("Wygral gracz grający krzyrzykamie X")
else:
    print("Nastąpił remis")

