unfinished_sandwiches = ['tuna sandwich', 'bacon sandwich', 'chicken sandwich']
for i in range(3):
    unfinished_sandwiches.append('pastrami sandwich')
finished = []
print("Sorry the deli has run out of ingredients to make pastrami sandwiches")
while 'pastrami sandwich' in unfinished_sandwiches:
    unfinished_sandwiches.remove('pastrami sandwich')
while unfinished_sandwiches:
    sandwich = unfinished_sandwiches.pop()
    print("I'm making a " + sandwich)
    finished.append(sandwich)
print("Sandiwiches that have been made: ")
for sandwich in finished:
    print(sandwich.title())