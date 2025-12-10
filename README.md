[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

# Python Mouse & Keyboard Activity

A simple Python script that keeps your system active by randomly moving the mouse and perform keyboard actions.
This script includes diagnostics so you can see the exact movements and click attempts and keyboard activities.

> ⚠️ **Failsafe enabled:** Move your mouse to the **top-left corner** or press **Ctrl + C** in the terminal to immediately stop the script.

---

## 📌 Features

- Random mouse movement within your full screen resolution  
- Mouse and keyboard simulation using PyAutoGUI and Pynput
- Real-time diagnostic logs (movement, clicks, current position)
- Function failsafe for safety  
- Adjustable timing and behavior (easily customizable)

---

## 🛠 Requirements

- Python **3.x**
- `pyautogui` library
- `pynput` library

Install PyAutoGUI and Pynput using:

```bash
pip install pyautogui
```
```bash
pip install pynput
```

---

## ▶️ Run the script

```python
python auto_activity.py
```
