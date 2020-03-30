# from ctypes import *
# import time
# # for i in range(1,45000000):
# windll.user32.SetCursorPos(900,50);
# time.sleep(2)
# windll.user32.SetCursorPos(900,300);

from pymouse import PyMouse
import time
import math
import pyautogui
import random

m = PyMouse()
a = m.position()    #获取当前坐标的位置
print(a)
time.sleep(1)

for i in range(1,500):
    pyautogui.mouseDown(random.randint(269,900), random.randint(200,900))
pyautogui.click(580, 580)

# 弹窗
# pyautogui.alert(123, 423, "ok")
# pyautogui.confirm(1111, 222, range(10))

# 圆
# r = 200;
# for i in range(1,1440):
#     time.sleep(0.001)
#     angle = math.pi / 720 * i
#     x2 = r * math.sin(angle)
#     y2 = r * math.cos(angle)
#     m.press(500 + int(x2),500 + int(y2))

# 正方形
# w = 0
# h = 0
# l = 0
# for i in range(1,1000):
#     time.sleep(0.0001)
#     l = i
#     if l <= 250 :
#         m.press(500 + i, 500)   #鼠标移动到(x,y)位置
#         w = w + 1
#     elif  l <= 500 :
#         m.press(500 + w, 500 + (i-w))   #鼠标移动到(x,y)位置
#         h = h + 1
#     elif l < 750 :
#         m.press(500 + w, 500 + h)
#         w = w - 1
#     else :
#         m.press(500 + w, 500 + h)
#         h = h - 1
    # m.click(1129, 649)  #移动并且在(x,y)位置左击
