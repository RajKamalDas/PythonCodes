import time
import random
import keyboard

random.seed(time.time())


def exiting(event):
    global raiseException
    global cheat

    cheat = (cheat + event.name)[-10:]
    time.sleep(.25)
    
    raiseException = True

def timeTrial():
    processSucess = True

    x = random.randint(120, 300) + 1

    for i in range(1, x):
        try:
            time.sleep(0.5)
            print(f"\r{i}", end="")
            if raiseException:
                raise KeyboardInterrupt       
               
            time.sleep(0.5)      
            if raiseException:
                raise KeyboardInterrupt          

        except KeyboardInterrupt:
            if 'time' in cheat:
                print("\rCheater. 😒")
                time.sleep(5)
                processSucess = False
                return True
            else:
                print(f"\r{i} years later, a voice echoes in the chamber:")
                print('"You Fool! You Shall Start over!"\n')
                return False

        except Exception as e:
            print(f'\r"Sorry, →{e}← Happened…"')
            processSucess = False
            return False


    if processSucess:
        print(f"{i} years later, a voice echoes in the chamber:")
        print('"Patience is a virtue, and thou art Virtuous!"')

    return True


sucess = False
raiseException = False
cheat = ''

print("\n\nTest Thy Patient(TTP):\n")


keyboard.on_press(exiting)
while not sucess:
    sucess = timeTrial()
    raiseException = False

print("\n\nThe Doors Close, and you leave.")
keyboard.press_and_release('esc')
