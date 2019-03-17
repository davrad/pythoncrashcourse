class Privileges():

    def __init__(self,privileges):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)