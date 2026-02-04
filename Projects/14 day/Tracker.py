import os
import configparser
import tkinter as tk


class Tracker:
    def __init__(self):
        self.root = tk.Tk()
        self.buttons = []
        self.load()
        self.launch()

    def load(self):
        self.path = os.getcwd().replace("\\", "/") + "/Projects/14 day/Tracker.py/record.ini"
        loader = configparser.ConfigParser()
        if os.path.exists(self.path):
            loader.read(self.path)
            self.period = int(loader["SET"]["period"])
            self.current = int(loader["SET"]["current"])
            self.checks = [
                True if each == "True" else False for each in loader["TRACK"]["checks"].replace("[", "").replace("]", "").split(", ")
            ]
        else:
            self.period = 14
            self.current = 0
            self.checks = [False for i in range(14)]

    def launch(self):
        self.root.title("Trcker 🏁")
        label = tk.Label(
            self.root,
            text="Right On Track! 😉",
            font=("Bahnschrift Bold", 14),
            justify="center",
            anchor="center",
        )
        label.pack(padx=10)
        track = tk.Label(
            self.root,
            text=f"Day: {self.current + 1}/{self.period}",
            font=("Bahnschrift Bold", 14),
            justify="center",
            anchor="center",
        )
        track.pack(padx=10)

        frame = tk.Frame(self.root, relief="groove", border=3)

        for key in range(14):
            self.buttons.append(tk.Button(frame, text=str(key + 1), width=5))

        for i, button in enumerate(self.buttons):
            if i < self.current:
                if self.checks[i]:
                    button.config(bg="green", fg="SystemButtonFace", relief=tk.SUNKEN)
                else:
                    button.config(bg="red", fg="SystemButtonFace", relief=tk.SUNKEN)
            elif i == self.current:
                button.config(bg="grey")
            else:
                break

        for i in range(self.period // 2):
            self.buttons[i].grid(column=i, row=0, padx=5, pady=5)
            self.buttons[self.period // 2 + i].grid(column=i, row=1, padx=5, pady=5)

        frame.pack(padx=10, ipady=1)
        set = tk.Button(self.root, text="✅", command=self.set, width=5)
        unset = tk.Button(self.root, text="⨉", command=self.unset, width=5)
        revert = tk.Button(self.root, text="⇦", command=self.revert, width=5)
        reset = tk.Button(self.root, text="↺", command=self.reset, width=5)
        set.pack(side="left", padx=30, pady=10)
        unset.pack(side="left", padx=30)
        revert.pack(side="left", padx=30)
        reset.pack(side="left", padx=30)

        self.root.mainloop()

    def set(self):
        self.buttons[self.current].config(bg="green", fg="SystemButtonFace", relief=tk.SUNKEN)
        self.checks[self.current] = True
        self.current += 1
        self.buttons[self.current].config(bg="gray")
        self.save()

    def unset(self):
        self.buttons[self.current].config(bg="red", fg="SystemButtonFace", relief=tk.SUNKEN)
        self.checks[self.current] = False
        self.current += 1
        self.buttons[self.current].config(bg="gray")
        self.save()

    def revert(self):
        self.buttons[self.current].config(bg="SystemButtonFace", fg="black", relief=tk.RAISED)
        self.current -= 1 if self.current else 0
        self.buttons[self.current].config(bg="grey", fg="black", relief=tk.RAISED)
        self.save()

    def reset(self):
        self.current = 0
        self.checks = [False for _ in range(14)]
        for each in self.buttons:
            each.config(bg="SystemButtonFace", fg="black", relief=tk.RAISED)
        self.buttons[self.current].config(bg="grey")
        self.save()

    def save(self):
        save = configparser.ConfigParser()
        save.add_section("SET")
        save.add_section("TRACK")
        save["SET"]["period"] = str(self.period)
        save["SET"]["current"] = str(self.current)
        save["TRACK"]["checks"] = str(self.checks)
        with open(self.path, "w") as config:
            save.write(config)


if __name__ == "__main__":
    Tracker()
