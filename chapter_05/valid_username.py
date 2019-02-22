users = ['John','Saskia','Georg','Melinda','Kent']
other_users = ['JOHN','Evelyn','oscar','melinda','Dustin']

def check_name(new_user,users_lower):
    if new_user.lower() not in users_lower:
        print("Welcome to our website!")
        users.append(new_user)
    else:
        print("Sorry " + new_user +" is already taken.") 

def check_names():
    users_lower = [user.lower() for user in users]
    list(map(lambda x :check_name(x,users_lower),other_users))

check_names()


