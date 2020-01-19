

def show_songs_in_database():
    with open('/Users/khalilshaik/Desktop/projects/nostalgia/dataBase/song_hashes.txt','r') as file:
            song_name = file.readline()
            song_char = file.readline()
            song_char_count = file.readline()
            i = 1
            while(song_name):
                try:
                    song_name,extension = song_name.rsplit('.')
                except:
                    extension = ''    
                print(i,'.',song_name)
                song_name = file.readline()
                song_hash = file.readline() 
                song_char_count = file.readline()
                i+=1

# show_songs_in_database()