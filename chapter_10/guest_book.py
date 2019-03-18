filename = 'text/guest_book.txt'

names = []
while True:
    print("What is your name?")
    user_input = input("Enter 'n' if you want to stop: ")
    if user_input == 'n':
        break
    names.append(user_input) 

with open(filename,'a') as file_object:
    for name in names:
        file_object.write(name+'\n')
