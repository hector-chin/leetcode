def toLowerCase(s) -> str:
    lower_dict = {'A':'a', 'B':'b','C':'c','D':'d','E':'e','F':'f','G':'g','H':'h',
                  'I':'i','J':'j','K':'k','L':'l','M':'m','N':'n','O':'o','P':'p',
                  'Q':'q','R':'r','S':'s','T':'t','U':'u','V':'v','W':'w','X':'x','Y':'y','Z':'z'
                  }
    for i in range(0, len(s)):
        if s[i] in lower_dict:
            s = s.replace(s[i], lower_dict[s[i]])
    print(s)
    return s



s = "LOVELY"
test = toLowerCase(s)
