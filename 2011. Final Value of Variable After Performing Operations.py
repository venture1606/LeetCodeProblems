class Solution(object):
    def finalValueAfterOperations(self, operations):
        ans = 0
        for x in operations:
            if x == "--X" or x == "X--":
                ans -= 1
            elif x == "++X" or x == "X++":
                ans += 1
        return ans