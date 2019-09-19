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

user_id_no_last = 0
class User():
    def __init__(self, login, name, lastname):
        self.login = login
        self.name = name
        self.lastname = lastname
        global user_id_no_last
        user_id_no_last += 1
        self.user_id_no = user_id_no_last
        self.data = []
        self.measurement = []

    def __str__(self):
        return "| %03d | %15s | %15s | %15s | %25s | %25s |"  % (self.user_id_no, self.login, self.name, self.lastname, self.data, self.measurement)


# user1 = User("A1", "A1", "A1")
# print(user1)