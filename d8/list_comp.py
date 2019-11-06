import random

tan = [1,2,3]
numbers = []
for c in range(100):
    if c % 2:
        numbers.append(random.randint(1,c))
print(numbers)

numbers = [x for x in range(100)]
print(numbers)

numbers = [random.randint(1,100) for x in range(100)]
numbers = [random.randint(1, x) for x in range(100) if x % 2]
numbers_2 = [random.randint(1, x) if x % 2 else None for x in range(100)]
print(numbers)

# przepisac na zwyklego fora
numbers = []
for x in range(100):
    if x % 2:
        numbers.append(random.randint(1, x))
    else:
        numbers.append(None)
print(numbers)

# napisac list comprehension które wybierze liczby podzielne przez 3 z numbers
number_3 = []
numbers_3 = [x for x in range(100) if x % 3 == 0]
print(numbers_3)

data = [
    ('Jan', 'Kowalski', 124023, 123),
    ('Adam', 'Kowalski', 123023, 10),
    ('Anna', 'Aniol', 124033, 10.57),
    ('Janusz', 'Nowak', 124053, 2.45),
]

# wyciagnac saldo typu decimal, sparametryzowac nazwisko (1, 2, 3 ...),
# trzy pierwsze liczby z numeru indeksu jako tuple

from decimal import Decimal
Decimal('1.0')

# saldo = [saldo for row in data]



new_data = []
names = {x[1] for x in data}
names = {x: n for n, x in enumerate(names)}
for student_data in data:
    balance_formatted = Decimal(student_data[3])
    name_formatted = names[student_data[1]]
    index_formatted = int(str(student_data[2])[:3])
    tuple_formatted = (balance_formatted, name_formatted, index_formatted)
    new_data.append(tuple_formatted)
print(new_data)


new_data = []
names = {x[1] for x in data}
names = {x: n for n, x in enumerate(names)}

new_data_comp = [
    (
        Decimal(student_data[3]),
        names[student_data[1]],
        int(str(student_data[2])[:3])
    )
    for student_data in data
]
print(new_data_comp)




# pobieranie wartosci ze slownika
print(names)
print(names.get('Kowalski2', 'Deafultowa wartosc'))
try:
    print(names['Kowalski2'])
except KeyError:
    print('Nie ma takiego klucza w slowniku')


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car["model"]
print(x)
x = car.get("model")
print(x)