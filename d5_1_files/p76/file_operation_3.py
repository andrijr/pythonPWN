# P76
# Napisz program, który wypisze w podanej przez użytkownika ścieżce:
# Zawartość katalogu
# Informację o rozmiarze plików
# Informacje o dacie ostatniej modyfikacji plików
# Informację jeśli ścieżka jest nieprawidłowa
from os import *
from time import ctime
class InformationDirectory:
    def __init__(self):
        self.nameDir = input("Podaj ścieżkę katalogu: C://Users//AUM//PycharmProjects//pythonPWN// : ")
        self.nameDir.replace("\\", "\\\\")
        try:
            chdir(self.nameDir)
            self.getDirectoryContent()
        except:
            print("Błedna ścieżka katalogu\n")
    def getDirectoryContent(self):
        print("%25s | %18s | %25s | %25s " % ("Nazwa Pliku","Rozmiar pliku MB", "Data utworzenia", "Data modyfikacji"))
        for file in sorted(listdir('.')):
            print("%25s | %18s | %25s | %25s " % (file, path.getsize(file)/10**6, ctime(path.getctime(file)), ctime(path.getmtime(file))))

InformationDirectory()

