last_index_no = 0
class Student:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        global last_index_no
        last_index_no += 1
        self.index_no = last_index_no
        self.grades = []
    def calculateAvg(self):
        sum = 0
        for grade in self.grades:
            sum += grade
        if len(self.grades) == 0:
            return 0
        return  round(sum / len(self.grades),2)
    def __str__(self):
        return "%06d | %15s | %15s | %7s " % (self.index_no, self.name, self.lastname , "B/D" if self.calculateAvg() == 0 else self.calculateAvg() )

# student1 = Student("A1", "A")
# student2 = Student("A2", "A")
# student3 = Student("A3", "A")
# student1.grades.append(3)
# student1.grades.append(4)
# student1.grades.append(5.5)
# print(student1)
# print(student1.grades)



