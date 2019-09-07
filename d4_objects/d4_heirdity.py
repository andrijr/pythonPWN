class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.permissionSelect = True
    def readPost(self):
        if(self.permissionSelect):
            print("READING...")
    def __str__(self):
        return "login: %s password: %s PERMISSIONS: %s " \
               %(self.login,self.password, ("SELECT" if self.permissionSelect else ""))
# moderator dziedziczy po obiekcie user
class Moderator(User):
    def __init__(self, login, password):
        # wywołanie metody __init__() klasy nadrzędnej
        super().__init__(login, password)
        self.permissionInsert = True
    def writePost(self):
        if(self.permissionInsert):
            print("WRITING...")
    def __str__(self):
        # wysołanie metody __str__() klasy nadrzędnej
        return super().__str__() + "INSERT" if self.permissionInsert else ""
# admin dziedziczy po obiekcie moderator
class Admin(Moderator):
    def __init__(self, login, password):
        super().__init__(login,password)
        self.permissionDelete = True
        self.permissionUpdate = True
    def deletePost(self):
        if(self.permissionInsert):
            print("DELETE...")
    def updatePost(self):
        if(self.permissionInsert):
            print("UPDATE...")
    def __str__(self):
        # wysołanie metody __str__() klasy nadrzędnej
        return super().__str__() + (" DELETE" if self.permissionInsert else "" + " UPDATE" if self.permissionInsert else "")




user = User("user", "user")
print(user)
user.readPost()

moderator = Moderator("moderator","moderator")
print(moderator)
moderator.readPost()
moderator.writePost()
admin  = Admin("admin", "admin")
print(admin)
admin.readPost()
admin.writePost()
admin.updatePost()
admin.deletePost()

