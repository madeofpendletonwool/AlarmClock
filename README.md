<p align="center">
  <img width="340" height="300" src="./images/Alarm_Clock.png">
</p>

# pyArmClock

- [pyArmClock](#AlarmClock)
  - [Features](#Features)
  - [Hosting](#Hosting)
  - [Installing/Running](#Installing/Running)
  - [ToDo](#ToDo)
  - [Platform Availability](#Platform-Availability)
      
A quick and dirty python based alarm clock with a GUI and alarm saving functionality

## Features
Basic Alarm funtionality with a GUI currently implemented. Run with Python.

## Hosting


## Installing/Running

#### There's two options for install - Manual and Automated with Ansible
I recommend the automated install

#### **Raspberry Pi Automated Install:**


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

#### **:**

#### **Manual Install:**

*Seriously I don't recommend this. It's kinda awful with all the commands needed*

*Instructions for this method a work in progress*

## ToDo

 - [x] Create Code that can set off Alarms using a time module
 - [x] Snooze funtionality
 - [x] Deploy via ansible and fully setup using raspberry pi
 - [ ] Easy setup with package management
 - [ ] Allow for saving of alarms after reboot
 - [ ] Display a big clock on the screen at all times
 - [ ] Dockerize (Probably?)
 - [x] Create alarm clock gui
 - [ ] arm it. Need it to run on a raspberry pi
 - [ ] Voice function to tell actual time
 - [x] Sound function
 - [x] Allow you to choose music/sound to play
 - [x] import of music from a location of choice 

## Platform Availability

Raspberry Pi and x86 Systems 