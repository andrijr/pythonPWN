# kłodka jest pięcio cyfrowa
# największą możliwa cyfrą jest 8
# brak 0 i 6
# suma cyfr wynosila 21
# cyfry nie powtarzają się
# iloczyn cyfr był albo większy lub równy 70
# ostatnia cyfra jest nie parzysta
licznik = 0
for a in range(1,9):
    for b in range(1,9):
        for c in range(1,9):
            for d in range(1,9):
                for e in range(1,9):
                    if e % 2 == 0:
                        liczbaKlodki = True
                        if a != b and a != c and a != d and a!= e and b != c and b != d and b!= e and c != d and c!= e and d!= e:
                            #print( a, b, c, d, e, "nie równe sobie")
                            if a * b * c * d * e >= 70:
                                #print( a, b, c, d, e, "wieksze 70")
                                if a + b + c + d + e == 21:
                                    #print(a, b, c, d, e, "suma równa 21")
                                    if a != 6 and b != 6 and c != 6 and d != 6 and e != 6:
                                        #print(a, b, c, d, e, "brak 0 i 6")
                                        print(a, b, c, d, e)
                                        licznik += 1
print(licznik)

# kłódka jest 5 cyfrowa
# liczba przedstawiająca kłodkę jest liczbą pierwszą
# suma cyfr była z zakresu  30 i 40
# nie było żadnego 0

from math import sqrt
liczbaPierwsza = True
licznik = 0
suma = 0
for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            for d in range(1,10):
                for e in range(1,10):
                    if 30 <= a+b+c+d+e <=40:
                        liczba = (int(a)*10000+int(b)*1000+int(c)*100+int(d)*10+int(e))
                        #print(a,b,c,d,e)
                        #print(liczba)
                        liczbaPierwsza = True
                        for dzielnik in range(2,int(sqrt(liczba))):
                            if liczba % dzielnik == 0:
                                liczbaPierwsza = False
                                #print(liczba, "podzielna na liczbę", dzielnik)
                        if liczbaPierwsza == True:
                            print(liczba, "Liczba pierwsza")

                            licznik += 1
print(licznik)