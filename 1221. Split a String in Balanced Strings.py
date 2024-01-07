class Solution:
    def balancedStringSplit(self, s: str) -> int:
        substring = 0
        count = 0
        for x in s: #for x in range(len(s)):
            if x == 'R':
                count -= 1 # count = count - 1
            elif x == 'L':
                count += 1 # count = count + 1
            if count == 0:
                substring += 1

        return substring
