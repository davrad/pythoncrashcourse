from user_module import User
from privilege_module import Privileges

class Admin(User):

    def __init__(self,first_name,last_name,privileges):
        super().__init__(first_name,last_name)
        self.privileges = Privileges(privileges) 
    
    def show_privileges(self):
        self.privileges.show_privileges()
