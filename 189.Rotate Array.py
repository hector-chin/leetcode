def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """

    rotate_nums = []
    for i in range(0, len(nums)):
        rotate_nums.append(nums[i])
    for i in range(0, len(rotate_nums)):
        index_moved = i + k
        recursive_times = 0
        while index_moved >= len(rotate_nums):
            recursive_times += 1
            index_moved = index_moved - len(rotate_nums)*recursive_times
        nums[index_moved] = rotate_nums[i]
    print(nums)


# nums = [1,2,3,4,5,6,7]
# nums = [1]
nums = [1, 2, 3, 4, 5, 6]
k = 11
nums_to_rotate = rotate(nums, k)