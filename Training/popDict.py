dictionery = {"Name": "RajKamal", "Surname": "Das", "Age": 19, "Me": "Preferred", "Myself": "Loved", "I": "Liked"}

print("\n\nOriginal:", dictionery)

dictionery = dict([pairs for pairs in dictionery.items() if pairs[0] != "Surname"])

print("Updated: ", dictionery)
