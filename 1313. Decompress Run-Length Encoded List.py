class Solution(object):
    def decompressRLElist(self, nums):
        AnsList = []
        for x in range(0,len(nums),2):
            freq = nums[x]
            val = nums[x+1]
            for y in range(freq):
                AnsList.append(val)
        return AnsList
