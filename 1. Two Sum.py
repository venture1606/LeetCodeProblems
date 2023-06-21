class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lis = []
        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                if (nums[x] + nums[y]) == target:
                    lis.append(x)
                    lis.append(y)
                    return lis
