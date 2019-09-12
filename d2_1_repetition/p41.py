# Utwórz pusty słownik i dodaj do niego pary klucz-wartość: nazwa, ilość, cena_brutto, cena_netto.
# Przypisz dowolne wartości do podanych kluczy i oblicz w ten sposób koszt brutto i netto sześciu jednostek danego produktu.

# P41
slownik = dict()
slownik = {"produkt1": [2, 115, 115*1.23]}
slownik["produkt2"] = [2, 115, 115*1.23]
slownik["produkt2"] = [10, 300, 300*1.23]
print(slownik)
print(slownik["produkt1"][1])
ilesztuk = 6
print("Produkt",   "Wartość netto",  round(ilesztuk * slownik["produkt1"][1]), "Wartość brutto", round(ilesztuk * slownik["produkt1"][2]))