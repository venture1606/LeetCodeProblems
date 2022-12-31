class Solution(object):
    def restoreString(self, s, indices):
        AnsString = list(s)
        for x in range(len(indices)):
            # print(x, s[indices[x]])
            AnsString[indices[x]] = s[x]
        string = ""
        for y in AnsString:
            string += y
        return string
