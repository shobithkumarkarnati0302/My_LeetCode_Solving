class Solution(object):
    def isSubsequence(self, s, t):
        s_len = 0
        t_len = 0

        while s_len < len(s) and t_len < len(t):
            if s[s_len] == t[t_len]:
                s_len += 1
                t_len += 1
            else:
                t_len += 1

        return s_len == len(s)