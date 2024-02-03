class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        answer = [pref[0]]
        for x in range(1,len(pref)):
            answer.append(pref[x-1] ^ pref[x])
        return answer
