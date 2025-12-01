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




# import pyautogui
# import time
# import math
# import random
# import sys
# from pynput.keyboard import Controller, Key

# pyautogui.FAILSAFE = False
# pyautogui.PAUSE = 1

# def mover_mouse_y_teclas(duracion_minutos, radio=None):
#     keyboard = Controller()
#     ancho, alto = pyautogui.size()
#     if radio is None:
#         radio = min(ancho, alto) // 2
#     centro_x, centro_y = ancho // 2, alto // 2
#     inicio = time.time()
#     duracion_segundos = duracion_minutos * 60 if duracion_minutos > 0 else float('inf')

#     click_counter = 0
#     proxima_pausa = time.time() + random.uniform(240, 300) # Random break every 4-5 mins

#     try:
#         while time.time() - inicio < duracion_segundos:
#             ahora = time.time()
#             if ahora >= proxima_pausa:
#                 # Take a short random pause
#                 pausa_duracion = random.uniform(5, 15)
#                 time.sleep(pausa_duracion)
#                 proxima_pausa = time.time() + random.uniform(240, 300)
#                 continue

#             # Simulate mouse movement
#             max_dist = max(30, int(radio * 0.7))
#             distancia = random.randint(20, max_dist)
#             angulo = random.uniform(0, 2 * math.pi)
#             x = centro_x + distancia * math.cos(angulo)
#             y = centro_y + distancia * math.sin(angulo)

#             pyautogui.moveTo(x, y, duration=0.6 + random.random() * 0.5)
#             click_counter += 1

#             # Simulate clicks
#             if click_counter >= random.randint(8, 18):
#                 time.sleep(0.2 + random.random() * 0.3)
#                 pyautogui.click(button='left')
#                 click_counter = 0
#                 time.sleep(0.3 + random.random() * 0.5)

#             # Simulate keyboard activity (Alt+Tab, Ctrl+Tab, Scroll)
#             prob = random.random()
#             if prob < 0.05:
#                 with keyboard.pressed(Key.alt):
#                     keyboard.press(Key.tab)
#                     time.sleep(0.1)
#                     keyboard.release(Key.tab)
#             elif prob < 0.08:
#                 with keyboard.pressed(Key.ctrl):
#                     keyboard.press(Key.tab)
#                     time.sleep(0.1)
#                     keyboard.release(Key.tab)
#             elif prob < 0.12:
#                 direction = random.choice([1, -1])
#                 scroll_amount = random.randint(1, 3)
#                 pyautogui.scroll(direction * scroll_amount)

#             time.sleep(1.5 + random.random() * 1.5)

#     except KeyboardInterrupt:
#         pass


# if __name__ == "__main__":
#     duracion = 0
#     if len(sys.argv) > 1:
#         try:
#             duracion = float(sys.argv[1])
#         except ValueError:
#             duracion = 0
#     try:
#         mover_mouse_y_teclas(duracion)
#     except KeyboardInterrupt:
#         pass