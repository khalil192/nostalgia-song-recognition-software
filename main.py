from tkinter import filedialog
from tkinter import *
from check_for_match import check_for_match
from prepare_song_hash import song_hash,add_hash_to_database
from functools import partial
from show_songs_in_database import show_songs_in_database



if __name__ == '__main__':
    root = Tk()
    print('this is going on')
    root.filename =  filedialog.askopenfilename(initialdir = "/Users/khalilshaik/Desktop/spectre",title = "Select file",filetypes = (("mp3 files","*.mp3"),("all files","*.*")))
    fullpath = root.filename
    add_to_database = Button(root,text = 'add song to database',command =partial(add_hash_to_database,fullpath))
    add_to_database.pack()
    check_for_match_button = Button(root,text = 'check for song in database',command= partial(check_for_match,fullpath))
    check_for_match_button.pack()
    show_songs_button = Button(root,text ='show songs in database',command = show_songs_in_database)
    show_songs_button.pack()
    Exit_button = Button(root,text = 'exit',command = root.destroy)
    Exit_button.pack()
    root.mainloop()
