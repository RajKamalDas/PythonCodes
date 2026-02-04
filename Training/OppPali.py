inputs = []

for i in range(5):
    inputs.append(input(f'Insert {i + 1}) String:'))

for i, lines in enumerate(inputs):
    if lines.lower() != lines[::-1].lower():
        inputs[i] = lines[::-1]

print(inputs)