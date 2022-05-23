#pip install pyautogui
import pyautogui
#pip install keyboard
import keyboard
#pip install time
import time
#pip install random
import random as ran
#pip install os
import os

var = f"screenshot{int(ran.uniform(1,10000))}.png"
while True:
    if keyboard.is_pressed("Alt + s"):
        screen_shot = pyautogui.screenshot(var)
        print("screenshot taked")
        time.sleep(1)
        os.system(var)
