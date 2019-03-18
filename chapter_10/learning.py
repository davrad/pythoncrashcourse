filename = 'text/learning_python.txt'

with open(filename) as file_object:
    #print whole file
    contents = file_object.read().rstrip()
    print(contents)
    print('---')

with open(filename) as file_object:
    #print file line by line
    for line in file_object:
        print(line.rstrip())
    print('---')

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
