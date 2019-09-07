a_tekst = "Tekst"
a_list = [1,2,3,4,5,6,7,8,9]

# Instrukcja if-elif i if-elif-else
if a_tekst == "Tekst":
    print(True)
elif len(a_tekst) == 5:
    print(True)
else:
    print(False)

# Wyrażenie trójargumentowe
# [działanie war-tak] if [war] else [działanie war-nie]

print(True if a_tekst == "Tekst" else False)
print(True) if a_tekst == "Tekst" else print(False)

# Pętla while i while-else
while len(a_tekst)  < 4:
    print(True)
else:
    print(False)

# Pętla for-in stosowana do list
for i in a_tekst:
    print(i)

for index, a_tekst in enumerate(a_tekst):
    print(index, a_tekst)

a_set = {"key1": "var1", "key2": "var2", "key3":"var3"}
for key in a_set:
    print(key, a_set[key])

# Formatowanie długości wyjścia z programu
for x in range(5,50,10):
    print("Pierwiastkiem liczby %2i jest %5.3f" % (x, x**0.5))


# break – przerwanie instrukcji
# continue – pomijanie instrukcji

import random
print(random.choice(range(10)))
print(random.sample(range(10),3))

seqString = 'Python'
print(list(reversed(seqString)))