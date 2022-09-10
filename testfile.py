import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
[sg.FileBrowse()]
# All the stuff inside your window.

layout = [[sg.Text("Choose a file: "), sg.FileBrowse()]]

# Create the Window
window = sg.Window('Window Title', layout)
