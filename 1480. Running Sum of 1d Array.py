class Solution(object):
    def runningSum(self, nums):
        num = nums[::-1]
        ans = []
        for x in range(len(num)):
            total = num[x]
            y = x+1
            while (y<len(num)):
                total += num[y]
                y += 1
            ans.append(total)
        return ans[::-1]
