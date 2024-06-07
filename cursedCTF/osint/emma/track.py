import pyautogui
import time
import random

"""
while True:
    print( pyautogui.position())
"""


for i in "bcdef":
    for j in "0123456789abcdef":
        pyautogui.scroll(10) 
        x,y = (288,798)
        time.sleep(2)
        pyautogui.moveTo(x, y,random.randrange(2,3))
        pyautogui.scroll(10) 
        pyautogui.scroll(10) 
        pyautogui.scroll(10) 
        pyautogui.scroll(10) 
        pyautogui.scroll(10) 
        pyautogui.scroll(10) 
        pyautogui.scroll(10) 
        pyautogui.scroll(10) 
        pyautogui.scroll(10) 

        pyautogui.moveTo(x, y,random.randrange(2,3))
        pyautogui.click()

        time.sleep(random.randrange(1,2))
        x,y = (926, 757)
      
        pyautogui.moveTo(x, y,random.randrange(2,3))
        pyautogui.click()
        time.sleep(random.randrange(1,2))

        pyautogui.write('emma-worship-'+i+j)  

        time.sleep(random.randrange(1,2))

        x,y = (1095,902)
        pyautogui.moveTo(x, y,random.randrange(2,3))
        pyautogui.click()