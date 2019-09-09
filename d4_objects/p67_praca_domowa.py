class Users:
    def __init__(self,  name, lastname, index):
        self.name = name
        self.lastname = lastname
        self.index = index
        self.permissionSelect = True
    def __str__(self):
        return "Imię: %-15s Nazwisko: %-15s Indeks: %-15s PERMISSIONS: %s" % \
               (self.name, self.lastname, self.index, " SELECT" if self.permissionSelect else '')
    def readUsers(self):
        if (self.permissionSelect):
            return "READING..."
class Sercretariat(Users):
    def __init__(self,  name, lastname, index):
        super().__init__(name, lastname, index)
        self.permissionInsert = True
        self.permissionUpdate = True
        self.permissionDelete = True
    def __str__(self):
        return super().__str__() + \
               (" INSERT" if self.permissionInsert else '' + " UPDATE" if self.permissionUpdate else '' + " DELETE" if self.permissionDelete else '')
    def writeUsers(self):
        if (self.permissionInsert):
            return "WRITING..."
    def updateUsers(self):
        if (self.permissionUpdate):
            return "UPDATE..."
    def deleteUsers(self):
        if (self.permissionDelete):
            return "DELETE"
# class GradeStudent(Users):
#     def __init__(self, name, lastname, index, grade):
#         super().__init__(name,lastname,index)
#         self.grade = grade
#     def __str__(self):
#         return "Imię: %-15s Nazwisko: %-15s Indeks: %-15s Grade: %s" % (self.name, self.lastname, self.index, self.grade)
class GradeSekretariat(Users):
    def __init__(self, name, lastname, index, grade):
        super().__init__(name,lastname,index)
        self.grade = grade
    def __str__(self):
        return "Imię: %-15s Nazwisko: %-15s Indeks: %-15s Grade: %s" % (self.name, self.lastname, self.index, self.grade)
    def writeGrade(self):
        if (self.permissionSelect):
            grade = int(input("Podaj ocene studenta: "))
            return grade


Users()
studentUser1 = Users("Andrzej", "Student1", "A-123456")
print(studentUser1)
secretariat1 = Sercretariat("Iwona", "Sekretariat1", "6")
print(secretariat1)
gradeSekretariat1 = GradeSekretariat("Andrzej", "Student1", "A-123456", 5)
print(gradeSekretariat1)
gradeSekretariat1.writeGrade()
