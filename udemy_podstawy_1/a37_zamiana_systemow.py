# zamiana liczb 2 w 10      5 = 101  5//2 = 2 5%2 = 1 ; 2//2 = 1 2%2 = 0 ; 1//2 = 0 1%2=1
# zamiana liczb 10 w 10     1111  =  1*8   + 1*4+  1*2 + 1*1 = 15

def naDziesiatny(n):
    potenga = 1
    wynik = 0
    while n > 0:
        wynik += (n % 10) * potenga
        potenga *= 2
        n //= 10
    return wynik

def naDwojkowy(n):
    lista = []
    while n >0:
        lista.append(n%2)
        n //=2
    lista.reverse()
    wynik = 0
    for element in lista:
        wynik += element
        wynik *= 10
    wynik //=10
    return wynik

print(naDziesiatny(1111))
print(naDwojkowy(15))



print()

n = 487
while n >0 :
    wynik = n % 10
    n //= 10
    print("//10" ,n, "    n % 10", wynik)
print()


n = 1
x = 2
print( n/x, n//x,n%x)

n = 17
lista = []
while n >0:
    lista.append(n%2)
    n //= 2
    print(lista, n)