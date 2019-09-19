from os import *
from time import ctime

print(getcwd())
print(listdir('.'))
print(listdir("C:\\Users\\AUM\\PycharmProjects\\pythonPWN\\d5_1_files"))
for file in sorted(listdir('.')):
    print(file)

chdir("p75")
print(getcwd())
chdir("C:\\Users\\AUM\\PycharmProjects\\pythonPWN")
print(getcwd())
chdir("d5_1_files")
print(getcwd())

mkdir("test")
rmdir("test")
# remove("file3_copy.txt")
# rename("files_directory.py", "files.py")
print(path.isdir('.'))
print(path.isdir("C:\\Users\\AUM\\PycharmProjects\\pythonPWN\\d5_1_files"))
print(path.isdir("p76"))
print(path.isfile("file3.txt"))
print(path.isfile("directory.py"))
print(path.ismount("C:"))
print(path.getsize("file3.txt"))
print(ctime(path.getctime("file3.txt")))
print(ctime(path.getmtime("file3.txt")))
print(ctime(path.getatime("file3.txt")))

