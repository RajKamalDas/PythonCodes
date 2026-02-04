superList = [i for i in range(1, 21)]

evenList = []
oddList = []

for x in superList:
    if x % 2 == 0:
        evenList.append(x)
    else:
        oddList.append(x)

print("The Main List:", superList)
print("The Even List:", evenList)
print("The Odd List:", oddList)