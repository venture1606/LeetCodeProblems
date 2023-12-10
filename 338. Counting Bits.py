class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = []
        for x in range(n+1):
            x = bin(x)
            x = x [2:]
            sums = x.count(str(1))
            answer.append(sums)
        return answer         
