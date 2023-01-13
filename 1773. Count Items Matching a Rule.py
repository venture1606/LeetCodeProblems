class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        if ruleKey == "type":
            index = 0
        elif ruleKey == "color":
            index = 1
        elif ruleKey == "name":
            index = 2
        ans = 0
        for x in range(len(items)):
            if items[x][index] == ruleValue:
                ans += 1
        return ans
