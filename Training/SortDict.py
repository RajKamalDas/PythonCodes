dictionery = {"Name": "RajKamal", "Surname": "Das", "Age": 19, "Me": "Preferred", "Myself": "Loved", "I": "Liked"}
keys = list(dictionery.keys())

print(sorted(dictionery.keys()))

for i in range(len(keys)):
    for j in range(i, len(keys)):
        if keys[i] > keys[j]:
            keys[i], keys[j] = keys[j], keys[i]

print(keys)