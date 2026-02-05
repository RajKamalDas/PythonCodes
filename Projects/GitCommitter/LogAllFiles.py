import os


def LogAllFiles():
    ignore = [".git", ".code-workspace", "VEnv"]
    allFiles = []

    for root, _, files in os.walk("C:/Python"):
        for file in files:
            file = os.path.join(root, file).replace("\\", "/").replace("C:/Python/","")
            add = True
            for i in ignore:
                if i in file:  # Check if the file should be ignored
                    add = False
                    break
            if add:
                allFiles.append(file)

    return set(allFiles)


LogAllFiles()
