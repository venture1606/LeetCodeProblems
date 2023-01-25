class Solution(object):
    def differenceOfSum(self, nums):
        sum1 = 0
        for y in nums:
            sum1 += y
        sum2 = 0
        for x in nums:
            x = str(x)
            for i in x:
                sum2 += int(i)
        return sum1 - sum2
