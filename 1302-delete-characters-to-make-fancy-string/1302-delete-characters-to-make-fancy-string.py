class Solution(object):
    def makeFancyString(self, s):
        if len(s) < 3:
            return s

        res = s[0]

        for i in range(1, len(s) - 1):
            curr = s[i]
            if s[i - 1] == curr and s[i + 1] == curr:
                continue
            res += curr

        res += s[-1] 
        return res
