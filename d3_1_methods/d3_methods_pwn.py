import datetime
from math import sqrt
from random import choices, randint
from time import localtime, time, ctime

returnedValue = localtime()
print(returnedValue)



productNames = ["A","B","C"]
productPrice = [1.99,2.33,5.00]

# metoda przyjmująca agrumnty i nie zwracająca wartości
def printSequence(sequence):
    for element in sequence:
        print(element, end=" ")
    print()

printSequence(productNames)
printSequence(productPrice)
printSequence([1,3,4,5,6,7,8,9,5,3])

"""
1. Szukanie min i max [1,23] | 
2. a = |0-1|/|1-23| = a = |0 - 1| / |min - max|
3. b = 1 - 1/22 * 23 = b = 1 - (a * max)
4. y = a*x + b -> 1/22*x - 1/22 | min - max
"""
# def findMinimum(data):
#     return min(data)
#
# def findMaximum(data):
#     return max(data)

def findExtrema(data):
    return min(data), max(data)

def normalizeDataset(data, lowBorder=0, topBorder=1):
    normalizedData = []
    a = abs(lowBorder - topBorder) / abs(findExtrema(data)[0] - findExtrema(data)[1])
    b = topBorder - (a * findExtrema(data)[1])
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
printDataset(normalizeDataset(data, lowBorder = -1, topBorder = 1))

# Dowolna liczba argumentów
def gradesAvg(*grades):
    sum = 0
    for grade in grades:
        sum += grade
    return sum/len(grades)

print("Uczeń 1: " + str(gradesAvg(2,3,1,4,5,6)),
      "Uczeń 2: " + str(gradesAvg(4,5)),
      "Uczeń 3: " + str(gradesAvg(4,4,4,4)))


#P57
def factorial(n):
    result = 1
    if(n < 0):
        return "Error"
    if(n == 0):
        return 1
    for i in range(2,n+1):
        result *= i
    return result

print(factorial(4))
print(factorial(0))
print(factorial(-19))

# REKURENCYJNIE
def factorialRec(n):
    if(n == 1):
        return 1
    return n * factorialRec(n - 1)

def date_diff_in_microseconds(dt2, dt1):
    timedelta = dt2 - dt1
    return timedelta.microseconds

t_start = datetime.datetime.now()
print(factorial(1000))
t_stop = datetime.datetime.now()
print("Factorial: " + str(date_diff_in_microseconds(t_stop, t_start)))

t_start = datetime.datetime.now()
print(factorialRec(800))
t_stop = datetime.datetime.now()
print("Factorial Rec: " + str(date_diff_in_microseconds(t_stop, t_start)))

# P58
# 1,1,2,3,5,8,....
def fibonacciSeries(n):
    fib = []
    sum = 0
    for index, value in enumerate(range(0,n+1)):
        if(index == 0):
            fib.append(0)
        elif(index == 1):
            fib.append(1)
        else:
            fib.append(fib[index - 1] + fib[index - 2])
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

content = "Ciąg został omówiony w roku 1202 przez Leonarda z Pizy, zwanego Fibonaccim, " \
          "w dziele Liber abaci jako rozwiązanie zadania o rozmnażaniu się królików. " \
          "Nazwę ciąg Fibonacciego spopularyzował w XIX w. Edouard Lucas"

"""
1. Podziel zdanie na wyrazy 
2. Losuj wyrazy i przypisuj je do nowo wygenerowanego zdania 
"""
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
def distanceMeasure(x_start, y_start, x_stop, y_stop):
    return sqrt(pow(x_stop - x_start, 2) + pow(y_stop - y_start, 2))

print(distanceMeasure(1,1,2,2))

# P61
def geometricSeries(a1, q, n):
    sum = 0
    for i in range(1,n+1):
        sum += a1*pow(q,i-1)
    return sum, a1*pow(q,n-1)

print("Geometric series")
print(geometricSeries(2,3,5)[0], geometricSeries(2,3,5)[1])


# ZADANIE DLA WAS: DODAJ ARGUMENT OKREŚLAJACY ILE DUPLIKAGÓW ZNACZNIKA MA BY WYGENEROWANYCH
posts = ["Post1","Post2","Post3","Post4"]

def generateHtmlSpanCode(posts, color = "black", fontSize = 12):
    html_content = ""
    for post in posts:
        html_content += '<h1 style="color: %s; font-size: %s;">%s</h1>\n' % (color, fontSize, post)
    return html_content

# print(generateHtmlSpanCode(posts, "red", 16))
print(generateHtmlSpanCode(posts))

def generateHtmlSpanCodeWithBackground(posts, color = "black", fontSize = 12):
    html_content = ""
    backgrounColor = "black"
    for post in posts:
        html_content += '<h1 style="color: %s; font-size: %s; background-color: %s">%s</h1>\n' % \
                        (color, fontSize, backgrounColor, post)
        if(backgrounColor == "black"):
            backgrounColor = "white"
        else:
            backgrounColor = "black"
    return html_content

print(generateHtmlSpanCodeWithBackground(posts, color = "red"))

# color = "black"
def generateDifferentColors(color1 = "black", color2 = "white"):
    global color
    if(color == color1):
        color = color2
    else:
        color = color1
    return color

color = "black"
print(generateDifferentColors("red","yellow"))
print(generateDifferentColors("red","yellow"))
print(generateDifferentColors())

def generateSignal(n):
    signal = []
    for i in range(0, n):
        signal.append(randint(-1000, 1000))
    return signal
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

