import json

file_name = 'text/fav_num.json'

def get_fav_from_user():
    return int(input("What's your favourite number?: "))

def save_fav_number():
    n = get_fav_from_user()
    with open(file_name,'w') as file_object:
        json.dump(n,file_object)

def get_fav_number():
    try:
        with open(file_name) as file_object:
            return json.load(file_object)
    except FileNotFoundError:
        save_fav_number()
        return "Number saved"
        

print(get_fav_number())
