#Importing libraries
from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog

#Add songs to the playlist
def addsongs():
    temp_song = filedialog.askopenfilenames(initialdir="Music/", title="Choose a Song", filetypes=(("mp3 Files", "*.mp3"),))
    for s in temp_song:
        s=s.replace("D:/Users/Jake/Music/","")
        songs_list.insert(END,s)

def deletesong():
    curr_song=songs_list.curselection()
    songs_list.delete(curr_song[0])

def Play():
    song=songs_list.get(ACTIVE)
    song=f'D:/Users/Jake/Music/{song}'
    mixer.music.load(song)
    mixer.music.play()

def Pause():
    mixer.music.pause()

def Stop():
    mixer.music.stop()
    songs_list.selection_clear(ACTIVE)

def Resume():
    mixer.music.unpause()

def Previous():
    previous_one = songs_list.curselection()
    previous_one = previous_one[0]-1
    temp2 = songs_list.get(previous_one)
    temp2 = f'D:/Users/Jake/Music/{temp2}'
    mixer.music.load(temp2)
    mixer.music.play()
    songs_list.selection_clear(0, END)
    songs_list.activate(previous_one)
    songs_list.selection_set(previous_one)

def Next():
    next_one = songs_list.curselection()
    next_one=next_one[0]+1
    temp = songs_list.get(next_one)
    temp = f'D:/Users/Jake/Music/{temp}'
    mixer.music.load(temp)
    mixer.music.play()
    songs_list.selection_clear(0, END)
    songs_list.activate(next_one)
    songs_list.selection_set(next_one)

#Creating the root window
root = Tk()
root.title('My Music Player')
mixer.init()

#Creating the listbox to contain songs
songs_list = Listbox(root, selectmode=SINGLE, bg = "black", fg = "white", font = ('comicsans', 15), height = 12, width = 47, selectbackground = "gray", selectforeground = "black")
songs_list.grid(columnspan = 9)

#Defining the font
defined_font = font.Font(family = 'Helvetica')

#Play Button
play_button = Button(root, text = "Play", width = 7, command = Play)
play_button['font'] = defined_font
play_button.grid(row = 1, column = 0)

#Pause Button
pause_button = Button(root, text = "Pause", width = 7, command = Pause)
pause_button['font'] = defined_font
pause_button.grid(row = 1, column = 1)

#Stop Button
stop_button = Button(root, text = "Stop", width = 7, command = Stop)
stop_button['font'] = defined_font
stop_button.grid(row = 1, column = 2)

#Resume Button
resume_button = Button(root, text = "Resume", width = 7, command = Resume)
resume_button['font'] = defined_font
resume_button.grid(row = 1, column = 3)

#Previous Button
previous_button = Button(root, text = "Previous", width = 7, command = Previous)
previous_button['font'] = defined_font
previous_button.grid(row = 1, column = 4)

#Next Button
next_button = Button(root, text = "Next", width = 7, command = Next)
next_button['font'] = defined_font
next_button.grid(row = 1, column = 5)

#Menu
my_menu = Menu(root)
root.config(menu = my_menu)
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label = "Menu", menu = add_song_menu)
add_song_menu.add_command(label = "Add Songs", command = addsongs)
add_song_menu.add_command(label = "Delete Song", command = deletesong)

mainloop()