def points(alien_colour):
    if(alien_colour == 'green'):
        return 5
    elif(alien_colour == 'yellow'):
        return 10
    elif(alien_colour == 'red'):
        return 15
    else:
        return 0

print(points('green'))
print(points('yellow'))
print(points('red'))
print(points(''))
