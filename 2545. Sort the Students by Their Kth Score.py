class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        maxi = []
        for x in score:
            maxi.append([x[k],x])
        maxi = sorted(maxi, reverse = True)
        answer = [y[1] for y in maxi]
        return answer
