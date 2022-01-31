import pyautogui , time
time.sleep(3)
with open('message.txt', 'r') as file:
    word = file.read()
    while True:
        for i in word:
            pyautogui.typewrite(i)
