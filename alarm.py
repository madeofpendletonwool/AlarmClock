import time
import datetime
import PySimpleGUI as sg
import yaml
import pyglet

Time_Period = ("AM", "PM")
Hour = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
Min = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60)

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:",date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
            Wake_Up()
            break
def actual_time():
    set_alarm_timer = f"{hour_conv}:{min_conv}:{sec_conv}"
    Time_Period
    alarm(set_alarm_timer)

def Wake_Up():
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('Wake Up!')],
                [sg.Button('Ok'), sg.Button('Snooze')] ]

    # Create the Window
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        player = pyglet.media.Player()
        song = "/home/collinp/Music/DancingQueen.mp3"
        src = pyglet.media.load(song)
        player.queue(src)

        play()

        while True:
            if event == 'Snooze': # if user Clicks Snooze
                pause()
                time.sleep(600)
                play()
            else: # Otherwise break loop
                break

def play():
    player.play()

def pause():
    player.pause()


sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('When Would you like to wake up?')],
            [sg.Text('Select Time:')],
            [sg.Combo(Hour), sg.Combo(Min), sg.Combo(Time_Period)],
            [sg.Button('Ok')],
            [sg.Button('Choose Song'), sg.Button('Choose Alarm')]
             
        ]

# Create the Window
window = sg.Window('pyArmClock', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    # Check if alarm values were populated
    if values[0] or values[1] or values[2] == '':
        sg.theme('DarkAmber')   # Add a touch of color
        # All the stuff inside your window.
        layout = [  [sg.Text('ALARM TIME REQUIRED!!')],
                    [sg.Button('Ok')]
                    
                ]

        # Create the Window
        window = sg.Window('pyArmClock', layout)
        if event == sg.WIN_CLOSED or event == 'Ok': # if user closes window or clicks cancel
            break
            window.close()
    #End Alarm Values check
    if event == sg.WIN_CLOSED or event == 'Ok': # if user closes window or clicks cancel
        break




window.close()

hour_temp = values[0]
hour_time = values[0]
min_time = values[1]
time_section = values[2]

if time_section == "PM":
    hour_conv = hour_time + 12
else: hour_conv = hour_time

if min_time < 10:
    min_strconv = str(min_time)
    min_conv = "0" + min_strconv
else: min_conv = str(min_time)

if hour_time < 10:
    hour_strconv = str(hour_time)
    hour_conv = "0" + hour_strconv
else: hour_conv = str(hour_time)

print(f"Got it! I'll wake you up at {hour_temp}:{min_conv} {time_section}")

current_time = time.localtime()
if current_time.tm_sec < 10:
    sec_strconv = str(current_time.tm_sec)
    sec_conv = "0" + sec_strconv
else: sec_conv = str(current_time.tm_sec)




current_time = time.localtime()
actual_time()

# # print(f"Current Time is {modified_hour}:{current_time.tm_min}:{current_time.tm_sec} {Time_Period}")



# #ps.playsound('/home/collinp/Music/DancingQueen.mp3')