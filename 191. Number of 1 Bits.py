def hammingWeight(n: int) -> int:
    remainder = 0
    while n > 0:
        remainder += n % 2
        n = n // 2

    return remainder
