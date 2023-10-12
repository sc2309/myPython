import pyttsx3

def voiceProducer(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()