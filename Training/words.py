words = dict()

with open("Poem.txt", 'r')as file:
    for lines in file:
        for word in lines.replace(".",'').split():
            if word in words:
                words[word] += 1
            else:
                words[word] = 1

appearsOnce = [word[0] for word in words.items() if word[1] == 1]
longest = ''
mostCommon = ("none", 0)

for word in words.keys():
    if len(word) > len(longest):
        longest = word

for word, count in words.items():
    if count > mostCommon[1]:
        mostCommon = (word, count)


print(f"Longest Word:{longest}")
print(f"Most Common Word:{mostCommon}")
print("Words That Appear Once:")
for each in appearsOnce:
    print(each)