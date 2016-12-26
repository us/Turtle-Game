import winsound, sys

path = ".\\sound\\{}"
sounds = ["elmaisirirken.wav","Braumvictory","marioisirilirken.wav","gameover.wav","forquit"]

def beep(audio):
    winsound.PlaySound(path.format(audio), winsound.SND_FILENAME)