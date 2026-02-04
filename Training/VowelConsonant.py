vowel = 0
consonants = 0

with open("Journal-story.txt", "r") as f:
    for line in f.readlines():
        for c in line:
            if c in "AEIOUaeiou":
                vowel += 1
            elif c.isalpha():
                consonants += 1


print(f"The Text has {vowel} vowel & {consonants} consonants Letters.")
