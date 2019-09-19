# one line comment

"""
    multiline comments
"""

############################################
# data types (typy danych)
############################################

# dynamic typing (dynamiczne typowanie)

a = 1
print (type(a))
a = '1'
print (type(a))
a = 1.0
print (type(a))

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

print (zmienna_1)
print (zmienna_2)
print (zmienna_3)
print (zmienna_4)
print (zmienna_5)

print (zmienna_1, zmienna_2, zmienna_3, zmienna_4, zmienna_5)

a = 1
b = 2

tmp = a
a   = b
b   = tmp

print ((a)) # 2
print ((b)) # 1

c = 1
d = 2

# pattern matching
c,d = d,c

print (c)
print (d)

print (2-1)
print ("2-1")

a = 10
a = a + 5
a += 5 # a = a + 5
print (a)

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

r  = 100
PI = 3.14

print (PI * (r **2))
print (PI * 2 * r)

a = input("podaj liczbe a")
b = input("podaj liczbe b")

print (a * 2 + 2 * b)

spalanie = 8.0
km       = 382

a = 2
b = (2 * a) + 2
c = (2 * b) + 2

czas = 45

# drukarka kolorowa
print ((2*czas)/5)

# drukarka czarno biala
print  ((czas * 8)/2)

print ((km * 8) / 100)

a = None

print (round(3.14159, 2))

a = '1'
b = 10

print (type(int(a)))
print (type(str(b)))

brutto = 1000
vat    = 23.0/100
print (vat)

print ("netto ", round(brutto - (brutto/(vat + 1))  * vat,2))

chleb    = 1.99
mleko    = 2.50
cukierki = 12.99

chlebKoszt    = 2 * chleb
mlekoKoszt    = mleko * 0.5
cukierkiKoszt = (cukierki * 300) / 1000

zamowienie = chlebKoszt + mlekoKoszt + cukierkiKoszt
print (round(zamowienie, 2))

a = 0o11  # system osemkowy
print (a) # 9
a = 0x100
print (a) # system szesnastkowy

a = True
b = False

if 1<2:
    print ("ok1")

if "":
    print ("ok2")

print (bool(0))

print ("text" * 10)
print ("str" + " " + "text" + str(1))

kwota_netto  = round(5500/168, 2)
kwota_brutto = round(5500/168 * 1.23,2)

if 1<3 or 1>2:
    print ("ok")

print ("log")
print ('a' and 'b')

a = bool(0)
b = bool(0)
c = bool(1)

w1 = (not a) and (not b) and (not c)
w2 = (not a) and (not b) and c
w3 = (not a) and b and (not c)
w4 = a and (not b) and (not c)

print (w1 or w2 or w3 or w4)

print ("text\\ntext\\ntext")
print (r"text\ntext\ntext")

# napis = input("podaj napis")
# print (30 * (napis + '\n'))

h = float(input("podaj h"))
p = float(input("podaj p"))

print ((h * p)/2)

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
print()
############################################
# Tuple (krotka)
############################################

a = "sample text"
print (a[0])

# for each
for letter in a:
    print (letter)

a = (1,2,3,'a','b','c')
print (type(a))
print (a[5]) #c
print (a)

# for each
for elem in a:
    print (elem)

a = 1,2,3,'a','b','c'
print (type(a))

# tuple is immutable!!!
# a[0] = 0

############################################
# List (lista)
############################################

a = [1,2,3,'a','b','c']
print (type(a))

print (a[5]) #c

for elem in a:
    print (elem)

# aktulizowanie elementu pod indeksem 0
a[0] = 0
print (a)

a.append('d')
print (a)
a.insert(0, -1) # 0 to jest index, -1 to wartosc elementu
print (a)

#print dir(a)

print (len(a))

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

a = "sample text"
b = [1,2,3,1,1,2]
c = (1,2,1,2,1)

a_set = set(a)
b_set = set(b)
c_set = set(c)

print (a_set)
print (b_set)
print (c_set)
print (type(a_set))
#
a = 177
str_a = str(a)

print (str_a[0]) #1
print (str_a[1]) #7
print (str_a[2]) #7

print (len(set(str_a)))

#blad!
#print a_set[0]

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

a = ["art 1", "art 2", "art 3", "art 4", "art 5"]
print (a[0] + " " + a[-1])
lst =  a[0:5:4]

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

a = "sample text"

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
    print ("\n")
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
