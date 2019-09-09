from os import listdir, path, chdir


class FileOperation:
    def __init__(self):
        self.direct_path = input("wprowadź adres bezpośredni (np. 'C:\\xxx' aktualna lokalizacja .): ")
        self.direct_path = self.direct_path.replace("\\","\\\\")
        chdir(self.direct_path)
        self.getDirectoryContent()

    def getDirectoryContent(self):
        print("| %30s | %10s | %20s | %20s |" % ("FILENAME", "SIZE", "CREATED TIME", "MODIFIED TIME"))
        for content in listdir("."):
            print("| %30s | %10.2f | %20s | %20s |"
                  % (content,
                     path.getsize(content)/(10**6),
                     path.getctime(content),
                     path.getmtime(content)))
FileOperation()