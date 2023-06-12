#Importing mixer module from pygame library

from pygame import mixer
from tkinter import *
from tkinter import filedialog

# How to load, play, pause and and unpause audio file
mixer.init() #Initialzing pygame mixer

mixer.music.load('21.mp3') #Loading audio File

mixer.music.play() #Playing Music with Pygame
mixer.music.stop() #Stoping Music with Pygame

class Player:
    def __init__(self, window ):
        window.geometry('320x100'); window.title('Python Tiny Player'); window.resizable(0,0)
        Load = Button(window, text = 'Load',  width = 10, font = ('Times', 10), command = self.load)
        Play = Button(window, text = 'Play',  width = 10,font = ('Times', 10), command = self.play)
        Pause = Button(window,text = 'Pause',  width = 10, font = ('Times', 10), command = self.pause)
        Stop = Button(window ,text = 'Stop',  width = 10, font = ('Times', 10), command = self.stop)
        Load.place(x=0, y=20); Play.place(x=110, y=20); Pause.place(x=220, y=20); Stop.place(x=110, y=60) 
        self.music_file = False
        self.playing_state = False
    def load(self):
        self.music_file = filedialog.askopenfilename()
    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state=True
        else:
            mixer.music.unpause()
            self.playing_state = False
    def stop(self):
        mixer.music.stop()
        
new_root = Tk()
player_app = Player(new_root)
new_root.mainloop()
