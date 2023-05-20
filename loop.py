import pyautogui as py
import time
message= " AbhiRaj gand deta hai sabse bada gandi hai"
 
cnt= 1

time.sleep(2)

for i in range(1000):
    py.typewrite(message + " " +str(cnt))
    py.press('Enter')
    cnt = cnt+1

py.typewrite("abhiraj ki gand ka price 5 paise hai")
py.press('Enter')
