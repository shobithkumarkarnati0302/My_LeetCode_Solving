class Solution(object):
    def countPalindromicSubsequence(self, s):
        res = 0

        for c in set(s): 
            first = s.find(c)
            last = s.rfind(c)

            if last - first >= 2:
                middle_chars = set(s[first+1:last])
                res += len(middle_chars)

        return res
