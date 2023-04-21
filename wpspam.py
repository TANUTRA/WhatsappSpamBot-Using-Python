import pyautogui
import time
time.sleep (4)
count=0
while count<=10:
    pyautogui.typewrite("hello bhai !!")
    pyautogui.press ("enter")
    count=count+1