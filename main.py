# nums = [4, 3, 2, 6]
# a = 0
# k = 0
# b = []
# for i in range(0, len(nums)):
#     for j in range(0, len(nums)):
#         a += j*nums[j-k]
#     b.append(a)
#     a = 0
#     k += 1
# print(b)
#
#
# print(max(b))
import numpy as np
x = [1, 2, 3]
a = np.array(x)
print(a[0:len(a)])

