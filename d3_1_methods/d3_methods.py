from random import choices, randrange, randint
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

# dowolna liczba argumentów
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



# P61
# Zdefiniuj funkcję, która dla podanych trzech parametrów:

a = 2
q = 3
n = 5
def geometric(a, q = 3, n = 5):
    an = a * q **(n-1)
    sum = 0
    for i in range(1, n+1):
        sum += a * q ** (i-1)
    return (an, sum)

print(geometric(a,q, n))


def geometric(a, q = 3, n = 5):
    an = a * q **(n-1)
    sum = 0
    for i in range(0, n):
        sum += a * q ** (i)
    return (an, sum)

print(geometric(a,q, n))


# P 63
# Napisz funkcję generującą kod HTML dla napisu:
# <span style="color: color_name; font-size: value; “>content</span>

def generateHtmlSpanCode(content, color = "black", fontSize = 13, repetition =1):
        html =  '<span style="color: %s ; fontSize: %s; “>%s</span>\n' % (color, fontSize, content)
        html = html * repetition
        return html
print(generateHtmlSpanCode("Test","red", 16, 5))




posts = ["Post1","Post2","Post3","Post4"]

def generateHtmlSpanCode(posts, color = "black", fontSize = 12):
    html_content = ""
    for post in posts:
        html_content += '<h1 style="color: %s; font-size: %s;">%s</h1>\n' % (color, fontSize, post)
    return html_content

print(generateHtmlSpanCode(posts, "red", 16))

def generateHtmlSpanCodeWithBackground(posts, color = "black", fontSize = 12):
    html_content = ""
    backgroundColor = "black"
    for post in posts:
        html_content += '<h1 style="color: %s; font-size: %s; backgroundColor: %s">%s</h1>\n' % (color, fontSize,  backgroundColor, post)
        if (backgroundColor == "black"):
            backgroundColor = "white"
        else:
            backgroundColor = "black"
    return html_content

print(generateHtmlSpanCode(posts, "red"))

color = "black"
def generateDifferenceColors():
    global color
    if(color == "black"):
        color = "white"
    else:
        color = "black"
    return color

print(generateDifferenceColors())
print(generateDifferenceColors())
print(generateDifferenceColors())
print(generateDifferenceColors())
print(generateDifferenceColors())
print()

color = "black"
def generateDifferenceColors(color1 = "back", color2 = "white",):
    global color
    if(color == color1):
        color = color2
    else:
        color = color1
    return color

print(generateDifferenceColors())
print(generateDifferenceColors())
print(generateDifferenceColors())
print(generateDifferenceColors())
print(generateDifferenceColors())

# P65


def tableSum(ilosc, minSup = 0):
    tablica = []
    for i in range(0, ilosc):
        tablica.append(randint(-ilosc, ilosc))
    return tablica

print(tableSum(10))
print()

def generateSignal(n):
    signal = []
    for i in range(0, n):
        signal.append(randint(-1000, 1000))
    return signal
print(generateSignal(10))

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