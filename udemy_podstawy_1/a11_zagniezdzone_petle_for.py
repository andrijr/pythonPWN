for x in range(1,11):
    for y in range(1,11):
        if len(str(x*y)) < 2:
            print(x * y, end="   ")
        else:
            print(x* y, end="  ")
        #print("%i " " " % (x*y))
    print()

# napisz program któy wyświetli wszystkie możliwe kombinacje kłodki czterocefrowej gdzie pierwsza cyfra jest parzysta druga nie przysta
# trzecia podzielna przez 5
# czwarta podzielna przez 3

for a in range(0,10, 2):
    for b in range(1,10,2):
        for c in range(0,10,5):
            #for d in range(0,10, 3):
            for d in range(0,10):
                if d % 3 == 0:
                    print(a,b, c, d)

# 1. Zdanie
# napisz program przypominający możliwe kody do kłodki
# kłódka 5 cyfrowa
# żadna cyfra nie jest większa niż 6
# nie było w kodzie 0
# piersza trzecia oraz piąta cyfra to albo 0 albo 5
# drógę liczby były nie parzyste

# 2. Zadanie
# znaleść w jaki sposób poprawić nasz program tabliczki mnozenia

for a in [5]:
    for b in range(2,7,2):
        for c in [5]:
            for d in range(1,7):
                for e in [5]:
                    print(a, b, c, d, e)