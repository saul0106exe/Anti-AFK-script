# Changelog

All notable changes to this project will be documented in this file.

## [v1.1] - 2025-11-04

### Added

* **Graphical User Interface (GUI):** Replaced the command-line-only script with a user-friendly GUI built using `tkinter`.
* **Configurable Timers:** Users can now set the "Min Sleep" and "Max Sleep" intervals directly in the app.
* **Global Hotkey:** Added a dropdown to select a global hotkey (using the `keyboard` library) to quickly pause or unpause the script.
* **Live Action Log:** Added a table to the GUI that displays the 10 most recent actions (key pressed and wait interval).
* **Status Indicator:** A label clearly shows if the script is "Running" (green) or "Stopped" (red).
* **Error Handling:** Added basic error messages for invalid inputs, such as non-numeric sleep times.

### Changed

* **Threading:** The core anti-AFK loop now runs in a separate thread (`threading`) to keep the GUI responsive.
* **Dependencies:** Added the `keyboard` library as a new requirement.
* **Toggle Function:** The script is now started/stopped via a GUI button or hotkey, rather than requiring `Ctrl+C` in a terminal.

---

## [v1.0] - 2025-11-04

### Added

* Initial release.
* Simple command-line Python script.
* Uses `pyautogui` to press a random key (`w`, `a`, `s`, or `d`).
* Waits for a random duration between 3 and 5 seconds.
* Prints all actions directly to the console.
