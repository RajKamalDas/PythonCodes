dicts = {"first": {"okay": 4}, "second" : 99, "third": {"Never": 1, "Not":2}}
numbs = []


def getInt(dic):
    num = []
    for value in dic.values():
        if isinstance(value, dict):
            num += getInt(value)
        else:
            num.append(value)
    return num


for value in dicts.values():
    if isinstance(value, dict):
        numbs += getInt(value)
    else:
        numbs.append(value)

print(sum(numbs))
