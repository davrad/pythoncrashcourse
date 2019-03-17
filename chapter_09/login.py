class User():

    def __init__(self,
                first_name,
                last_name,
                password = '',
                id = '',
                mail =''):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.id = id
        self.mail = mail
        self.login_attempts = 0

    def describe_user(self):
        print("Name", 
            self.first_name.title(),
            self.last_name.title())
    def greet(self):
        print("Hello " + self.first_name.title() + " " + 
        self.last_name.title() + 
            "! How are you doing?")

    def increment_login_attempts(self,increment):
        new_value = self.login_attempts + increment
        old_value = self.login_attempts
        self.login_attempts = new_value if increment > 0 else old_value
    
    def reset_login_attempts(self):
        self.login_attempts = 0
        

u = User("patrick","nieri")
u.increment_login_attempts(5)
print(u.login_attempts)
u.reset_login_attempts()
print(u.login_attempts)