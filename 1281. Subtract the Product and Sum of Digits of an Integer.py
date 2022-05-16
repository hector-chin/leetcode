def subtractProductAndSum(n: int) -> int:
    n_str = str(n)
    product_nums = 1
    addition_nums = 0
    for i in range(0, len(n_str)):
        product_nums *= int(n_str[i])
        addition_nums += int(n_str[i])

    result = product_nums - addition_nums
    return result