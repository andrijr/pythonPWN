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

a6 = np.arange(9).reshape(3, 3)
print(a6)

a7 = np.identity(3)
print(a7)

a9 = 2 * np.random.rand(5, 5) - 1
print(a9)

a10 = np.linspace(0, 1, 20)
print(a10)
