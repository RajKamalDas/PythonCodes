x = int(input("Enter the element count:"))
inputs = []

for i in range(x):
    inputs.append(input(f'Insert {i+1} element:'))

numbs = tuple(inputs)

n = int(input("Enter the Index to remove:"))

numbs = numbs[:n] + numbs[n+1:]

print(numbs)