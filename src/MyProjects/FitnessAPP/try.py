import datetime
import pytz

# Set the time zone to IST
ist = pytz.timezone('Asia/Kolkata')

# Get the current time in IST
current_time_ist = datetime.datetime.now(ist)

# Extract the hours from the time
current_time_hours = current_time_ist.hour

print(f'Current time in IST (hours only): {current_time_hours} hours')
