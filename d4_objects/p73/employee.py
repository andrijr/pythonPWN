# P73
# Klasa Pracownik:
# Pola:
# imię
# nazwisko
# kontrakt (etat, staż - domyślny) full-time internship
# pensja (domyślnie 1000)
# Metody:
# konstruktor inicjujący pracownika o podanym w argumentach imieniu i nazwisku z domyślnym kontraktem stażysty
# metodę pozwalającą zmienić kontrakt przypisany do pracownika i zmienić wysokość pensji
# metoda zwracająca dane pracownika
# Klasa Firma
# Pola:
# Sekwencja przechowująca pracowników
# Metody
# metoda dodająca pracownika do firmy
# metoda usuwająca pracownika z firmy
# metoda wypisująca wszystkich pracowników w firmie
# metoda pozwalającą naliczyć pracownikowi dodatek zadaniowy do pensji jeżeli pracownik jest na etacie.
employee_last_no = 0
class Employee:
    def __init__(self, name, lastname, contract = "internship", salary = 1000): # full_time internship
        self.name = name
        self.lastname = lastname
        self.contract = contract
        self.salary = salary
        # self.salary = 1000
        global employee_last_no
        employee_last_no += 1
        self.employee_no = employee_last_no
    def __str__(self):
        return "%04d %15s | %15s | %12s | %10s zł" % (self.employee_no, self.name, self.lastname, self.contract, self.salary)
    # def changeContractAndSalaryEmployee(self, new_contract, new_salary):
    #     self.contract = new_contract
    #     self.salary = new_salary




# employee1 = Employee("Andrij", "Romaniw")
# employee2 = Employee("Andrij", "Romaniw")
# print(employee1)
# employee2.changeContractAndSalaryEmployee("Time", 6000)
# print(employee1)
# print(employee2)

