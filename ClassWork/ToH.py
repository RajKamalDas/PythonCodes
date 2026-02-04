# Steps to solving Tower of Hanoi


def solveToH(discs, start="A", medium="B", end="C"):
    if discs == 1:
        print(f"Move a Disc from {start} to {end}.")
    else:
        solveToH(discs - 1, start, end, medium)
        print(f"Move a Disc from {start} to {end}.")
        solveToH(discs - 1, medium, start, end)


discCount = int(input("The Number of Discs:"))
print(f"To solve a tower of Hanoi with {discCount} discs do the following:")
solveToH(discCount)
