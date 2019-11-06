class DataBaseManager:

    def __init__(self):
        self.user_id = None

    def login_user(self, login, password):
        user_id = self.check_password(login, password)
        if user_id is not None:
            self.user_id = user_id
        else:
            return ConnectionRefusedError('bad password')


    def check_password(self, login, password):
        """
        checks if password is ok for user
        """
        pass


    def check_privilage(self, login, privilige):
        """
        https://serverfault.com/questions/117525/how-can-i-show-users-privileges-in-mysql
        """
        pass

    def do_something(self, login):
        if self.check_privilage(login, 'something'):
            # do somethin
            pass
        else:
            return ConnectionRefusedError('not authorized for operation: something')