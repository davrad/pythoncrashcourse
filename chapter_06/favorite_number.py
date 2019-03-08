import math
favorite_numbers = {'Alice' : 42, 'Bob' : 23, 'Charlie' : math.pi,
                    'Dustin' : 3,'Eliza' : math.e}
for name, number in favorite_numbers.items():
    print(name+"s favorite number is " + str(number)+".")
