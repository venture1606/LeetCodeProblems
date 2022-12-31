class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        AnsList = []
        for x in range(len(nums)):
            total = 0
            for y in nums:
                if y < nums[x]:
                    total += 1
            AnsList.append(total)
        return AnsList
