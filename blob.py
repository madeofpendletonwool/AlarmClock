import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices)
for voice in voices:
    print(voice, voice.id)
    engine.setProperty('voice', voice.id)
    engine.say("Hello world")
    engine.runAndWait()
    engine.stop()