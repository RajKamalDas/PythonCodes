import time
import keyboard

def annoy():
    x = int(input("How many times?: "))
    for i in range(x):
        time.sleep(300)
        keyboard.write("…")
        keyboard.press_and_release('enter')

annoy()