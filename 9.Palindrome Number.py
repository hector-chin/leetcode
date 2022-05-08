def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    str_x = str(x)
    for i in range(0, round(len(str_x)/2)):
        if str_x[i] != str_x[-i-1]:
            print("False")
            # return False
        else:
            pass
        # return True
    print("True")
a=121
test_is_Palindrome= isPalindrome(a)
