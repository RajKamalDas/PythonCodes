def firstNonInt(s):
    for i, char in enumerate(s):
        if not char.isdigit():  # Find first non-digit character
            return i
    return -1  # No non-digit characters


string = input(
    "\n\t\t\tWelcome!\nInput a number to find the greatest odd number contained within it: "
)

while True:
    x = firstNonInt(string)
    if x == -1:  # All digits, exit loop
        break
    string = string[:x] + string[x + 1 :]  # Remove non-integer characters

if not string:  # Edge case: If input was only symbols/letters
    print("No valid digits found. Exiting.")
    exit()

integer = int(string)

# Find the largest odd number by checking from the right
for i in range(len(string) - 1, -1, -1):
    if int(string[i]) % 2 == 1:  # Found an odd number
        print(f"The greatest odd number contained within {integer} is {string[:i+1]}")
        break
else:
    print(f"No odd numbers found in {integer}.")
