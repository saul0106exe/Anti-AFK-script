# Anti-AFK Script

A simple Python script that periodically simulates key presses to prevent being disconnected from games or other applications due to inactivity.

## How it Works

This script uses the `pyautogui` library to simulate a key press.
* It randomly chooses one of the following keys: `w`, `a`, `s`, or `d`.
* It waits for a random duration between 3 and 5 seconds.
* It "presses" the chosen key.
* The script repeats this process in an infinite loop until it is manually stopped.

## ⚠️ Important Warning: Use at Your Own Risk

Using scripts to automate actions in online games almost always violates the game's **Terms of Service (ToS)**.

* **Detection:** This type of simple script is often easily detected by anti-cheat systems.
* **Consequences:** Using this script in certain games can and likely will result in your account being **permanently banned**.
* **Disclaimer:** The creator of this script is not responsible for any penalties, bans, or other consequences that result from its use.

**Proceed with extreme caution and at your own risk.**

## Requirements

* Python 3
* `pyautogui` library

## Installation

1.  Make sure you have Python 3 installed.
2.  Install the `pyautogui` library using pip:
    ```sh
    pip install pyautogui
    ```

## Usage

1.  Open your terminal or command prompt.
2.  Navigate to the directory where the `anti-afk.py` script is saved.
3.  Run the script:
    ```sh
    python anti-afk.py
    ```
4.  The script will start running immediately and will print its actions to the console.
5.  To **stop** the script, go back to the terminal window and press **Ctrl+C**.
