unfinished_sandwiches = ['tuna sandwich', 'bacon sandwich', 'chicken sandwich']
finished = []
while unfinished_sandwiches:
    sandwich = unfinished_sandwiches.pop()
    print("I'm making a " + sandwich)
    finished.append(sandwich)
print("Sandiwiches that have been made: ")
for sandwich in finished:
    print(sandwich.title())