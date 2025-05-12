import tkinter
from tkinter import *
from tkinter import ttk

import scipy.io.wavfile as wav
import sounddevice as sd

from player_functions import get_music_list, stop_music, play_music

player_window = Tk()
player_window.title('MP3 Player')

mainframe = ttk.Frame(player_window)
frame = ttk.Frame(mainframe, width=200, height=200)


music_list_display = tkinter.Listbox(mainframe)
music_list_display.grid(column=0, row=0)

music_playlist_display = tkinter.Listbox(mainframe)
music_playlist_display.grid(column=2, row=0)


def load_music_list():
    music_list = get_music_list()
    for music in music_list:
        if 'wav' in music:
            music_list_display.insert(tkinter.END,music)
    music_list_display.select_set(music_list_display.index(0))
load_music_list()


selected_playlist_music_name = None
selected_music_name = None
def select_music(event):
    global selected_music_name
    global selected_playlist_music_name
    try:
        selection_index = music_list_display.curselection()
        selected_music_name = music_list_display.get(selection_index)
    except Exception as e:
        print('Error:', e)

music_list_display.bind('<<ListboxSelect>>', select_music)


def select_next_music():
    selection_index = music_list_display.curselection()
    music_list_display.select_set(selection_index[0] + 1)
    music_list_display.selection_clear(selection_index)
    next_music = music_list_display.get(selection_index[0] + 1)
    if not next_music:
        music_list_display.select_set(music_list_display.index(0))
        return music_list_display.get(music_list_display.index(0))
    else:
        return next_music

def select_previous_music():
    selection_index = music_list_display.curselection()
    music_list_display.select_set(selection_index[0] - 1)
    music_list_display.selection_clear(selection_index)
    previous_music = music_list_display.get(selection_index[0] - 1)
    if not previous_music:
        music_list_display.select_set(selection_index[0])
        return music_list_display.get(music_list_display.index(0))
    else:
        return previous_music


def select_playlist_music(event):
    global selected_playlist_music_name
    try:
        selection_playlist_music_index = music_playlist_display.curselection()
        selected_playlist_music_name = music_playlist_display.get(selection_playlist_music_index)
    except Exception as e:
        print('Error:', e)

music_playlist_display.bind('<<ListboxSelect>>', select_playlist_music)

def add_music_to_playlist():
    global selected_music_name
    playlist_queue = []
    try:
        selection_index = music_list_display.curselection()
        selected_music_name = music_list_display.get(selection_index)
        playlist_queue.append(selected_music_name)
        for music in playlist_queue:
            music_playlist_display.insert(tkinter.END, music)
    except Exception as e:
        print('Error:', e)


def play_playlist_music():
    path='musics/'
    while music_playlist_display:
        sample_rate, data = wav.read(f'{path}{music_playlist_display.get(0)}')
        sd.play(data, samplerate=sample_rate)
        sd.wait()
        music_playlist_display.delete(0)



previous_music_button = ttk.Button(mainframe, text='Previous', command= lambda: play_music(select_previous_music()))
stop_music_button = ttk.Button(mainframe, text='Stop', command= lambda: stop_music())
play_music_button = ttk.Button(mainframe, text='Play', command= lambda: play_music(selected_music_name) )
next_music_button = ttk.Button(mainframe, text='Next', command= lambda: play_music(select_next_music()))
add_to_queue_button = ttk.Button(mainframe, text='+', command= lambda: add_music_to_playlist())
play_playlist_music_button = ttk.Button(mainframe, text='Play playlist', command= lambda : play_playlist_music())

mainframe.grid(column=0, row=0)
frame.grid(column=0, row=0, columnspan=3, rowspan=2)

previous_music_button.grid(column=0, row=3)
stop_music_button.grid(column=1, row=3)
play_music_button.grid(column=2, row=3)
next_music_button.grid(column=3, row=3)

add_to_queue_button.grid(column=1, row=1)
play_playlist_music_button.grid(column=2, row=1)




player_window.mainloop()
