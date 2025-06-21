class Solution(object):
    def minAddToMakeValid(self, s):
        Open = 0
        tot = 0

        for i in s:
            if i == '(':
                Open += 1
            elif i == ')':
                if Open > 0:
                    Open -= 1
                else:
                    tot += 1
        return Open+tot

