# P62
# Zdefiniuj funkcję, która dla dowolnej liczby parametrów zwróci ich średnią arytmetyczną (lub 0 dla 0 parametrów).
def funkcjaAvg(*n):
    s = 0
    for x in n:
        s += x
    # if n ==0:
    #     return 0
    # else:
    result = s / len(n)
    return result, s

print(funkcjaAvg(0, 2,5))