pet_one = {
        'name': 'harold',
        'species':'parrot',
        'owner': 'margeret'
        }
pet_two = {
        'name': 'bob',
        'species':'dog',
        'owner': 'elizbeth'
        }
pet_three = {
        'name': 'mandorlo',
        'species':'fish',
        'owner': 'eric'
        }
pets = [pet_one,pet_two,pet_three]
for pet in pets:
    print("The name is " + pet['name'].title() + '.')
    print("It's a " + pet['species'].title() + '.')
    print("The owner is " + pet['owner'].title() + '.')
