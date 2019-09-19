# Klasa Firma
# Pola:
# Sekwencja przechowująca pracowników
# Metody
# metoda dodająca pracownika do firmy
# metoda usuwająca pracownika z firmy
# metoda wypisująca wszystkich pracowników w firmie
# metoda pozwalającą naliczyć pracownikowi dodatek zadaniowy do pensji jeżeli pracownik jest na etacie.
from d4_objects.p73.employee import Employee

class EmployeeController:
    def __init__(self):
        self.employees = []
    def __str__(self):
        output = ''
        for employee in self.employees:
            output += employee.__str__() + "\n"
        return  output
    def addEmployee(self, name, lastname):
        employee = Employee(name, lastname)
        self.employees.append(employee)
    def findEmployeeByNumber(self,employee_no):
        for employee in self.employees:
            if employee.employee_no == employee_no:
                return  employee
        return None
    def findEmployeeByNameLastname(self, name, lastname):
        for employee in self.employees:
            if employee.name == name and employee.lastname == lastname:
                return  employee
        return None
    def deleteEmployeeByNumber(self, employee_no):
        findEmployee = self.findEmployeeByNumber(employee_no)
        if findEmployee != None:
            self.employees.remove(findEmployee)
            print("Usunięto pracownika " + findEmployee.__str__())
        else:
            print("Nie ma takiego pracownika " )
    def changeContractAndSalaryEmployee(self, employee_no, contract, salary):
        findEmployee = self.findEmployeeByNumber(employee_no)
        if findEmployee != None:
            # findEmployee.changeContractAndSalaryEmployee(contract, salary)
            findEmployee.contract = contract
            findEmployee.salary = salary
            print("Zmieniono dane pracownika " + findEmployee.__str__())
        else:
            print("Nie ma takiego pracownika " )
    def addSalaryForNumber(self, employee_no, percent_rise):
        findEmployee = self.findEmployeeByNumber(employee_no)
        if findEmployee != None:
            if findEmployee.contract.upper() == "FULL-TIME":
                findEmployee.salary = round(findEmployee.salary * (1 + percent_rise/100),2)
                print("Podwyższono wynagrodzenie dla pracownika " + findEmployee.__str__())
            else:
                print("Nie jest to pracownik etatowy nie można dodać podwyżki " )
        else:
            print("Nie ma takiego pracownika " )




# firma = EmployeeController()
# firma.addEmployee("Pawel", "Bystry")
# firma.addEmployee("Agnieszka", "Piękna")
# firma.addEmployee("Andrij", "Romaniw")
# firma.changeContractAndSalaryEmployee(2, "full-time", 5000)
# firma.changeContractAndSalaryEmployee(3, "full-time", 6000)
# print(firma)
# print(firma.findEmployeeByNumber(1))
# print(firma.findEmployeeByNameLastname("Andrij", "Romaniw"))
# print(firma.deleteEmployeeByNumber(2))
# print(firma.addSalaryForNumber(3, 15))
# print(firma.addSalaryForNumber(1, 15))



