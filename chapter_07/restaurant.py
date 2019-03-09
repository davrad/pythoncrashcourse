seats_necessary = int(input("How many persons are you?: "))
if seats_necessary > 8:
    print("I'm sorry, you'll have to wait.")
elif seats_necessary < 1:
    print("Sorry, you'll have to give me something that makes sense.")
else:
    print("Yes, we have a table ready for you.")
