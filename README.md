# Anti-AFK Script (v1.1)

A Python script with a graphical user interface (GUI) that periodically simulates key presses to prevent being disconnected from games or other applications due to inactivity.

## ⚠️ Important Warning: Use at Your Own Risk

Using scripts to automate actions in online games almost always violates the game's **Terms of Service (ToS)**.

* **Detection:** This type of simple script is often easily detected by anti-cheat systems.
* **Consequences:** Using this script in certain games can and likely will result in your account being **permanently banned**.
* **Disclaimer:** The creator of this script is not responsible for any penalties, bans, or other consequences that result from its use.

**Proceed with extreme caution and at your own risk.**

## Features

* **Graphical Interface:** Easy-to-use GUI to start and stop the script.
* **Configurable Timers:** Set the minimum and maximum random wait time between key presses.
* **Start/Stop Toggle:** A main button to run or stop the script.
* **Pause Hotkey:** Select a global hotkey (e.g., `Ctrl+P`) to quickly pause or unpause the script without focusing the window.
* **Live Action Log:** A table displays the last 10 actions taken (key pressed and wait interval).
* **Status Indicator:** A clear label shows if the script is "Running" or "Stopped".

## Requirements

* Python 3
* `pyautogui` library
* `keyboard` library

## Installation

1.  Make sure you have Python 3 installed.
2.  Install the required libraries using pip:
    ```sh
    pip install pyautogui keyboard
    ```

## Usage

1.  Open your terminal or command prompt.
2.  Navigate to the directory where the `anti-afk.py` script is saved.
3.  Run the script:
    ```sh
    python anti-afk.py
    ```
4.  The GUI window will open.
    * **(Optional)** Adjust the **Min Sleep** and **Max Sleep** times (in seconds).
    * **(Optional)** Select your preferred **Hotkey** from the dropdown menu.
5.  Press the **"Start"** button.
    * The status will change to "Running".
    * The script will now press a random key (`w`, `a`, `s`, or `d`) at random intervals defined by your sleep times.
    * The log table will update with each action.
6.  You can use your selected **hotkey** at any time to pause (toggle to "Stopped") or unpause (toggle to "Running") the script.
7.  Press the **"Stop"** button to fully stop the script and clear the log.
