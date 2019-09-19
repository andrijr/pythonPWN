# P59
# Napisz funkcję, która wygeneruje losowe zdanie zawierające podaną liczbę (domyślnie 5) losowo wygenerowanych wyrazów.

from random import sample, choice, randint, random, randint, choices

names = ["Ala","Ola","Ela", "Andrij", "Agni", "Andrij"]
# print(sample(names, 5))
for element in sample(names, 5):
    print("%s " % element, end=" ")
print()

def randSet(list):
    for element in sample(names, 5):
        print("%s " % element, end=" ")
print(randSet(names))
print()


##########################

# P 59
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

print(splitSentenceBySeparator(content, " "))
print(createSentenceByListOfWords(splitSentenceBySeparator(content, " ")))
print(generateSentence(content))
