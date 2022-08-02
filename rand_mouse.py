import pyautogui as pygui
import random

screenWidth, screenHeight = pygui.size()
currX, currY = pygui.position()

pygui.move(500,500, duration=0.5, tween=pygui.easeInBounce)