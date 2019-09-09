# utworzenie pliku z uprawnieniami do zapisu
file = open("file1.txt", "w", encoding="UTF-8")
# Szczególy pliku
print(file.name, "Czy zamnknięty", file.closed, file.mode)
# zapis do pliku
file.write("Pierwszy zapis do pliku\n")
file.write("Drugi zapis do pliku\n")
file.writelines(["s1\n", "s2\n", "s2\n", "s2\n"])
file.close()
print(file.name, "Czy zamnknięty", file.closed, file.mode)

fileAppend = open("file2.txt", "a")
fileAppend.writelines(['1', '1','3','4','5','6','7','8','9\n'])
fileAppend.close()

# odczyt pliku
fileReader = open("file2.txt", "r")
print(fileReader.read())
fileReader.close()

fileReader = open("file2.txt", "r")
print(fileReader.tell())
print(fileReader.read(3))
fileReader.close()