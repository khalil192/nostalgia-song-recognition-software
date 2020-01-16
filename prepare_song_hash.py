import pydub
from pydub import AudioSegment
from specgram import png_specgram
from song_resize import song_resize
from find_peaks import find_peaks
from max_list import max_sub_list_with_penality,calc_matches,max_sub_list_with_penality


def run_length_encoding(hash):
    # with open('normal.txt','a') as file:
    #     for i in hash:
    #         file.write(str(i) + ' ')
    #     file.write('\n')   
    # print('song is added to normal')      
    x_char   =  []
    x_count  =  []
    curr_index   = 1
    xlen = len(hash)
    freq_of_last = 1
    while(curr_index < xlen):
        if(hash[curr_index] != hash[curr_index-1]):
            x_char.append(hash[curr_index-1])
            x_count.append(freq_of_last)
            freq_of_last =1
        else:
            freq_of_last +=1
        curr_index +=1
    x_char.append(hash[curr_index-1])
    x_count.append(freq_of_last)
    return x_char , x_count

def song_hash(song_to_add):
    # song_to_Add is the fresh music file you want add to database
    song_path = ""
    try:
        song_path,song_name = song_to_add.rsplit('/',1)
    except:
        song_name = song_to_add
    song_name,extension = song_name.split('.',1)    
    number_of_parts = song_resize(song_to_add)
    hash =[]
    for i in range(number_of_parts):
        ans_y = find_peaks(song_path+'/'+song_name+str(i) + '.'+'png')
        hash.extend(ans_y)
    x_char , x_count = run_length_encoding(hash)
    return x_char , x_count    

    
def add_hash_to_database(song_file):
    song_path = ''
    try:
        song_path, song_name = song_file.rsplit('/',1)
    except :
        song_name = song_file
    hashed_x, hashed_count = song_hash(song_file)
    with open('song_hashes.txt','a') as file:
        file.write(song_name+'\n')
        for i in hashed_x:
            file.write(i)
        file.write('\n')   
    with open('song_hashes.txt','a') as file:
        for i in hashed_count:
            file.write(str(i) + ' ')
        file.write('\n')   
    print('song is added to database')        
