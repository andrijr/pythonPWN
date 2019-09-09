def dodawaniie(a = 0 , b = 0, c =0):
    print("suma równa jest", a + b + c)
    return a + b+c


dodawaniie(5)

def mnożenie(a: float , b: float, c:float):
    print("mnożenie równe jest", a * b * c)
    return a * b * c

mnożenie(5,5, 5)


# tworzymy listę gdzie dla każdego argumentu zostanie wywołąne przeksztalcenie na liczbę float
# zamien na liczbę float każdego x który jest wstawiony przez urzytkownika w tekscie podzielony spacjami

x, y, z = [float(x) for x in input("Podaj trzy liczby: ").split()]

mnożenie(x,y,z)