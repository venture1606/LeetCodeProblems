class Solution(object):
    def createTargetArray(self, nums, index):
        AnsList = []
        for x in range(len(nums)):
            AnsList.insert(index[x], nums[x])
        return AnsList
