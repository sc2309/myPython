import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    text = input("Enter the text you want the computer to speak: ")
    text_to_speech(text)