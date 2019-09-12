# Napisz program zliczający liczbę wartości unikatowych wprowadzonych przez użytkownika

# P44
slowo = input("Pdaj co kolwiek: ")
zbior = set(slowo)
print(sorted(zbior))

for index, element in enumerate(sorted(zbior)):
    print(element + ":=", index,  end=" ")

