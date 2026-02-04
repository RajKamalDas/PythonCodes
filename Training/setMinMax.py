Set = {1, 2, 3, 9, 0, 4, 5, 6}

max = min = list(Set)[0]

for i in Set:
    if min > i:
        min = i
    if max < i:
        max = i

print(f'\n\nMax: {max}\nMin: {min}\n')
