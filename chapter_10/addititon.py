print("Please enter two numbers")
print("Add two zeros to quit")
def add_two():
    try:
        one = int(input())
        two = int(input())
    except ValueError:
        print("Sorry one of your numbers couldn't be read.")
        return True
    else:
        print(str(one + two))
        if one == 0 and two == 0:
            return False
        return True 

while add_two():
   continue 
