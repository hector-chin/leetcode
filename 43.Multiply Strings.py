class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if (num1 == '0') or (num2 == '0'):
            return '0'
        num1_int = 0
        num2_int = 0
        str_int_dict = {
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '0': 0
        }

        for i in range(0, len(num1)):
            num1_int += str_int_dict[num1[i]] * 10 ** (len(num1) - 1 - i)

        for i in range(0, len(num2)):
            num2_int += str_int_dict[num2[i]] * 10 ** (len(num2) - 1 - i)
        return str(num1_int * num2_int)