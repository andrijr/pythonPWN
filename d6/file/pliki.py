# zapisywanie do pliku
F = open("zwierzeta.txt", 'w+', encoding='UTF-8')

# sprawdzic jaki jest tryb domyslny
for param in ['name', 'mode', 'closed']:
    print(getattr(F, param))
print(getattr(F,'name'))
print(getattr(F,'mode'))
print(getattr(F,'closed'))
print(F.name)
print(F.mode)
print(F.closed)
print()

F.write('Zwierzeta\n')
animals = ['słoń', 'lew', 'pingwin']

F.writelines([animal + '\n' for animal in animals])

# readlines
F = open("zwierzeta.txt", 'r', encoding='UTF-8')
for el in F.readlines():
    print(el)
F.close()