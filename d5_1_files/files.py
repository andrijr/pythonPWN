

file3 = open("file3.txt", "w", encoding="UTF-8")
file3.write("Pierwsza linia\n")
file3.write("Druga linia\n")
file3.writelines("jeden\ndwa\ntrzy\n")
print(file3.name, file3.mode,  file3.closed)
file3.close()

print(file3.name, file3.mode,  file3.closed)
file3 = open("file3.txt", "a+")
file3.write("Dodano linie z atrybutem 'a' ")
file3.close()

fileReader = open("file3.txt", "r" )
print(fileReader.read())
fileReader.close()

fileReader = open("file3.txt", "r" )
print(fileReader.readline(5))
print(fileReader.read(5))
print(fileReader.readline(5))
fileReader.seek(1)
print(fileReader.read(5))
print(fileReader.tell())
fileReader.close()
