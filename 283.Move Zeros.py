def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    zero_nums = 0
    for i in range(0, len(nums)):
        if nums[i] == 0:
            zero_nums += 1
    for i in range(0, zero_nums):
        nums.remove(0)
    for i in range(0, zero_nums):
        nums.append(0)
    print(nums)
nums = [0, 1, 0, 3, 12]
# nums = [2, 1]
moveZeroes_func = moveZeroes(nums)