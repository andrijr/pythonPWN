from d3_2_objects.p67.student import Student


class StudentController:
    def __init__(self):
        self.students = []
    def __str__(self):
        output = ""
        sum = 0
        studentGrade = 0
        for student in self.students:
            output += (student.__str__() + "\n")
            if len(student.grades) != 0:
                sum += student.calculateAvg()
                studentGrade += 1
        if studentGrade == 0:
            output += "Serednia oscena studentów wynosi %4.2f \n" % (0)
        else:
            output += "Serednia oscena studentów wynosi %4.2f \n" % (round(sum/studentGrade, 2))
        return output
    def addStudent(self, name, lastname):
        student = Student(name, lastname)
        self.students.append(student)
    def findStudentByIndex(self, index_no):
        for student in self.students:
            if index_no == student.index_no:
                return student
        return None
    def deleteStudentByIndex(self, index_no):
        findStudent = self.findStudentByIndex(index_no)
        if findStudent != None:
            self.students.remove(findStudent)
            print("Usunięto studenta %s " % (findStudent.__str__() + "\n"))
        else:
            print("Nie ma takiego studenta ")
    def addGradesToStudent(self, index_no, new_grades):
        findStudent = self.findStudentByIndex(index_no)
        if findStudent != None:
            findStudent.grades.extend(new_grades)
            print("Zaktualizowano listę ocen studenta " + findStudent.__str__() + "\n")
        else:
            print("Nie ma takiego studenta ")
    def deleteStudentGrades(self, index_no):
        findStudent = self.findStudentByIndex(index_no)
        if findStudent != None:
            findStudent.grades = []
            print("Wyczyszczono listę ocen studenta "+ findStudent.__str__() + "\n")
        else:
            print("Nie ma takiego studenta ")

# student1 = Student("A1", "A")
# student2 = Student("A2", "A")
# student3 = Student("A3", "A")
# student1.grades.append(3)
# student1.grades.append(4)

# dziekanat = StudentController()
# dziekanat.addStudent("X1", "X1")
# dziekanat.addStudent("X2", "X2")
# dziekanat.addStudent("X3", "X3")
# print(dziekanat)
# print(dziekanat.findStudentByIndex(2))
# print()
# dziekanat.deleteStudentByIndex(3)
# dziekanat.deleteStudentByIndex(3)
# print(dziekanat)
# dziekanat.addGradesToStudent(1, [2,5,6])
# dziekanat.addGradesToStudent(2, [4,5,6])
# print(dziekanat)
# dziekanat.deleteStudentGrades(2)
# print(dziekanat)
