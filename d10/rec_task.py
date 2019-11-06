# napisac funkcje, ktora z tablicy wybierze wszystkie liczby calkowite, ktore:
# nie sa zerem, nie zawiraja zera z przodu, zawieraja tylko liczby, ....

tab = ['0 12', '12 0', '12.', '12', '2a', '15']


def get_numbers_2(nmumber_list):
    valid_numbers = []
    invalid_numbers = []
    for x in nmumber_list:
        try:
            valid_numbers.append(float(x))
        except ValueError:
            invalid_numbers.append(x)
    return valid_numbers, invalid_numbers


def get_numbers(numbers_list):
    valid_numbers = []
    for x in numbers_list:
        try:
            valid_numbers.append(int(x))
        except ValueError:
            pass
    return valid_numbers


def is_int(number):
    try:
        int(number)
        return True
    except ValueError:
        return False


# napisać funkcje zwracająca liczbę całkowite w list compreh
# print([x for x in range(10)])

list_comp = [int(number) for number in tab if is_int(number) and int(number) < 13]
print('list_comp', list_comp)

integers = get_numbers(tab)
print('<13', [x for x in integers if x < 13])
print('<13', [x if x < 13 else None for x in integers])

print('get_numbers', get_numbers(tab))


# w samolocie chcemt ustalic ile jest mozliwosci posadzenia rodziny trzyosobowej na miejscach znajdujacych sie obok siebie
# schemat samolotu:
#     [A B C    D E F G    H I J]
#     [A B C    D E F G    H I J]
#     [A B C    D E F G    H I J]
#     [A B C    D E F G    H I J]
# dodac parametr dlugosci samolotu (ilosci rzedow)
tab =  [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
]
# result = 6

# result = 6for

# [A x x   x x x G  H I J]
# [A B C   D E F G  H I J]
# [A B C   D E F G  H I J]
# [A B C   D E F G  H I J]
