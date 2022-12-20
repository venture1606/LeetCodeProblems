class Solution(object):
    def maximumWealth(self, accounts):
        total = []
        for x in range(len(accounts)):
            value = 0
            for y in range(len(accounts[x])):
                value += accounts[x][y]
            total.append(value)
        return max(total)
