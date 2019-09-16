# P75
# Napisz program do generowania wyników urządzenia pomiarowego:
# Użytkownik może wykonać pomiar (M)
# Użytkownik może zapisać pomiar (S) do pliku
# Użytkownik może dalej wykonywać pomiary dopisując ich wynik do pliku (A)
# Użytkownik może wyjść z programu (Q)
# Wynik pomiaru powinien być sformatowany w następujący sposób:
# Dane użytkownika
# Data pomiaru
# Wynik pomiaru -> przykładowy: User;Data,Result

class Uses():
    def __init__(self, login, name, lastname):
        self.login = login
        self.name = name
        self.lastname = lastname
    def __str__(self):
        return "| %15s | %15s | %15s" % (self.login, self.name, self.lastname)


user1 = Uses("A1", "A1", "A1")
print(user1)