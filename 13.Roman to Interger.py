def romanToInt(s):
    """
    :type s: str
    :rtype: int
    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    IV            4
    IX            9
    XL            40
    XC            90
    CD            400
    CM            900

    """
    roman_convert_int_single = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    roman_convert_int = {
                        "IV": 4,
                        "IX": 9,
                        "XL": 40,
                        "XC": 90,
                        "CD": 400,
                        "CM": 900
                        }
    a = 0
    for i in roman_convert_int.keys():
        if i in s:
            a += roman_convert_int[i]
            s = s.replace(i, '')
        else:
            pass
    for i in range(0, len(s)):
        if s[i] in roman_convert_int_single:
            a += roman_convert_int_single[s[i]]
        else:
            pass
    # return a
    print(a)



convert_machine = romanToInt("MCMXCIV")
