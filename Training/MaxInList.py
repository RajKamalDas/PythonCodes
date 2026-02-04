numbers = [1, 3, 577, 3295, 7593, 1029, 9, 0]

print(max(numbers))
maximum = numbers[0]

for i in numbers:
    if i>maximum:
        maximum = i

print(maximum)