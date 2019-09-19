a = "sample text"
b = [1,2,3,1,1,2] # lista
c = (1,2,1,2,1) # krotka
d = {1,2,3,4,5} # zbiór
e = {'a':1,'b':2,'c':3} # Słownik
print()

############ Napisy
print("# napisy = Tekst")
a_tekst = "tekst"
print(a_tekst.capitalize())
print(a_tekst)
print(a_tekst[1])
print ('a' and 'b', "'a' and 'b‘# 'b'")
print ('a' or 'b'," 'a' or 'b' #'a'")
print()


############# Krotka Tuple
# krotka nie jest modyfikowalna nie możemy modyfikować i usuwać elementów krotek
print("# Krotka  Tuple = () ")
a_tuple = (0, 1,2,3,4, 5, 6, 7, 8, 9, 10)
print(a_tuple)
print()


############## Listy
print("# Lista = [] ")
a_list = [0, 1,2,3,4, 5, 6, 7, 8, 9, 10]

a_list.append(6)
a_list.append(6)
print(a_list, "a_list.append(6) dodaje element x na koniec listy")
a_list.remove(6)
print(a_list, "a_list.remove(6) odnajduje pierwszy napotkany x i usuwa go z listy ")
a_list.insert(0,'x')
print(a_list, "a_list.insert(0,'x') dodaje do listy element x w miejsce o indeksie i")
a_list.pop(0)
print(a_list, "a_list.pop(0) zwraca i-ty element i usuwa go z listy.")

print(a_list[0])
print(a_list[0:5:1], "List[indeksStart : indeksStop]")
print(a_list[:5], "List[indeksStart : indeksStop]")
print(a_list[::3], "List[indeksStart :: wielokrotność]")
print(a_list[1::3], "List[indeksStart :: wielokrotność]")

print(9 in a_list )
print(9 not in a_list )

for elem in a_tekst:
    print (elem)
    print (a_tekst)

for i in range(3):
    print("a_tekst\t")


print([a_tekst for i in a_tekst])
print()
print(a_tekst, end=' ')

############### Set zbiory = {1,2,3,4,5}'
# Zbiory zmienne nie mogą być ani kluczami w słownikach ani elementami innych zbiorów.
print('# Set zbiory = {1,2,3,4,5}')

a_set = {1, 2, 3,4,5,6,7,8,9,10}
a_set = frozenset(a_list)
a_set = set(a_list) # Nowy zbiór tworzymy używając słowa kluczowego set()


a_set.add('80')
a_set.add('99')
print (a_set, "a_set.add('80') dodanie do zbioru")

a_set.discard('99')
print (a_set, "a_set.discard('99') usunięcie z zbioru")

a_set.remove('80')
print (a_set,  "a_set.remove('80') usunięcie z  zbioru")


x = [1,2] + [3,4]
print(x)

print (2 in [1,2,3])
a_set = a_set ^ a_set
print(a_set)
print()


############## Dictionary (slownik)
print('# Dictionary (slownik)')

a_dict = { 'a':1,'b':2, 'c':3 , 'd':4}
# Dodawanie klucza i wartości do słownika
a_dict["e"] = 5
print(len(a_dict))
print (a_dict.keys())
print (a_dict.values())
print (a_dict.items())

print (a_dict['a'])

a_dict.pop("c")
print (a_dict,  "a_dict.pop('c') Odczytuje i usuwa wartość ze słownika")

a_dict.popitem()
print (a_dict,  "a_dict.popitem()  Odczytuje i usuwa ostatnią wartość ze słownika")

a_dict.clear()
print (a_dict,  "a_dict.clear() Czyści cały słownik")
a_dict = { 'a':1,'b':2, 'c':3 , 'd':4}

a_dict2 = a_dict
a_dict2 = a_dict.copy() # Nadpisuje całą zawartość Slownik2 do Slownik1
a_dict2.update(a_dict) #Aktualizuje Slownik1 w oparciu o Slownik2
print(a_dict2,  "a_dict2")




'a' in a_dict.keys() #Sprawdza występowanie określonego klucza w słowniku

a_set = set(a_list)
a_list = list(a_set)
a_tuple = tuple(a_list)

print(" %2i %5.2f %d %e %s %c" % (11, 1, 1.01, 100, 'A', 'A'))


#################################
tekst = "tekst1 tekst2"
lista = list(tekst)
print(lista)
lista = tekst.split()
print(lista)
lista = sorted(lista, reverse = True)
print(lista)
lista.sort()
print(lista)
tekst.count('t')
print(tekst.count(""))


zbior = set([1,2,3])
tekst = str(zbior) + "}" +'3'
print(tekst)
zbior = set(tekst)
print(zbior)
sorted(zbior)
print(sorted(zbior, reverse = False))
print()

slownik = {1 : 'wartość1', 2 : 'wartośćN'}
print(slownik[1])
slownik[1] = 'wartość2'
print(slownik[1])
slownik2 = slownik.copy()
print(slownik)
print(slownik2)
print()
slownik[3] = "wartość3"
slownik[2] = "wartość2"
print(slownik)
print(slownik2)
print()
slownik2.update(slownik)
print(slownik2)
slownik2.update(slownik)
print(slownik2)
