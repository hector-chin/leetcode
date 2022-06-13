class Solution:
    def plusOne(self, digits):
        digits[-1] += 1
        index = 1
        while digits[-index] >= 10:
            if index < len(digits):
                digits[-index] -= 10
                digits[- index - 1] += 1
            if index == len(digits):
                digits[-index] -= 10
                a = [1]
                digits = a + digits
            index += 1
        return digits