import os


def LogAllFiles():
    ignore = ["./.", ".code-workspace", "VEnv"]
    allFiles = []

    for root, _, files in os.walk("."):
        for file in files:
            file = os.path.join(root, file).replace("\\", "/")
            add = True
            for i in ignore:
                if i in file:  # Check if the file should be ignored
                    add = False
                    break
            if add:
                allFiles.append(file)

    return set(allFiles)


LogAllFiles()
