class Solution(object):
    def buildArray(self, nums):
        x = 0
        ans = []
        for x in range(len(nums)):
            ans.append(nums[nums[x]])
        return ans