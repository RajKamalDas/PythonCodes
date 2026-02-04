path = input("Enter the file path: ")

try:
    with open(path, "r") as file:
        x = 0
        for _ in file:
            x += 1
    print(f"Total lines read: {x}")

except FileNotFoundError:
    print("File not found. Please ensure the file path is correct.")