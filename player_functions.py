import os
import scipy.io.wavfile as wav
import sounddevice as sd

def get_music_list(path='musics'):
    try:
        return os.listdir(path)
    except FileNotFoundError:
        return []

def play_music(music):
    path='musics/'
    sample_rate, data = wav.read(f'{path}{music}')
    sd.play(data, samplerate=sample_rate)

def stop_music():
    sd.stop()


