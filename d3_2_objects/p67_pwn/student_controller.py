from d3_2_objects.p67_pwn.student import Student

class StudentController:
    def __init__(self):
        # lista obiektów klasty Student
        self.students = []
    def __str__(self):
        output = ""
        sum = 0
        studentHasGrade = 0
        for student in self.students:
            output += (student.__str__() + "\n")
            if(len(student.grades) != 0):
                sum += student.calculateAvg()
                studentHasGrade += 1
        # średnia wszystkich studentów
        if(studentHasGrade == 0):

            output += "ŚREDNIA STUDENTÓW Z LISTĄ OCEN: %5.2f" % (0)
        else:
            output += "ŚREDNIA STUDENTÓW Z LISTĄ OCEN: %5.2f" % (sum/studentHasGrade)
        return output
    # metoda dodająca studenta do listy
    def addStudent(self, name, lastname):
        # utowrzenie obiektu klasy student
        student = Student(name, lastname)
        # dodanie obiektu do listy
        self.students.append(student)
    # metoda szukająca i zwracająca studenta
    def findStudentByIndex(self,index_no):
        for student in self.students:
            # porównanie szukanego indeksu z wartością pól studenta index_no
            if(index_no == student.index_no):
                return student
        return None
    # metoda usuwająca studenta z listy
    def deleteStudentByIndex(self,index_no):
        # wywołanie metody szukającej studenta po indeksie
        deletedStudent = self.findStudentByIndex(index_no)
        # jeżeli zwócono niepusty obiekt klasy student
        if(deletedStudent != None):
            self.students.remove(deletedStudent)
            print("usunięto studenta\n" + deletedStudent.__str__()+"\n")
        else:
            print("Nie ma takiego studenta")
    # dodawanie listy ocen do studenta
    def addGradesToStudent(self, index_no, new_grades):
        # wyszukiwanie studenta po indeksie
        findStudent = self.findStudentByIndex(index_no)
        if(findStudent != None):
            # rozszerzenie listy ocen studenta o listę new_grades
            findStudent.grades.extend(new_grades)
            print("zaktualizowano listę ocen studenta")
    def deleteStudentGrades(self, index_no):
        findStudent = self.findStudentByIndex(index_no)
        if (findStudent != None):
            # przypisuję pustą listę ocen studenta
            findStudent.grades = []
            print("wyczyszczona lista ocen studenta")


dziekanat = StudentController()
dziekanat.addStudent("X1", "X1")
dziekanat.addStudent("X2", "X2")
dziekanat.addStudent("X3", "X3")
dziekanat.addStudent("X4", "X4")
dziekanat.addStudent("X5", "X5")
print(dziekanat)
dziekanat.deleteStudentByIndex(1)
dziekanat.addGradesToStudent('000002', 4)
print(dziekanat)