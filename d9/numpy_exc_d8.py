import numpy as np


tab = np.arange(1,16.0)
print(tab)
tab = np.arange(15).reshape(3,5)
print(tab)

# wyciągnąć z tab tablicę [10 , 11, 12, 14] i póznije samą liczbę 8

# print(tab[2])
# print(tab[1][3])

# sprawdzić wymiar, size, typ objektu i typ danych
print(tab.size)
print(type(tab))
print(tab.dtype)

# liczby urojone
c = np.array([[1,2],[3,4]], dtype=complex)
# print(c)

import numpy as np


a1 = np.zeros(10)
print(a1)

a2 = np.ones(10)
print(a2)

a3 = np.ones(10) * 5
print(a3)

a4 = np.arange(10, 51)
print(a4)

a5 = np.arange(10, 51, 2)
print(a5)


