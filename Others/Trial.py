import time
import random
import threading
import msvcrt

random.seed(time.time())

print("\n\nTest Thy Patient(TTP):\n")


def check(endProcess, restart):
    while True:
        if msvcrt.kbhit():
            restart.set()
            msvcrt.getch()
        if endProcess.is_set():
            return
        time.sleep(0.1)


def timeTrial(endProcess, restart, continueProcess):
    processSucess = True

    while continueProcess.is_set():
        x = random.randint(120, 300)

        continueProcess.clear()

        for i in range(1, x):
            try:
                time.sleep(0.25)
                print(f"{i}", end="")
                if restart.is_set():
                    raise KeyboardInterrupt
                time.sleep(0.25)
                print(".", end="")
                if restart.is_set():
                    raise KeyboardInterrupt
                time.sleep(0.25)
                print(".", end="")
                if restart.is_set():
                    raise KeyboardInterrupt
                time.sleep(0.25)
                print(".", end="\r")
                if restart.is_set():
                    raise KeyboardInterrupt

            except KeyboardInterrupt:
                print(f"\r{i} years later, a voice echoes in the chamber:")
                print('"You Fool! You Shall Start over!"')
                restart.clear()
                continueProcess.set()
                break

            except Exception as e:
                print(f'\r"Sorry, →{e}← Happened…"')
                processSucess = False
                break

    print(f"{i} years later, a voice echoes in the chamber:")

    endProcess.set()
    if processSucess:
        print('"Patience is a virtue, and thou art Virtuous!"')


endProcess = threading.Event()
restart = threading.Event()
continueProcess = threading.Event()

thread1 = threading.Thread(target=check, args=(endProcess, restart))
thread2 = threading.Thread(target=timeTrial, args=(endProcess, restart, continueProcess))

thread1.start()
thread2.start()

thread1.join()  # Wait for thread1 to complete
thread2.join()

print("\n\nThe Doors Close, and you leave Victorious.")
