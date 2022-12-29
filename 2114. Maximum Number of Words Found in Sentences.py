class Solution(object):
    def mostWordsFound(self, sentences):
        TotalList = []
        for x in sentences:
            total = 0
            for y in range(len(x)):
                if x[y] == " ":
                    total += 1 
            TotalList.append(total)
        return (max(TotalList)+1)
