from tkinter import filedialog
from tkinter import *
from .compareTwoFingerPrints.check_for_match import check_for_match
from .generateFingerPrint.prepare_song_hash import song_hash,add_hash_to_database
from functools import partial
from database.show_songs_in_database import show_songs_in_database
import os




def addSongToDatabase (root): 
    root.filename =  filedialog.askopenfilename(initialdir = "/Users/khalilshaik/Desktop",title = "Select file",filetypes = (("mp3 files","*.mp3"),("all files","")))
    fullpath = root.filename
    add_hash_to_database(fullpath)

def checkForSongInDatabase(root):
    root.filename =  filedialog.askopenfilename(initialdir = "/Users/khalilshaik/Desktop",title = "Select file",filetypes = (("mp3 files","*.mp3"),("all files","")))
    fullpath = root.filename
    check_for_match(fullpath)
def add_directory(root):
    root.dirname =  filedialog.askdirectory()
    dir_path = root.dirname
    print(dir_path)
    for filename in os.listdir(dir_path):
        try: 
            add_hash_to_database(dir_path + '/' +filename)
        except : 
            pass
if __name__ == '__main__':
    root = Tk()
    print('this is going on')
    add_to_database = Button(root,text = 'add song to database',command =partial(addSongToDatabase,root))
    add_to_database.pack()
    check_for_match_button = Button(root,text = 'check for song in database',command= partial(checkForSongInDatabase,root))
    check_for_match_button.pack()
    show_songs_button = Button(root,text ='show songs in database',command = show_songs_in_database)
    show_songs_button.pack()
    add_directory_button = Button(root,text = 'add directory' , command = partial(add_directory,root))
    add_directory_button.pack()

    Exit_button = Button(root,text = 'exit',command = root.destroy)
    
    Exit_button.pack()
    root.mainloop()
