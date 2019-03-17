from random import randint

#Currying!
def dice_generator(n):
    def function():
        return randint(1,n)
    return function 


def print_dice(d):
    for i in range(10):
        print(d())

sides = [6,10,20]
dice = map(dice_generator,sides)

for d in dice:
    print('---')
    print_dice(d)
