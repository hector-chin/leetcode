def maximumWealth(accounts) -> int:
    target_return = 0
    for i in range(0, len(accounts)):
        temp_sum = sum(accounts[i])
        if temp_sum > target_return:
            target_return = temp_sum
        else:
            pass
    print(target_return)
    return target_return



accounts_test = [[1,2,3],[3,2,1]]
test = maximumWealth(accounts_test)
