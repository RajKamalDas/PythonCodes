import math

cords = [(0, 0)]


def save():
    with open("Points.txt", "w") as f:
        for each in cords:
            f.write(str(each) + "\n")


def load():
    try:
        with open("Points.txt", "r") as f:
            for line in f.readlines():
                x, y = line[1:-2].split(", ")
                x = float(x)
                y = float(y)
                if (x, y) not in cords:
                    cords.append((x, y))
    except FileNotFoundError:
        pass


def addCords():
    global cords

    lati = float(input("Enter Latitude:"))
    long = float(input("Enter Longitude:"))

    cords.append((lati, long))


def display():
    for i, each in enumerate(cords, 1):
        print(f"{i}> {each}")


def distance(x=None, y=None, show=True):
    if show:
        display()
    if not x:
        x = cords[int(input("Enter 1st Point's number:")) - 1]
    if not y:
        y = cords[int(input("Enter 2nd Point's number:")) - 1]
    dist = abs(math.dist(x, y))
    if show:
        print(f"{x} is {dist:.2f} away from {y}")
    return float(f"{dist:.2f}")


def inRange(base=None):
    length = float(input("Enter the Range/Radius:"))
    if not base:
        display()
        base = cords[int(input("Enter the number of the cordianate of the center:")) - 1]
    loc = []
    for each in cords:
        if each == base:
            continue
        if distance(base, each, False) <= abs(length):
            loc.append(each)
    if loc == []:
        print(f"No Points in {length} of {base}")
    else:
        print(f"{loc} are within {length} of {base}")


def fromDifferent():
    display()
    known = cords[int(input("Enter 1st Point's number:")) - 1]
    x = float(input("Enter 2nd Point's Latitude:"))
    y = float(input("Enter 2nd Point's Longitude:"))
    dist = distance(known, (x, y), False)
    print(f"{known} is {dist} away from {(x,y)}")


def run():
    runner = True
    load()
    while runner:
        print(
            """What would you like to do?
            1) Save a Point
            2) Distance of two saved Points
            3) Points within range of saved Point
            4) Distance of a Saved Point From Unsaved Point
            5) Points Within Range of Center
            6) Exit"""
        )
        x = int(input("Your Choice:"))
        match x:
            case 1:
                addCords()
            case 2:
                distance()
            case 3:
                inRange()
            case 4:
                fromDifferent()
            case 5:
                inRange((0, 0))
            case 6:
                runner = False
    save()


run()
