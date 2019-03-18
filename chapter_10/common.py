def count_occurences_file(f, to_count):
    try:
        with open(f) as file_object:
            lines = file_object.readlines()
    except FileNotFoundError:
        print("File not found")
    else:
        s =''
        for l in lines:
            if l.isspace():
                continue
            s += l.strip() 
            
        return s.lower().count('the')

file_name = 'text/frankenstein.txt'
print(count_occurences_file(file_name,'the'))

