person_one = {
        'first_name' : 'john',
        'last_name' : 'smith', 
        'age':'33',
        'city' : 'New Orleans'}
person_two = {
        'first_name' : 'Eileen',
        'last_name' : 'Wade', 
        'age':'43',
        'city' : 'Vancouver'}
person_three = {
        'first_name' : 'Aisling',
        'last_name' : 'Bloom', 
        'age':'33',
        'city' : 'Belfast'}
persons = [person_one,person_two,person_three]
for person in persons:
    print('Their name is ' + person['first_name'] +' ' +  person['last_name'])
    print("They're " + person['age'] +" years old and lives in " + person['city'])

