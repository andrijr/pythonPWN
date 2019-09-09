i = 3
if i > 0:
    print(i)

for i in range(0, 10000):
    if i % 17 == 0:
        if i % 2 ==0:
            if i % 3 ==0:
                if i % 10 ==0:
                    print(i)


for x in range(1,11):
    for y in range(1,11):
        if len(str(x*y)) < 2:
            print(x * y, end="   ")
        elif len(str(x*y)) < 4:
            print(x * y, end="  ")
        else:
            print(x* y, end="  ")
        #print("%i " " " % (x*y))
    print()

for x in range(1,11):
    for y in range(1,11):
            print("{:3}".format(x * y), end=" ")

    print()