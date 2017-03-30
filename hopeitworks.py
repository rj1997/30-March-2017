import subprocess,pyautogui,time
subprocess.Popen(["C:\\Users\\Rishabh Jain\\Desktop\\paint1.png"],shell=True)
time.sleep(2)
pyautogui.moveTo(200,200,2)
dist=200

while dist>0:
    pyautogui.dragRel(dist,0,0.1)
    dist-=5
    pyautogui.dragRel(0,dist,0.1)
    pyautogui.dragRel(-dist,0,0.1)
    dist-=5
    pyautogui.dragRel(0,-dist,0.1)
