# P76
# Napisz program, który wypisze w podanej przez użytkownika ścieżce:
# Zawartość katalogu
# Informację o rozmiarze plików
# Informacje o dacie ostatniej modyfikacji plików
# Informację jeśli ścieżka jest nieprawidłowa

from os import *

sciezka = input("Podaj ścieżkę: ")

print(listdir("."))

