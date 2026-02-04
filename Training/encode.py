encode = []
index = 0

code = input("Input the words:")

for c in code:
    if encode == []:
        encode.append([c, 1])
    elif encode[index][0] == c:
        encode[index][1] += 1
    else:
        index += 1
        encode.append([c, 1])

string = ""

for each in encode:
    string = string + f"{each[0]}{each[1]}"

print(string)
