# Napisz program, który zamieni podaną przez użytkownika liczbę zapisaną słownie
# na wartość (z zakresu od 1 do 5) na odpowiadającą jej liczbę dziesiętną.

# P39
# slowo = input("Podaj liczbę słownie")

slownik = {"jeden": 1, "dwa": 2, "trzy": 3, "cztery": 4, "pięć": 5, "sześć": 6, "siedem": 7,
           "osiem": 8, "dziewięć": 9, "dziesięć": 10, "jedenaście": 11, "dwanaście": 12, "trzynaście": 13,
           "czternaście": 14, "piętnaście": 15, "szesnaście": 16, "siedemnaście": 17, "osiemnaście": 18,
           "dziewiętnaście": 19, "dwadzieścia": 20, "trzydzieści": 30, "czterdzieści": 40, "pięćdziesiąt": 50,
           "sześdziesiąt": 60, "siedemdziesiąt": 70, "osiemdziesiąt": 80, "dziewięćdziesiąt": 90, "sto": 100}

slowo = input("Podaj liczbę słownie od 1 do 100 : ")

lista = slowo.split()
# lista = ["dwadzieścia", "cztery"]
# print(lista)
result = []
for x in lista:
    # print(x)
    if x in slownik:
        # print(x)
        result.append(int(slownik[x]))
print(result)
print(sum(result))
