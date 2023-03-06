import pyautogui
import time
with open("pf24.txt",'r') as f:
    pf24 = [[str(entry) for entry in line.split()] for line in f.readlines()]
    lista24 = pf24
with open("pf25.txt", 'r') as f:
    pf25 = [[str(entry) for entry in line.split()] for line in f.readlines()]
    lista25 = pf25
pyautogui.PAUSE = 3
pyautogui.press ("win")
time.sleep(2)
pyautogui.write ("chrome")
time.sleep(2)
pyautogui.press ("enter")
time.sleep(2)
pyautogui.hotkey ("ctrl","shift","n")
time.sleep(2)
#laço de repeticao
for info1 in lista25:
    pyautogui.hotkey("ctrl", "t")
    pyautogui.write(info1[0])
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.click(x=460, y=522)
    time.sleep(1)
    pyautogui.click(x=484, y=670)
    time.sleep(1)
    pyautogui.click(x=680, y=409)
    pyautogui.write(info1[1])
    pyautogui.press("tab")
    pyautogui.write(info1[2])
    pyautogui.press("enter")
    pyautogui.time.sleep(3)
    pyautogui.click(x=911, y=130)
    pyautogui.click(x=928, y=231)
    pyautogui.time.sleep(2)
    pyautogui.click(x=441, y=627)
for info in lista24:
    pyautogui.hotkey("ctrl", "t")
    pyautogui.write(info[0])
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.click(x=460, y=522)
    time.sleep(1)
    pyautogui.click(x=484, y=670)
    time.sleep(1)
    pyautogui.click(x=680, y=409)
    pyautogui.write(info[1])
    pyautogui.press("tab")
    pyautogui.write(info[2])
    pyautogui.press("enter")
    pyautogui.time.sleep(3)
    pyautogui.click(x=911, y=130)
    pyautogui.click(x=928, y=231)
    pyautogui.time.sleep(2)
    pyautogui.click(x=438, y=545)

