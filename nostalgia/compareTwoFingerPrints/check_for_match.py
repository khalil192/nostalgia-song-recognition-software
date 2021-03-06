import os
import shutil
import pydub 
from pydub import AudioSegment
from ..generateFingerPrint.specgram import png_specgram
from ..generateFingerPrint.specgram import max_freqency_limit,max_height,max_width
from .max_list import checkForMatch
from ..generateFingerPrint.find_peaks import find_peaks
from ..generateFingerPrint.song_resize import trim_leading_silence
from ..generateFingerPrint.prepare_song_hash import run_length_encoding
import os.path
from os import path



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
    pwd = os.getcwd()
    print(pwd)
    yetAnswer = "noSong"
    yetMaximum = -1
    while i<parts:
        song_part = song[5000*i:5000*(i+1)]
        if((i+1)*5 > duration):
            break
        i+=1
        song_part_name = song_path+'/'+song_name +str(i)+'.'+extension
        song_part.export(song_part_name)
        png_specgram(song_part_name)
        ans_y =find_peaks(song_path+'/'+song_name+str(i) +'.png')
        os.remove(song_path+'/'+song_name+str(i) +'.png')
        os.remove(song_path+'/'+song_name+str(i) +'.' + extension)
        # shutil.move(song_path+'/'+song_name +'.png' , pwd + '/image_cut/' +song_part_name +'.png' )
        # shutil.move(song_path+'/'+song_name +'.'+extension , pwd + 'audio_cut/' +song_part_name +'.'+extension )
        #ans_y is hashed info
        matched = 0
        song_hash_char , song_hash_count = run_length_encoding(ans_y)
        with open('database/song_hashes.txt','r') as file:
            current_song_name = file.readline()
            current_hash_char = file.readline() 
            current_hash_count = file.readline()
            current_hash_char = [x for x in current_hash_char]
            current_hash_count = [int(x) for x in current_hash_count.split()]
            matched = 0
            while(current_song_name and  matched ==0):      
                print('checking with ',current_song_name)
                result, maxMatches = checkForMatch(current_hash_char,song_hash_char,current_hash_count,song_hash_count)
                if(result == True):
                    print('the song is matched with ', current_song_name) 
                    matched =1
                    Final_answer = True
                else :
                    if(maxMatches > yetMaximum):
                        yetMaximum = maxMatches
                        yetAnswer = current_song_name
                current_song_name  = file.readline()
                current_hash_char  = file.readline() 
                current_hash_count = file.readline()
                current_hash_char  = [x for x in current_hash_char]
                current_hash_count = [int(x) for x in current_hash_count.split()]  
            if(matched == 0):
                Final_answer = False
        if(matched ==1):
            return
    if((matched == 0 and yetAnswer == "noSong")or yetMaximum < 50):
        Final_answer = False
        print('there was no match in the database') 
    elif(yetMaximum > 50) :
        print("the song is most likely to be matched with " + yetAnswer)
# if __name__ == '__main__':
    # check_song = '/Users/khalilshaik/Desktop/spectre/music/rockstar\ -\ post\ malone0.mp3'
    # check_for_match(check_song)
    

