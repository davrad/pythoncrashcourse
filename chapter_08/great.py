def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

def make_great(magicians):
    new_list = []
    for magician in magicians:
        new_list.append(magician.title() + " the Great")
    return new_list 

magicians = ['merlin','gandalf','voldemort']
new_list = make_great(magicians[:])
show_magicians(magicians)
show_magicians(new_list)

