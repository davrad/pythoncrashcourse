def greet_user(username):
    if username is 'admin':
        print("Hello Admin! You're now operating with special rights")
    else:
        print("Hello " + username.title() + "! How are you doing today ?")

def greeting(usernames):
    if usernames:
        for username in usernames:
            greet_user(username)
    
usernames = ['admin','john','black knight']
greeting(usernames)

