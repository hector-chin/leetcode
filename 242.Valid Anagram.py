def isAnagram(s: str, t: str) -> bool:
    if len(s) == len(t):
        for i in range(0, len(s)):
            print(s[i])
            try:
              t = t.replace(s[i], '', 1)
            except:
                pass
        if t == '':
            return True
        return False
    return False






s = "rat"
t = "car"
test = isAnagram(s, t)