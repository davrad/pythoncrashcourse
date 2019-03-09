places_dict = {
    'Franky': ['High Acre','Westerbeach','Raymead'],
    'Marlyn': ['Lorfield','Mallowport','Faysnow'],
    'Kaydon': ['Dorhall','Reddell','Linvale']
}
for person, places in places_dict.items():
    print(person+'s favourite places are:')
    for place in places:
        print(place)
    print()