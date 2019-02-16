def p(guest):
    print("Hello " +guest+ ". I would like to invite you to dinner.")
def sorry(guest):
    print("Sorry "+guest+ ". Sadly you can't come since we won't have enough room for all of you.")

guest_list = ['Aristotle','Sartre','Epictetus']
list(map(p,guest_list))
print(len(guest_list))
print("Oh no! Epictetus was enslaved by the Epaphroditus. He can't come to diner!")
guest_list.remove('Epictetus')
guest_list.append('Senecea')
list(map(p,guest_list))
print(len(guest_list))
print("Ordered a bigger table! More guests!")
guest_list.insert(0,'Kant')
guest_list.insert(2,'Gautama')
guest_list.append('Confucius')
list(map(p,guest_list))
print(len(guest_list))
print("Oh no! The table won't arrive in time!")
white_list = ['Aristotle','Confucius']

#Side effects and parenthesis almost as bad as in lisp...
print(len(list(map(p,filter(lambda guest: guest in white_list,guest_list)))))
print(len(list(map(sorry,filter(lambda guest: guest not in white_list,guest_list)))))
print(guest_list.clear())
#Does the same thing just with list comprehension
#list(map(p,[guest for guest in guest_list if guest in white_list]))
#list(map(p,[guest for guest in guest_list if guest not in white_list]))