def matrixReshape(mat, r, c):
    target_matrix = []
    wait_nums = []
    total_nums = 0
    for i in range(0, len(mat)):
        for j in range(0, len(mat[i])):
            total_nums += 1
            wait_nums.append(mat[i][j])
    print(total_nums)
    if r*c != total_nums:
        print(mat)
        return mat
    else:
        for i in range(0, r):
            elements = []
            for j in range(0, c):
                elements.append(wait_nums[0])
                del wait_nums[0]
            target_matrix.append(elements)
        print(target_matrix)
        return target_matrix


mat = [[1, 2], [3, 4]]
r = 2
c = 4
test = matrixReshape(mat, r, c)


