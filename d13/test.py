import random

name = [ 'Ola', 'Piotr',  'Zaneta',  'Tomek',   'Angelika',  'Michal',  'Igor', 'Andrij', 'Filip'  ]
print(name)

zbior = set()
for x in range(1,100):
    if len(zbior) < 10:
        zbior.add(random.choice(name))
    else:
        break
print(zbior)

slownik = dict()
for i, x in enumerate(zbior, start=1):
    if i % 3 == 0:
        lider = str(i) + 'L'
        print(lider, x)
    elif i % 3 != 0:
        print(i, x)
