import os
import pydub 
from pydub import AudioSegment
from specgram import png_specgram
from specgram import max_freqency_limit,max_height,max_width
from max_list import calc_matches,max_sub_list_with_penality
from find_peaks import find_peaks
from max_list import max_sub_list_with_penality
from Final_answer import Final_answer
from song_resize import trim_leading_silence

def check_for_match(file_path):
    song_path = ''
    try:
        song_path,song_name = file_path.split('/')
    except:
        song_name = file_path
    song_name,extension = song_name.split('.')    
    last_stamp = 0
    song = AudioSegment.from_file(file_path)
    trim_front = trim_leading_silence(song)
    song = song[trim_front:]
    duration = song.duration_seconds
    parts = duration/5
    i=0
    matched=0
    while i<parts:
        song_part = song[5000*i:5000*(i+1)]
        if((i+1)*5 > duration):
            break
        i+=1
        song_part_name = song_path+'/'+song_name +'.'+extension
        song_part.export(song_part_name)
        png_specgram(song_part_name)
        ans_x,ans_y =find_peaks(song_path+'/'+song_name +'.png')
        #ans_y is hashed info
        matched = 0
        with open('song_hashes.txt','r') as file:
            current_song_name = file.readline()
            current_hash = file.readline() 
            matched = 0
            while(current_song_name and  matched ==0):
                print('checking with ',current_song_name)
                result = max_sub_list_with_penality(ans_y,current_hash)
                if(result == True):
                    # try:
                    #     current_song_name,extension = current_song_name.rsplit('.')
                    # except:
                    #     extension = ''
                    print('the song is matched with ', current_song_name) 
                    matched =1
                    Final_answer = True
                current_song_name = file.readline()
                current_hash = file.readline()     
            if(matched == 0):
                Final_answer = False
                print('there was no match in the database') 
        if(matched ==1):
            return
    if(matched == 0):
        Final_answer = False
        print('there was no match in the database') 

# if __name__ == '__main__':
    # check_song = '/Users/khalilshaik/Desktop/spectre/music/rockstar\ -\ post\ malone0.mp3'
    # check_for_match(check_song)
    
