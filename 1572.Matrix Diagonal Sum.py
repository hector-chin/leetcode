def diagonalSum(mat):
    left = 0
    right = len(mat)
    total = 0
    for i in range(0, right):
        if left != right -1:
            total += mat[i][left]
            total += mat[i][right - 1]
        else:
            total += mat[i][left]
        left += 1
        right -= 1
    print(total)
    return total



mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]
test = diagonalSum(mat)
