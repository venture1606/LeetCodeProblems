class Solution:
    def sortSentence(self, s: str) -> str:
        answer = []
        string_list = s.split()
        for x in range(len(s)):
            for y in string_list:
                if str(x+1) in y:
                    answer.append(y[:len(y)-1])
        return ' '.join(answer)
