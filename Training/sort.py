numbers = [1, 3, 577, 9, 0, 577, 577, 7, 0, 9, 1]

for i in range(len(numbers)):
    for j in range(i, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

print(numbers)