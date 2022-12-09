class Solution(object):

    def kWeakestRows(self, mat, k):
        val = {}
        for x in range(len(mat)):
            RowSum = 0
            for y in range(len(mat[x])):
                if mat[x][y] == 1:
                    RowSum += 1
            val[x] = RowSum
        #print(val)
        value = sorted(val.items(), key=lambda x:x[1])
        # print(value)
        lis = list(x[0] for x in value)
        ans = []
        for x in range(k):
            ans.append(lis[x])
        return ans