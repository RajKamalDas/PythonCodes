import math

choice = 11

while choice != 0:
    try:

        choice = int(input("\n==== Math Module Python ====\n1) Powers\n2) Factorial\n3) Trigonametry\n4) Rounding\nChoice:"))

        while not -1 < choice <= 4:
            choice = int(input("Invalid Input Try Again:"))

        match (choice):
            case 0:
                break

            case 1:
                x = int(input("Base:"))
                y = int(input("Exponent:"))
                print(f"{x} to the power of {y}: {math.pow(x, y)}")

            case 2:
                x = int(input("Integer:"))
                print(f"Factorial of {x}: {math.factorial(x)}")

            case 3:
                angle = float(input("Input the Angle:"))
                radAngle = math.radians(angle)  # ←All Trig functions need Radions instead of Degrees
                print(f"Sin {angle}° = {math.sin(radAngle)}")
                print(f"Cos {angle}° = {math.cos(radAngle):.5}")
                print(f"Tan {angle}° = {math.tan(radAngle):.5}")

            case 4:
                b = float(input("Input Float:"))
                print(f"Rounding {b} to the Ceiling: {math.ceil(b)}")
                print(f"Rounding {b} to the Floor: {math.floor(b)}")
                print(f"Rounding {b} using Truncate: {math.trunc(b)}")

    except ValueError:
        print("Sorry We Take Only Integer Input.")
