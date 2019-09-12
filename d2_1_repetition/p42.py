# Napisz program, który wyświetli 6 losowych i nie powtarzających się liczb z zakresu od 1 do 49.
from random import *

print(sample(range(1,49), 6))

# print(randint(1, 49))



zbior = set()
for x in range(1,100000000000):
    if len(zbior) < 6:
        zbior.add(randint(1, 49))
    else:
        break
print(zbior)



zbior = set()
while len(zbior) < 6:
    zbior.add(randint(1, 49))
print(zbior)