[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

# Python Mouse Mover & Auto Clicker

A simple Python script that keeps your system active by randomly moving the mouse and performing a left-click.  
This script includes diagnostics so you can see the exact movements and click attempts in real-time.

> ⚠️ **Failsafe enabled:** Move your mouse to the **top-left corner** or press **Ctrl + C** in the terminal to immediately stop the script.

---

## 📌 Features

- Random mouse movement within your full screen resolution  
- Left-click simulation using `mouseDown` + `mouseUp`  
- Real-time diagnostic logs (movement, clicks, current position)
- Built-in PyAutoGUI failsafe for safety  
- Adjustable timing and behavior (easily customizable)

---

## 🛠 Requirements

- Python **3.x**
- `pyautogui` library

Install PyAutoGUI using:

```bash
pip install pyautogui
