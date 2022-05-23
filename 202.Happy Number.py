def isHappy(n) -> bool:
    tar_nums = 0
    a = 0
    while (tar_nums != 1) & (a <= 100):
        tar_nums = 0
        a += 1
        for i in range(0, len(str(n))):
            tar_nums += int(str(n)[i]) ** 2
        n = tar_nums
    if tar_nums == 1:
        print(f'tar_nums is {tar_nums}')
        return True
    else:
        print('False')
        return False




n = 19
test = isHappy(n)
