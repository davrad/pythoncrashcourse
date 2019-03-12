def make_album(artist_name,album_title,number_songs=''):
    album = {'artist': artist_name,
            'title' : album_title
            }
    if number_songs:
        album['tracknumbers'] = number_songs
    return album

print(make_album('Marvin Gaye',"What's going on"))
print(make_album('Micheal Jackson',"Thriller"))
print(make_album('Kraftwerk',"Autobahn"))
print(make_album('The Velvet Underground & Nico','The Velvet Underground & Nico',number_songs=11))