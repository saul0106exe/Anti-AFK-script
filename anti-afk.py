import tkinter as tk
from tkinter import ttk
import pyautogui
import random
import time
import threading
import keyboard 

class AntiAFKGUI:
    def __init__(self, root):
        self.root = root
        root.title("Anti-AFK Script")

        self.running = False
        self.min_sleep = tk.StringVar(value="3")
        self.max_sleep = tk.StringVar(value="5")
        self.hotkey = tk.StringVar(value="Ctrl+P")
        self.log_data = []

        self.running_label = ttk.Label(root, text="Stopped", foreground="red")
        self.running_label.grid(row=0, column=0, columnspan=2)

        ttk.Label(root, text="Min Sleep (sec):").grid(row=1, column=0, sticky="w")
        ttk.Entry(root, textvariable=self.min_sleep).grid(row=1, column=1)

        ttk.Label(root, text="Max Sleep (sec):").grid(row=2, column=0)
        ttk.Entry(root, textvariable=self.max_sleep).grid(row=2, column=1)

        ttk.Label(root, text="Hotkey (Pause/Unpause):").grid(row=3, column=0)
        ttk.Entry(root, textvariable=self.hotkey).grid(row=3, column=1)
        self.hotkey_combo = ttk.Combobox(root, textvariable=self.hotkey, 
                                         values=["Ctrl+P", "Ctrl+Q", "Ctrl+Shift+P", "F9"], 
                                         state="readonly")
        self.hotkey_combo.grid(row=3, column=1)

        self.start_stop_button = ttk.Button(root, text="Start", command=self.toggle_script)
        self.start_stop_button.grid(row=4, column=0, columnspan=2)

        self.table_frame = ttk.Frame(root)
        self.table_frame.grid(row=5, column=0, columnspan=2)
        self.table_headers = ["Key", "Interval (sec)"]
        for i, header in enumerate(self.table_headers):
            ttk.Label(self.table_frame, text=header).grid(row=0, column=i)
        
        self.table_row_widgets = []
        for i in range(10):
            key_label = ttk.Label(self.table_frame, text="")
            interval_label = ttk.Label(self.table_frame, text="")
            key_label.grid(row=i + 1, column=0, sticky="w", padx=5)
            interval_label.grid(row=i + 1, column=1, sticky="w", padx=5)
            self.table_row_widgets.append((key_label, interval_label))

        self.error_label = ttk.Label(root, text="", foreground="red")
        self.error_label.grid(row=6, column=0, columnspan=2)

        self.protocol = None

    def toggle_script(self):
        self.running = not self.running
        if self.running:
            self.running_label.config(text="Running", foreground="green")
            self.start_stop_button.config(text="Stop")
            self.register_hotkey()
            self.anti_afk_thread = threading.Thread(target=self.anti_afk_loop, daemon=True)
            self.anti_afk_thread.start()
        else:
            self.stop_script()

    def stop_script(self):
        self.running = False
        self.running_label.config(text="Stopped", foreground="red")
        self.start_stop_button.config(text="Start")
        self.unregister_hotkey()
        self.log_data.clear()
        self.update_table()

    def anti_afk_loop(self):
        keys = ['w', 'a', 's', 'd']
        while self.running:
            try:
                min_sleep = float(self.min_sleep.get())
                max_sleep = float(self.max_sleep.get())
                sleep_duration = random.uniform(min_sleep, max_sleep)
            except ValueError:
                print("Invalid sleep duration. Please enter a number.")
                self.show_error("Invalid sleep duration. Please enter a number.")
                return

            key_to_press = random.choice(keys)
            pyautogui.press(key_to_press)
            print(f"Pressed '{key_to_press}'. Waiting for {sleep_duration:.2f} seconds.")
            if len(self.log_data) >= 10:
                self.log_data.pop(0)
            self.log_data.append((key_to_press, sleep_duration))
            self.update_table()
            time.sleep(sleep_duration)

    def update_table(self):
        log_to_display = list(reversed(self.log_data))
        for i in range(10):
            key_label, interval_label = self.table_row_widgets[i]
            if i < len(log_to_display):
                key, interval = log_to_display[i]
                key_label.config(text=key)
                interval_label.config(text=f"{interval:.2f}")
            else:
                key_label.config(text="")
                interval_label.config(text="")

    def register_hotkey(self):
        try:
            self.protocol = keyboard.add_hotkey(self.hotkey.get(), self.toggle_script)
        except ValueError:
            self.show_error("Invalid hotkey. Please enter a valid hotkey.")
            self.stop_script()

    def unregister_hotkey(self):
        if self.protocol is not None:
            keyboard.remove_hotkey(self.protocol)

    def show_error(self, message):
        self.error_label.config(text=message)

if __name__ == "__main__":
    root = tk.Tk()
    gui = AntiAFKGUI(root)
    root.mainloop()
