#!/bin/python3

import time
import datetime
import PySimpleGUI as sg
import yaml
import pyglet
import tkinter.font
import os
import threading
import playsound
import pygame


def wait_for_event():

    pygame.mixer.init()
    pygame.mixer.music.load("/home/collinp/Documents/GitHub/pyArmClock/ExampleMusic/UpInSpace.mp3")
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play()

wait_for_event()
print("wow this was easy")
time.sleep(15)