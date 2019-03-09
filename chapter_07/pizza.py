def print_pizza(toppings):
    if len(toppings) == 0:
        print("A pizza without any toppings it is!")
        return
    print("A pizza with: ")
    for topping in toppings:
        print(topping)

def get_toppings(toppings,prompt):
    topping = input(prompt)
    if len(topping.strip()) == 0 or topping == 'quit':
        return False
    toppings.append(topping)
    return True

def run():
    prompt = "What topping do you want on your pizza?\n"
    prompt += "Type 'quit' if you have don't have anything to add: "
    toppings = []
    valid_topping = True 
    while valid_topping:
        valid_topping = get_toppings(toppings,prompt)
    print_pizza(toppings)

run()