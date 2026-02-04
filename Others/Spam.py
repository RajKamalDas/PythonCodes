import time
import keyboard


def repeat(message, count, showCounter=False, startCounter=1):
    for i in range(count):
        time.sleep(0.3)
        if showCounter:
            text = f"{i+startCounter}) {message}"
        else:
            text = message
        keyboard.write(text)
        keyboard.press("shift")
        keyboard.press_and_release("enter")
        keyboard.release("shift")


if __name__ == "__main__":
    time.sleep(3)
    repeat("", 30, True)
