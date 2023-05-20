import pyautogui as py
import time
message= "hi"
 
cnt= 1

time.sleep(2)

for i in range(1000):
    py.typewrite(message + " " +str(cnt))
    py.press('Enter')
    cnt = cnt+1

py.typewrite("hellow")
py.press('Enter')
