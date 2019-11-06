
class User:
    def __init__(self, user_login, user_password):
        self.user_login = user_login
        self.user_password = user_password
        self.active = True
        self.permissionSelect = True
        self.permissionInsert = False
        self.permissionUpdate = False
        self.permissionDelete = False
    def __str__(self):
        return 'Login: %10s | Active: %6s | Permission %s %s %s %s' % \
               (self.user_login, self.active, "SELECT" if self.permissionSelect else "", "INSERT" if self.permissionInsert else "",
                "UPDATE" if self.permissionUpdate else "", "DELETE" if self.permissionDelete else "")
class Moderator(User):
    def __init__(self, user_login, user_password):
        super().__init__(user_login, user_password)
        self.permissionInsert = True
        self.permissionUpdate = True
        self.permissionDelete = False
    def __str__(self):
        return super().__str__()
class Admin(Moderator):
    def __init__(self, user_login, user_password):
        super().__init__(user_login, user_password)
        self.permissionDelete = True
    def __str__(self):
        return super().__str__()

# user = User("user", "user")
# print(user)
# moderator = Moderator("moderator", "moderator")
# print(moderator)
# admin = Admin("admin", "admin")
# print(admin)
# user.active = False
# print(user)
# print(moderator)