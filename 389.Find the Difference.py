def findTheDifference(s: str, t: str) -> str:
    for i in range(0, len(s)):
        if s[i] in t:
            t = t.replace(s[i], '', 1)
    print(t)
    return t

s = "abcd"
t = "abcde"
test = findTheDifference(s, t)