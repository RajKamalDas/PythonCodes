mat = [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
sumrow = []
sumcol = [0, 0, 0]


for row in mat:
    sumrow.append(sum(row))
    for i, n in enumerate(row):
        sumcol[i] += n

if len(set(sumcol)) == 1 and len(set(sumrow)) == 1 and sumcol == sumrow:
    print("Magic")
else:
    print("Not Magic")
