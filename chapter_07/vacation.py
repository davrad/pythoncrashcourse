active = True
vacations = {}
while active:
    name = input("What's your name?: ")
    location = input("And where do you want to travel?: ")
    vacations[name] = location
    state = input("Do you want to continue?: yes or no ")
    if state == 'no':
        active = False
for name, location in vacations.items():
    print(name+ " wants to travel to " + location)