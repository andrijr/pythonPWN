
def get_list(tab=[1, 2, 3]):
    return tab


lst = get_list()
print(lst)
lst.append([1, 2])
print(lst)
lst = get_list()
print(lst)
lst = get_list()
print(lst)


def is_int(number):
    try:
        int(number)
        return True
    except ValueError:
        return False


tab = [1, 2, 4, 15, 210, 1000, 10, '10', '13.']
list_comp = [int(number) for number in tab if is_int(number) and int(number) < 200]
print(list_comp)