string = input("Enter a String:")
word = input("Word to Find:")

print(f"{word} appears {string.count(word)} times")
print("\nReplacing The First & The Last Character…")
newString = string[-1] + string[1:-1] + string[0]
print(newString)
