class Solution(object):
    def shuffle(self, nums, n):
        ListOne = []
        ListTwo = []
        for x in range(2*n):
            if x < n:
                ListOne.append(nums[x])
            else:
                ListTwo.append(nums[x])
        
        ans = []
        for x in range(n):
            ans.append(ListOne[x])
            ans.append(ListTwo[x])
        return ans
