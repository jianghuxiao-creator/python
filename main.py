import pyautogui

# 获取当前屏幕分辨率
screenWidth, screenHeight = pyautogui.size()

# 获取当前鼠标位置
currentMouseX, currentMouseY = pyautogui.position()


for i in range(1,5):
    pyautogui.moveTo(x=-235, y=151,duration=0.8, tween=pyautogui.linear)
    pyautogui.click()
    pyautogui.moveTo(x=-416, y=650,duration=0.8, tween=pyautogui.linear)
    pyautogui.click() 
    pyautogui.moveTo(x=-333, y=951,duration=0.8, tween=pyautogui.linear)
    pyautogui.click()
print ("Hello, Python!")  (-235,151) (-333.951) (-416,650)
# import pyautogui
# try:
#     while True:
#         x,y = pyautogui.position()
#         print(x,y)
# except KeyboardInterrupt:
#     print('\nExit.')