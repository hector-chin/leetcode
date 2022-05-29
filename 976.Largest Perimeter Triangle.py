def largestPerimeter(nums) -> int:
    nums.sort(reverse=True)
    for i in range(0, len(nums)):
        if i+2 < len(nums):
            if nums[i] >= nums[i+1] + nums[i+2]:
                continue
            elif nums[i] < nums[i+1] + nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        else:
            return 0
nums = [2,1,2]
test = largestPerimeter(nums)