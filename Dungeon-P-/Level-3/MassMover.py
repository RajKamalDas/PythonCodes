import os
import configparser
import tkinter as tk
from tkinter import filedialog


class MassMover:
    def __init__(self, oldPath=None, newPath=None, extension=None, cofigPath=""):
        if extension != None and not extension.startswith("."):
            extension = "." + extension

        self.CONFIG_PATH = cofigPath + "MoverConfigs.ini"
        self.loadConfig(oldPath, newPath, extension)
        self.UI()

    def loadConfig(self, oldPath=None, newPath=None, extension=None):
        loader = configparser.ConfigParser()
        try:
            loader.read(f"{os.getcwd()}/{self.CONFIG_PATH}".replace("\\", "/"))
            if oldPath == None:
                oldPath = loader["Paths"]["oldPath"]
            if newPath == None:
                newPath = loader["Paths"]["newPath"]
            if extension == None:
                extension = loader["Exe"]["Extension"]
        except FileNotFoundError:
            oldPath = "C:/"
            newPath = "C:/"
            extension = ""
        except KeyError:
            oldPath = "C:/"
            newPath = "C:/"
            extension = ""

        self.root = tk.Tk()
        self.oldPath = tk.StringVar(self.root, oldPath)
        self.newPath = tk.StringVar(self.root, newPath)
        self.extension = tk.StringVar(self.root, extension)
        self.message = tk.StringVar(self.root, " ")

    def UI(self):
        self.root.title("Mover")
        label = tk.Label(
            self.root,
            text="Welcome!",
            font=("Bahnschrift Bold", 14),
            justify="center",
            anchor="center",
        )
        label.pack(padx=10)

        frame = tk.Frame(self.root, relief="groove", border=3)

        oldLabel = tk.Label(frame, text="Old File Location:", font=("Bahnschrift", 10))
        oldField = tk.Entry(frame, textvariable=self.oldPath, width=40)
        oldSelect = tk.Button(frame, text="Select", command=self.selectOldDirectory, width=5)
        newLabel = tk.Label(frame, text="New File Location:", font=("Bahnschrift", 10))
        newField = tk.Entry(frame, textvariable=self.newPath, width=40)
        newSelect = tk.Button(frame, text="Select", command=self.selectNewDirectory, width=5)
        extensionLabel = tk.Label(frame, text="Move Only: (e.g. .img, .txt, etc.)", font=("Bahnschrift", 10))
        extensionField = tk.Entry(frame, textvariable=self.extension, width=40)
        extensionDetail = tk.Label(frame, text="Leave Blank To Move All Files.", font=("Bahnschrift", 10))
        self.informer = tk.Label(frame, textvariable=self.message, width=40)
        done = tk.Button(frame, text="Move Files", command=self.mover, width=10)
        exit = tk.Button(frame, text="Quit", command=self.root.quit, width=10)

        oldLabel.grid(column=0, row=0, columnspan=3, padx=5, sticky="w")
        oldField.grid(column=0, row=1, columnspan=2, padx=5, ipady=5, sticky="w")
        oldSelect.grid(column=2, row=1, padx=5, pady=5, sticky="w")
        newLabel.grid(column=0, row=2, columnspan=3, padx=5, sticky="w")
        newField.grid(column=0, row=3, columnspan=2, padx=5, ipady=5, sticky="w")
        newSelect.grid(column=2, row=3, padx=5, pady=5, sticky="w")
        extensionLabel.grid(column=0, row=4, columnspan=3, padx=5, sticky="w")
        extensionField.grid(column=0, row=5, columnspan=3, padx=5, ipady=5, sticky="w")
        extensionDetail.grid(column=0, row=6, columnspan=1, padx=5, sticky="w")
        done.grid(column=1, row=6, columnspan=2, padx=5, pady=5, sticky="e")
        self.informer.grid(column=0, row=7, columnspan=2, padx=5, pady=15, sticky="w")
        exit.grid(column=2, row=7, padx=5, pady=15, sticky="e")

        frame.pack(padx=10, pady=10)

        self.root.mainloop()

    def selectOldDirectory(self):
        directory_path = filedialog.askdirectory(
            title="Select a Folder:",
            initialdir=self.oldPath.get(),  # Optional: set initial directory
        )

        if directory_path:
            self.oldPath.set(directory_path)
            print(f"Selected directory: {directory_path}")
        else:
            print("No directory selected.")

        self.message.set("")

    def selectNewDirectory(self):
        directory_path = filedialog.askdirectory(
            title="Select a Folder:",
            initialdir=self.newPath.get(),  # Optional: set initial directory
        )

        if directory_path:
            self.newPath.set(directory_path)
            print(f"Selected directory: {directory_path}")
        else:
            print("No directory selected.")

        self.message.set("")

    def mover(self):
        try:
            os.makedirs(self.newPath.get(), exist_ok=True)
            filelist = [
                file
                for file in os.listdir(self.oldPath.get())
                if file.endswith(self.extension.get()) and os.path.isfile(os.path.join(self.oldPath.get(), file))
            ]
            rename = False
            for file in filelist:
                old = f"{self.oldPath.get()}/{file}"
                new = f"{self.newPath.get()}/{file}"
                if os.path.exists(new):
                    rename = True
                    i = 0
                while rename:
                    new = new.split(".")[0].replace(f"- New Copy ({i-1})", "") + f"- New Copy ({i})" + new.split(".")[1]
                    i += 1
                    if not os.path.exists(new):
                        rename = False
                os.rename(old, new)

            self.informer.config(fg="green")
            self.message.set("Files Moved!")
            self.save()

        except PermissionError:
            self.informer.config(fg="red")
            self.message.set("Directory Beyond Thy Access!")

    def save(self):
        save = configparser.ConfigParser()
        save.add_section("Paths")
        save.add_section("Exe")
        save["Paths"]["oldPath"] = self.oldPath.get()
        save["Paths"]["newPath"] = self.newPath.get()
        save["Exe"]["Extension"] = self.extension.get()
        with open(f"{os.getcwd()}/{self.CONFIG_PATH}".replace("\\", "/"), "w") as config:
            save.write(config)


if __name__ == "__main__":
    MassMover(cofigPath="Dungeon/Level-3/")
