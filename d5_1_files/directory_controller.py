from os import *

print("Directory path:" , getcwd())
print("Zawartość aktualnego katalogu", listdir("."))
print("Zawartość aktualnego katalogu", listdir("C:\\Users\\AUM\\PycharmProjects\\pythonPWN"))

for file in listdir("C:\\Users\\AUM\\PycharmProjects\\pythonPWN"):
    print(file)
# zmiana katalogu
chdir("D:\\00 Analityk Danych\\04 Python\work")
print(listdir("."))
# mkdir("generated from python")
# rmdir("generated from python")
# remove("day1_ar")
for file in listdir("."):
    print("50%s \t %20.2f MB" % (file, path.getsize(file)/100000))