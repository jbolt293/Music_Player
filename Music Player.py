# Importing libraries
from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog
import random

# Functions to manage the playlist and music playback
def addsongs():
    temp_song = filedialog.askopenfilenames(
        initialdir="Music/", 
        title="Choose a Song", 
        filetypes=(("mp3 Files", "*.mp3"),)
    )
    for s in temp_song:
        s = s.replace("D:/Users/Jake/Music/", "")
        songs_list.insert(END, s)

def deletesong():
    curr_song = songs_list.curselection()
    songs_list.delete(curr_song[0])

def Play():
    song = songs_list.get(ACTIVE)
    song = f'D:/Users/Jake/Music/{song}'
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
    previous_one = songs_list.curselection()[0] - 1
    temp2 = songs_list.get(previous_one)
    temp2 = f'D:/Users/Jake/Music/{temp2}'
    mixer.music.load(temp2)
    mixer.music.play()
    songs_list.selection_clear(0, END)
    songs_list.activate(previous_one)
    songs_list.selection_set(previous_one)

def Next():
    next_one = songs_list.curselection()[0] + 1
    temp = songs_list.get(next_one)
    temp = f'D:/Users/Jake/Music/{temp}'
    mixer.music.load(temp)
    mixer.music.play()
    songs_list.selection_clear(0, END)
    songs_list.activate(next_one)
    songs_list.selection_set(next_one)

def Shuffle():
    total_songs = songs_list.size()
    random_index = random.randint(0, total_songs - 1)
    song = songs_list.get(random_index)
    song = f'D:/Users/Jake/Music/{song}'
    mixer.music.load(song)
    mixer.music.play()
    songs_list.selection_clear(0, END)
    songs_list.activate(random_index)
    songs_list.selection_set(random_index)

def set_volume(val):
    volume = int(val) / 100
    mixer.music.set_volume(volume)

# Creating the root window
root = Tk()
root.title('My Music Player')
root.geometry('600x450')
root.config(bg='black')
mixer.init()

# Creating the listbox to contain songs
songs_list = Listbox(
    root, 
    selectmode=SINGLE, 
    bg="black", 
    fg="white", 
    font=('Helvetica', 12), 
    height=15, 
    width=60, 
    selectbackground="gray", 
    selectforeground="black"
)
songs_list.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Defining the font
defined_font = font.Font(family='Helvetica', size=12)

# Function to create buttons with a unified style
def create_button(text, row, column, command, width=10):
    button = Button(root, text=text, width=width, command=command, bg="gray", fg="black", font=defined_font)
    button.grid(row=row, column=column, padx=5, pady=5)
    return button

# Creating control buttons
play_button = create_button("Play", 1, 0, Play)
pause_button = create_button("Pause", 1, 1, Pause)
stop_button = create_button("Stop", 1, 2, Stop)
resume_button = create_button("Resume", 1, 3, Resume)
previous_button = create_button("Previous", 2, 1, Previous)
next_button = create_button("Next", 2, 2, Next)
shuffle_button = create_button("Shuffle", 2, 3, Shuffle)

# Volume Control
volume_scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=set_volume, bg="black", fg="white", font=defined_font, length=200)
volume_scale.set(70)  # Set default volume
volume_scale.grid(row=3, column=1, columnspan=3, padx=10, pady=20)

# Menu
my_menu = Menu(root)
root.config(menu=my_menu)
add_song_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Menu", menu=add_song_menu)
add_song_menu.add_command(label="Add Songs", command=addsongs)
add_song_menu.add_command(label="Delete Song", command=deletesong)

mainloop()
