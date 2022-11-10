import pyautogui
from time import sleep


def acessar_modulo_admissao_preliminar():
    pyautogui.hotkey('alt', 'a')
    sleep(1)
    pyautogui.hotkey('d')