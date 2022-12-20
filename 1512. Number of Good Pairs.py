class Solution(object):
    def numIdenticalPairs(self, nums):
        ans = 0
        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                if nums[x] == nums[y]:
                    ans += 1
        return ans
