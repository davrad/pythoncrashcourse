from random import randint

numbers = [randint(0,9) for i in range(99)]
print(numbers)
print("First three items are " + str(numbers[:3]))
print("Middle three items are" + str(numbers[49:52]))
print("Last three items are" + str(numbers[-3:]))
