def read_files(f):
    try:
        with open(f) as file_object:
            lines = file_object.readlines()
    except FileNotFoundError:
        print(f,'not found')
    else:
        for l in lines:
            print(l.strip())

files = ['pets/dog.txt','cat.txt']

for f in files:
    read_files(f)