from math import sqrt

# suma = 0
# for x in range(0,10,2):
#     print(x)
#     suma += x
# print(suma)


#program oblicza sęrednią aretmetyczną z dowolnej ilości liczb

ileLiczb = 4 # int(input("Podaj ile liczb: "))
suma = 0
for x in range(0, ileLiczb):
    suma += 4 #int(input("Podaj liczbe: "))
print("średnia z podanych liczb", suma/ileLiczb)

# 1. napisz programy liczące: średnią harmoniczną , średnią geometryczną, srednią kwadratową
# 2. oblicz sume liczb od 1 do 1000 wszystkich oraz tych które są podzielne przez 3 oraz nie podzielne przez 3



# ileLiczb = 4 # int(input("Podaj ile liczb: "))
# suma = 0
# for i in range(0,ileLiczb):
#     suma += 1/ float(input("Podaj ile liczb: "))
# print("średnia harmoniczna", ileLiczb/suma)



# ileLiczb = 4 # int(input("Podaj ile liczb: "))
# suma = 1
# for i in range(0,ileLiczb):
#     suma *= float(input("Podaj ile liczb: "))
# print("średnia geometryczna", pow(suma,1/ileLiczb))



# ileLiczb = 4 # int(input("Podaj ile liczb: "))
# suma = 0
# for i in range(0,ileLiczb):
#     suma += float(input("Podaj ile liczb: "))**2
# print("średnia kwadratowa", sqrt(suma/ileLiczb))



dzieloneNaTrzy = 0
nieDzieloneNaTrzy = 0
for i in range(1,10):
    if i % 3 == 0:
        dzieloneNaTrzy += i
        print("dzielone na trzy", i)
    else:
        nieDzieloneNaTrzy +=i
        print("Nie dzielone na trzy", i)
print(dzieloneNaTrzy)
print(nieDzieloneNaTrzy)