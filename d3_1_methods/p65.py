# P65
# Napisz funkcję, która będzie sumowała wszystkie te elementy tablicy które są większe od żądane j wartości.
# Użytkownik podaje wartość progu MinSup (domyślnie 0) i ilość generowanych elementów tablicy
# Elementy tablicy przy każdym uruchomieniu programu są generowane losowo z zakresu od -1000 do 1000
# Niech funkcja zwróci wszystkie elementy większe od wartości progowej oraz wartość ich sumy.
from random import randint

# def tableSum(ilosc, minSup = 0):
#     tablica = []
#     for i in range(0, ilosc):
#         tablica.append(randint(-ilosc, ilosc))
#     return tablica
# print(tableSum(10))
# print()

def generateSignal(n):
    signal = []
    for i in range(0, n):
        signal.append(randint(-1000, 1000))
    return signal
print(generateSignal(10))
print()


def sumRandomValuesWithSuport(minSupp, maxSupp, n):
    signal = generateSignal(n)
    processedSignal = []
    sum = 0
    sumProcessed = 0
    for i,v in enumerate(signal):
        sum += v
        if(v < minSupp or v > maxSupp):
            processedSignal.append(0)
        else:
            processedSignal.append(v)
            sumProcessed += v
    return signal, sum, sum/len(signal), processedSignal,sumProcessed, sumProcessed/len(processedSignal)

x = sumRandomValuesWithSuport(-900,900,10)
print(x[0],x[1],x[2])
print(x[3],x[4],x[5])
print(x[2],x[5])

print(sumRandomValuesWithSuport(-900,900,10))
