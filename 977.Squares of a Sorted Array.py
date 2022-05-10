nums = [-4, -1, 0, 3, 10]


def sortedSquares(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    square_list = []
    for i in range(0, len(nums)):
        a = nums[i]*nums[i]
        print(a)
        square_list.append(a)
    square_list.sort()
    print(square_list)


result = sortedSquares(nums)
