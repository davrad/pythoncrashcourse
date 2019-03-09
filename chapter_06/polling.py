persons = ['jen','sarah','jordanna','charlize','thelma','edward']
favourite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'}
    
for person in persons:
    print("Hello " + person.title() + "!")
    if person in favourite_languages.keys():
        print("Thank you for taking the survey!")
    else:
        print("Hey how about this neat little survey here?")
