string = 'I love IceCreame'

for word in string.split():
    if 'e' in word:
        print(word)

capitalized = string[0].upper() + string[1:].lower()
print(capitalized)
print(string[::-1])
print(string.startswith("I"))
print(string.replace("IceCreame", "Hockey"))