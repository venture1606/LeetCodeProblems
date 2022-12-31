class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        NewCandies = []
        Max = max(candies)
        for x in candies:
            a = x + extraCandies
            NewCandies.append(a)
        # print(NewCandies, "\n", Max )
        AnsList = []
        for y in NewCandies:
            # print(y, Max)
            if y >= Max:
                AnsList.append(True)
            else:
                AnsList.append(False)
        # print(AnsList)
        return AnsList
