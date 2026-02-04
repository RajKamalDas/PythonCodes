file = open("test.txt", "a")

file.write("\nTumi boka")
file.write("-chele")

file.close()
file = open("test.txt", "r")
print(file.read())
