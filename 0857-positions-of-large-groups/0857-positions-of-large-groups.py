class Solution(object):
    def largeGroupPositions(self, s):
        res = []
        start = 0
        
        for i in range(1,len(s)+1):
            if i == len(s) or s[i] != s[i-1]:
                if i - start >= 3:
                    res.append([start,i-1])
                start = i
        return res
