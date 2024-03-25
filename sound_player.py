import playsound
import threading
import os

def button_sound():
    threading.Thread(target=playsound.playsound, args=(os.path.join('sounds','191380-Modular_UI_-Solo_Beeps-011.wav'), True)).start()

def ui_sound():
    threading.Thread(target=playsound.playsound, args=(os.path.join('sounds','191412-Modular_UI_-Solo_Beeps-050.wav'), True)).start()