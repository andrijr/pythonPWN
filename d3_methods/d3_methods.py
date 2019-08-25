from random import choices
from time import localtime, time
from timeit import timeit
from cmath import sqrt

# funkcje to tez metody w python
# metody są malymi literami a klasy są dużymi

returnValue = localtime()
print(returnValue)

productNames = ["A", "B", "C"]
productPrice = [1.99, 2.33, 5.00]

# metoda prezentująca zawartość sekwencji
# metoda przyjmująca argumenty i nie zwracająca wartości
def printSequence(sequence):
    for element in sequence:
        print(element, end=" ")
    print()

printSequence(productNames)
printSequence(productPrice)
printSequence([1,2,3,4,5])

"""
1. Szukanie min i max [1,23] | 
2. a = |0-1|/|1-23| = a = |0 - 1| / |min - max|
3. b = 1 - 1/22 * 23 = b = 1 - (a * max)
4. y = a*x + b -> 1/22*x - 1/22 | min - max
"""
def findMinimum(data):
    return min(data)

def findMaximum(data):
    return max(data)

def findExtrema(data):
    return min(data), max(data)

def normalizeDataset(data, lowBorder=0, topBorder=1):
    normalizedData = []
    a = abs(lowBorder - topBorder) / abs(findMinimum(data) - findMaximum(data))
    b = topBorder - (a * findMaximum(data))
    for element in data:
        # normalizacja liniowa aX + b
        normalizedData.append(a * element + b)
    return normalizedData

def printDataset(data):
    for element in data:
        print("%6.3f" % element, end= " ")
    print()
data = [1 ,23 ,4 ,2 , 4, 5, 4, 11] # do znormalizowania od 0 -> 1


printDataset(data)
printDataset(normalizeDataset(data))
printDataset(normalizeDataset(data, -1, 1))
printDataset(normalizeDataset(data, lowBorder = -1, topBorder = 1))
findExtrema(data)

# dowolna liczba argumentó
def gradesAvg(*grades):
    sum = 0
    for grade in grades:
        sum += grade
    return sum/len(grades)

print("Uczeń 1: " + str( gradesAvg(2,3,1,4,5,6)),
      "Uczeń 1: " + str(gradesAvg(2,3)),
      "Uczeń 1: " + str(gradesAvg(2,3,1,5)) )


# P 57
# Napisz program implementujący funkcję n! - silnia
def factorial(n):
    result = 1
    if(n<0):
        return "Error"
    if(n == 0):
        return 1
    for i in range(2, n+1):
        result *= i
    return result

print(factorial(4))
print(factorial(0))
print(factorial(-5))

# Rekurencyjnie
def factorialRec(n):
    if(n == 1):
        return 1
    return n * factorialRec(n-1)

t_start = timeit()
print(factorialRec(4))
t_stop = timeit()
print(t_start - t_stop)

t_start = timeit()
print(factorial(4))
t_stop = timeit()
print(t_start - t_stop)



# P 58
# Napisz program obliczający wartość zadanego elementu ciągu Fibonacciego i obliczający sumę elementów ciągu.


def fibonacciSeries(n):
    fib = []
    sum = 1
    for index, value in enumerate(range(0, n+1)):

        if(index == 0):
            fib.append(0)
        elif(index == 1):
            fib.append(1)
        else:
            fib.append(fib[index -1] + fib[index -1])
        sum += fib[index]
    return fib, fib[n], sum

print(fibonacciSeries(15))


names = ["Ala","Ola","Ela"]
for i, name in enumerate(names):
    print(i, name)
# == #
i = 0
for name in names:
    print(i, name)
    i += 1

# 59
# Napisz funkcję, która wygeneruje losowe zdanie zawierające podaną liczbę (domyślnie 5) losowo wygenerowanych wyrazów.

content = "Ciąg został omówiony w roku 1202 przez Leonarda z Pizy, zwanego Fibonaccim, " \
"w dziele Liber abaci jako rozwiązanie zadania o rozmnażaniu się królików. " \
"Nazwę ciąg Fibonacciego spopularyzował w XIX w. Edouard Lucas"

"""
1. Podziel zdania na wyrazy
2. Losuj wyrazy i przypisów je do nowo wygenerowanego zdania
"""

# print(str.split(content))
# for slowo in content:
#     print(slowo, end=" ")
# print()

def splitSentenceBySeparator(content, separator):
    return content.split(separator)
def createSentenceByListOfWords(listOfWords):
    sentence = ""
    for word in listOfWords:
        sentence += word + " "
    return sentence + "."
def generateSentence(content, n = 5):
    words = splitSentenceBySeparator(content, " ")
    generatedSentence = choices(words, k = n)
    return createSentenceByListOfWords(generatedSentence)

print(generateSentence(content))

# P60
# Napisz program do wyliczania odległości między dwoma punktami na płaszczyźnie.

def distanceMeasure(x_start, y_start, x_stop, y_stop):
    return sqrt(pow(x_stop - x_start, 2) + pow(y_stop - y_start, 2))

print(distanceMeasure(1,1,2,2))












