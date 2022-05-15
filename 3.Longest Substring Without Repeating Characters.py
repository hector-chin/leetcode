def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    a = ''
    for i in range(0, len(s)):
        while i + 1 < len(s):
            if s[i] != s[i+1]:
                a += s[i]
    return len(a)

s = "abcabcbb"
test = lengthOfLongestSubstring(s)
