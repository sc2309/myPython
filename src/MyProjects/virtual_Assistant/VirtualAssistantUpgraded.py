import tkinter
import speech_recognition as sr
import pyttsx3
import sys
import subprocess
import random

def help():
    text = '''App Launcher: Allow me to open applications.
File Opener: Let me open files with the .txt extension using the command: "open filename.txt" (with a space between filename and extension).
Conversion Tools: Provide tools for unit conversions (cg, g, kg, ml, l, kl), currency conversions (rupees, dollars), and measuring units (cm, m, km, foot).
Random Generators: Generate random numbers and passcodes.
First Aid Assistant: Offer solutions for minor injuries such as burns, cuts, sprains, and general body pain.
Feedback: Allow me to provide feedback. and even i am capable of repeating the text you entered.'''
    return text

def recognize2():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    with microphone as source:
        label = tkinter.Label(window, text='listening...')
        label.pack()
        text_to_speech('listening')
        audio = recognizer.listen(source)
    try:
        recognized_text3 = recognizer.recognize_google(audio)
        recognized_text4 = recognized_text3
        label = tkinter.Label(window, text=recognized_text4)
        label.pack()
        return recognized_text4

    except sr.UnknownValueError:
        label = tkinter.Label(window, text="Sorry, I couldn't understand what you said.")
        label.pack()
        text_to_speech('Sorry, I could not understand what you said.')
    except sr.RequestError as e:
        label = tkinter.Label(window, text="There was an error with the request; {0}".format(e))
        label.pack()

window = tkinter.Tk()

window.title("Virtual Assistant")

window.geometry("900x900")

def text_to_speech(text):
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)  
        engine.setProperty('volume', 1.0)
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        label = tkinter.Label(window, text=f"An error occurred: {str(e)}")
        label.pack()

def start_operation(user):
    if 'help' in user:
        text2 = help()
        label = tkinter.Label(window, text=text2)
        label.pack()
        text_to_speech(text2)
    elif 'hello' in user or 'hi' in user:
        label = tkinter.Label(window, text='hello sir')
        label.pack()
        text_to_speech('hello sir')
    elif 'terminate' in user:
        sys.exit()
    elif 'notepad' in user:
        path = 'notepad.exe'
        try:
            subprocess.Popen([path])
        except FileNotFoundError:
            label = tkinter.Label(window, text="App not found. Please ensure it's installed on your PC.\nTo install it, visit the appropriate source: https://apps.microsoft.com/detail/windows-notepad/9MSMLRH6LZF3?hl=en-us&gl=IN")
            label.pack()
            text_to_speech('App not found. Please ensure it is installed on your PC. To install it, visit the appropriate source')
    elif 'chrome' in user or 'browser' in user:
        path = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
        try:
            subprocess.Popen([path])
        except FileNotFoundError:
            label = tkinter.Label(window, text="App not found. Please ensure it's installed on your PC.\nTo install it, visit the appropriate source: https://www.google.com/chrome/?brand=YTUH&gclid=CjwKCAjwyY6pBhA9EiwAMzmfwSLkDA9Oq73vYw4OS6uUNj_MXSw9md9DXwD1lB5DQc_htYV39RxXYBoCMzcQAvD_BwE&gclsrc=aw.ds") 
            label.pack()
            text_to_speech('App not found. Please ensure it is installed on your PC. To install it, visit the appropriate source')
    elif 'edge' in user:
        path = 'C:\\Program Files (x86)\\Microsoft\\Edge\Application\\msedge.exe'
        try:
            subprocess.Popen([path])
        except FileNotFoundError:
            label = tkinter.Label(window, text="App not found. Please ensure it's installed on your PC.\nTo install it, visit the appropriate source: https://www.microsoft.com/en-us/edge/download?form=MA13FJ")
            label.pack()
            text_to_speech('App not found. Please ensure it is installed on your PC. To install it, visit the appropriate source')
    elif 'excel' in user:
        path = 'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.EXE'
        try:
            subprocess.Popen([path])
        except FileNotFoundError:
            label = tkinter.Label(window, text="App not found. Please ensure it's installed on your PC.\nTo install it, visit the appropriate source: https://www.microsoft.com/en-in/microsoft-365/excel")
            label.pack()
            text_to_speech('App not found. Please ensure it is installed on your PC. To install it, visit the appropriate source')
    elif 'access' in user:
        path = 'C:\\Program Files (x86)\\Microsoft Office\\root\Office16\\MSACCESS.EXE'
        try:
            subprocess.Popen([path])
        except FileNotFoundError:
            label = tkinter.Label(window, text="App not found. Please ensure it's installed on your PC.\nTo install it, visit the appropriate source: https://www.microsoft.com/en-us/download/confirmation.aspx?id=50040")
            label.pack()
            text_to_speech('App not found. Please ensure it is installed on your PC. To install it, visit the appropriate source')
    elif 'word' in user:
        path = 'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE'
        try:
            subprocess.Popen([path])
        except FileNotFoundError:
            label = tkinter.Label(window, text="App not found. Please ensure it's installed on your PC.\nTo install it, visit the appropriate source: https://www.microsoft.com/en/microsoft-365/word?market=af")
            label.pack()
            text_to_speech('App not found. Please ensure it is installed on your PC. To install it, visit the appropriate source')
    elif 'power point' in user:
        path = 'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.EXE'
        try:
            subprocess.Popen([path])
        except FileNotFoundError:
            label = tkinter.Label(window, text="App not found. Please ensure it's installed on your PC.\nTo install it, visit the appropriate source: https://www.microsoft.com/en-in/microsoft-365/powerpoint")
            label.pack()
            text_to_speech('App not found. Please ensure it is installed on your PC. To install it, visit the appropriate source')
    elif 'untitled1' in user or 'untitled 1' in user or 'untitled one' in user:
        file_path = 'untitled1.txt'
        try:
            subprocess.Popen(['notepad.exe', file_path])
        except FileNotFoundError:
            label = tkinter.Label(window, text="The file cannot be found. Please ensure it is on your PC.")
            label.pack()
            text_to_speech('The file cannot be found. Please ensure it is on your PC.')
    elif 'untitled2' in user or 'untitled 2' in user or 'untitled two' in user:
        file_path = 'untitled2.txt'
        try:
            subprocess.Popen(['notepad.exe', file_path])
        except FileNotFoundError:
            label = tkinter.Label(window, text="The file cannot be found. Please ensure it is on your PC.")
            label.pack()
            text_to_speech('The file cannot be found. Please ensure it is on your PC.')
    elif 'untitled3' in user or 'untitled 3' in user or 'untitled three' in user:
        file_path = 'untitled3.txt'
        try:
            subprocess.Popen(['notepad.exe', file_path])
        except FileNotFoundError:
            label = tkinter.Label(window, text="The file cannot be found. Please ensure it is on your PC.")
            label.pack()
            text_to_speech('The file cannot be found. Please ensure it is on your PC.')
    elif 'untitled4' in user or 'untitled 4' in user or 'untitled four' in user:
        file_path = 'untitled4.txt'
        try:
            subprocess.Popen(['notepad.exe', file_path])
        except FileNotFoundError:
            label = tkinter.Label(window, text="The file cannot be found. Please ensure it is on your PC.")
            label.pack()
            text_to_speech('The file cannot be found. Please ensure it is on your PC.')
    elif 'untitled5' in user or 'untitled 5' in user or 'untitled five' in user:
        file_path = 'untitled5.txt'
        try:
            subprocess.Popen(['notepad.exe', file_path])
        except FileNotFoundError:
            label = tkinter.Label(window, text="The file cannot be found. Please ensure it is on your PC.")
            label.pack()
            text_to_speech('The file cannot be found. Please ensure it is on your PC.')
    elif 'repeat' in user or 'say' in user:
        text_to_speech('speak the text you want me to repeat')
        val = recognize2()
        text_to_speech(val)
    elif 'convert' in user:
        text_to_speech('Please provide the number to optimize my code. ')
        val = recognize2()
        num = int(val)
        if 'cm to m' in user or 'cl to l' in user or 'cg to g' in user:
            convert = num/100
        elif 'm to cm' in user or 'l to cl' in user or 'g to cg' in user:
            convert = num * 100
        elif 'm to km' in user or 'l to kl' in user or 'g to kg' in user:
            convert = num / 1000
        elif 'km to m' in user or 'kl to l' in user or 'kg to g' in user:
            convert = num * 1000
        elif 'cm to km' in user or 'cl to kl' in user or 'cg to kg' in user:
            convert = num / 100000
        elif 'km to cm' in user or 'kl to cl' in user or 'kg to cg' in user:
            convert = num * 100000
        elif 'cm to foot' in user:
            convert = num / 30.48
        elif 'foot to cm' in user:
            convert = num * 30.48
        elif 'm to foot' in user:
            convert = num * 3.281
        elif 'foot to m' in user:
            convert = num / 3.281
        elif 'km to foot' in user:
            convert = num * 3281
        elif 'foot to km' in user:
            convert = num / 3281
        elif 'dollar to rupees' in user or '$ to rupees' in user or 'dollars to rupees' in user:
            convert = num * 83.12
        elif 'rupees to dollar' in user or 'rupees to $' in user or 'rupees to dollars' in user:
            convert = num / 83.12
        else:
            convert = 'the option you provided is not available'
        label = tkinter.Label(window, text=convert)
        label.pack()
        text_to_speech(convert)
    elif 'number' in user:
        text_to_speech('Please enter the final number for the range')
        val = recognize2()
        gen = int(val)
        out = random.randrange(1, gen)
        label = tkinter.Label(window, text=out)
        label.pack()
    elif 'passcode' in user or 'password' in user:
        out = str(random.randrange(1,100000000))
        text_to_speech('For security reasons, I cannot disclose the passcode.')
        if len(out) < 2 and len(out) > 0:
            label = tkinter.Label(window, text=f'0000000{out}')
            label.pack()
        elif len(out) < 3 and len(out) > 1:
            label = tkinter.Label(window, text=f'000000{out}')
            label.pack()
        elif len(out) < 4 and len(out) > 2:
            label = tkinter.Label(window, text=f'00000{out}')
            label.pack()
        elif len(out) < 5 and len(out) > 3:
            label = tkinter.Label(window, text=f'0000{out}')
            label.pack()
        elif len(out) < 6 and len(out) > 4:
            label = tkinter.Label(window, text=f'000{out}')
            label.pack()
        elif len(out) < 7 and len(out) > 5:
            label = tkinter.Label(window, text=f'00{out}')
            label.pack()
        elif len(out) < 8 and len(out) > 6:
            label = tkinter.Label(window, text=f'0{out}')
            label.pack()
        else:
            label = tkinter.Label(window, text=out)
            label.pack()
    elif 'feedback' in user:
        text_to_speech('speak the feedback')
        feedback = recognize2()
        file_name = 'feedback.txt'
        with open(file_name, "a") as file:
            file.write("\n" + feedback)
        label = tkinter.Label(window, text='feedback saved!')
        text_to_speech('feedback saved! ')
    elif 'burns' in user or 'burn' in user:
        sol = '''Remove any items or accessories near site of injury such as watch or jewellery. However do not remove if
                the item is stuck to the skin as this will worsen the situation. 
                Place the scalded area under running tap water for 10-20 minutes. Avoid placing ice cubes or ice water as
                the sudden change in temperature may worsen the situation. Plus, the ice could have been in the freezer next
                to your uncooked food and may contain bacteria. 
                Dab dry the wet areas surrounding the injury with a clean cloth. Avoid using fibrous items such as tissue,
                which may stick on the scalded area. 
                Resist from popping any blisters that may form, the intact skin serves as protection from getting an open wound infection. 
                Do not apply any type of ointment, cream or “home remedies” such as toothpaste that is not prescribed by a doctor.
                Incorrect medication will slow the release of heat from the scalded area and prolong injury. 
                Cover the scalded area loosely with non-stick dressing or clean plastic cling wrap. Consult a doctor if redness
                or pain continues for more than a few hours.'''
        label = tkinter.Label(window, text=sol)
        label.pack()
        text_to_speech(sol)
    elif 'cuts' in user or 'cut' in user:
        sol = '''Wash the injured area with soap and water to remove any debris (if possible). Dab dry with clean cloth.
                Avoid using fibrous items such as tissue, which may stick on the injury and worsen it. 
                Cover injured area with a clean cloth and apply pressure for about 5 minutes. 
                Check the injured area. Proceed with second application of pressure for another 5 minutes if bleeding still occurs. 
                You can apply an antiseptic ointment before covering the cut with a band-aid or non-stick dressing.'''
        label = tkinter.Label(window, text=sol)
        label.pack()
        text_to_speech(sol)
    elif 'sprain' in user:
        sol = '''Rest the sprained area to prevent it from worsening. 
                Place ice on the sprained area for not more than 20 minutes. It can be done every three hours to relief some
                swelling and pain. 
                Bandage the sprained area to keep it immobilised and supported. Do not wrap too tightly as this constricting
                effect may impede blood circulation. 
                Raise the sprained area when possible as it will help in blood circulation and reduce swelling. For example,
                place a pillow to support ankle / leg when sleeping or elevate legs on another chair when sitting down.'''
        label = tkinter.Label(window, text=sol)
        label.pack()
        text_to_speech(sol)
    elif 'pain' in user:
        sol = '''Rest and elevate the painful area. 
                Alternate between ice packs to reduce inflammation and heat to improve blood flow. 
                Soak in a warm bath or take a warm shower. 
                Take over-the-counter pain relievers (aspirin, acetaminophen, ibuprofen, naproxen). 
                Try complementary therapies, such as massage, meditation or acupuncture.'''
        label = tkinter.Label(window, text=sol)
        label.pack()
        text_to_speech(sol)
    else:
        label = tkinter.Label(window, text='Retry the operation; the previous option is not available.')
        label.pack()
        text_to_speech('Retry the operation; the previous option is not available.')

label = tkinter.Label(window, text="Hello, I am your virtual assistant. Please provide me with an operation to perform")
label.pack()
label = tkinter.Label(window, text='say \'terminate\' to exit')
label.pack()
button = tkinter.Button(window, text="Give Command!")
button.pack()

def recognize():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    with microphone as source:
        label = tkinter.Label(window, text='listening...')
        label.pack()
        text_to_speech('listening')
        audio = recognizer.listen(source)
    try:
        recognized_text = recognizer.recognize_google(audio)
        recognized_text2 = recognized_text.lower()
        label = tkinter.Label(window, text=recognized_text2)
        label.pack()
        start_operation(recognized_text2)

    except sr.UnknownValueError:
        label = tkinter.Label(window, text="Sorry, I couldn't understand what you said.")
        label.pack()
        text_to_speech('Sorry, I could not understand what you said.')
    except sr.RequestError as e:
        label = tkinter.Label(window, text="There was an error with the request; {0}".format(e))
        label.pack()

button.config(command=recognize)
text_to_speech('hello, I am your virtual assistant. Please provide me with an operation to perform')
window.mainloop()