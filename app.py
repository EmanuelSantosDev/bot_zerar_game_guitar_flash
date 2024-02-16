import pyautogui
import keyboard
from time import sleep


# continua executando enquanto a tecla "1" não for pressionada
while keyboard.is_pressed('1') == False:
    # procurando a cor 'verde'
    if pyautogui.pixelMatchesColor(1114, -266, (0, 152, 0)):
        pyautogui.press('a')
        sleep(0.05)
    # procurando a cor 'amarela'
    elif pyautogui.pixelMatchesColor(1203, -260, (255, 0, 0)):
        pyautogui.press('s')
        sleep(0.05)
    # procurando a cor 'vermelha'
    elif pyautogui.pixelMatchesColor(1291, -266, (244, 244, 2)):
        pyautogui.press('j')
        sleep(0.05)