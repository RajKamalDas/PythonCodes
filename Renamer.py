import os
import configparser
import tkinter as tk
from tkinter import filedialog


class Renamer:
    def __init__(
        self,
        extension=".txt",
        newName="",
        oldName="",
        oldNameHas="",
        debugPath="",
    ):
        if not extension.startswith("."):
            extension = "." + extension

        self.CONFIG_PATH = debugPath + "Configs.ini"
        self.extension = extension
        self.loadConfig(newName, oldName, oldNameHas)
        self.UI()

    def loadConfig(self, newName="Screenshot", oldName="", oldNameHas=""):
        loader = configparser.ConfigParser()
        try:
            loader.read(f"{os.getcwd()}/{self.CONFIG_PATH}".replace("\\", "/"))
            path = loader["Locations"]["past"]
            if not oldName:
                oldName = loader["Names"]["oldName"]
            if not oldNameHas:
                oldNameHas = loader["Names"]["oldNameHas"]
            if newName == "Screenshot":
                newName = loader["Names"]["newName"]
        except FileNotFoundError:
            path = "C:/"
        except KeyError:
            path = "C:/"

        self.root = tk.Tk()
        self.oldName = tk.StringVar(self.root, oldName)
        self.newName = tk.StringVar(self.root, newName)
        self.oldNameHas = tk.StringVar(self.root, oldNameHas)
        self.directory = tk.StringVar(self.root, path)
        self.message = tk.StringVar(self.root, " ")

    def UI(self):
        self.root.title("Renamer")
        label = tk.Label(
            self.root,
            text="Welcome!",
            font=("Bahnschrift Bold", 14),
            justify="left",
            anchor="e",
        )
        label.pack(padx=10)

        frame = tk.Frame(self.root, relief="groove", border=3)

        details = tk.Label(
            frame, text=f"Rename '{self.extension}'s in:", font=("Bahnschrift", 10)
        )
        detailsName = tk.Label(
            frame,
            text=f"The Files Will Be Renamed If They Start With:",
            font=("Bahnschrift", 10),
        )
        detailsFind = tk.Label(
            frame,
            text=f"The Files Will Be Renamed If The Name Has:",
            font=("Bahnschrift", 10),
        )
        detailsRename = tk.Label(
            frame, text=f"Files Will Be Renamed To:", font=("Bahnschrift", 10)
        )
        directoryField = tk.Entry(frame, textvariable=self.directory, width=40)
        nameField = tk.Entry(frame, textvariable=self.oldName, width=40)
        findField = tk.Entry(frame, textvariable=self.oldNameHas, width=40)
        renameField = tk.Entry(frame, textvariable=self.newName, width=40)
        select = tk.Button(frame, text="Select", command=self.select_directory, width=5)
        done = tk.Button(frame, text="Rename All Files", command=self.rename, width=15)
        exit = tk.Button(frame, text="Quit", command=self.root.quit, width=5)
        self.onceDone = tk.Label(
            frame,
            textvariable=self.message,
            font=("Bahnschrift", 10),
        )

        details.grid(column=0, row=0, padx=5, sticky="w")
        directoryField.grid(column=0, row=1, columnspan=2, padx=5, pady=5)
        select.grid(column=2, row=1, padx=5, pady=5)
        detailsName.grid(column=0, row=2, columnspan=2, padx=5, pady=5, sticky="w")
        nameField.grid(column=0, row=3, columnspan=2, padx=5, pady=5)
        detailsFind.grid(column=0, row=4, columnspan=2, padx=5, pady=5, sticky="w")
        findField.grid(column=0, row=5, columnspan=2, padx=5, pady=5)
        detailsRename.grid(column=0, row=6, columnspan=2, padx=5, pady=5, sticky="w")
        renameField.grid(column=0, row=7, columnspan=2, padx=5, pady=5)
        self.onceDone.grid(column=0, row=8, padx=5, pady=5, sticky="w")
        done.grid(column=1, row=8, padx=5, pady=5, sticky="e")
        exit.grid(column=2, row=8, padx=5, pady=5)

        frame.pack(padx=10, pady=10)

        self.root.mainloop()
        #Redundent `destroy` but prevents the code getting stuck
        try:
            self.root.destroy()
        except:
            pass

    def select_directory(self):
        directory_path = filedialog.askdirectory(
            title="Select a Folder:",
            initialdir=self.directory.get(),  # Optional: set initial directory
        )

        if directory_path:
            self.directory.set(directory_path)
            print(f"Selected directory: {directory_path}")
        else:
            print("No directory selected.")

    def rename(self):
        try:
            filelist = [
                file
                for file in os.listdir(self.directory.get())
                if file.endswith(self.extension)
                and file.startswith(self.oldName.get())
                and self.oldNameHas.get() in file
            ]
            for i, file in enumerate(filelist):
                old = f"{self.directory.get()}/{file}"
                new = f"{self.directory.get()}/{self.newName.get()}{i+1:03d}{self.extension}"
                j = 1
                while os.path.exists(new):
                    new = (
                        new.split(".")[0].replace(f"({j-1})", "")
                        + f"({j})"
                        + self.extension
                    )
                    j += 1
                os.rename(old, new)
            self.onceDone.config(fg="Green")
            self.message.set("Done!")
            self.save()
        except FileNotFoundError as e:
            print(e)
            self.onceDone.config(fg="Red")
            self.message.set("Directory Does NOT Exist!")
        except PermissionError:
            self.onceDone.config(fg="Red")
            self.message.set("Directory Out Beyond Access!")

    def save(self):
        save = configparser.ConfigParser()
        save.add_section("Locations")
        save.add_section("Names")
        save["Locations"]["past"] = self.directory.get()
        save["Names"]["oldName"] = self.oldName.get()
        save["Names"]["oldNameHas"] = self.oldNameHas.get()
        save["Names"]["newName"] = self.newName.get()
        with open(
            f"{os.getcwd()}/{self.CONFIG_PATH}".replace("\\", "/"), "w"
        ) as config:
            save.write(config)


if __name__ == "__main__":
    Renamer(".png")
