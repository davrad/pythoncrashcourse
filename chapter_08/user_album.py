def make_album(artist_name,album_title,number_songs=''):
    album = {'artist': artist_name,
            'title' : album_title
            }
    if number_songs:
        album['tracknumbers'] = number_songs
    return album

active = True
while active:
    artist = input("What is the name of the artist?: ")
    title = input("What is the name of the title?: ")
    print(make_album(artist, title))
    further = input("Do you want to continue?: y n ")
    if further == 'n':
        active = False
