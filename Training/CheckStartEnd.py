word = input("Enter a Word:")
vowels = "aeiouAEIOU"

if word[0] in vowels and word[-1] in vowels:
    print(f"{word} starts and ends with a vowel.")
else:
    print(f"{word} doesn't start and end with a vowel.")
