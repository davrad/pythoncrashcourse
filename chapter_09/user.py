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

    def describe_user(self):
        print("Name", 
            self.first_name.title(),
            self.last_name.title())
    def greet(self):
        print("Hello " + self.first_name.title() + " " +
            self.last_name.title() + 
            "! How are you doing?")

users = [User("patrick","nieri"),
        User("rafael","hardy"),
        User("olga","schuyler")]

for u in users:
    u.describe_user()
    u.greet()
