import pyautogui
from pynput import mouse
import time
import random

# File to store mouse movements and clicks
log_file = "mouse_log.txt"

# Open the log file in append mode
with open(log_file, "a") as f:
    f.write("Mouse Log\n\n")

    # Define function to log mouse events
    def on_click(x, y, button, pressed):
        if pressed:
            f.write(f"Click at position: ({x}, {y})\n")
        else:
            f.write(f"Release at position: ({x}, {y})\n")

    # Register the mouse event handler
    listener = mouse.Listener(on_click=on_click)
    listener.start()

    # Set the flag coordinates
    flag_coordinates = [
        (288, 798),  # First click position
        (926, 757),  # Second click position
        (1095, 902)  # Third click position
    ]

    # Iterate through each flag coordinate
    for i in "bcdef":
        for j in "0123456789abcdef":
            # Scroll the mouse wheel
            pyautogui.scroll(10)

            # Move to the first click position
            pyautogui.moveTo(*flag_coordinates[0], duration=random.uniform(2, 3))

            # Click at the first click position
            pyautogui.click()

            # Wait for a random duration
            time.sleep(random.uniform(1, 2))

            # Move to the second click position
            pyautogui.moveTo(*flag_coordinates[1], duration=random.uniform(2, 3))

            # Click at the second click position
            pyautogui.click()

            # Wait for a random duration
            time.sleep(random.uniform(1, 2))

            # Write text
            pyautogui.write('emma-worship-' + i + j)

            # Wait for a random duration
            time.sleep(random.uniform(1, 2))

            # Move to the third click position
            pyautogui.moveTo(*flag_coordinates[2], duration=random.uniform(2, 3))

            # Click at the third click position
            pyautogui.click()

            # Wait for a random duration
            time.sleep(random.uniform(1, 2))

# Print a message when the script completes
print("Flag drawing completed. Mouse events logged in:", log_file)
