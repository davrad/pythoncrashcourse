filename = 'text/guest.txt'

name = input("What is your name?: ")
with open(filename,'a') as file_object:
    file_object.write(name+'\n')
