import pyautogui
import random
import time

print("Anti-AFK script has started.")
print("Press Ctrl+C in the terminal to stop the program.")

try:
    while True:
        keys = ['w', 'a', 's', 'd']

        key_to_press = random.choice(keys)

        sleep_duration = random.uniform(3, 5)

        pyautogui.press(key_to_press)
        print(f"Pressed '{key_to_press}'. Waiting for {sleep_duration:.2f} seconds.")

        time.sleep(sleep_duration)
except KeyboardInterrupt:
    print("\nAnti-AFK script has been stopped.")