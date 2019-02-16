def print_invitation(guest_list):
    for guest in guest_list:
        print("Hello " +guest+ ". I would like to invite you to dinner.")

guest_list = ['Artistotle','Sartre','Epictetus']
print_invitation(guest_list)
print("Oh no! Epictetus was enslaved by the Epaphroditus. He can't come to diner!")
guest_list.remove('Epictetus')
guest_list.append('Senecea')
print_invitation(guest_list)
print("Found a bigger table! More guests!")
guest_list.insert(0,'Kant')
guest_list.insert(2,'Gautama')
guest_list.append('Confucius')
print_invitation(guest_list)

#Alternate/ "simpler" version
# Same as in previous changing_guest_list.py, but with more print statements