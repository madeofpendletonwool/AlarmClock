import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 115)
engine.setProperty('voice', 'english-us')

engine.say('The time is 08:35 PM')
engine.runAndWait()
