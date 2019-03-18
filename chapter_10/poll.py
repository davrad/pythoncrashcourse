filename = 'poll.txt'

reasons = []

print("To exit the poll press 'n'")
while True:
    user_input = input("Why do you like programming?: ")
    if user_input == 'n':
        break
    reasons.append(user_input)

with open(filename,'a') as file_object:
    for reason in reasons:
        file_object.write(reason+'\n')