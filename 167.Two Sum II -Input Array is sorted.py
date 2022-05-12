def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    find_dict = {}
    for i in range(0, len(numbers_test)):
        if numbers_test[i] not in find_dict:
            find_dict[target_test - numbers_test[i]] = i
        print(find_dict[numbers_test[i]]+1, i+1)
# numbers_test = [2, 7, 11, 15]
# numbers_test = [-1, 0]
numbers_test = [0, 0, 3, 4]
target_test = 0
twoSum_check = twoSum(numbers_test, target_test)