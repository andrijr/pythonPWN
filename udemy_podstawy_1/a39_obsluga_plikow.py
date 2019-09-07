
file = open("plik_przykladowy.txt", "w+", encoding="UTF-8")
file.write("Przykładowy plik \ndruga linia\ntrezecia linia\n" )
file.close()

file = open("plik_przykladowy.txt", "r", encoding="UTF-8")
print(file.read())
# print(file.readline())
# print(file.readlines())
print()
file.close()

file = open("plik_przykladowy.txt", "r", encoding="UTF-8")
numberOfLine =1
for line in file:
    print(str(numberOfLine) + ": " + line, end="")
    numberOfLine += 1
print()
file.close()

file = open("plik_przykladowy.txt", "r", encoding="UTF-8")
numberOfLine =1
texstToWrite = ""
for line in file:
    texstToWrite += str(numberOfLine) + " : " + line
    numberOfLine += 1
print(texstToWrite)
file.close()

file = open("plik_przykladowy.txt", "w", encoding="UTF-8")
file.write(texstToWrite)
file.close()

file = open("plik_przykladowy.txt", "a", encoding="UTF-8")
file.write(texstToWrite)
file.close()

file = open("plik_przykladowy.txt", "a+", encoding="UTF-8")
file.write("\nKoniec")
file.close()