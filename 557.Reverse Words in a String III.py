def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    a = s.rsplit()
    b = ''
    for i in range(0, len(a)):
        if i != len(a)-1:
            b += a[i][::-1]+ ' '
        else:
            b += a[i][::-1]
    print(b)
    # print(a)



s = "Let's take LeetCode contest"
reverseWord = reverseWords(s)
