import os, random, time, pyautogui

pyautogui.PAUSE = 0.2
pyautogui.FAILSAFE = True

try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)

except:
    os.system('cls' if os.name == 'nt' else 'clear')
