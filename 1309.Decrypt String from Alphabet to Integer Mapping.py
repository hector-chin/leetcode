def freqAlphabets(s: str) -> str:
    tar_dict = {'1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h',
                '9':'i','10#':'j','11#':'k','12#':'l','13#':'m','14#':'n','15#':'o',
                '16#':'p','17#':'q','18#':'r','19#':'s','20#':'t','21#':'u','22#':'v',
                '23#':'w','24#':'x','25#':'y','26#':'z'}
    tar_str = ''
    times = 0
    for i in range(0, len(s)):
        if i + 2 + times < len(s):
            if i + 2 < len(s):
                if s[i + 2 + times] != '#':
                    tar_str += tar_dict[s[i + times]]
                else:
                    tar_str += tar_dict[s[i + times: i + times + 3]]
                    times += 2
        elif i + times < len(s):
            tar_str += tar_dict[s[i + times]]
    print(tar_str)
    return tar_str


s = "10#11#12"
test = freqAlphabets(s)
