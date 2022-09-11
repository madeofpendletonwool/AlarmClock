#!/bin/python3

import time
import datetime
import PySimpleGUI as sg
import yaml
import pyglet
import tkinter.font
import os
from threading import Thread
import playsound

def play(playsong):
    # print(f'In play {playsong}')
    # player = pyglet.media.Player()
    # src = pyglet.media.load(playsong)
    # player.queue(src)

    # player.play()


    # source = pyglet.media.load(playsong)
    # source.play()
    # pyglet.app.run()

    # player = pyglet.media.Player()
    # song = '/home/collinp/Documents/GitHub/pyArmClock/ExampleMusic/UpInSpace.mp3'
    # src = pyglet.media.load(song)
    # player.queue(src)

    # player.play()
    t = Thread(target=playsound.playsound, args=["/home/collinp/Documents/GitHub/pyArmClock/ExampleMusic/UpInSpace.mp3"])
    t.start()
    print('test')


def snooze():
    t.rai

play('test')