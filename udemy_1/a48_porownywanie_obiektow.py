from Cat import Cat

kot1 = Cat("Rudy", 3, "bialy")
kot2 = Cat("Rudy", 3, "bialy")
kot3 = Cat("Smialek", 2, "czarny")

print(kot1 == kot2)
print(kot1 == kot3)
print(kot2 == kot3)
kot4 = kot1
print(kot1 == kot4)