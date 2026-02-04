uppercase = 0
lowercase = 0

with open("Journal-story.txt", "r") as f:
    for line in f.readlines():
        for c in line:
            if c.isupper():
                uppercase += 1
            elif c.islower():
                lowercase += 1


print(f"The Text has {uppercase} Uppercase & {lowercase} Lowercase Letters.")
