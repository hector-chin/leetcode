def containsDuplicate(nums) -> bool:
    target_dict = {}
    for i in range(0, len(nums)):
        if nums[i] in target_dict:
            return True
        target_dict[nums[i]] = 1
    return False








nums = [1, 2, 3, 1]
test = containsDuplicate(nums)