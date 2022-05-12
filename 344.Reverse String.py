def reverseString(s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    # Use python list method to solve question.
    # s[:] = s[::-1]
    # Use for loop to solve question.

    a = []
    for i in range(0, len(s)):
        a.append(s[-i - 1])
    s = a
    print(s)
# test_str = ["h","e","l","l","o"]
test_str = ["H","a","n","n","a","h"]
reverseString(test_str)

