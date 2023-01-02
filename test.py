import pyttsx3
speak_volume = '100%'

if speak_volume == '25%':
    newVolume = .3
elif speak_volume == '50%':
    newVolume = .5
elif speak_volume == '75%':
    newVolume = .7
elif speak_volume == '100%':
    newVolume = 1

#Get Current Time
# wake_current = now(Set_Format, 'time')


engine = pyttsx3.init()
engine.setProperty('rate', 115)
engine.setProperty('volume', newVolume)
engine.setProperty('voice', 'english-us')

engine.say(f'The time is')
engine.runAndWait()