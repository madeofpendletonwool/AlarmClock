from tkinter import*
import pyglet

root = Tk()

player = pyglet.media.Player()
song = "/home/collinp/Music/DancingQueen.mp3"
src = pyglet.media.load(song)
player.queue(src)

def play():
    player.play()

def pause():
    player.pause()

button_1 = Button(root,text = "Play", command = play)
button_1.pack()
button_2 = Button(root,text = "Pause", command = pause)
button_2.pack()

root.mainloop()
