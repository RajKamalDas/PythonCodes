import random

dice = (1, 2, 3, 4, 5, 6)
counter = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
}

for i in range(100):
    x = random.choice(dice)
    try:
        counter[x] += 1
    except KeyError:
        counter[x] = 1

[print(f"{i} : {j}") for i, j in counter.items()]
