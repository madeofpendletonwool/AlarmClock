import PySimpleGUI as sg
import pyglet
import time

player = pyglet.media.Player()
song = "/home/collinp/Music/DancingQueen.mp3"
src = pyglet.media.load(song)
player.queue(src)

def play():
    player.play()

def pause():
    player.pause()


while True:
    play()

    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('Wake up!')],
                [sg.Button('Ok'), sg.Button('Snooze')]             
            ]
        
    window = sg.Window('pyArmClock', layout)

    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Snooze': # if user closes window or clicks cancel
        window.close()
        pause()
        time.sleep(5)
    else: break

    # button_1 = Button(root,text = "Play", command = play)
    # button_1.pack()
    # button_2 = Button(root,text = "Snooze", command = pause)
    # button_2.pack()

    print("Here's a message")

    #     # Create the Window
    #     window = sg.Window('pyArmClock', layout)
    #     if event == sg.WIN_CLOSED or event == 'Ok': # if user closes window or clicks cancel
    #         break
    #         window.close()
    # #End Alarm Values check
    # if event == sg.WIN_CLOSED or event == 'Ok': # if user closes window or clicks cancel
    #     break
