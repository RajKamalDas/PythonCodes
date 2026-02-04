def transpose(mat):
    rows = len(mat)
    cols = len(mat[0])
    tMat = []
    for i in range(cols):
        tMat.append([])

    for i in range(cols):
        for j in range(rows):
            tMat[i].append(mat[j][i])

    return tMat


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
transposedMatrix = transpose(matrix)

for row in transposedMatrix:
    for ele in row:
        print(ele, end=", ")
    print()
