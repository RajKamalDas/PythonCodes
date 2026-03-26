# Completed.
"""
Docstring for Projects.14 day.DailyLogger

What this is?: A program that gives a way to save/document/journal and see past entries.

How to use it?: Running the program, you are asked to choose whether you want to read, or write.

If you want to only read at a glance: Input “R”, or anything starting with it.
What will happen: You'll be shown the 3 most recent entries.
Example:
→   Would you like to
    Read (R)
    Write(W)
→   :Read   {← User Input}
→   In the past three days you have accomplished:
    Day:9 > [14 January 1902] > Things.
    Day:10 > [15 January 2026] > Nothing.
    Day:11 > [16 January 3902] > More Things.
→   {Exits}

If you want to insert a new entry: Input “W”, or anything starting with it.
What will happen: You'll see all the past entries, and then be asked for the entry.
⇒If you already added one entry today, then you'll not be asked for an entry.
Example #1:
→   Would you like to
    Read (R)
    Write(W)
→   :Write  {←User input}
→   {
        …
        All past entries
        …
    }
    What steps you took toady?
→   :Added Examples to the Docstring.   {←User input}
→   {Exits}

Example #2:
→   Would you like to
    Read (R)
    Write(W)
→   :Write  {←User input}
→   {
        …
        All past entries
        …
    }
→   Only one step a day, keep your mind out of the hay. Come back tomorrow, 👋🏽😊.
→   {Exits}

"""

import os
import datetime

AllowedModes = {"r", "w"}
PathToRecord = os.getcwd().replace("\\", "/") + "/Projects/14 day/record.txt"


def reader():
    try:
        with open(PathToRecord, "r") as f:
            logs = f.readlines()
        print("In the past three days you have accomplished:")
        for log in logs[-3:]:
            print(log, end="")

    except FileNotFoundError:
        print("There's no record found, sorry.")


def logger():
    try:
        with open(PathToRecord, "r") as f:
            logs = f.readlines()
    except FileNotFoundError:
        logs = []

    for log in logs:
        print(log, end="")

    if logs:
        try:
            lastDate = "[" + logs[-1].split("[")[1].split("]")[0] + "]"
        except:
            lastDate = ""
    else:
        print("The sprint starts with the first step…")
        lastDate = ""

    formattedDate = datetime.date.today().strftime("[%d %B %Y]")

    if formattedDate == lastDate:
        print("Only one step a day, keep your mind out of the hay. Come back tomorrow, 👋🏽😊.")
    else:
        text = input("What steps you took toady?\n:")

        logs.append(f"Day:{len(logs) + 1} > {formattedDate} > {text}\n")

        with open(PathToRecord, "w") as f:
            for log in logs:
                f.write(log)


choose = input("Would you like to\nRead (R)\nWrite(W)\n:").lower().strip()
if choose[0] in AllowedModes:
    if choose[0] == "r":
        reader()
    else:
        logger()
else:
    print("Invalid Input, Sorry.")
