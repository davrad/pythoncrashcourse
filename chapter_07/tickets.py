def get_price(age):
    if age < 3:
        return 0
    if age < 12:
        return 10
    return 15

def run():
    while True:
        try:
            print(get_price(int(input("What's your age?: ")))) 
        except:
            print("Mistakes were made")
            break
        
def run_alt():
    limit = 5
    counter = 0
    while counter < limit:
        age = input("What's your age? ") 
        print("Your price is: " + str(get_price(int(age))))
run()