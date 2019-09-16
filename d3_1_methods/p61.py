# P61
# Zdefiniuj funkcję, która dla podanych trzech parametrów:
# n=numer elementu ciągu,
# a1=wartość pierwszego elementu ciągu (domyślnie 1),
# q=wartość iloczynu ciągu geometrycznego (domyślnie 2)
# Zwróci sumę i n-ty element ciągu geometrycznego.

# Zdefiniuj funkcję, która dla podanych trzech parametrów:
a = 2
q = 3
n = 5
def geometric(a, q = 3, n = 5):
    an = a * q **(n-1)
    sum = 0
    for i in range(1, n+1):
        sum += a * q ** (i-1)
    return (an, sum)

print(geometric(a,q, n))


def geometric(a, q = 3, n = 5):
    an = a * q **(n-1)
    sum = 0
    for i in range(0, n):
        sum += a * q ** (i)
    return (an, sum)

print(geometric(a,q, n))