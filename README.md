<p align="center">
  <img width="340" height="300" src="./images/Alarm_Clock.png">
</p>

# AlarmClock

- [AlarmClock](#AlarmClock)
  - [Features](#Features)
  - [Hosting](#Hosting)
  - [Installing/Running](#Installing/Running)
  - [ToDo](#ToDo)
  - [Platform Availability](#Platform-Availability)
      
A quick and dirty python based alarm clock with a GUI and alarm saving functionality

## Features
Basic Alarm funtionality with a GUI currently implemented. Run with Python.

## Hosting
N/A

## Installing/Running

#### There's two options for install - Manual and Automated with Ansible
I recommend the automated install

#### **Automated Install:**


Update!
```
sudo apt update
```
Install Ansible
```
sudo apt install ansible
```
Now, pull the Git repo
```
git clone https://github.com/madeofpendletonwool/AlarmClock.git
```
cd into the pulled folder
```
cd AlarmClock/
```
Lastly, run the playbook to set everything up
```
ansible-playbook setup.yaml
```

#### **Manual Install:**

*Seriously I don't recommend this. It's kinda awful with all the commands needed*

Reqired dependancies: 
- PySimpleGUI
- playsound
Install and run with

```
pip install pysimplegui pyglet pyyaml
python alarm.py
```

## ToDo

 - [x] Create Code that can set off Alarms using a time module
 - [x] Snooze funtionality
 - [ ] Deploy via ansible and fully setup using raspberry pi
 - [ ] Easy setup with package management
 - [ ] Allow for saving of alarms after reboot
 - [ ] Dockerize (Probably?)
 - [ ] Create alarm clock gui
 - [ ] arm it. Need it to run on a raspberry pi
 - [ ] Voice function to tell actual time
 - [x] Sound function - 
 - [ ] Allow you to choose music/sound to play
 - [ ] import of music from a location of choice 

## Platform Availability

Raspberry Pi (Coming Soon) and x86 Systems 