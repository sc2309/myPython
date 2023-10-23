import time

def timer():
    # Set the duration of the timer in seconds
    duration = 120  # 2 minutes

    # Start the timer
    start_time = time.time()

    # Calculate the end time
    end_time = start_time + duration

    print("Timer started for 2 minutes.")

    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        print(f"Time remaining: {remaining_time} seconds", end='\r')
        time.sleep(1)  # Update the timer display every second

    print("\nTimer completed! 2 minutes have passed.")
