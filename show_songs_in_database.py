# 

def show_songs_in_database():
    with open('song_hashes.txt','r') as file:
            song_name = file.readline()
            song_hash = file.readline()
            i = 1
            while(song_name):
                try:
                    song_name,extension = song_name.rsplit('.')
                except:
                    extension = ''    
                print(i,'.',song_name)
                song_name = file.readline()
                song_hash = file.readline() 
                i+=1

# show_songs_in_database()