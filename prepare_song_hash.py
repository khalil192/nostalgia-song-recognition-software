import pydub
from pydub import AudioSegment
from specgram import png_specgram
from song_resize import song_resize
from find_peaks import find_peaks
from max_list import max_sub_list_with_penality,calc_matches,max_sub_list_with_penality


def song_hash(song_to_add):
    # song_to_Add is the fresh music file you want add to database
    song_path = ""
    try:
        song_path,song_name = song_to_add.rsplit('/',1)
    except:
        song_name = song_to_add
    song_name,extension = song_name.split('.')    
    number_of_parts = song_resize(song_to_add)
    hash =[]
    for i in range(number_of_parts):
        ans_x,ans_y = find_peaks(song_path+'/'+song_name+str(i) + '.'+'png')
        hash.extend(ans_y)
    return hash    

def add_hash_to_database(song_file):
    song_path = ''
    try:
        song_path, song_name = song_file.rsplit('/',1)
    except :
        song_name = song_file
    hashed_info = song_hash(song_file)
    with open('song_hashes.txt','a') as file:
        file.write(song_name+'\n')
        for i in hashed_info:
            file.write(i)
        file.write('\n')   
    print('song is added to database')        

# if __name__ == '__main__':
#     song_file = '/Users/khalilshaik/Desktop/spectre/n/n1.mp3'
#     add_hash_to_database(song_file)


