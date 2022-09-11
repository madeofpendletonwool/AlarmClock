#!/bin/python3

import time
import datetime
import PySimpleGUI as sg
import yaml
import pyglet
import tkinter.font
import os


def play():
    player = pyglet.media.Player()
    src = pyglet.media.load('/home/collinp/Music/DancingQueen.mp3')
    player.queue(src)

    player.play()

play()