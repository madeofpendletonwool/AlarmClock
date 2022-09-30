<p align="center">
  <img width="340" height="300" src="./images/Alarm_Clock.png">
</p>

# pyArmClock

- [pyArmClock](#AlarmClock)
  - [Features](#Features)
  - [Hosting](#Hosting)
  - [Installing](#Installing)
  - [ToDo](#ToDo)
  - [Platform Availability](#Platform-Availability)
      
A quick and dirty python based alarm clock with a GUI and alarm saving functionality. Allows for choosing of song/audio that you wake up to and can speak the time before playing the audio. Works great on a raspberry pi as well as other linux based OS's with automated setup using ansible.

## Features
- Alarm Functionality
- Song Choice
- Setup Automation
- Custom Snooze Duration (10 mins by Default)
- GUI with custom themes implemented
- Large List of Custom Clock Fonts
- Saves previous theme, font, and song choice in config file after reboots
- Saves up to 3 Alarms with custom names - More will be implemented in the furture

## Installing

#### There's two options for instalation on a Raspberry Pi - Automated with Ansible and install an image directly to an sd card

The ansible install is a little more hands on and can be seen a bit of a learning experience. They both work great though. 

#### **Raspberry Pi Automated Ansible Install:**
NOTE: No ansible knowledge is really needed. Just run these commands exactly.

Simply get a raspberry pi going with the base 32-bit raspberry pi os on it. Leave the user as the default 'pi'. Connect it to the internet and ssh into it. Run these commands next.


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
git clone https://github.com/madeofpendletonwool/pyArmClock.git
```
cd into the pulled folder
```
cd pyArmClock/
```
Lastly, run the playbook to set everything up
```
ansible-playbook setup.yaml
```
Reboot!
```
sudo reboot 0
```
#### **Raspberry Pi Image Install**
This method is a work in progress
#### **x86 Computer Install:**
The intention here is that you can install the alarm clock on anything, regardless of platform or architechture. I may add more options down the road as well for CPU architecture. The instructure are almost the same as with raspberry pi. Just a different playbook. 

Also note that while I tried to make this agnostic of distro, package names vary, and you may need to install some packages manaully/change the playbook. Some basic ansible knowledge might be helpful. 

First, Install ansible - I assume you can handle this based on your distro package management.

Now, pull the Git repo
```
git clone https://github.com/madeofpendletonwool/pyArmClock.git
```
cd into the pulled folder
```
cd pyArmClock/
```
Use your editor of choice to open vars.yml and edit the user to reflect yourself.
```
user_name: your_user_name
```
Lastly, run the playbook to set everything up
```
ansible-playbook x86setup.yaml
```
Reboot!
```
sudo reboot 0
```


## ToDo

 - [x] Create Code that can set off Alarms using a time module
 - [x] Snooze functionality
 - [x] Custom Snooze Duration
 - [x] Deploy via ansible and fully setup using raspberry pi
 - [x] Allow for saving of alarms after reboot
 - [x] Display a big clock on the screen at all times
 - [x] Create alarm clock gui
 - [x] Custom GUI Themes
 - [x] arm it. Need it to run on a raspberry pi
 - [x] Sound function
 - [x] Allow you to choose music/sound to play
 - [x] import of music from a location of choice 
 - [x] Option to select 12 or 24 hour clock
 - [x] Voice function to tell actual time
 - [x] Make theme, previous song choice, and font all write to a yaml file so they continue for each reboot
 - [x] Add a 'Alarm set for:' display after alarm is set
 - [x] Implement 'Full Screen Mode' to play in better with Raspberry Pi. This will ask on first boot if full screen mode is desired. 
 - [x] Support for music files other than mp3's (Can now also select flac files)
 - [ ] Show next alarm time while snoozed
 - [ ] Custom Pi image that can be deployed using an img file
 - [ ] Easy setup with package management
 - [ ] Check is values are populated (This will prevent crashing)

## Platform Availability

Raspberry Pi and x86 Systems 