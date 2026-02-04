code = input("Enter Code:")

char = ""
string = ""

for c in code:
    if c.isalpha():
        char = c
    elif c.isdigit():
        string = string + char * int(c)

print(string)
