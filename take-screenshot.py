#pip install pyautogui
#pip install keyboard
#pip install random

import pyautogui
import keyboard
import random as ran

while True:
    if keyboard.is_pressed("Alt + s"):
        screen_shot = pyautogui.screenshot(f"screenshot({int(ran.uniform(1,10000))}).png")
        print("screenshot saved")
