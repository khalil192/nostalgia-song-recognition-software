import os
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg') # No pictures displayed 
import pylab
import librosa
import librosa.display
import numpy as np


max_freqency_limit = 32768
max_height = 5
max_width = 5
def find_max(fs):
    m = -1
    for i in fs:
        if m< i:
            m = i
    return m

def png_specgram(filepath):
    try:
        filepath,filename = filepath.rsplit('/',1)
    except :
        filepath = ""
        filename = filepath
    print(filename)    
    filename,extension = filename.split('.')
    sig, fs = librosa.load(filepath+'/'+filename+'.'+extension)   
    # make pictures name 
    save_path = filename+'.png'
    plt.figure(figsize=(max_width,max_height))
    pylab.axis('on') # no axis
    pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[]) # Remove the white edge
    S = librosa.feature.melspectrogram(y=sig, sr=fs)
    librosa.display.specshow(librosa.power_to_db(S,ref=np.max),y_axis='mel', fmax=16384, x_axis='time')
    # plt.colorbar(format='%+2.0f dB')
    # print(S)
    pylab.savefig(filepath+'/'+save_path, bbox_inches=None, pad_inches=0)
    pylab.close()


def png(filepath):
    # print("came here for "+filepath)
    try:
        filepath,filename = filepath.rsplit('/')
    except :
        filepath = ""
        filename = filepath
    print(filename)    
    filename,extension = filename.split('.')
    sig, fs = librosa.load(filepath+'/'+filename+'.'+extension)   
    # make pictures name 
    save_path = filename+'.png'
    plt.figure(figsize=(max_width,max_height))
    S = librosa.feature.melspectrogram(y=sig, sr=fs)
    librosa.display.specshow(librosa.power_to_db(S,ref=np.max),y_axis='mel', fmax=16384, x_axis='time')
    # plt.colorbar(format='%+2.0f dB')
    # print(S)
    pylab.savefig(filepath+'/'+save_path, bbox_inches=None, pad_inches=0)
    pylab.close()

