# P76
# Napisz program, który wypisze w podanej przez użytkownika ścieżce:
# Zawartość katalogu
# Informację o rozmiarze plików
# Informacje o dacie ostatniej modyfikacji plików
# Informację jeśli ścieżka jest nieprawidłowa

from os import *
from time import ctime

# nameDir = getcwd()
# print(listdir(nameDir))
nameDir = input("Podaj ścieżkę katalogu: ")
nameDir.replace("\\", "\\\\")
try:
    print("%25s | %25s |%25s |%25s |" % ("Nazwa Pliku", "Rozmiar Pliku", "Data Utworzenia", "Data Modyfikacja"))
    for file in sorted(listdir(nameDir)):
        print("%25s | %25s |%25s |%25s |" % (file, path.getsize(file), ctime(path.getctime(file)), ctime(path.getmtime(file))))
except:
    print("ścieżka jest nieprawidłowa")