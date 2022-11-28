import time
import pyautogui
import webbrowser


time.sleep(3)


url = 'https://profile.intra.42.fr/'
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
webbrowser.get(chrome_path).open(url)

time.sleep(3)

pyautogui.moveTo(1340, 140)
pyautogui.click()

time.sleep(1)
pyautogui.moveTo(1340, 188)
pyautogui.click()

time.sleep(1)
pyautogui.scroll(-500)

pyautogui.moveTo(800, 500)

pyautogui.scroll(500)
time.sleep(1)

pyautogui.moveTo(1160, 500)

pyautogui.moveTo(1160, 774)
pyautogui.mouseDown(button='left')
pyautogui.moveTo(1160, 790)
pyautogui.click()



# while True:
#     pyautogui.moveTo(1080, 380)
#     pyautogui.mouseDown(button='left')
#     pyautogui.moveTo(917, 564, 1)
#     time.sleep(10)













