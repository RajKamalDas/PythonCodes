new_file = open("Dungeon/Level-2/EchoSkeleton.txt", "w")

try:
    with open("Dungeon/Level-2/LineCounterOoze.py", "r") as file:
        for lines in file:
            new_file.write(lines)

    print("File copied successfully.") 

except FileNotFoundError:
    print("Source file not found. Please ensure the file path is correct.")

new_file.close()