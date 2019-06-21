import pydub
from pydub import AudioSegment
from specgram import png_specgram

def trim_leading_silence(sound, silence_threshold=-50.0, chunk_size=10):
    trim_ms = 0  # ms
    while sound[trim_ms:trim_ms+chunk_size].dBFS < silence_threshold:
        trim_ms += chunk_size
    return trim_ms

def song_resize(filepath):
    song_name = ''
    try:
        filepath,filename = filepath.rsplit('/',1)
    except:
        filepath = ''
        filename = filepath
    song_name,extention = filename.rsplit('.',1)
    song = AudioSegment.from_mp3(filepath+'/'+filename)
    trim_front =  trim_leading_silence(song)
    song = song[trim_front:]
    i=0
    len = song.duration_seconds
    len_to_forward = 5
    len_of_part = 5
    num_parts = 0
    while i<len:
        if (i+len_of_part)*1000<len:
            part = song[i*1000:]
        else:    
            part = song[i*1000:(i+len_of_part)*1000]
        final_path = filepath+'/'+song_name+str(int(i/len_to_forward))+'.'+extention
        part.export(final_path)
        png_specgram(final_path)
        i+=len_to_forward
        num_parts+=1
    return num_parts
