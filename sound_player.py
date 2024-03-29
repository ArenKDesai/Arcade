import playsound
import threading
import os

def button_sound():
    threading.Thread(target=playsound.playsound, args=(os.path.join('sounds','191380-Modular_UI_-Solo_Beeps-011.wav'), True)).start()

def ui_sound():
    threading.Thread(target=playsound.playsound, args=(os.path.join('sounds','191412-Modular_UI_-Solo_Beeps-050.wav'), True)).start()

def spit_sound():
    threading.Thread(target=playsound.playsound, args=(os.path.join('sounds','107126-Quick_spit-AOS02329.wav'), True)).start()

def block_sound():
    threading.Thread(target=playsound.playsound, args=(os.path.join('sounds','97665-sword_hit_3.wav'), True)).start()

def stomp_sound():
    threading.Thread(target=playsound.playsound, args=(os.path.join('sounds','581120__audiosea__foot-stomping.wav'), True)).start()

def slash_sound():
    threading.Thread(target=playsound.playsound, args=(os.path.join('sounds','370204__nekoninja__samurai-slash.wav'), True)).start()

def death_sound():
    threading.Thread(target=playsound.playsound, args=(os.path.join('sounds','717768__1bob__death-sound.wav'), True)).start()

class MusicPlayer:
    def __init__(self, music):
        self.music = music
        self.playing = False
        self.thread = None
    def play(self):
        self.playing = True
        self.thread = threading.Thread(target=playsound.playsound, args=(os.path.join('sounds', self.music), False))
        self.thread.start()
    def stop(self):
        self.playing = False
        self.thread.join()
