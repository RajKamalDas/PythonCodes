x = int(input("Enter the element count:"))
inputs = []

for i in range(x):
    inputs.append(input(f'Insert {i+1} element:'))

numbs = tuple(inputs)
max = min = numbs[0]

for i in numbs:
    if min > i:
        min = i
    if max < i:
        max = i

print(f'Max: {max}\nMin: {min}')