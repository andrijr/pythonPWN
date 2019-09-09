class Uses():
    def __init__(self, login, name, lastname):
        self.login = login
        self.name = name
        self.lastname = lastname
    def __str__(self):
        return "| %15s | %15s | %15s" % (self.login, self.name, self.lastname)


user1 = Uses("A1", "A1", "A1")
print(user1)