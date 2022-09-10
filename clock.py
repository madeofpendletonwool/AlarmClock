#!/bin/python3

import PySimpleGUI as sg
from datetime import datetime
import tkinter.font

#getting current time and return it
def now():
    ntime=datetime.now()
    nt=ntime.strftime('%H:%M:%S')
    return nt

#make ordinary window
def make_window(theme,cfont):
    if theme:
        sg.theme(theme)
#ordinary window's layout
#current time、theme change button、font change button、close button
    layout=[[sg.Text('',key='-time-',font=(cfont,40),justification='center')],
        [sg.Button('change theme',key='-theme-',size=(10,3))],
        [sg.Button('change clock font',key='-font-',size=(10,3))],
        [sg.Button('close',key='-close-',size=(10,3))]]

    return sg.Window('digital clock',layout,size=(300,250))    
    

def main():
    #preset font and theme
    cfont='Times New Roman'
    theme='Black'
    wnd=make_window(theme,cfont)

    while True:
#if you set timeout, you can operate GUI by spend time
        event,values=wnd.read(timeout=10,timeout_key='-timeout-')
        #getting current time per 10ms
        if event == '-timeout-':
            wnd['-time-'].update(now())

        if event in (sg.WIN_CLOSED,'-close-'):
            break

        #when click theme change button, open the window with pulldown menu.
        if event == '-theme-':
            #layout and window create
            event,values = sg.Window('Theme Browser',
            [[sg.Text('theme browsing')],
            [sg.Text('click theme color')],
            [sg.Combo(values=sg.theme_list(),size=(20,12),key='-LIST-',readonly=True)],
            [sg.OK(),sg.Cancel()]]).read(close=True)

            #select and click 'OK', change theme value 
            #and pass over  make_window function it
            if event == 'OK':
                theme=values['-LIST-']
                wnd.close()
                wnd= make_window(theme,cfont) 
        #when click font change button, open the window its looks like theme window
        if event == '-font-':
            #layout and window create
            event,values = sg.Window('Font Browser',
            [[sg.Text('Font browsing')],
            [sg.Text('click font')],
            [sg.Combo(values=tkinter.font.families(),size=(20,12),key='-FONT-',readonly=True)],
            # or
            # [sg.Combo(values=sg.Text.fonts_installed_list(),size=(20,12),key='-FONT-',readonly=True)],
            [sg.OK(),sg.Cancel()]]).read(close=True)

            #change font value and pass over make_window function it
            if event == 'OK':
                cfont=values['-FONT-']
                wnd.close()
                wnd= make_window(theme,cfont)
                
            
    wnd.close()

if __name__ == '__main__':
    main()