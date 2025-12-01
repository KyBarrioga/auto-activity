import pyautogui
import time
import random
import sys

pyautogui.FAILSAFE = True   # keep this on for safety (move to top-left to abort)
pyautogui.PAUSE = 0.1       # small automatic pause after actions

print('Mouse mover script started. Press Ctrl+C to stop or move mouse to top-left corner.')
print('Running diagnostics so you can see move+click attempts.')

screenWidth, screenHeight = pyautogui.size()
print(f"Screen size detected: {screenWidth} x {screenHeight}")

try:
    while True:
        x = random.randint(0, screenWidth - 1)
        y = random.randint(0, screenHeight - 1)

        print(f"Moving to: ({x}, {y})")
        pyautogui.moveTo(x, y, duration=0.25)

        # tiny extra pause to ensure the OS has updated the pointer
        time.sleep(0.05)

        # explicit down/up click (left button)
        try:
            pyautogui.mouseDown(button='left')
            time.sleep(0.03)            # hold down briefly
            pyautogui.mouseUp(button='left')
            print("Click attempted (mouseDown/mouseUp).")
        except Exception as e:
            print("Click failed with exception:", e)

        # confirm actual current mouse position reported by OS
        cur_x, cur_y = pyautogui.position()
        print(f"Current pos after click: ({cur_x}, {cur_y})")

        # wait before next move
        time.sleep(5)

except KeyboardInterrupt:
    print('\nScript stopped by user (KeyboardInterrupt).')
    sys.exit(0)
except pyautogui.FailSafeException:
    print('\nScript stopped by pyautogui failsafe (mouse moved to top-left).')
    sys.exit(0)