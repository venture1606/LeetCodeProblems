class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = []
        total = 0
        for x in nums:
            left_sum.append(total)
            total += x
        # print(left_sum)
        right_sum = []
        new_num = nums[::-1]
        total = 0
        for x in new_num:
            right_sum.append(total)
            total += x
        right_sum = right_sum[::-1]
        # print(right_sum)
        answer = []
        for y in range(len(nums)):
            value = abs(left_sum[y] - right_sum[y])
            answer.append(value)
        return answer
