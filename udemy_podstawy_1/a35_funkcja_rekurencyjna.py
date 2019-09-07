def silnia(n: int):
    wynik = 1
    for i in range(1,n+1):
        wynik *= i
    return  wynik

def silniaRecurencyjnie(n: int):
    if n == 1:
        return 1
    else:
        return n * silniaRecurencyjnie(n-1)


def silniaRecurencyjnie(n: int):
    print("Funkcja została wywołana dla n równegoe: ", n)
    if n == 1:
        return 1
    else:
        temp = n * silniaRecurencyjnie(n-1)
        print("Wynik dla ", n, "silnia(", n -1, ") to: ", temp)
        return temp

print(silnia(4))
print(silniaRecurencyjnie(4))

