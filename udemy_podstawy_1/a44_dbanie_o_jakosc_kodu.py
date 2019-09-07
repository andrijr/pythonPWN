lista = []
text = 'lsadjflsajfowiefoisd f'
for charakter in text:
    if not charakter in lista and charakter != '':
        lista.append(charakter)
print(lista)
sortedLista = sorted(lista)
print(sortedLista)

listaIlosciWystapien = []
for charakter in lista:
    ile = 0
    for lista in text:
        if lista == charakter:
            ile += 1
        else:
            pass
    listaIlosciWystapien.append((ile))
print(listaIlosciWystapien)

for i in range(0,len(sortedLista)):
    print(sortedLista[i], listaIlosciWystapien[i])
print()


##################
text = 'lsadjflsajfowiefoisd f'
setOfLetters = set(text).difference("")
print(setOfLetters)
dictOfLetters = dict((letter, text.count(letter)) for letter in setOfLetters )
print(dictOfLetters)
listOfLetters = sorted(dictOfLetters.keys())
for letter in listOfLetters:
    print(letter, dictOfLetters[letter])