import tkinter as tk
import datetime
import pytz

def currentTime():

    # Set the time zone to IST
    ist = pytz.timezone('Asia/Kolkata')

    # Get the current time in IST
    current_time_ist = datetime.datetime.now(ist)

    # Extract the hours from the time
    current_time_hours = current_time_ist.hour

    return current_time_hours

if __name__ == '__main__':
    root = tk.Tk()

    root.title("Virtual Assistant")

    root.geometry("900x900")
    present_time = currentTime()
    if present_time <= 11 and present_time > 0:
        wish = 'good morning'
    elif present_time >= 12 and present_time < 18:
        wish = 'good afternoon'
    elif present_time >= 18 and present_time < 24:
        wish = 'good evening'
    label = tk.Label(root, text=f"{wish} sir please select an option\nDo push ups\nDo squats\n")
    label.pack()
    root.mainloop()