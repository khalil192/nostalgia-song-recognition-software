# nostalgia---song-recognition-software
Algorithm and software for Acoustic fingerprinting and song recognition

## project outline <br/>
**Problem Statement / Hypothesis** 
<br/>
non-technical : *Identify a song/music.*
<br/>
technical : *device an algorithm to compare the present required song with existing songs in the database and determine if they are identical*


> *the software recognises songs only which are already stored in the database*

**what the basic user interactivity should be**
<br/>
- add songs/music to database
- if want to know a song's details use the **check for match** functionality 
- show the songs in the database

## Technical details

### concept :
Every song/music you hear is nothing but composition of **pressure waves** that your brain can interpret after hearing.Just like our fingerprints, every song can be represented by a *unique* name like a fingerprint.
In this context this is called ***Acoustic Fingerprint***.
<br/> 
> If two music files have same Acoustic fingerprint, then they are most likely to be identical. 
<br/>There are many ways to create an Acoustic Fingerprint, each way has its own hashing algorithm.<br/>
> Acoustic fingerprint for a song is not universal, it depends on the hashing algorithm.
<br/>

**claims/assumptions and planning**
- If two music files have same Acoustic fingerprint, then they are most likely to be identical. 
- after preparing the fingerprint we no longer need the actual music file we can just discard the music file
- If we only to need to store the fingerprint then we need to store only strings/fingerprints i.e in text format which occupies very
less memory in comparison to music file
- that is the database consists of text files with acoustic fingerprints of songs which are added.

**notes and important points**

*Here are my previous assumptions and noted observations by self-done research:* 
- Music is simply the combination of pressure waves which vibrate through our ears and our brain
responds to the pressure wave signal and process it.
- For a Music signal there are three parameters : time, frequency,intensity/loudness. At a certain
point in time a music signal can have a certain frequency, which is the result of frequencies played at that time and loudness/intensity is the result of the intensities of the individual wave superpositions.
- By using those three parameters we can represent /music signal into a 3-d graph called spectrogram.
- For any piece of music there are some notes/ time stamps which when played together gives the song a unique rhythm which our brains use to identify the song.
- If there are certain nodes in a song which are loud enough then they can overcome the noise in the environment and those nodes are very important to remember and we can get these time-stamp nodes from the spectrogram itself.
- One golden point to make here is that, the peaks just by themselves doesn'’ provide much information.It's the time difference between them and their combinations which are useful.So after identifying peaks (t,f,l) loudness can be omitted because it's use is fulfilled now we are left with (t,f) pairs for peaks in song's spectrogram.
- We need to develop an algorithm to use the above information to prepare a unique name/file for a song called acoustic fingerprint.
- Basing on that acoustic fingerprint, we can identify the song

a sample mel-scale spectrogram 
![mel-scale spectrogram](https://miro.medium.com/max/768/1*MoiYQrW3Qaft6lfPQYbUbw.png)



