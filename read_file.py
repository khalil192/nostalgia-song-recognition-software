import os
from subprocess import check_call
from tempfile import mktemp
from scikits.audiolab import wavread, play
from scipy.signal import remez, lfilter
from pylab import *

# convert mp3, read wav
mp3filename = 'XC124158.mp3'
wname = mktemp('.wav')
check_call(['avconv', '-i', mp3filename, wname])
sig, fs, enc = wavread(wname)
os.unlink(wname)

# bandpass filter
bands = array([0,3500,4000,5500,6000,fs/2.0]) / fs
desired = [0, 1, 0]
b = remez(513, bands, desired)
sig_filt = lfilter(b, 1, sig)
sig_filt /=  1.05 * max(abs(sig_filt)) # normalize

subplot(211)
specgram(sig, Fs=fs, NFFT=1024, noverlap=0)
axis('tight'); axis(ymax=8000)
title('Original')
subplot(212)
specgram(sig_filt, Fs=fs, NFFT=1024, noverlap=0)
axis('tight'); axis(ymax=8000)
title('Filtered')
show()

play(sig_filt, fs)