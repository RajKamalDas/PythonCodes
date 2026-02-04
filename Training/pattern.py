x = int(input("Lines(1-7): "))

x += 1

print("-" * (2 * x + 2))

for i in range(1, x):
    print(f"|{i}|" + (" *" * i) + ("  " * (x - i - 1)) + "|")

print("-" * (2 * x + 2))

for i in range(1, x):
    print(f"|{i}|" + (" *" * (x - i) + ("  " * (i - 1)) + "|"))

print("-" * (2 * x + 2))

for i in range(1, x):
    print(f"|{i}|" + ("  " * (x - i - 1)) + (" *" * i) + "|")

print("-" * (2 * x + 2))

for i in range(1, x):
    print(f"|{i}|" + ("  " * (i - 1)) + (" *" * (x - i)) + "|")

print("-" * (2 * x + 2))
