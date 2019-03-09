''' Interestingly enough, although it is stated later in the book that the order
of insertion is not maintained, because of the implementation of dicts in 3.6 using 
more compact hashtables, the order of insertion is being preserverd, although 
one should use ordereddict if order is necessary'''

import math
favorite_numbers = {'Alice' : [42],
                    'Bob' : [23],
                    'Charlie' : [math.pi],
                    'Dustin' : [3],
                    'Eliza' : [math.e]
                    }
for name, number in favorite_numbers.items():
    print(name+"s favorite numbers are: ")
    for x in number:
        print(x)