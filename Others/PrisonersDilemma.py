import random


def sim(boxes):
    seq = list(range(1, BoxCount + 1))
    longestLoop = 0
    while len(seq) > 0:
        find = seq[0]
        ind = find - 1
        for i in range(BoxCount):
            seq.pop(seq.index(boxes[ind]))
            if boxes[ind] == find:
                if longestLoop <= i:
                    longestLoop = i + 1
                if i >= BoxCount / 2:
                    return longestLoop
                break
            ind = boxes[ind] - 1
    return longestLoop


BoxCount = 100
boxes = list(range(1, BoxCount + 1))
random.shuffle(boxes)

allProb = {}
winRate = 0
RunCount = 0
while RunCount <= 0:
    try:
        RunCount = int(input("Run Sim x Times. \nx:"))
    except ValueError:
        print("Please input only integers.")

for i in range(RunCount):
    random.shuffle(boxes)
    x = sim(boxes)
    if x in allProb:
        allProb[x] += 1
    else:
        allProb[x] = 1
    if x <= BoxCount / 2:
        winRate += 1

keys = list(allProb.keys())
keys.sort()
keySort = {i: allProb[i] for i in keys}

valueSort = dict(sorted(allProb.items(), key=lambda kv: (kv[1], kv[0]), reverse=True))
values = list(valueSort.keys())

x = len(allProb)
k = 0
v = 0
for i in range(int(x / 2) + x % 2):
    print(
        f"{keys[k]} : {keySort[keys[k]]}  \t||\t  {values[v]} : {valueSort[values[v]]}",
        end="\t #\t ",
    )
    print(
        f"{keys[x-1-k]} : {keySort[keys[x-1-k]]}  \t||\t{values[x-1-v]} : {valueSort[values[x-1-v]]}"
    )
    k += 1
    v += 1

print(f"\nWin Rate : {winRate/RunCount}")
