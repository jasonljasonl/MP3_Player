import tkinter
from gc import collect
from tkinter import *
from tkinter import ttk

from player_functions import get_music_list, stop_music, play_music

player_window = Tk()
player_window.title('MP3 Player')

mainframe = ttk.Frame(player_window)
frame = ttk.Frame(mainframe, width=200, height=200)


music_list_display = tkinter.Listbox(mainframe)
music_list_display.grid(column=0, row=0)

def load_music_list():
    music_list = get_music_list()
    for music in music_list:
        if 'wav' in music:
            music_list_display.insert(tkinter.END,music)
load_music_list()

previous_music_name = None
selected_music_name = None
next_music_name = None
def select_music(event):
    global previous_music_name
    global selected_music_name
    global next_music_name
    try:
        selection_index = music_list_display.curselection()
        previous_music_name = music_list_display.get(selection_index[0] - 1)
        selected_music_name = music_list_display.get(selection_index)
        next_music_name = music_list_display.get(selection_index[0] + 1)
    except Exception as e:
        print('Error:', e)

music_list_display.bind('<<ListboxSelect>>', select_music)


previous_music_button = ttk.Button(mainframe, text='Previous', command= lambda: play_music(previous_music_name))
stop_music_button = ttk.Button(mainframe, text='Stop', command= lambda: stop_music())
play_music_button = ttk.Button(mainframe, text='Play', command= lambda: play_music(selected_music_name) )
next_music_button = ttk.Button(mainframe, text='Next', command= lambda: play_music(next_music_name))


mainframe.grid(column=0, row=0)
frame.grid(column=0, row=0, columnspan=3, rowspan=2)

previous_music_button.grid(column=0, row=3)
stop_music_button.grid(column=1, row=3)
play_music_button.grid(column=2, row=3)
next_music_button.grid(column=3, row=3)

player_window.mainloop()