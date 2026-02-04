string = input("Enter a String:")
x = int(input("Please, Enter N-th to Remove:"))

string = string[:x] + string[x+1:]

print(string)