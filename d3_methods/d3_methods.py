from time import  localtime

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