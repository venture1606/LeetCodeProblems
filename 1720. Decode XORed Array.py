class Solution(object):
    def decode(self, encoded, first):
        AnsList = [first]
        for x in encoded:
            a = x ^ AnsList[-1]
            AnsList.append(a)
        return AnsList
