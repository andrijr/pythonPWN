# P52

# Wygeneruj tabliczkę Wygenerujmnożenia 10x10.10

for x in range(1,11):
    for y in range(1,11):
        print("%3i " % (x*y), end=" ")
    print()
print()

for x in range(1,11):
    for y in range(1,11):
        print("{:3}".format(x*y), end=" ")
    print()