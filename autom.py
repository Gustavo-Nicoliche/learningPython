import pyautogui

print('Resolução da tela: ', pyautogui.size())
print('Posição atual do mouse: ', pyautogui.position())

pixelcolor = pyautogui.pixel(100, 200)
print('Cor do pixel (100, 200): ', pixelcolor)