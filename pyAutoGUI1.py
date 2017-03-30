import pyautogui
scrnwidth,scrnheight=pyautogui.size()
#pyautogui.PAUSE=2.5
#pyautogui.moveTo(100,100,0.5)
distance=200
"""
while distance>0:
    pyautogui.moveRel(distance,0,duration=.5)
    distance-=10
    pyautogui.moveRel(0,distance,duration=0.5)
    pyautogui.moveRel(-distance,0,duration=0.5)
    distance-=10
    pyautogui.moveRel(0,-distance,duration=0.5)
"""

#pyautogui.doubleClick()
print(pyautogui.size())
print(pyautogui.position())
#pyautogui.click(100,200,clicks=1,button="middle")
pyautogui.scroll(400,300,400)
#pyautogui.typewrite(['a','b','c','left','left','d'],interval=0.25,)
print(pyautogui.KEYBOARD_KEYS)
pyautogui.prompt("This is alert")
print(pyautogui.position())