numbers = [1, 3, 577, 9, 0, 577, 577, 7, 0, 9, 1]
duplicates = []

for i in numbers:
    if numbers.count(i) > 1 and i not in duplicates:
        duplicates.append(i)

print("Duplicate Numbers:", duplicates)

if len(set(numbers)) == len(numbers):
    print("Chilo na")
else:
    print("Chilo")
