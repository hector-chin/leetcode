class NumArray:

    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        new_nums = self.nums[ left : right + 1]
        sum_answer = sum(self.nums)
        # for i in range(left, right+1):
        #     sum_answer += self.nums[i]
        return sum_answer
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)