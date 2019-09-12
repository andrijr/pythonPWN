# P46

# Utwórz test korzystający z pojedynczej instrukcji if, który sprawdzi, czy podana wartość znajduje się w przedziale od 0 do 9 (włącznie z tymi wartościami).
# Wyświetl komunikat, jeśli wartość znajduje się w zadanym przedziale
# Jeśli wartość nie znajduje się w zadanym przedziale wypisz komunikat: „out of range”


liczba = 10 # int(input("Podaj liczbę: "))
print("Wartość %i znajduę się w zadanym przedziale" % (liczba)) if 0 <= liczba <= 9 else print("wartość %i nie miesci się przedziale" % (liczba) )
print("Wartość %i znajduę się w zadanym przedziale" % (liczba) if 0 <= liczba <= 9 else "wartość %i nie miesci się przedziale" % (liczba) )

