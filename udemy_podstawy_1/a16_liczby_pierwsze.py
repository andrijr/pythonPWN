
# liczba = int(input("Podaj liczbę: "))
#
# liczbaPierwsza = True
#
# for dzielnik in range(2, liczba):
#     if liczba %  dzielnik == 0:
#         liczbaPierwsza = False
#         print("Podana liczba ", liczba, "Dzieli się przez " , dzielnik)
#
# if liczbaPierwsza:
#     print("Podana liczba ", liczba, " jest pierwsza ")

for liczba in range(2,1001):
    liczbaPierwsza = True
    for dzielnik in range(2, liczba):
        if liczba % dzielnik ==0:
            liczbaPierwsza = False
            print("Podana liczba ", liczba, "Dzieli się przez ", dzielnik)

    if liczbaPierwsza:
        print("Podana liczba ", liczba, " jest pierwsza ")



