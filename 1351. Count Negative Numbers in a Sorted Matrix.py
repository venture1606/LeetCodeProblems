class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for x in grid:
            for y in x:
                if y < 0:
                    count += 1
        return count
