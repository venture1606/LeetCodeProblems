class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # values = []
        # for x in range(2):
        #     ans = max(nums)
        #     values.append(ans-1)
        #     nums.remove(ans)
        # return (values[0] * values[1])
        nums = sorted(nums, reverse = True)
        return (nums[0]-1) * (nums[1]-1)
