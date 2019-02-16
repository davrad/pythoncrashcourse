def print_invitation(guest_list):
    for guest in guest_list:
        print("Hello " +guest+ ". I would like to invite you to dinner.")

guest_list = ['Artistotle','Sartre','Epictetus']
print_invitation(guest_list)
print("Oh no! Epictetus was enslaved by the Epaphroditus. He can't come to diner!")
guest_list.remove('Epictetus')
guest_list.append('Senecea')
print_invitation(guest_list)

#Alternate/ "simpler" version
#print("Hello " + guest_list[0] +". I would like to invite you to dinner.")
#print("Hello " + guest_list[1] +". I would like to invite you to dinner.")
#print("Hello " + guest_list[2] +". I would like to invite you to dinner.")
#print("Oh no! Epictetus was enslaved by the Epaphroditus. He can't come to diner!")
#guest_list[2] = 'Seneca'
#print("Hello " + guest_list[0] +". I would like to invite you to dinner.")
#print("Hello " + guest_list[1] +". I would like to invite you to dinner.")
#print("Hello " + guest_list[2] +". I would like to invite you to dinner.")