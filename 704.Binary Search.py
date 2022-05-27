def search(nums, target: int) -> int:
    # if target in nums:
    #     return nums.index(target)
    # else:
    #     return -1
    left = 0
    right = len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            print(mid)
            return mid
        if nums[mid] < target:
            left = mid + 1
        if nums[mid] > target:
            right = mid
    print(-1)
    return -1

nums = [-1,0,3,5,9,12]
target = 9
test = search(nums, target)