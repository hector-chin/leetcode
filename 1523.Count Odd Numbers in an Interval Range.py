def countOdds(low, high):
    """
    :type low: int
    :type high: int
    :rtype: int
    """
    if ((high - low) % 2 == 0) & (low % 2 == 0):
        odd_nums = (high - low) / 2
    elif ((high - low) % 2) == 0 & (low % 2 == 1):
        odd_nums = (high - low) / 2 + 1
    else:
        odd_nums = (high - low) // 2 + 1
    print(odd_nums)
    return odd_nums

test = countOdds(3, 7)

