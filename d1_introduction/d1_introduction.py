# one line comment
"""
    multiline comments
"""

### Zmienne
############################################
# data types (typy danych)
############################################
print ('# Zmienne')
# dynamic typing (dynamiczne typowanie)
tekst = 'Andrij'
a = 3
PI = 3.14
print ('tekst')
print (tekst)
print(a)
print(PI)

# PO
imie   = "Anna"
adres_zamieszkania = "Nieznana-20"
drugie_imię = "Beata"
ulubione_potrawy = "x,y,z"
print(ulubione_potrawy)
and_dana = "dana"
And = "hello"
wart2 = "2"

# POa
zmienna_1 = 45
zmienna_2 = 'Szkolenia'
zmienna_3 = 23.3
zmienna_4 = 'Test'
zmienna_5 = '?'
print(zmienna_1, zmienna_2, zmienna_3, zmienna_4, zmienna_5)



# P0b
Cel = 'Cel'
sukces = 'sukces'
zwycięstwo = 'zwycięstwo'
chwala_1 = 'chwala'
debiut = 'debiut'

sukces = 58
zwycięstwo = 147
debiut = 258
print(Cel, sukces, chwala_1, zwycięstwo, debiut)

###
a = 1
b = a
print(b)

a = 1
b = 2
tmp = 1
a = 2
b = 1
print(a,b)

# pattern matching
a = 1
b = 2
a,b = b,a
print(a,b)

# P0c
zmienna_1 = "Ciekawe"
zmienna_2 = "Programowanie"
zmienna_3 = "Jest"
zmienna_4 = "wciagajace"
zmienna_5 = "i"

tmp       = zmienna_1 # Ciekawe
zmienna_1 = zmienna_2 # Programowanie
zmienna_2 = tmp       # Ciekawe

tmp       = zmienna_2 # Ciekawe
zmienna_2 = zmienna_3 # Jest
zmienna_3 = tmp       # Ciekawe

tmp       = zmienna_4 # wciagajace
zmienna_4 = zmienna_5 # i
zmienna_5 = tmp       # wciagajace

print (zmienna_1, zmienna_2, zmienna_3, zmienna_4, zmienna_5)

###
zmienna_1 = "Ciekawe"
zmienna_2 = "Programowanie"
zmienna_3 = "Jest"
zmienna_4 = "wciagajace"
zmienna_5 = "i"

zmienna_1, zmienna_2, zmienna_3, zmienna_4, zmienna_5 = zmienna_2, zmienna_3, zmienna_4, zmienna_5, zmienna_1
print (zmienna_1, zmienna_2, zmienna_3, zmienna_4, zmienna_5)

# Usuwanie zmiennej
a = 1
#del(a)
print(a)

### Instrukcje
print ("# Instrukcje")

a = 10
a = a + 5
a += 5 # a = a + 5
print (a)

# P0e
a = 1
b = 2
c = 3
d = 4
e = 5
print(a+b*c+d*e)

print (2-1)
print ("2-1")

# P1
a = 1
b = 2.4
c = 'w1'
print(a, b, c)

# P2
a = 2.1
b = 'abc'
c = 0
print(a,b,c)

# P3
b = c
a = 13
print(a, b, c)

x, y, z = 10, 50 , 100
print(x, y, z)

# P3a
y += 18
print(x, y, z)

# P3b
x = x+100
print(x, y, z)

# P3d
z *=5
print(x,y, z)

# P4
#del(a,c)
print(b)
print(a,c)
c += 31.1

# P5
imie          = "James"
nazwisko      = "Spring"
rok_urodzenia = "21.04.1987"
stanowisko    = "dev"
placa         = 4500
wiek          = 35

print (imie)
print (nazwisko)
print (rok_urodzenia)
print (stanowisko)
print (placa)

# P6
PI = 3.14
# r = int(input("podaj promień koła: "))
r = 100
obwod = 2 * PI * r
pole = PI*r**2
print(obwod)
print(pole)

# P6b
a = 15
b = 80
print( 2*a + 2*b)

# P7b
spala = 8
km = 382
print(km / 100 * spala)

# P7c
a = 2
b = (2 * a) + 2
c = (2 * b) + 2
d = (2 * c) + 2
e = (2 * d) + 2
x = (2 * e) + 2
y = (2 * x) + 2
z = (2 * y) + 2
print(a, b, c, d, e, x, y, z)

# P7d
kol_il = 2
kol_cz = 5
cza_il = 8
cza_cz = 2
print(45 *  kol_il / kol_cz  + 45 * cza_il  / cza_cz )

### Podstawowe typy zmiennych
print("# Podstawowe typy zmiennych")
a = 1
b = 2.1
c = 'tekst'
print(type(a))
print(type(b))
print(type(c))

a = 1e+3
print(a)
print(3.0/2.0)
print(3.0//2.0)
print(round(1.314313, 2))
print(round(1.4))
print(round(1.5))
print(round(1.6))
print(int(1.6))

# P8
print(type(wiek))
print(type(imie))

# P9
wiek = str(wiek)
print("wiek ", type(wiek))
print(wiek)
#imie = int(imie)
print("imie ", imie)

# P10
brutto = 1000
vat_1 = 3
vat_2 = 7
vat_3 = 23
print("netto vat_1 ", round(brutto / (1 + vat_1/100), 2))
print("netto vat_2 ", round(brutto / (1 + vat_2/100), 2))
print("netto vat_3 ", round(brutto / (1 + vat_3/100), 2))

# P11
chleb    = 1.99
mleko    = 2.50
cukierki = 12.99

chlebKoszt    = 2 * chleb
mlekoKoszt    = mleko * 0.5
cukierkiKoszt = (cukierki * 300) / 1000

zamowienie = chlebKoszt + mlekoKoszt + cukierkiKoszt
print (round(zamowienie, 2))

# Systemy liczbowe
a = 0o11  # system osemkowy
print (a) # 9
a = 0x100
print (a) # system szesnastkowy

# Zmienne logiczne
a = True
b = False

if 1<2:
    print ("ok1")

if "":
    print ("ok2")

print (bool(0))
print (bool(1))
print (bool('a'))

print ("text " * 10)
print ("str" + " " + "text " + str(1))

if 1<3 or 1>2:
    print ("ok")

if 1<3 and 1>2:
    print ("ok2")

print ("log")
print ('a' and 'b')
print ('a' or 'b')

a = '3'
b = int(a)
d = float(a)
print(type(a))
print(type(b))
print(type(d))

# P16
a = 7
a = bool(a)
print(type(a))
print((a))

# P18
a = 'tekst'
a  = 3 * a
print(a)


###
print ("text\\ntext\\ntext")
print (r"text\ntext\ntext")
print ("text\ntext\ntext")

""" 
h = float(input("podaj h "))
p = float(input("podaj p "))
print ((h * p)/2)
"""

print('Junaid' + '\n' + 'Effendi')

# P22
imie = 'Andrij'
nazwisko = 'Roman'
wiek = 33
pensja = 11000
stanowisko = 'młodszy inżynier procesu'
print(imie, nazwisko, '(wiek:', wiek, 'lat) pracuję na stanowisku', stanowisko, '(pensja:', pensja, 'brutto).')

# P 22a
dochod = 700
koszt = 500
przyrost =1.5

print(  round(dochod - koszt, 2))
dochod = dochod * przyrost
print(  round(dochod - koszt, 2))
dochod = dochod * przyrost
print(  round(dochod - koszt, 2))
dochod = dochod * przyrost
print(  round(dochod - koszt, 2))
dochod = dochod * przyrost
print(  round(dochod - koszt, 2))
dochod = dochod * przyrost
print(  round(dochod - koszt, 2))


dochod = 700
koszt = 500
przyrost =1.5
miesiac = [1,2,3,4,5]
for i in miesiac:
    dochod = dochod * przyrost
    print( dochod - koszt)


# Operatory
print("# Operatory")

bok_kw = 2
bok_tr_1 = 3
bok_tr_2 = 4
bok_tr_3 = 6
r = 3
print("pole kwadrata ", bok_kw ** 2)
print("obwód trójkonta ", bok_tr_1  + bok_tr_2 + bok_tr_3)
print("pole kołą ", 3.14 * r ** 2)


# P25
wynagr_net = 5500
czas = 168
print("stawka godzinowa netto:", round(wynagr_net / czas ,2))
print("stawka godzinowa brutoo:", round(wynagr_net / czas * 1.23,2))

# Operatory logiczne
print("# Operatory logiczne")

print('0, "''", [], (), {} i None są fałszem w kontekście logicznym, natomiast wszystko inne jest prawdą.')

print("and zwraca ostatnią prawdziwą wartość", "a" and "b" and 'c')
print("Jeśli jakaś wartość jest fałszywa  and zwraca pierwszą fałszywą wartość.", "" and "b")

print("or zwraca pierwszą prawdziwą wartość","a" or "b" or 'c')
print("Jeśli jakaś wartość jest fałszywa  or zwraca pierwszą prawdziwą wartość.","" or "b" or 'c' or 'd')
print("Jeśli wszystkie wartości sąfałszem, OR zwraca ostatniąwartość.","" or  '' or {} or 0 or ())

# P27
# bramki logiczne
print ("# Bramki logiczne")
a = bool(0)
b = bool(0)
c = bool(1)

w1 = (not a) and (not b) and (not c)
w2 = (not a) and (not b) and c
w3 = (not a) and b and (not c)
w4 = a and (not b) and (not c)
print (w1 or w2 or w3 or w4)

print('Hello \\')
print('Hello \' ')
print('Hello \" ')
print('Hello \n'*3)
print('Hello \t'*3)

# P35
#imie = input("Podaj swoję imię: ")
#print(imie, ", witaj w kursię Python")

# P36
#napis = input('Podaj napis: ')
#print(30 * (napis + '\n'))

# P37
""" 
h = float(input('podaj wysokość trójkąta h: '))
a = float(input('podaj podstawe trójkąta a: '))
print('Pole trójkąta', h * a / 2)
"""

# Typy sekwencyjne
print('# Typy sekwencyjne')


text = "string"
print (text[0]) # operator indeksowania []

#strings are immutable! ciagi tekstowe sa niemodyfikowalne!!!
#text[0] = 'b'

text = "hello world"
print (text.capitalize())
print (text.upper())
a = text.upper()
b = text.split(" ")
print (b)


############################################
# Tuple (krotka)
############################################
# nie możemy zmieniać wartości elementów krotki

print("# Tuple (krotka)")
a = "sample text"
print (a[0])

# for each
for letter in a:
    print (letter)

a = 1,2,3,4,5,6
b = (1,2,3,4,5,6)
for i in a:
    print(i)


names = ('Andrij', "Agni", 'Człowiek')
for name in names:
    print(name)

for i in range(3):
    print(names[i])

# krotka ma różne wartości pod jedną zmienną lub to się nazywa tablicami
a = (1,2,3,'a','b','c')
print (type(a))
print (a[5]) #c
print (a)


# tuple is immutable!!! Krotki  są niezmienne
# a[0] = 0
#names.append(12.23)


############################################
# List (lista)
############################################
# Wartości elementów listy mogą być zmieniane
# Element listy możemy też przypisać do innej zmiennej

print("# List (lista)")
a = [1,2,3,'a','b','c']
print (type(a))

print (a[5]) #c

for elem in a:
    print (elem)

# aktulizowanie elementu pod indeksem 0
a[0] = 0
print (a)


a.append('y') # dodaje element x na koniec listy
a.insert(0,'x') # dodaje do listy element x w miejsce o indeksie i
a.remove('x') # usuwa z listy pierwszy napotkany element x. Jeśli na liście nie ma elementu o wartosści x, Sage wyświetli błąd.
a.pop(0) #- usuwa z listy element o indeksie i, jednocześnie zmniejszając rozmiar tablicy o 1.
       # Jeśli wywołamy pop() bez podawania wartości i, usuniemy ostatni element listy.

print(a.count('c')) # zwraca liczbę wystąpień x na liście
print (a)
a.insert(0, 9)
print (a)

# pełęn wykaz funckji dla tego objektu
#print dir(a)

print('# len')
print (len(a)) # zwraca liczbę elementów listy

x        = [1,2,3,4,5,6,7,8,9,10]
new_list = []
for item in x:
    if item > 3:
        new_list.append(item)
print (new_list)

even_list = []
for item in x:
    if item % 2 == 0:
        even_list.append(item)
print (even_list)

n_list = []
for item in range(50):
    if item % 2 == 0:
        n_list.append(item)
print(n_list, '\n')
#4 % 2 == 0 => liczba jest parzysta, sprawdzamy reszte z dzielenia

new_list = []
for item in x:
    new_list.append(item * 2)
print (new_list)

# comprehension list => skladanie list
print ([elem * 2 for elem in x])

# slices (wycinki, dzialaja na elementach ktore ss indeksowalne)
print (x[0])        # 1
print (x[6])        # 7
print (x[len(x)-1]) # last element
print (x[-1])       # last element
print (x[0:6:1])    # < ) od zera do 6 bez 6 elementu
print (x[0:6:2])
print (x[0:6]) #krok domyslny to 1
print (x[-1:-5:-1]) #< )

a = [1,2,3]
del a[2] #2 to index elementu
print (a)
print ("log")


############################################
# Set (zbior)
############################################
# nie możemy zmieniać wartości elementów zbioru ??? sprawdzić
print('# Set zbiory')
a = "sample text"
b = [1,2,3,1,1,2] # lista
c = (1,2,1,2,1) # krotka
d = {1,2,3,4,5} # zbiór
numbers = {'a':1,'b':2,'c':3} # Słownik

a_set = set(a)
b_set = set(b)
c_set = set(c)


print (a_set)
print (b_set)
print (c_set)
print (type(a_set))
print(type(d))
#
a = 177
str_a = str(a)

print (str_a[0]) #1
print (str_a[1]) #7
print (str_a[2]) #7

print (len(set(str_a)))

#blad!
#print (a_set[0])

a = "sample text"
a_set = set(a)
for item in a_set:
    print (item)

print ('m' in a_set)

a_set.add('80')
print (a_set)

a_set.remove('80')
print (a_set)

a = {1,2,3,4,5}
print (type(a))


############################################
# Dictionary (slownik)
############################################
print('# Dictionary (slownik)')

numbers = {
    'a':1,
    'b':2,
    'c':3
}

print (numbers['a'])
print (numbers['b'])
print (numbers['c'])

print (numbers.keys())
print (numbers.values())
print (numbers.items())

dictionary = dict()
print (type(dictionary))

print ([1,2,3] * 3)
t = [1,2]
t += [1,2,3]
print (t)

x = [1,2] + [3,4]
print(x)

print (2 in [1,2,3])

combo = [ [], [] ]
combo[0].append(1)
combo[0].append(2)
combo[0].append(3)
combo[1].append("Tom")
combo[1].append("James")
combo[1].append("Alice")
print (combo)

drugie_imie = combo[1][1]
print(drugie_imie)


a = ["art 1", "art 2", "art 3", "art 4", "art 5"]
print (a[0] + " " + a[-1])
lst =  a[0:5:4]
print(lst)

result = ""
for elem in lst:
    result = result + elem
print (result)

print (" ".join(lst))

a = (1,2,3)
print (a * 3)

a = ('1', '2','1977')
print ("data waznosci artykulu to " + a[0] + "-" + a[1] + "-" + a[2])

combo = (('1', '2','1977'), ('4', '2','1977'), ('6', '2','1977'))

print ("data waznosci artykulu to " + combo[0][0] + "-" + combo[0][1] + "-" +combo[0][2])

################################

a = "sample textt"

letters = dict()
for letter in a:
    if letter in letters.keys():
        letters[letter] += 1
    else:
        letters[letter] = 1
print (letters)

##############################
even_list = []
for x in [1,2,3,4,5,6,7,8,9,10]:
    for y in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        #print (x*y, end="\t")
        if (x*y) % 2 == 0:
            even_list.append(x * y)
    #print (even_list)
print (len(even_list))
print (len(set(even_list)))
print (set(even_list))

##############################
cars = ['bmw', 'toyota', 'seat']
#[3,6,4]
cars_len = []
for item in cars:
    cars_len.append(len(item))
print (cars_len)

a = [len(item) for item in cars]
print (a)

##############################
a = [1,2,3,4,5] #silnia  = 120

result = 1
for elem in a:
    result = result * elem
print (result)

result = "sample text"
print (result[::-1])
print (result[::])

lst = (1,2,3)
a   = set()

a.add(lst)

a = [1,2,3,4,5,1]
b = frozenset(a)

#frozenset is immutable!
#b.add(1)

















