slownik = {}
print(slownik)
slownik = dict()
print(slownik)
slownik = {"a": 1, "b": 2, "c": 3}
print(slownik)
print(slownik['a'])
print(slownik.keys())
print(slownik.values())
print(slownik.items())

# klucz-vartość
slownik['a'] = 9
print(slownik)
slownik['d'] = 4
print(slownik)
slownik['d'] = 'e'
print(slownik)
slownik = list(slownik)
print(slownik)
slownik = dict(slownik)
print(slownik)