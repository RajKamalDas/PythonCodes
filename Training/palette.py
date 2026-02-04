palette = []


def addcolour():
    global palette

    red = input("Red:")
    green = input("Green:")
    blue = input("Blue:")
    colour = (red, green, blue)

    colour = tuple([f"{ele:0>3s}" for ele in colour])

    palette.append(colour)


def display():
    for colour in palette:
        print(f"red: {colour[0]} | green: {colour[1]} | blue: {colour[2]}")


def save():
    with open("Training/Palette.txt", "w") as f:
        for colour in palette:
            f.write(f"{colour[0]}|{colour[1]}|{colour[2]}\n")


def load():
    global palette
    palette.clear()
    try:
        with open("Traning/Palette.txt", "r") as f:
            for line in f.readlines():
                red, green, blue = line[:-1].split("|")
                palette.append((red, green, blue))
    except FileNotFoundError:
        print("Oops! Nothing to see here.")


def run():
    runner = True
    while runner:
        print(
            """What would you like to do?
            1) Add a new colour
            2) Display palette
            3) Save palette
            4) Load palette
            5) Exit"""
        )
        x = int(input("Your Choice:"))
        match x:
            case 1:
                addcolour()
            case 2:
                display()
            case 3:
                save()
            case 4:
                load()
            case 5:
                runner = False


run()
