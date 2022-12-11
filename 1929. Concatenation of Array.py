class Solution(object):
    def getConcatenation(self, nums):
        ans = []
        index = 0
        for x in range(len(nums)*2):
            if index == len(nums):
                index = 0
            ans.append(nums[index])
            index += 1
        return ans